# -*- coding:utf8 -*-
from config import TEST_CASE_PATH
# master info
PERCEPTION_AUTOWARE4_IP = '127.0.0.1'  # as master
PERCEPTION_AUTOWARE4_USER = 'adlink'
PERCEPTION_AUTOWARE4_PWD = 'adlink'
PERCEPTION_AUTOWARE4_DEVEL = '~/workspace/test_autoware/AutowareArchitectureProposal'
PERCEPTION_ROS1_SETUP = '/opt/ros/melodic/setup.bash'

PERCEPTION_ROS_MASTER_URI = 'http://{}:11311'.format(PERCEPTION_AUTOWARE4_IP)

# perception server info
PERCEPTION_IP = '127.0.0.1'
PERCEPTION_USER = 'adlink'
PERCEPTION_PWD = 'adlink'
PERCEPTION_BAG_PATH = '{}/bags/perception'.format(TEST_CASE_PATH)  # record bags, play bags path
PERCEPTION_BAG_PATH_OPEN = '{}/bags/perception_open'.format(TEST_CASE_PATH)  # record bags, play bags path

PERCEPTION_BAG_REMOTE = False  # record or play bags env, True remote, False local
PERCEPTION_BAG_REMOTE_IP = '127.0.0.1'
PERCEPTION_BAG_REMOTE_USER = 'adlink'
PERCEPTION_BAG_REMOTE_PWD = 'adlink'

# =================================== open source config ===================================
AUTOWARE_DOCKER_NAME = 'runtime'
AUTOWARE_NODE_LIST = []
AUTOWARE_RUN_STATUS = {1: 'docker stopped', 2: 'docker and autoware are running ',
                       3: 'docker is running, but autoware is not ok'}

# =================================== compare standard deviation and euclidean distance config ===================================
MSG_COUNT_STEP = 1000  # rosbag msg count step
UUID_STD_MAX = 1000
SEM_STD_MAX = 1000
PST_STEP = 500  # position point max step
PST_STD_MAX = 1000  # position max std
PST_DIS_MAX = 1000  # position max distance
ORI_STEP = 500  # orientation point max step
ORI_STD_MAX = 1000
ORI_DIS_MAX = 1000
LINE_STEP = 1000  # line speed point max step
LINE_STD_MAX = 1000
LINE_DIS_MAX = 1000
PRE_PATH_STEP = 1000  # prediction point max step
PRE_PATH_STD_MAX = 1000
PRE_PATH_DIS_MAX = 1000
PRE_PATH_ORI_DIS_MAX = 1000
SHAPE_STEP = 1000
SHAPE_STD_X_MAX = 1000
SHAPE_STD_Y_MAX = 1000
SHAPE_DIS_X_MAX = 1000
SHAPE_DIS_Y_MAX = 1000
