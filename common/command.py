# -*- coding:utf8 -*-
"""
命令
"""
from config import PCU_IP, LOCAL_IP, TEST_IP
from common.perception_conf import PERCEPTION_IP, PERCEPTION_ROS_MASTER_URI, PERCEPTION_BAG_REMOTE_IP, PERCEPTION_AUTOWARE4_DEVEL
# ====================== source env ======================
SOURCE_1 = 'source /opt/ros/melodic/setup.bash'
SOURCE_2 = 'source /opt/autocore/ros1_ws/setup.bash'
EXPORT_IP = 'export ROS_IP={}'.format(PCU_IP)
EXPORT_MASTER = 'export ROS_MASTER_URI=http://{}:11311/'.format(PCU_IP)
EXPORT_LOCAL_IP = 'export ROS_IP={}'.format(LOCAL_IP)


# ====================== local command ======================
ROS_PLAY_BAG_MAP = '{0};{1};{2};$(nohup bag play /home/duan/PycharmProjects/auto_test/bag/make_map.bag  > /dev/null 2>&1 &) && sleep 1'.format(SOURCE_1, EXPORT_LOCAL_IP,
                                                                                             EXPORT_MASTER)

# ====================== launch command ======================
RADAR_MAPPING = '{};{};{};{}; $(nohup roslaunch radar_mapping radar_mapping.launch cellWidth:=1.0 radar_back_right_topic:=/radar408_raw2 point_map_path:=/opt/autocore/test_data/map radar_front_topic:=/radar408_raw1 keyFrameStep:=5.0 gps_topic:=/map_navsatfix cellPointNumThreshold:=3 distanceThreshold:=30.0 radar_back_left_topic:=/radar408_raw3 point_map_topic:=/radar_map cellHeight:=3  > /dev/null 2>&1 &) && sleep 3'.\
                format(SOURCE_1, SOURCE_2, EXPORT_IP, EXPORT_MASTER)

RADAR_PF_LOCALIZER = '{};{};{};{}; $(roslaunch radar_pf_localizer radar_pf_localizer.launch line_x_dev_:=2.0 tf_br_yaw_:=-2.5 gps_lat_dev_:=0.5 tf_fm_y_:=0 utm_path_:=%s tf_bl_y_:=0.90 tf_br_y_:=-0.9 angle_z_dev_:=0.000017 tf_bl_x_:=-1.85 tf_br_x_:=-1.85 particles_pro_dis_:=10 map_dir_:=%s tf_fm_yaw_:=0 sigma_hit_:=0.5 gps_lon_dev_:=0.2 map_scale_:=0.5 particles_num_from_gps_:=1000 tf_bl_yaw_:=2.42 particles_num_for_pf_:=2000 tf_fm_x_:=2.85 > %s 2>&1 &) && sleep 3'.\
    format(SOURCE_1, SOURCE_2, EXPORT_IP, EXPORT_MASTER)

# ====================== Perception command ======================
# START_AUTOWARE_4 = 'roslaunch autoware_launch autoware.launch map_path:=/home/duan/AutowareArchitectureProposal/lishui_new rosbag:=true'
# START_AUTOWARE_4 = 'cd ~/AutowareArchitectureProposal;./start_bag_test.sh'
# CHECK_AUTOWARE_4 = 'ps -ef| grep Autoware | grep -v grep'
# START_AUTOWARE_4 = 'cd ~/workspace/test_autoware/AutowareArchitectureProposal;$(nohup ./start_bag_test.sh > /dev/null 2>&1 &) && sleep 1'
AUTOWARE_SCREEN_NAME = 'autoware_test'
START_AUTOWARE_4 = 'cd ~/workspace/test_autoware/AutowareArchitectureProposal;screen -d -m -S {} ./start_bag_test.sh'.format(AUTOWARE_SCREEN_NAME)
# START_AUTOWARE_4 = 'export ROS_IP={};ROS_MASTER_URI={};cd ~/workspace/test_autoware/AutowareArchitectureProposal;./start_bag_test.sh'.format(TEST_IP, PERCEPTION_ROS_MASTER_URI, AUTOWARE_SCREEN_NAME)
CHECK_AUTOWARE_4 = 'screen -ls| grep {}'.format(AUTOWARE_SCREEN_NAME)
STOP_AUTOWARE_4 = 'screen -S {} -X quit'.format(AUTOWARE_SCREEN_NAME)

