# -*- coding:utf8 -*-
"""
Fabric is really powerful because it can easily execute shell commands on remote machines. It is based on SSH
1. Connect to the remote and execute the command
2. Upload files
3. Download the file
"""
import time
import os
import logging
from socket import timeout
from fabric import Connection
import paramiko
from paramiko.ssh_exception import AuthenticationException

logger = logging.getLogger()


class Remote:
    """Remote operation"""

    def __init__(self, host, user, pwd):
        """
        init connect
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
        exec command
        :param cmd:
        :param hide: 默认为 False, 默认情况下将远程的输出信息在当前命令行输出, 为 True 时, 则不会, 但不论是什么, 都不会影响 Result
         对象的 stdout 和 stderr 结果, 还可以只隐藏 stdout 或 stderr
        :param timeout: time out
        :return: fabric.runners.Result
        """
        logger.info('exec remote command: {}'.format(cmd))
        return self.conn.run(cmd, hide=hide, timeout=timeout, warn=True)

    def local(self, cmd, hide=False, timeout=3):
        """
        exec local command
        :param cmd:
        :param hide:
        :param timeout: time out
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
        down load remote file to local
        :param remote_path: It can be an absolute or relative path to a file or directory
        if is a dir, will tar *.tar.gz，then download，and decompression，after download, will clean file remote.
        if it is a file, will download directly
        :param local_path: If the directory does not exist, a new one will be created.
        Take / as the separator and take the last one. If it contains
        :return:
        """
        logger.info('get remote {} to local {}'.format(remote_path, local_path))
        # judge whether the remote file or directory exists
        if not local_path:
            return False, 'local path is empty'

        if int(self.conn.run('[ -e {0} ];echo $?'.format(remote_path)).stdout) != 0:
            logger.info('{} is not exist.'.format(remote_path))
            return False, '{} is not exist.'.format(remote_path)

        # judge local path is a file or dir
        if '.' not in local_path.split('/')[-1]:
            local_flag = 'd'  # local path flag
            logger.info('local path is a directory: {}'.format(local_path))
            # judge whether local path exists
            if not os.path.exists(local_path):
                os.makedirs(local_path)
        else:
            local_flag = 'f'
            # get path
            local_path_temp = '/'.join(local_path.split('/')[:-1])
            if not os.path.exists(local_path_temp):
                os.makedirs(local_path_temp)

        # judge remote is a dir
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
                # clean remote tar
                ret = self.conn.run('rm -rf {}'.format(tmp_tar_gz))
                if ret.stderr:
                    return False, ret.stderr

        # remote is a file
        elif int(self.conn.run('[ -f {0} ];echo $?'.format(remote_path)).stdout) == 0:
            if local_flag == 'd':
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
        Upload local file or folder to remote
        :param local_path: Local file or folder
        :param remote_path: Remote file or folder
        :return:
        """
        logger.info('put local {} to remote {}'.format(local_path, remote_path))
        # 1. judge local file path
        if not os.path.exists(local_path):
            return False, 'local path {} is not exist'.format(local_path)

        # 2. judge remote
        if int(self.conn.run('[ -e {0} ];echo $?'.format(remote_path)).stdout) != 0:
            return False, 'remote path is not exist'

        # 3. judge local path is a file or a dir
        if os.path.isdir(local_path):
            logger.info('local path {} is a directory, need to tar'.format(local_path))
            # a. pack
            tar_name = '%s.tar.gz' % str(time.time())
            tar_path = '/tmp/%s' % tar_name
            try:
                os.chdir(local_path)
                logger.info('tar -zcvf {} ./'.format(tar_path))
                os.system('tar -zcvf {} ./'.format(tar_path))
                # b. upload
                self.conn.put(tar_path, remote_path)
                # c. decompression
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
        else:  # local is a file
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
        # Allow connection not in know_Hosts in the hosts file
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host, username=self.user, port=22, password=self.pwd)
        return ssh

    def exec_comm(self, command):
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
