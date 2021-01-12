# -*- coding:utf8 -*-

# @Time : DATEDATE{TIME}
# @File : planning_conf.py
from config import TEST_CASE_PATH

PLANNING_AUTOWARE4_IP = '127.0.0.1'  # as master
PLANNING_AUTOWARE4_USER = ''
PLANNING_AUTOWARE4_PWD = ''
PLANNING_AUTOWARE4_DEVEL = ''

PLANNING_ROS_MASTER_URI = 'http://{}:11311'.format(PLANNING_AUTOWARE4_IP)

LOCAL_JIRA_PLANNING_FILE_PATH = '{}/testcases/test_ODD/cases/planning_cases_open.csv'. \
    format(TEST_CASE_PATH)

PLANNING_BAG_PATH = "{}/bags/planning/". \
    format(TEST_CASE_PATH)
PLANNING_BAG_PATH_OPEN = '{}/bags/planning_open'. \
    format(TEST_CASE_PATH)  # record bags, play bags path

PLANNING_NODES = ['/autoware_state_monitor\n', '/control/latlon_muxer\n',
                  '/control/mpc_follower\n', '/control/vehicle_cmd_gate\n',
                  '/control/velocity_controller\n', '/map/lanelet2_map_loader\n',
                  '/map/lanelet2_map_visualization\n', '/map/map_tf_generator\n',
                  '/map/pointcloud_map_loader\n',
                  '/perception/object_recognition/',
                  '/perception/object_recognition/prediction/map_based_prediction\n',
                  '/perception/object_recognition/tracking/multi_object_tracker\n',
                  '/planning/mission_planning/mission_planner\n',
                  '/planning/scenario_planning/lane_driving/behavior_planning/auto_approve_lane_change\n',
                  '/planning/scenario_planning/lane_driving/behavior_planning/behavior_velocity_planner\n',
                  '/planning/scenario_planning/lane_driving/behavior_planning/lane_change_planner\n',
                  '/planning/scenario_planning/lane_driving/behavior_planning/turn_signal_decider\n',
                  '/planning/scenario_planning/lane_driving/motion_planning/obstacle_avoidance_planner\n',
                  '/planning/scenario_planning/lane_driving/motion_planning/obstacle_stop_planner\n',
                  '/planning/scenario_planning/motion_velocity_optimizer\n',
                  '/planning/scenario_planning/parking/costmap_generator\n',
                  '/planning/scenario_planning/parking/freespace_planner\n',
                  '/planning/scenario_planning/scenario_selector\n', '/robot_state_publisher\n',
                  '/rosapi\n', '/rosbridge_websocket\n', '/rosout\n', '/simulation_vehicle_engage_publisher\n']
