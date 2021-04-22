#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
ODD some common config
@Project ：autotest 
@File    ：config.py
@Date    ：2021/1/7 下午6:06 
"""

from config import TEST_CASE_PATH

BAG_PATH = '{}/testSDV/bags'.format(TEST_CASE_PATH)
PATH_CSV_CASES = '{}/testSDV/testcases'.format(TEST_CASE_PATH)

TRAJECTORY_TOPIC = '/planning/scenario_planning/trajectory'
CURRENT_POSE_TOPIC = '/current_pose'
TWIST_TOPIC = '/vehicle/status/twist'
VELOCITY_TOPIC = '/vehicle/status/velocity'
ROUTE_TOPIC = '/planning/mission_planning/route'
STATE = '/autoware/state'

RECORD_TOPIC_LIST = [
    # TRAJECTORY_TOPIC,
    CURRENT_POSE_TOPIC,
    TWIST_TOPIC,
    VELOCITY_TOPIC,
    ROUTE_TOPIC,
    STATE
    ]

STOP_RECORD_SIGNAL_TOPIC = ''