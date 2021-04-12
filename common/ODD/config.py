#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
ODD some common config
@Project ：autotest 
@File    ：config.py
@Date    ：2021/1/7 下午6:06 
"""

from config import TEST_CASE_PATH
from common.ODD.perception.perception_conf import PERCEPTION_NODE_LIST
from common.ODD.planning.planning_conf import PLANNING_NODES

# bag path
BAG_PATH = '{}/bags'.format(TEST_CASE_PATH)

EXEC_CASE_TYPE = 1  # 1: open source 2: home 3: future way
EXEC_CASE_SCENE = {
    1: {'desc': 'open source aw4 scene', 'bag_dir': 'aw4', 'case_dir': 'aw4'},
    2: {'desc': 'home aw4 scene', 'bag_dir': 'home', 'case_dir': 'home'},
    3: {'desc': 'future way', 'bag_dir': 'fw', 'case_dir': 'fw'},
}

# docker environment
TEST_MODULE_INFO = {
    'test_perception': {'ros1_docker_ip': '127.0.0.1', 'ros1_docker_user': '', 'ros1_docker_pwd': '',
                        'ros1_container_name': 'runtime', 'ros1_aw4_workspace': '/ros1_workspace',
                        'ros2_docker_ip': '127.0.0.1', 'ros2_docker_user': '', 'ros2_docker_pwd': '',
                        'ros2_container_name': 'runtime-ros2', 'ros2_aw4_workspace': '/AutowareArchitectureProposal',
                        'master_uri': 'http://127.0.0.1:11311',
                        'node_list': PERCEPTION_NODE_LIST,
                        'start_cmd': 'cd {0}/common/ODD/script/;./run_rosbag.sh'.format(TEST_CASE_PATH),
                        'start_cmd_rviz': 'cd {0}/common/ODD/script/;./run_rosbag_rviz.sh'.format(TEST_CASE_PATH),
                        },
    'test_planning': {'ros1_docker_ip': '127.0.0.1', 'ros1_docker_user': '', 'ros1_docker_pwd': '',
                      'ros1_container_name': 'runtime', 'ros1_aw4_workspace': '/ros1_workspace',
                      'ros2_docker_ip': '127.0.0.1', 'ros2_docker_user': '', 'ros2_docker_pwd': '',
                      'ros2_container_name': 'runtime-ros2', 'ros2_aw4_workspace': '/AutowareArchitectureProposal',
                      'master_uri': 'http://127.0.0.1:11311',
                      'node_list': PLANNING_NODES,
                      'start_cmd': 'cd {0}/common/ODD/script/;./run_psim.sh'.format(TEST_CASE_PATH),
                      'start_cmd_rviz': 'cd {0}/common/ODD/script/;./run_psim_rviz.sh'.format(TEST_CASE_PATH)
                      },
    'test_future_way': {'ros1_docker_ip': '127.0.0.1', 'ros1_docker_user': '/ros1_workspace', 'ros1_docker_pwd': '',
                          'ros1_container_name': 'runtime', 'ros1_aw4_workspace': '',
                          'ros2_docker_ip': '127.0.0.1', 'ros2_docker_user': '', 'ros2_docker_pwd': '',
                          'ros2_container_name': 'runtime-ros2', 'ros2_aw4_workspace': '/AutowareArchitectureProposal',
                          'master_uri': 'http://127.0.0.1:11311',
                          'node_list': PERCEPTION_NODE_LIST,
                          'start_cmd': 'cd {0}/common/ODD/script/;./run_rosbag.sh'.format(TEST_CASE_PATH),
                          'start_cmd_rviz': 'cd {0}/common/ODD/script/;./run_rosbag_rviz.sh'.format(TEST_CASE_PATH)
                          },
}

AW4_RUN_STATUS = {
    1: 'docker stopped',
    2: 'docker and aw4 are running ',
    3: 'docker is running, but aw4 is not ok'
}

RVIZ = False  # True show rviz

ROS1_SETUP = '/opt/ros/noetic/setup.bash'
ROS2_SETUP = '/opt/ros/foxy/setup.bash'

# csv cases path
ODD_CSV_CASES = '{}/testcases/test_ODD/cases'.format(TEST_CASE_PATH)
