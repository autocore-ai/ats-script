#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@Project ：auto_test 
@File    ：cases_env_args.py
@Date    ：2020/12/18 下午5:10 
"""

import config as conf
import common.perception.perception_conf as per_conf
import common.planning.planning_conf as pn_conf


def get_case_argv() -> dict:
    """
    according to case type to get case argvs
    :return: case dict
    """
    case_dict = {}
    if conf.EXEC_CASE_TYPE == 1:
        case_dict['perception'] = '{}/testcases/test_ODD/cases/perception_cases_open.csv'.format(conf.TEST_CASE_PATH)
        case_dict['planning'] = '{}/testcases/test_ODD/cases/planning_cases_open.csv'.format(conf.TEST_CASE_PATH)
        case_dict['perception_bag_path'] = per_conf.PERCEPTION_BAG_PATH_OPEN
        case_dict['planning_bag_path'] = pn_conf.LOCAL_PLANNING_BAG_PATH
    else:
        case_dict['perception'] = '{}/testcases/test_ODD/cases/perception_cases.csv'.format(conf.TEST_CASE_PATH)
        case_dict['planning'] = '{}/testcases/test_ODD/cases/planning_cases.csv'.format(conf.TEST_CASE_PATH)
        case_dict['perception_bag_path'] = per_conf.PERCEPTION_BAG_PATH
        case_dict['planning_bag_path'] = pn_conf.LOCAL_PLANNING_BAG_PATH
    return case_dict
