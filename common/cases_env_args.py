#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@Project ：auto_test 
@File    ：cases_env_args.py
@Date    ：2020/12/18 下午5:10 
"""

import config as conf
import common.ODD.perception.perception_conf as per_conf
import common.ODD.planning.planning_conf as pn_conf
import common.ODD.localization.localization_conf as lo_conf


def get_case_argv() -> dict:
    """
    according to case type to get case argvs
    :return: case dict
    """
    case_dict = {}
    if conf.EXEC_CASE_TYPE == 1:  # open source
        case_dict['perception'] = '{}/perception_cases_open.csv'.format(conf.ODD_CSV_CASES)
        case_dict['planning'] = '{}/planning_cases_open.csv'.format(conf.ODD_CSV_CASES)
        case_dict['localization'] = '{}/localization_cases_open.csv'.format(conf.ODD_CSV_CASES)
        case_dict['perception_bag_path'] = per_conf.PERCEPTION_BAG_PATH_OPEN
        case_dict['planning_bag_path'] = pn_conf.PLANNING_BAG_PATH_OPEN
        case_dict['localization_bag_path'] = lo_conf.LOCALIZATION_BAG_PATH_OPEN
    else:  # home
        case_dict['perception'] = '{}/perception_cases.csv'.format(conf.ODD_CSV_CASES)
        case_dict['planning'] = '{}/planning_cases.csv'.format(conf.ODD_CSV_CASES)
        case_dict['localization'] = '{}/localization_cases.csv'.format(conf.ODD_CSV_CASES)
        case_dict['perception_bag_path'] = per_conf.PERCEPTION_BAG_PATH
        case_dict['planning_bag_path'] = pn_conf.PLANNING_BAG_PATH
        case_dict['localization_bag_path'] = lo_conf.LOCALIZATION_BAG_PATH
    return case_dict
