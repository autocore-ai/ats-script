#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
ODD's some common actions
@Project ：auto_test 
@File    ：aw4_action.py
@Date    ：2020/12/8 上午11:20 
"""

import subprocess
import logging
import common.ODD.config as conf
import common.ODD.command as command
import common.utils.docker as docker
import config

logger = logging.getLogger()


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


def check_aw4_status_docker(env_ip: str, module: str) -> (bool, int):
    """
    check aw4 running status by screen
    1. judge: Is aw4 and test env same env?
    2. if same, local check
    3. if not, remote to aw4 and check

    check step:
    1. check docker
    2. get node list
    3. check node list
    return:
    bool, exec cmd result,if exec successful, True, or not False,
    int: 1. docker stopped 2. docker and aw4 are running 3. docker is running, but aw4 is not ok
    """
    docker_name = conf.TEST_MODULE_INFO[module]['ros1_docker_name']
    node_list = conf.TEST_MODULE_INFO[module]['node_list']
    aw4_ws = conf.TEST_MODULE_INFO[module]['ros1_aw4_workspace']
    master_uri = conf.TEST_MODULE_INFO[module]['master_uri']

    if config.TEST_IP == env_ip:
        # 1. check docker
        r_bool, status_bool = docker.check_docker(docker_name)
        if not r_bool:
            logger.info('check aw4 docker(name: {}) error: {}'.format(docker_name, status_bool))
            return False, status_bool

        if not status_bool:
            return True, 1  # docker stopped

        # 2. get node list
        cmd = command.GET_ROS_NODE_LIST % (docker_name, aw4_ws, env_ip, master_uri)
        logger.info('get ros node list command: %s' % cmd)
        r_bool, node_list_str = get_node_list(cmd)
        if not r_bool:
            logger.info('get autoware rosnode list failed, error: {}'.format(node_list_str))
            return False, node_list_str

        # 3. check node list
        r_bool, msg = check_node_list(node_list, node_list_str)
        if not r_bool:
            logger.info('check autoware rosnode failed, msg: {}'.format(msg))
            return True, 3  # docker is running, but autoware is not ok
        return True, 2  # docker and autoware are running
    else:
        """remote to check aw4"""
        # TO DO
    logger.error('wrong path ...')
    return False, 1


def stop_aw4_docker(module) -> (bool, str):
    """
    stop aw4
    :return:
        bool: if True that means docker stopped
        str:  Error message description
    """
    docker_name = conf.TEST_MODULE_INFO[module]['ros1_docker_name']
    r_bool, s_bool = docker.stop_docker(docker_name)
    if not r_bool:
        logger.error('stop aw4 failed, msg: {}'.format(s_bool))
        return False, s_bool

    if not s_bool:
        return True, 'stop aw4 failed'
    return True, ''


def start_aw4_docker(module, aw_log_path):
    cmd = conf.TEST_MODULE_INFO[module]['start_cmd']
    if conf.RVIZ:
        cmd = conf.TEST_MODULE_INFO[module]['start_cmd_rviz']
    start_cmd = '{cmd} > {log_path}'.format(cmd=cmd, log_path=aw_log_path)
    logger.info('start aw4 cmd: {}'.format(start_cmd))
    r_bool, msg = docker.start_docker(start_cmd)
    return r_bool, msg
