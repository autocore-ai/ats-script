# -*- coding:utf8 -*-
"""
进程操作
1. 启动进程，并检测
2. 杀掉进程，并检测
"""
import os
import time
import logging
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
    os.system(command)

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
    return False, 'start failed, exec command: {}'.format(command)


def remote_start_process(server, command, check_key, start_time=2):
    """
    远程启动命令
    :param server: 远程服务
    :param command: 执行命令
    :param check_key: 检测启动成功关键字
    :param start_time:  启动时间
    :return:
    """
    try:
        ret = server.exec_comm(command)
        logger.info('stdout: {}'.format(ret.stdout))

        # 等待进程启动
        logger.info('wait time: {}'.format(start_time))
        time.sleep(start_time)

        # 检查启动结果
        cmd = 'ps -ef | grep {} | grep -v grep'.format(check_key)
        ret = server.exec_comm(cmd)
        ret = ret.stdout
        logger.info('stdout: {}'.format(ret))
        if check_key in ret:
            return True, 'start successfully, command: {}'.format(command)
        else:
            return False, 'exec failed, command: {}'.format(command)

    except Exception as e:
        logger.exception(e)
        return False, 'raised except, command: {}'.format(command)


def remote_stop_process(server, process_name, kill_cmd='-9', stop_time=1):
    """
    远程停止进程
    :param server:  远程服务
    :param process_name: 进程名字，必须包含在运行的进程命令中，否则不会被kill
    :param kill_cmd:  停止进程方式
    :param stop_time:  检测进程停止的时间
    :return:
    """
    try:
        server.exec_comm('kill {} `ps -ef|grep "{}"|awk \'{{print $2}}\'`'.format(kill_cmd, process_name))
        # 进程停止所需时间
        logger.info('wait time: {}s'.format(stop_time))
        time.sleep(stop_time)
        # 检查是否kill 成功
        ret = server.exec_comm('ps -ef| grep {} | grep -v grep'.format(process_name))
        ret = ret.stdout
        logger.info('stdout: {}'.format(ret))
        if process_name in ret:
            return False, 'stop failed, remote process : {}'.format(process_name)
        return True, 'stop successfully, remote process : {}'.format(process_name)
    except Exception as e:
        logger.exception(e)
        return False, 'raised except, stop remote process : {}'.format(process_name)


def local_stop_process(process_name, kill_cmd='-9', stop_time=1):
    """
    远程本地进程
    :param process_name: 进程名字，必须包含在运行的进程命令中，否则不会被kill
    :param kill_cmd:  停止进程方式
    :param stop_time:  检测进程停止的时间
    :return:
    """
    try:
        stop_cmd = 'kill {} `ps -ef|grep "{}"|awk \'{{print $2}}\'`'.format(kill_cmd, process_name)
        logger.info('local stop process: {}'.format(stop_cmd))
        ret_obj = os.popen(stop_cmd)
        ret = ret_obj.read()
        logger.info('stdout: {}'.format(ret))

        # 进程停止时间
        logger.info('wait time: {}s'.format(stop_time))
        time.sleep(stop_time)

        # 检查是否kill 成功
        check_cmd = 'ps -ef| grep {} | grep -v grep'.format(process_name)
        logger.info('local check process: {}'.format(check_cmd))
        ret_obj = os.popen(check_cmd)
        ret = ret_obj.read()
        logger.info('stdout: {}'.format(ret))

        if process_name in ret:
            return False, 'stop failed, local process : {}'.format(process_name)
        return True, 'stop successfully, local process : {}'.format(process_name)
    except Exception as e:
        logger.exception(e)
        return False, 'raised except, stop local process : {}'.format(process_name)