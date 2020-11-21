# -*- coding:utf8 -*-

import time
import os
import logging
import subprocess


logger = logging.getLogger()


def check_process(process_name):
    """
    check process is running
    """
    check_cmd = 'ps -ef| grep {} | grep -v grep'.format(process_name)
    logger.info('check local process exists: {}'.format(check_cmd))
    ret_obj = subprocess.Popen(check_cmd, shell=True, stdout=subprocess.PIPE)
    ret = ret_obj.stdout.read().decode('utf-8')
    logger.info('check result: {}'.format(ret))
    if process_name in ret:
        return True
    return False


def stop_process(process_name, signal='-9', stop_time=1):
    """
    stop process by kill signal
    """
    try:
        stop_cmd = 'kill {} `ps -ef|grep "{}"|awk \'{{print $2}}\'`'.format(signal, process_name)
        logger.info('stop local process[{}]: {}'.format(process_name, stop_cmd))
        p = subprocess.Popen(stop_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        std = p.stdout.read().decode('utf-8')
        err = p.stderr.read().decode('utf-8')
        logger.info('kill process[{}] stdout: {}'.format(process_name, std))
        logger.info('kill process[{}] stderr: {}'.format(process_name, err))

        # wait time
        logger.info('kill process wait time: {}s'.format(stop_time))
        time.sleep(stop_time)

        # check stop ok
        r_bool = check_process(process_name)
        if r_bool:
            return False, 'stop failed, local process : {}'.format(process_name)
        return True, 'stop successfully, local process : {}'.format(process_name)
    except Exception as e:
        logger.exception(e)
        return False, 'raised except, stop local process : {}'.format(process_name)

