# -*- coding:utf8 -*-
"""
Fabric真正强大在于可以很方便的执行远程机器上的Shell命令，它基于SSH实现
1. 连接到远程，执行命令
2. 上传文件
3. 下载文件
"""
from fabric import Connection
import time
import os
import logging
from socket import timeout
import paramiko
from paramiko.ssh_exception import AuthenticationException


logger = logging.getLogger()


class Remote:
    """远程操作"""

    def __init__(self, host, user, pwd):
        """
        初始化连接
        :param host:
        :param user:
        :param pwd:
        """
        try:
            self.conn = Connection(host, user=user, connect_kwargs={'password': pwd, 'timeout': 5})

        except Exception as e:
            logger.exception(e)
            raise e

    def check_is_connect(self):
        try:
            self.conn.run('cd ~')
            return True, 'connect successfully'
        except timeout:
            return False, 'connect time out.'
        except AuthenticationException:
            return False, 'Authentication failed.'
        except Exception as e:
            logger.exception(e)
            return False, '{}'.format(e)

    def exec_comm(self, cmd, hide=False, timeout=30):
        """
        执行命令
        :param cmd:
        :param hide: 默认为 False, 默认情况下将远程的输出信息在当前命令行输出, 为 True 时, 则不会, 但不论是什么, 都不会影响 Result 对象的 stdout 和 stderr 结果, 还可以只隐藏 stdout 或 stderr
        :param timeout: 超时时间
        :return: fabric.runners.Result
        """
        logger.info('exec remote command: {}'.format(cmd))
        return self.conn.run(cmd, hide=hide, timeout=timeout, warn=True)

    def local(self, cmd, hide=False, timeout=3):
        """
        执行本地命令
        :param cmd:
        :param hide: 默认为 False, 默认情况下将远程的输出信息在当前命令行输出, 为 True 时, 则不会, 但不论是什么, 都不会影响 Result 对象的 stdout 和 stderr 结果, 还可以只隐藏 stdout 或 stderr
        :param timeout: 超时时间
        :return: fabric.runners.Result
        """
        logger.info('exec local command: {}'.format(cmd))
        return self.conn.local(cmd)

    def sudo(self, cmd, hide=False):
        """
        :param cmd:
        :param hide:
        :return:
        """
        return self.conn.sudo(cmd, hide=hide)

    def get(self, remote_path, local_path='.'):
        """
        下载远程文件或目录到本地
        :param remote_path: 可以是一个绝对或者相对路径的文件或目录
        如若是目录，会打包目录为*.tar.gz，再下载，并在本地解压，下载结束后，会清理远程压缩文件
        若是文件，则直接下载
        :param local_path: 目录不存在，则会新建。以/为分割符，取最后一个，若含有.，则认为是文件，否则为目录
        :return:
        """
        logger.info('get remote {} to local {}'.format(remote_path, local_path))
        # 判断远程文件或者目录是否存在
        if not local_path:
            return False, 'local path is empty'

        # 判断远程目录或文件是否存在
        if int(self.conn.run('[ -e {0} ];echo $?'.format(remote_path)).stdout) != 0:
            logger.info('{} is not exist.'.format(remote_path))
            return False, '{} is not exist.'.format(remote_path)

        # 判断本地路径是一个文件还是一个目录
        if '.' not in local_path.split('/')[-1]:
            local_flag = 'd'  # 本地文件类型标志
            logger.info('local path is a directory: {}'.format(local_path))
            # 判断本地是否存在，不存在，则创建
            if not os.path.exists(local_path):
                os.makedirs(local_path)
        else:
            local_flag = 'f'
            # 获取目录
            local_path_temp = '/'.join(local_path.split('/')[:-1])
            if not os.path.exists(local_path_temp):
                os.makedirs(local_path_temp)

        # 判断远程是目录
        if int(self.conn.run('[ -d {0} ];echo $?'.format(remote_path)).stdout) == 0:
            if local_flag == 'f':
                logger.error('remote path is a directory, but local path is a file, need a directory path. '
                             'Remote path: {}, Local path: {}'.format(remote_path, local_path))
                return False, 'remote path is a directory, but local path is a file, need a directory path. ' \
                              'Remote path: {}, Local path: {}'.format(remote_path, local_path)

            logger.info('{} is a directory, need to tar'.format(remote_path))
            tar_name = str(time.time())
            tmp_tar_gz = '/tmp/{}.tar.gz'.format(tar_name)
            try:
                logger.info('exec: cd {0}'.format('/'.join(remote_path.split('/')[:-1])))
                with self.conn.cd('/'.join(remote_path.split('/')[:-1])):
                    logger.info('exec: tar -zcvf {0} {1}'.format(tmp_tar_gz, './%s' % remote_path.split('/')[-1]))
                    self.conn.run('tar -zcvf {} {}'.format(tmp_tar_gz, './%s' % remote_path.split('/')[-1]))

                local_path_new = '{}{}.tar.gz'.format(local_path, tar_name)
                logger.info('get tar {0} to local path {1}'.format(tmp_tar_gz, local_path_new))
                self.conn.get(tmp_tar_gz, local_path_new)
                logger.info('local exec: tar -zxvf {} -C {}'.format(local_path_new, local_path))
                self.conn.local('tar -zxvf {} -C {}'.format(local_path_new, local_path))
                logger.info('rm local tar {}'.format(local_path_new))
                self.conn.local('rm -rf {}'.format(local_path_new))
            except Exception as e:
                logger.exception(e)
                return False, 'get remote {} except, except info: {}'.format(remote_path, e)
            finally:
                # 清理远程tar包
                ret = self.conn.run('rm -rf {}'.format(tmp_tar_gz))
                if ret.stderr:
                    return False, ret.stderr

        # 远程是文件
        elif int(self.conn.run('[ -f {0} ];echo $?'.format(remote_path)).stdout) == 0:
            if local_flag == 'd':
                # 默认使用远程文件名字
                local_path += remote_path.split('/')[-1]
            try:
                self.conn.get(remote_path, local_path)
            except Exception as e:
                logger.exception(e)
                return False, 'get remote {} except, except info: {}'.format(remote_path, e)
        else:
            return False, 'unknown remote file: {}'.format(remote_path)

        return True, 'download success'

    def put(self, local_path, remote_path):
        """
        上传本地文件或者文件夹到远程
        :param local_path: 本地文件或文件夹
        :param remote_path: 远程文件夹
        :return:
        """
        logger.info('put local {} to remote {}'.format(local_path, remote_path))
        # 1. 判断本地文件是否存在
        if not os.path.exists(local_path):
            return False, 'local path {} is not exist'.format(local_path)

        # 2. 判断远程目录是否存在
        if int(self.conn.run('[ -e {0} ];echo $?'.format(remote_path)).stdout) != 0:
            return False, 'remote path is not exist'

        # 3. 判断本地是文件还是目录
        if os.path.isdir(local_path):
            logger.info('local path {} is a directory, need to tar'.format(local_path))
            # a. 打包
            tar_name = '%s.tar.gz' % str(time.time())
            tar_path = '/tmp/%s' % tar_name
            try:
                os.chdir(local_path)
                logger.info('tar -zcvf {} ./'.format(tar_path))
                os.system('tar -zcvf {} ./'.format(tar_path))
                # b. 上传
                self.conn.put(tar_path, remote_path)
                # c. 解压
                with self.conn.cd(remote_path):
                    self.conn.run('tar -zxvf {}'.format(tar_name))
                    self.conn.run('rm -rf {}'.format(tar_name))
            except Exception as e:
                logger.exception(e)
                return False, 'put local {} to remote {} failed, detail info, please check log'.format(local_path,
                                                                                                       remote_path)
            finally:
                os.chdir(local_path)
                os.system('rm -rf {}'.format(tar_path))
        else:  # 本地是文件
            try:
                self.conn.put(local_path, remote_path)
            except Exception as e:
                logger.exception(e)
                return False, 'put local {} to remote {} failed, detail info, please check log'.format(local_path,
                                                                                                       remote_path)

        return True, 'put success'

    def close(self):
        self.conn.close()


