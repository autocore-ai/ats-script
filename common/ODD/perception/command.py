# -*- coding:utf8 -*-
from config import TEST_IP
from common.ODD.perception.perception_conf import *

AUTOWARE_SCREEN_NAME = 'autoware_test'
# START_AUTOWARE_4 = 'cd {};export ROS_IP={};export ROS_MASTER_URI={};' \
#                    'screen -d -m -S {} ./start_bag_test.sh'.format(PERCEPTION_AUTOWARE4_DEVEL, PERCEPTION_AUTOWARE4_IP,
#                                                                    PERCEPTION_ROS_MASTER_URI, AUTOWARE_SCREEN_NAME)
# CHECK_AUTOWARE_4 = 'screen -ls| grep {}'.format(AUTOWARE_SCREEN_NAME)
# CHECK_AUTOWARE_4_NODES = 'source {}/devel/setup.bash;export ROS_IP={};export ROS_MASTER_URI={};' \
#                          'rosnode list'.format(PERCEPTION_AUTOWARE4_DEVEL, PERCEPTION_AUTOWARE4_IP,
#                                                PERCEPTION_ROS_MASTER_URI)
AUTOWARE_4_NODES_LIST = ['rviz']
STOP_AUTOWARE_4 = 'screen -S {} -X quit'.format(AUTOWARE_SCREEN_NAME)

PERCEPTION_DOCKER_NAME = 'devel'
START_PERCEPTION = 'cd {}/common/script/;export ROS_IP={};export ROS_MASTER_URI={};' \
                   'screen -d -m -S perception-test ./run_autoware4_perception.sh'.format(TEST_CASE_PATH,
                                                                                          PERCEPTION_IP,
                                                                                          PERCEPTION_ROS_MASTER_URI)
CHECK_PERCEPTION_DOCKER = 'docker ps | grep %s' % PERCEPTION_DOCKER_NAME
CHECK_PERCEPTION_NODE = 'docker exec {} /bin/bash -c \'source /opt/ros/melodic/setup.bash && ' \
                        'source /root/autoware4/devel/setup.bash && export ROS_IP={} && ' \
                        'export ROS_MASTER_URI={} && rosnode list | grep perception\''.format(PERCEPTION_DOCKER_NAME,
                                                                                              PERCEPTION_IP,
                                                                                              PERCEPTION_ROS_MASTER_URI)
PERCEPTION_NODES_LIST = ['perception']
STOP_PERCEPTION = 'cd ~/workspace;screen -S perception-test -X quit'

# local record cmd
ROSBAG_RECORD_O = 'export ROS_IP=%s;ROS_MASTER_URI=%s;rosbag record -O {name} ' \
                  '--duration {t} {topic}' % (TEST_IP, PERCEPTION_ROS_MASTER_URI)
# ROSBAG_RECORD_O_REMOTE = 'export ROS_IP=%s;ROS_MASTER_URI=%s;screen -d -m -S ' \
#                          'record_test rosbag record -O {name} --duration {t} {topic}' % \
#                          (PERCEPTION_BAG_REMOTE_IP, PERCEPTION_ROS_MASTER_URI)
ROSBAG_PLAY = 'export ROS_IP=%s;export ROS_MASTER_URI=%s;rosbag play {bag_path} --clock' %\
              (TEST_IP, PERCEPTION_ROS_MASTER_URI)
# ROSBAG_PLAY_REMOTE = 'export ROS_IP=%s;export ROS_MASTER_URI=%s;source %s;rosbag play {bag_path} ' \
#                      '--clock' % (PERCEPTION_BAG_REMOTE_IP, PERCEPTION_ROS_MASTER_URI, ROS1_SETUP)
