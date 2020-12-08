#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@Project ：auto_test 
@File    ：action.py.py
@Date    ：2020/12/8 上午11:20 
"""

import subprocess
import logging
logger = logging.getLogger()


def check_docker(d_name: str) -> bool:
    """
    check docker status
    :param d_name: docker name
    :return: bool
    """
    cmd = 'docker ps | grep {d_name}'.format(d_name=d_name)
    logger.debug('check docker cmd: {cmd}'.format(cmd=cmd))
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = p.stdout.read().decode('utf-8')
    stderr = p.stderr.read().decode('utf-8')
    logger.debug('check docker result, stdout: {}, stderr: {}'.format(stdout, stderr))
    if stderr:
        logger.error(stderr)
        raise Exception(stderr)
    if stdout:
        return True
    return False


def check_node_list(exp_n_list: list, real_n_list: str) -> (bool, str):
    """
    check node list

    :param exp_n_list:  expect nodes list
    :param real_n_list:  real nodes list
    :return:  bool, str
    """
    if sorted(exp_n_list) == sorted(real_n_list):
        return True, ''
    for node in exp_n_list:
        if node not in real_n_list:
            return False, '{} not in expect nodes list'.format(node)
    return True, ''


def get_node_list(node_list_cmd: str) -> (bool, list):
    """
    1. get node list from current docker
    2. if successful, return list
    3. if not, return error
    :param node_list_cmd:
    :return: bool, list
    """

    pass

if __name__ == '__main__':
    # print(check_docker('test'))
    check_docker('test')
