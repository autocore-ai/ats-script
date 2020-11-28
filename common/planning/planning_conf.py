# -*- coding:utf8 -*-
# @Time : DATEDATE{TIME}
# @File : planning_conf.py
from config import TEST_CASE_PATH

PLANNING_AUTOWARE4_IP = '127.0.0.1'  # as master
PLANNING_AUTOWARE4_USER = 'adlink'
PLANNING_AUTOWARE4_PWD = 'adlink'
PLANNING_AUTOWARE4_DEVEL = '~/workspace/test_autoware/AutowareArchitectureProposal'

PLANNING_ROS_MASTER_URI = 'http://{}:11311'.format(PLANNING_AUTOWARE4_IP)

LOCAL_JIRA_PLANNING_FILE_PATH = '{}/testcases/test_ODD/cases/planning_cases.csv'.format(TEST_CASE_PATH)
LOCAL_GT_BAG_PATH = "{}/bags/planning_bags/groundtruth_bags/".format(TEST_CASE_PATH)
LOCAL_TEST_BAG_PATH = "{}/bags/planning_bags/test_bags/".format(TEST_CASE_PATH)
