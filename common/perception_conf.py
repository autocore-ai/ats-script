# -*- coding:utf8 -*-
from config import TEST_CASE_PATH
# master info
PERCEPTION_AUTOWARE4_IP = '192.168.50.235'  # as master
PERCEPTION_AUTOWARE4_USER = 'adlink'
PERCEPTION_AUTOWARE4_PWD = 'adlink'
PERCEPTION_AUTOWARE4_DEVEL = '~/workspace/test_autoware/AutowareArchitectureProposal'

PERCEPTION_ROS_MASTER_URI = 'http://{}:11311'.format(PERCEPTION_AUTOWARE4_IP)

# perception server info
# PERCEPTION_IP = '192.168.50.98'
# PERCEPTION_USER = 'train'
# PERCEPTION_PWD = '123456'
PERCEPTION_IP = '192.168.50.235'
PERCEPTION_USER = 'adlink'
PERCEPTION_PWD = 'adlink'
PERCEPTION_BAG_PATH = '{}/bags'.format(TEST_CASE_PATH)  # record bags, play bags path

PERCEPTION_BAG_REMOTE = False  # record or play bags env, True remote, False local
PERCEPTION_BAG_REMOTE_IP = '192.168.50.235'
PERCEPTION_BAG_REMOTE_USER = 'adlink'
PERCEPTION_BAG_REMOTE_PWD = 'adlink'