# START_AUTOWARE_4 = 'roscore'
# START_PERCEPTION = 'cd /home/nv/workspace/autoware4-xavier;$(nohup ./run_perception.sh > /dev/null 2>&1 &) && sleep 1'
# START_PERCEPTION = 'cd ~/workspace;$(nohup ./run_autoware4_perception.sh > /dev/null 2>&1 &) && sleep 1'
PERCEPTION_DOCKER_NAME = 'devel'
START_PERCEPTION = 'cd ~/workspace;screen -d -m -S perception-test ./run_autoware4_perception.sh'
CHECK_PERCEPTION_DOCKER = 'docker inspect -f {{.Name}} $(docker ps -q) | grep %s' % PERCEPTION_DOCKER_NAME
CHECK_PERCEPTION_NODE = 'docker exec {} /bin/bash -c \'source /opt/ros/melodic/setup.bash && source /root/autoware4/devel/setup.bash && export ROS_IP=192.168.50.98 && export ROS_MASTER_URI=http://192.168.50.235:11311 && rosnode list | grep perception\''.format(PERCEPTION_DOCKER_NAME)
STOP_PERCEPTION = 'cd ~/workspace;screen -S perception-test -X quit'
# START_PERCEPTION = 'cd /home/nv/NVME/aw_debug/perception/perception_radar_v2/autoware4-xavier;source devel/setup.bash;export ROS_MASTER_URI=http://192.168.10.79:11311;$(nohup /home/nv/NVME/aw_debug/perception/perception_radar_v2/autoware4-xavier/run_perception.sh > /dev/null 2>&1 &) && sleep 1'
# START_PERCEPTION = 'cd /home/nv/NVME/aw_debug/perception/perception_radar_v2/autoware4-xavier;source devel/setup.bash;export ROS_IP=192.168.10.68;export ROS_MASTER_URI=http://192.168.10.79:11311;screen -d -m -S percetion-test /home/nv/NVME/aw_debug/perception/perception_radar_v2/autoware4-xavier/run_perception.sh'
# START_PERCEPTION = 'export ROS_IP={};ROS_MASTER_URI={};cd /home/nv/workspace/autoware4-xavier;./run_perception.sh'.format(PERCEPTION_IP, PERCEPTION_ROS_MASTER_URI)





# ====================== rosbag command ======================
# bag记录全名
# ROSBAG_RECORD_O = 'export ROS_IP=%s;ROS_MASTER_URI=%s;source ~/AutowareArchitectureProposal/devel/setup.bash;$(nohup rosbag record -O {} --duration {} {} > /dev/null 2>&1 &) && sleep 1' % (TEST_IP, PERCEPTION_ROS_MASTER_URI)
# ROSBAG_RECORD_O = 'export ROS_IP=%s;ROS_MASTER_URI=%s;source ~/AutowareArchitectureProposal/devel/setup.bash;rosbag record -O {} --duration {} {}' % (TEST_IP, PERCEPTION_ROS_MASTER_URI)
# local record cmd
ROSBAG_RECORD_O = 'export ROS_IP=%s;ROS_MASTER_URI=%s;source ~/AutowareArchitectureProposal/devel/setup.bash;rosbag record -O {name} --duration {t} {topic}' % (TEST_IP, PERCEPTION_ROS_MASTER_URI)
ROSBAG_RECORD_O_REMOTE = 'export ROS_IP=%s;ROS_MASTER_URI=%s;source %s/devel/setup.bash;screen -d -m -S record_test rosbag record -O {name} --duration {t} {topic}' % (PERCEPTION_BAG_REMOTE_IP, PERCEPTION_ROS_MASTER_URI, PERCEPTION_AUTOWARE4_DEVEL)
ROSBAG_PLAY = 'export ROS_IP=%s;export ROS_MASTER_URI=%s;rosbag play {bag_path} --clock' % (TEST_IP, PERCEPTION_ROS_MASTER_URI)
ROSBAG_PLAY_REMOTE = 'export ROS_IP=%s;export ROS_MASTER_URI=%s;source %s/devel/setup.bash;rosbag play {bag_path} --clock' % (PERCEPTION_BAG_REMOTE_IP, PERCEPTION_ROS_MASTER_URI, PERCEPTION_AUTOWARE4_DEVEL)


# ====================== Planning command ======================

LOCAL_JIRA_PLANNING_FILE_PATH = "/home/minwei/autotest/testcases/test_ODD/cases/planning_cases.csv"
LOCAL_GT_BAG_PATH = "/home/minwei/autotest/bags/planning_bags/groundtruth_bags/"
LOCAL_TEST_BAG_PATH = "/home/minwei/autotest/bags/planning_bags/test_bags/"
