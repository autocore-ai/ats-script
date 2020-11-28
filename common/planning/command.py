from config import TEST_IP, TEST_CASE_PATH
from common.planning.planning_conf import PLANNING_AUTOWARE4_IP, PLANNING_ROS_MASTER_URI, PLANNING_AUTOWARE4_DEVEL

#====================== Planning command ======================

START_AUTOWARE_4_PLANNING = 'cd {};./start_planning_test.sh'.format(PLANNING_AUTOWARE4_DEVEL)
START_PLANNING_DOCKER = 'export ROS_IP={};export ROS_MASTER_URI={};{}/common/script/run_docker_sim.sh'.format(PLANNING_AUTOWARE4_IP, PLANNING_ROS_MASTER_URI, TEST_CASE_PATH)


