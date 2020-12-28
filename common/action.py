#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@Project ：auto_test 
@File    ：action.py
@Date    ：2020/12/8 上午11:20 
"""

import subprocess
import logging
logger = logging.getLogger()


def check_docker(d_name: str) -> (bool, bool):
    """
    check docker status
    :param d_name: docker name
    :return: bool
    """
    # cmd = 'docker ps | grep {d_name}'.format(d_name=d_name)
    cmd = 'docker ps --format "{{.Names}}"'
    logger.info('check docker cmd: {cmd}'.format(cmd=cmd))
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = p.stdout.read().decode('utf-8')
    stderr = p.stderr.read().decode('utf-8')
    logger.info('check docker result, \nstdout: \n{}, \nstderr: \n{}\n'.format(stdout.split('\n'), stderr.split('\n')))
    if stderr:
        return False, stderr
    stdout_list = [n for n in stdout.split('\n') if n]
    logger.info(stdout_list)
    if len(stdout_list) == 1 and stdout_list[0] == d_name:
        return True, True
    return True, False


def check_node_list(exp_n_list: list, real_n_list: str) -> (bool, str):
    """
    check node list

    :param exp_n_list:  expect nodes list
    :param real_n_list:  real nodes list
    :return:  bool, str
    """
    for node in exp_n_list:
        if node not in real_n_list:
            return False, '{} not in expect nodes list'.format(node)
    return True, ''


def get_node_list(node_list_cmd: str) -> (bool, str):
    """
    1. get node list from current docker
    2. if successful, return list
    3. if not, return error

    :param node_list_cmd:
    :return: bool, list
    """
    p = subprocess.Popen(node_list_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = p.stdout.read().decode('utf-8')
    stderr = p.stderr.read().decode('utf-8')
    logger.debug('start docker result, stdout: {}, stderr: {}'.format(stdout, stderr))
    if stderr:
        return False, stderr
    return True, stdout


def start_docker(cmd: str) -> (bool, str):
    """
    start docker
    :param cmd: start command
    :return:
    """
    # p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # stdout = p.stdout.read().decode('utf-8')
    # stderr = p.stderr.read().decode('utf-8')
    # logger.info('start docker result, stdout: {}, stderr: {}'.format(stdout, stderr))
    # if stderr:
    #     logger.error(stderr)
    #    return False, stderr
    subprocess.Popen(cmd, shell=True)
    return True, ''


def stop_docker(d_name: str) -> (bool, bool):
    """
    stop docker
    :param d_name:
    :return:
    """
    cmd = 'docker stop {}'.format(d_name)
    logger.debug('stop docker cmd: {cmd}'.format(cmd=cmd))
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = p.stdout.read().decode('utf-8')
    stderr = p.stderr.read().decode('utf-8')
    logger.debug('stop docker result, stdout: {}, stderr: {}'.format(stdout, stderr))
    if stderr:
        logger.error(stderr)
        return False, stderr
    if stdout and stdout == d_name:
        return True, True
    return True, False
