# -*- coding:utf8 -*-
"""
进程操作
1. 启动进程，并检测
2. 杀掉进程，并检测
"""
import os
import time
import logging
import subprocess
from utils.remote import Remote, RemoteP
import config
logger = logging.getLogger()


def local_start_process(command, check_key, start_time=2):
    """
    本地启动进程
    :param command:  启动命令
    :param check_key:  检测启动命令key
    :param start_time:  进程启动时间
    :return:
    """
    logger.info('exec local command: {}'.format(command))
    # os.popen(command)
    proc = subprocess.Popen(command, shell=True)

    # 等待进程启动
    logger.info('wait time: {}'.format(start_time))
    time.sleep(start_time)

    # 检查启动结果
    cmd = 'ps -ef | grep {} | grep -v grep'.format(check_key)
    logger.info('check process, check key: {}, check command: {}'.format(check_key, cmd))
    ret_obj = os.popen(cmd)
    ret = ret_obj.read()
    logger.info('stdout: {}'.format(ret))
    if check_key in ret:
        return True, 'start successfully, exec command: {}'.format(command)

    proc.terminate()
    return False, 'start failed, exec command: {}'.format(command)


def remote_start_process(command, check_key, start_time=2):
    """
    远程启动命令
    :param server: 远程服务
    :param command: 执行命令
    :param check_key: 检测启动成功关键字
    :param start_time:  启动时间
    :return:
    """
    try:
        server = Remote(config.PERCEPTION_IP, config.PERCEPTION_USER, config.PERCEPTION_PWD)
        ret = server.exec_comm(command)
        print(ret)
        logger.info('stdout: {}'.format(ret.stdout))

        # 等待进程启动
        print('wait time')
        logger.info('wait time: {}'.format(start_time))
        time.sleep(start_time)

        # 检查启动结果
        cmd = 'ps -ef | grep {} | grep -v grep'.format(check_key)
        ret = server.exec_comm(cmd)
        ret = ret.stdout
        logger.info('stdout: {}'.format(ret))
        server.close()
        if check_key in ret:
            return True, 'start successfully, command: {}'.format(command)
        else:
            return False, 'exec failed, command: {}'.format(command)

    except Exception as e:
        logger.exception(e)
        return False, 'raised except, command: {}'.format(command)


def remote_stop_process(process_name, kill_cmd='-9', stop_time=1):
    """
    远程停止进程
    :param server:  远程服务
    :param process_name: 进程名字，必须包含在运行的进程命令中，否则不会被kill
    :param kill_cmd:  停止进程方式
    :param stop_time:  检测进程停止的时间
    :return:
    """
    try:
        server = RemoteP(config.PERCEPTION_IP, config.PERCEPTION_USER, config.PERCEPTION_PWD)
        server.exec_comm('kill {} `ps -ef|grep "{}"|awk \'{{print $2}}\'`'.format(kill_cmd, process_name))
        # 进程停止所需时间
        logger.info('wait time: {}s'.format(stop_time))
        time.sleep(stop_time)
        # 检查是否kill 成功
        r_bool, ret = server.exec_comm('ps -ef| grep {} | grep -v grep'.format(process_name))
        logger.info('stdout: {}'.format(ret))
        if process_name in ret:
            return False, 'stop failed, remote process : {}'.format(process_name)
        return True, 'stop successfully, remote process : {}'.format(process_name)
    except Exception as e:
        logger.exception(e)
        return False, 'raised except, stop remote process : {}'.format(process_name)


def local_stop_process(process_name, kill_cmd='-9', stop_time=2):
    """
    远程本地进程
    :param process_name: 进程名字，必须包含在运行的进程命令中，否则不会被kill
    :param kill_cmd:  停止进程方式
    :param stop_time:  检测进程停止的时间
    :return:
    """
    try:
        stop_cmd = 'kill {} `ps -ef|grep "{}"|awk \'{{print $2}}\'`'.format(kill_cmd, process_name)
        logger.info('stop the local process[{}]: {}'.format(process_name, stop_cmd))
        ret_obj = os.popen(stop_cmd)
        ret = ret_obj.read()
        logger.info('kill process[{}] stdout: {}'.format(process_name, ret))

        # 进程停止时间
        logger.info('kill process wait time: {}s'.format(stop_time))
        time.sleep(stop_time)

        # 检查是否kill 成功
        r_bool = check_process(process_name)
        if r_bool:
            return False, 'stop failed, local process : {}'.format(process_name)
        return True, 'stop successfully, local process : {}'.format(process_name)
    except Exception as e:
        logger.exception(e)
        return False, 'raised except, stop local process : {}'.format(process_name)


def check_process(process_name: str):
    """通过ps检查进程是否存在
    return: True 进程存在； False 进程不存在"""
    check_cmd = 'ps -ef| grep {} | grep -v grep'.format(process_name)
    logger.info('check the local process exists: {}'.format(check_cmd))
    ret_obj = subprocess.Popen(check_cmd, shell=True, stdout=subprocess.PIPE)
    ret = ret_obj.stdout.read()
    logger.info('check result: {}'.format(ret))
    if process_name in str(ret):
        return True
    return False


def remote_check_process(process_name: str):
    """
    check remote process status
    """
    check_cmd = 'ps -ef| grep {} | grep -v grep'.format(process_name)
    logger.info('check the remote process status: {}'.format(check_cmd))
    server = RemoteP(config.PERCEPTION_IP, config.PERCEPTION_USER, config.PERCEPTION_PWD)
    t_bool, ret = server.exec_comm(check_cmd)
    logger.info('check result: {}'.format(ret))
    if process_name in ret:
        return True
    return False


def remote_check_rosnode_list():
    """
    check remote process status
    """
    check_cmd = 'export ROS_MASTER_URI=http://192.168.10.29:11311;rosnode list'
    logger.info('check rosnode list command: {}'.format(check_cmd))
    server = RemoteP(config.PERCEPTION_IP, config.PERCEPTION_USER, config.PERCEPTION_PWD)
    r_bool, ret = str(server.exec_comm(check_cmd))
    logger.info('check result: {}'.format(ret))
    return True

