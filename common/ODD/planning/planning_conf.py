# -*- coding:utf8 -*-

# @Time : DATEDATE{TIME}
# @File : planning_conf.py
from config import TEST_CASE_PATH

PLANNING_AUTOWARE4_IP = '127.0.0.1'  # as master
PLANNING_AUTOWARE4_USER = ''
PLANNING_AUTOWARE4_PWD = ''
PLANNING_AUTOWARE4_DEVEL = ''

PLANNING_ROS_MASTER_URI = 'http://{}:11311'.format(PLANNING_AUTOWARE4_IP)

LOCAL_JIRA_PLANNING_FILE_PATH = '{}/testcases/test_ODD/cases/planning_cases.csv'. \
    format(TEST_CASE_PATH)

PLANNING_BAG_PATH = "{}/bags/planning/". \
    format(TEST_CASE_PATH)
PLANNING_BAG_PATH_OPEN = '{}/bags/planning_open'. \
    format(TEST_CASE_PATH)  # record bags, play bags path

# PLANNING_NODES = [
#     # 'autoware_engage_relay',
#     '/awapi_awiv_adapter_node',
#     '/control/remote_cmd_converter',
#     '/control/shift_decider',
#     '/control/trajectory_follower/latlon_muxer',
#     '/control/trajectory_follower/mpc_follower',
#     '/control/trajectory_follower/transform_listener_impl',
#     '/control/trajectory_follower/velocity_controller',
#     '/control/vehicle_cmd_gate',
#     '/emergency_relay',
#     '/force_lane_change_relay',
#     '/gate_mode_relay',
#     '/lane_change_approval_relay',
#     '/map/lanelet2_map_loader',
#     '/map/lanelet2_map_visualization',
#     '/map/map_tf_generator',
#     '/map/pointcloud_map_loader',
#     '/obstacle_avoid_approval_relay',
#     '/perception/object_recognition/prediction/dynamic_object_visualization',
#     '/perception/object_recognition/prediction/map_based_prediction',
#     '/perception/object_recognition/prediction/transform_listener_impl',
#     '/perception/object_recognition/tracking/dynamic_object_visualization',
#     '/perception/object_recognition/tracking/multi_object_tracker',
#     '/perception/object_recognition/tracking/transform_listener_impl',
#     '/planning/mission_planning/mission_planner',
#     '/planning/mission_planning/transform_listener_impl',
#     '/planning/scenario_planning/lane_driving/behavior_planning/behavior_velocity_planner',
#     '/planning/scenario_planning/lane_driving/behavior_planning/lane_change_planner',
#     '/planning/scenario_planning/lane_driving/behavior_planning/transform_listener_impl',
#     '/planning/scenario_planning/lane_driving/behavior_planning/turn_signal_decider',
#     '/planning/scenario_planning/lane_driving/motion_planning/obstacle_avoidance_planner',
#     '/planning/scenario_planning/lane_driving/motion_planning/obstacle_stop_planner',
#     '/planning/scenario_planning/lane_driving/motion_planning/surround_obstacle_checker',
#     '/planning/scenario_planning/lane_driving/motion_planning/transform_listener_impl',
#     '/planning/scenario_planning/motion_velocity_optimizer',
#     '/planning/scenario_planning/parking/costmap_generator',
#     '/planning/scenario_planning/parking/freespace_planner',
#     '/planning/scenario_planning/parking/transform_listener_impl',
#     '/planning/scenario_planning/scenario_selector',
#     '/planning/scenario_planning/transform_listener',
#     '/predict_object_relay',
#     '/put_route_relay',
#     '/robot_state_publisher',
#     '/rosbridge_server_node',
#     '/route_relay',
#     '/rviz2',
#     '/simple_planning_simulator',
#     '/simulation/dummy_perception_publisher',
#     '/simulation/shape_estimation',
#     '/simulation/transform_listener_impl',
#     '/system/aggregator_node',
#     '/system/autoware_error_monitor',
#     '/system/autoware_state_monitor',
#     '/system/transform_listener_impl',
#     '/transform_listener_imp',
#     '/twist_relay',
#     '/upper_vel_relay',
#     '/vehicle_engage_relay',
# ]


PLANNING_NODES = [





]


