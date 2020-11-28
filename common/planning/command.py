#====================== Planning command ======================

START_PLANNING_DOCKER = 'export ROS_IP={};export ROS_MASTER_URI={};{}/common/script/run_docker_sim.sh'.format(PLANNING_AUTOWARE4_IP, PLANNING_ROS_MASTER_URI, TEST_CASE_PATH)


