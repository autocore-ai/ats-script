# -*- coding:utf8 -*-
from config import TEST_IP, TEST_CASE_PATH
from common.perception.perception_conf import PERCEPTION_ROS_MASTER_URI, PERCEPTION_BAG_REMOTE_IP,\
    PERCEPTION_AUTOWARE4_DEVEL, PERCEPTION_IP, PERCEPTION_AUTOWARE4_IP

# ====================== Perception command ======================
# START_AUTOWARE_4 = 'roslaunch autoware_launch autoware.launch map_path:=/home/duan/AutowareArchitectureProposal/lishui_new rosbag:=true'
# START_AUTOWARE_4 = 'cd ~/AutowareArchitectureProposal;./start_bag_test.sh'
# CHECK_AUTOWARE_4 = 'ps -ef| grep Autoware | grep -v grep'
# START_AUTOWARE_4 = 'cd ~/workspace/test_autoware/AutowareArchitectureProposal;$(nohup ./start_bag_test.sh > /dev/null 2>&1 &) && sleep 1'
AUTOWARE_SCREEN_NAME = 'autoware_test'
START_AUTOWARE_4 = 'cd {};export ROS_IP={};export ROS_MASTER_URI={};' \
                   'screen -d -m -S {} ./start_bag_test.sh'.format(PERCEPTION_AUTOWARE4_DEVEL, PERCEPTION_AUTOWARE4_IP,
                                                                   PERCEPTION_ROS_MASTER_URI, AUTOWARE_SCREEN_NAME)
# START_AUTOWARE_4_PLANNING = 'cd ~/workspace/test_autoware/AutowareArchitectureProposal;screen -d -m -S {} ./start_planning_test.sh'.format(AUTOWARE_SCREEN_NAME)
START_AUTOWARE_4_PLANNING = 'cd {};./start_planning_test.sh'.format(PERCEPTION_AUTOWARE4_DEVEL)
# START_AUTOWARE_4 = 'export ROS_IP={};ROS_MASTER_URI={};cd ~/workspace/test_autoware/AutowareArchitectureProposal;./start_bag_test.sh'.format(TEST_IP, PERCEPTION_ROS_MASTER_URI, AUTOWARE_SCREEN_NAME)
CHECK_AUTOWARE_4 = 'screen -ls| grep {}'.format(AUTOWARE_SCREEN_NAME)
CHECK_AUTOWARE_4_NODES = 'source {}/devel/setup.bash;export ROS_IP={};export ROS_MASTER_URI={};' \
                         'rosnode list'.format(PERCEPTION_AUTOWARE4_DEVEL, PERCEPTION_AUTOWARE4_IP,
                                               PERCEPTION_ROS_MASTER_URI)
AUTOWARE_4_NODES_LIST = ['planning']
STOP_AUTOWARE_4 = 'screen -S {} -X quit'.format(AUTOWARE_SCREEN_NAME)

# START_AUTOWARE_4 = 'roscore'
# START_PERCEPTION = 'cd /home/nv/workspace/autoware4-xavier;$(nohup ./run_perception.sh > /dev/null 2>&1 &) && sleep 1'
# START_PERCEPTION = 'cd ~/workspace;$(nohup ./run_autoware4_perception.sh > /dev/null 2>&1 &) && sleep 1'
PERCEPTION_DOCKER_NAME = 'devel'
START_PERCEPTION = 'cd {}/common/script/;export ROS_IP={};export ROS_MASTER_URI={};' \
                   'screen -d -m -S perception-test ./run_autoware4_perception.sh'.format(PERCEPTION_IP,
                                                                                          PERCEPTION_ROS_MASTER_URI,
                                                                                          TEST_CASE_PATH)
# CHECK_PERCEPTION_DOCKER = 'docker inspect -f {{.Name}} $(docker ps -q) | grep %s' % PERCEPTION_DOCKER_NAME
CHECK_PERCEPTION_DOCKER = 'docker ps | grep %s' % PERCEPTION_DOCKER_NAME
CHECK_PERCEPTION_NODE = 'docker exec {} /bin/bash -c \'source /opt/ros/melodic/setup.bash && ' \
                        'source /root/autoware4/devel/setup.bash && export ROS_IP={} && ' \
                        'export ROS_MASTER_URI={} && rosnode list | grep perception\''.format(PERCEPTION_DOCKER_NAME,
                                                                                              PERCEPTION_IP,
                                                                                              PERCEPTION_ROS_MASTER_URI)
PERCEPTION_NODES_LIST = ['perception']
STOP_PERCEPTION = 'cd ~/workspace;screen -S perception-test -X quit'
# START_PERCEPTION = 'cd /home/nv/NVME/aw_debug/perception/perception_radar_v2/autoware4-xavier;source devel/setup.bash;export ROS_MASTER_URI=http://192.168.10.79:11311;$(nohup /home/nv/NVME/aw_debug/perception/perception_radar_v2/autoware4-xavier/run_perception.sh > /dev/null 2>&1 &) && sleep 1'
# START_PERCEPTION = 'cd /home/nv/NVME/aw_debug/perception/perception_radar_v2/autoware4-xavier;source devel/setup.bash;export ROS_IP=192.168.10.68;export ROS_MASTER_URI=http://192.168.10.79:11311;screen -d -m -S percetion-test /home/nv/NVME/aw_debug/perception/perception_radar_v2/autoware4-xavier/run_perception.sh'
# START_PERCEPTION = 'export ROS_IP={};ROS_MASTER_URI={};cd /home/nv/workspace/autoware4-xavier;./run_perception.sh'.format(PERCEPTION_IP, PERCEPTION_ROS_MASTER_URI)

# ====================== rosbag command ======================
# bag记录全名
# ROSBAG_RECORD_O = 'export ROS_IP=%s;ROS_MASTER_URI=%s;source ~/AutowareArchitectureProposal/devel/setup.bash;$(nohup rosbag record -O {} --duration {} {} > /dev/null 2>&1 &) && sleep 1' % (TEST_IP, PERCEPTION_ROS_MASTER_URI)
# ROSBAG_RECORD_O = 'export ROS_IP=%s;ROS_MASTER_URI=%s;source ~/AutowareArchitectureProposal/devel/setup.bash;rosbag record -O {} --duration {} {}' % (TEST_IP, PERCEPTION_ROS_MASTER_URI)
# local record cmd
ROSBAG_RECORD_O = 'export ROS_IP=%s;ROS_MASTER_URI=%s;source %s/devel/setup.bash;rosbag record -O {name} --duration {t} {topic}' % (TEST_IP, PERCEPTION_ROS_MASTER_URI, PERCEPTION_AUTOWARE4_DEVEL)
ROSBAG_RECORD_O_REMOTE = 'export ROS_IP=%s;ROS_MASTER_URI=%s;source %s/devel/setup.bash;screen -d -m -S record_test rosbag record -O {name} --duration {t} {topic}' % (PERCEPTION_BAG_REMOTE_IP, PERCEPTION_ROS_MASTER_URI, PERCEPTION_AUTOWARE4_DEVEL)
ROSBAG_PLAY = 'export ROS_IP=%s;export ROS_MASTER_URI=%s;rosbag play {bag_path} --clock' % (TEST_IP, PERCEPTION_ROS_MASTER_URI)
ROSBAG_PLAY_REMOTE = 'export ROS_IP=%s;export ROS_MASTER_URI=%s;source %s/devel/setup.bash;rosbag play {bag_path} ' \
                     '--clock' % (PERCEPTION_BAG_REMOTE_IP, PERCEPTION_ROS_MASTER_URI, PERCEPTION_AUTOWARE4_DEVEL)

