#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@Project ：autotest 
@File    ：aw4_env.py
@Date    ：2021/1/7 下午6:05 
"""

import time
import logging
import allure

import common.ODD.config as conf
import common.ODD.perception.perception_conf as per_conf
import common.ODD.aw4_action as act

logger = logging.getLogger()


def check_aw4(env_ip, module, step_desc='check aw4 status, if running, stop it'):
    """
    check aw4 status
    :param env_ip: environment IP
    :param module: test module, such as planning, localization, perception
    :param step_desc: description about this action
    :return:
    """
    logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step=step_desc))

    with allure.step(step_desc):
        r_bool, status = act.check_aw4_status_docker(env_ip, module)
        logger.info('check aw4 status, return: {}, {}'.format(r_bool, status))
        assert r_bool, status
        if status in [2, 3]:
            step_desc = '{}, stop it'.format(conf.AW4_RUN_STATUS)
            with allure.step(step_desc):
                logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step=step_desc))
                r_bool, status = act.stop_aw4_docker(module)
                logger.info('stop autoware result: {}, {}'.format(r_bool, status))
                assert r_bool, status


def start_aw4(case_path, module, step_desc='start aw4'):
    """
    :param case_path: get aw4 log path
    :param module: according to module get start command
    :param step_desc: step description
    :return:
    """
    logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step=step_desc))
    aw_log_path = '{}_aw4.txt'.format(case_path)
    logger.info('aw4 log path: {}'.format(aw_log_path))
    with allure.step(step_desc):
        r_bool, msg = act.start_aw4_docker(module, aw_log_path)
        assert r_bool, msg


def wait_aw4_start(env_ip, module, wait_aw4_time, step_desc):
    """
    waiting aw4 start
    :param env_ip: check aw4 environment ip
    :param module: start module
    :param wait_aw4_time: waiting aw4 start max time
    :param step_desc: step description
    :return:
    """
    logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step=step_desc))
    t = 0
    with allure.step(step_desc):
        while t < wait_aw4_time:
            time.sleep(1)
            logger.info('waiting w4 start, wait {}s ......'.format(t+1))
            r_bool, status = act.check_aw4_status_docker(env_ip, module)
            assert r_bool, status
            if status == 2:
                logger.info('autoware started successfully')
                break
            t += 1
    assert t < wait_aw4_time, 'aw4 didn\'t start in {}s'.format(wait_aw4_time)


def stop_aw4(module, step_desc='stop aw4'):
    """
    stop aw4 docker
    :param module:
    :param step_desc:
    :return:
    """
    logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step='1. stop autoware'))
    with allure.step(step_desc):
        r_bool, status = act.stop_aw4_docker(module)
        logger.info('stop autoware result: {}, {}'.format(r_bool, status))
    assert r_bool, status