class RemoteP:
    def __init__(self, host, user, pwd):
        self.host, self.user, self.pwd = host, user, pwd

    def __get_conn(self):
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 建立连接
        ssh.connect(self.host, username=self.user, port=22, password=self.pwd)
        return ssh

    def exec_comm(self, command):
        # 使用这个连接执行命令
        ssh = self.__get_conn()
        try:
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
            stdout = ssh_stdout.read().decode("utf-8")
            stderr = ssh_stderr.read().decode('utf-8')
            ssh.close()
            if len(stderr) != 0:
                return False, stderr
            # get stdout
            return True, stdout
        except Exception as e:
            logger.error('exec command exception: {}'.format(command))
            logger.exception(e)
            return False, 'exec command exception: {}'.format(command)

    def exec_comm_no_out(self, command):
        # 使用这个连接执行命令
        ssh = self.__get_conn()
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
        ssh.close()

    def get(self, remote_file, local_file):
        logger.info('remote file: {}'.format(remote_file))
        logger.info('local file: {}'.format(local_file))
        t = paramiko.Transport((self.host, 22))
        try:
            t.connect(username=self.user, password=self.pwd)
            sftp = paramiko.SFTPClient.from_transport(t)
            sftp.get(remote_file, local_file)
            t.close()
            return True, ''
        except Exception as e:
            t.close()
            logger.error("get remote file execption")
            logger.exception(e)
            return False, 'get remote file execption'

if __name__ == '__main__':
    from common.command import *
    from config import PCU_IP, PCU_USER, PCU_PWD

    pcu_ser = Remote(PCU_IP, PCU_USER, PCU_PWD)
    # print(pcu_ser.exec_comm('ls -1', hide=True))
    print(RADAR_MAPPING)
    print(pcu_ser.exec_comm(RADAR_MAPPING, hide=True))
    print(pcu_ser.exec_comm('echo $ROS_IP', hide=True))
    # print(pcu_ser.exec_comm('echo $ROS_IP', hide=False))
    # result = pcu_ser.exec_comm('pwd')
    # client = pcu_ser.client
    # print(dir(client))
    # print(client.exec_command('ls'))
    # print(pcu_ser.get('/home/train/disk/Share/duanrongjie/data_2.tar.gz', './file5/'))
    # print(os.getcwd())
    # print(os.path.exists(os.getcwd()))
    # print(pcu_ser.put('./file5/test.txt', '/home/train/disk/Share/duanrongjie/ll'))


