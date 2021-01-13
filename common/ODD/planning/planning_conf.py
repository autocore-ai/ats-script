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

PLANNING_NODES = [
    'aggregator_node',
    '/awapi/autoware_engage_relay',
    '/awapi/awapi_awiv_adapter',
    '/awapi/emergency_relay',
    '/awapi/force_lane_change_relay',
    '/awapi/force_obstacle_avoid_relay',
    '/awapi/gate_mode_relay',
    '/awapi/lane_change_approval_relay',
    '/awapi/obstacle_avoid_approval_relay',
    '/awapi/overwrite_traffic_light_state_relay',
    '/awapi/predict_object_relay',
    '/awapi/put_route_relay',
    '/awapi/route_relay',
    '/awapi/upper_vel_relay',
    '/awapi/vehicle_engage_relay',
    '/control/remote_cmd_converter',
    '/control/shift_decider',
    '/control/trajectory_follower/latlon_muxer',
    '/control/trajectory_follower/mpc_follower',
    '/control/trajectory_follower/velocity_controller',
    '/control/vehicle_cmd_gate',
    '/map/lanelet2_map_loader',
    '/map/lanelet2_map_visualization',
    '/map/map_tf_generator',
    '/map/pointcloud_map_loader',
    '/perception/object_recognition/dynamic_object_visualization',
    '/perception/object_recognition/prediction/dynamic_object_visualization',
    '/perception/object_recognition/prediction/map_based_prediction',
    '/perception/object_recognition/tracking/dynamic_object_visualization',
    '/perception/object_recognition/tracking/multi_object_tracker',
    '/perception/traffic_light_recognition/traffic_light_classifier',
    '/perception/traffic_light_recognition/traffic_light_image_decompressor',
    '/perception/traffic_light_recognition/traffic_light_map_based_detector',
    '/perception/traffic_light_recognition/traffic_light_recognition_nodelet_manager',
    '/perception/traffic_light_recognition/traffic_light_roi_visualizer',
    '/perception/traffic_light_recognition/traffic_light_ssd_fine_detector',
    '/planning/mission_planning/mission_planner',
    '/planning/scenario_planning/lane_driving/behavior_planning/auto_approve_lane_change',
    '/planning/scenario_planning/lane_driving/behavior_planning/behavior_velocity_planner',
    '/planning/scenario_planning/lane_driving/behavior_planning/lane_change_planner',
    '/planning/scenario_planning/lane_driving/behavior_planning/turn_signal_decider',
    '/planning/scenario_planning/lane_driving/motion_planning/obstacle_avoidance_planner',
    '/planning/scenario_planning/lane_driving/motion_planning/obstacle_stop_planner',
    '/planning/scenario_planning/lane_driving/motion_planning/surround_obstacle_checker',
    '/planning/scenario_planning/motion_velocity_optimizer',
    '/planning/scenario_planning/parking/costmap_generator',
    '/planning/scenario_planning/parking/freespace_planner',
    '/planning/scenario_planning/scenario_selector',
    '/relay',
    '/robot_state_publisher',
    '/rosapi',
    '/rosbridge_websocket',
    '/rosout',
    '/roswww',
    '/simple_planning_simulator',
    '/simulation/dummy_perception_publisher',
    '/simulation/shape_estimation',
    '/system/autoware_error_monitor',
    '/system/autoware_state_monitor',
    '/system/emergency_handler']
