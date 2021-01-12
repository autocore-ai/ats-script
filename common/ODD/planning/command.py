from config import TEST_CASE_PATH
from common.ODD.planning import PLANNING_AUTOWARE4_IP, PLANNING_ROS_MASTER_URI, PLANNING_AUTOWARE4_DEVEL

# ====================== Planning command ======================

START_AUTOWARE_4_PLANNING = 'cd {};./start_planning_test.sh'.format(PLANNING_AUTOWARE4_DEVEL)

START_PLANNING_DOCKER = 'export ROS_IP={};export ROS_MASTER_URI={};{}/common/script/run_docker_sim.sh'. \
    format(PLANNING_AUTOWARE4_IP, PLANNING_ROS_MASTER_URI, TEST_CASE_PATH)

START_DOCKER_4_PLANNING = '{}/common/script/run_psim.sh'.format(TEST_CASE_PATH)

START_DOCKER_4_PLANNING_RVIZ = '{}/common/script/run_psim_rviz.sh'.format(TEST_CASE_PATH)

PLANNING_DOCKER_NAME = 'runtime'

PLANNING_TOPICS = ['/autoware/engage\n', '/autoware/state\n',
                   '/checkpoint\n', '/client_count\n', '/connected_clients\n',
                   '/control/control_cmd\n', '/control/lateral/control_cmd\n',
                   '/control/longitudinal/control_cmd\n',
                   '/control/mpc_follower/debug/steering_cmd\n',
                   '/control/mpc_follower/parameter_descriptions\n',
                   '/control/mpc_follower/parameter_updates\n', '/control/vehicle_cmd\n',
                   '/control/velocity_controller/debug_values\n', '/lane_change_approval\n',
                   '/localization/twist\n', '/map/pointcloud_map\n', '/map/vector_map\n',
                   '/map/vector_map_marker\n', '/move_base_simple/goal\n',
                   '/perception/object_recognition/detection/objects\n',
                   '/perception/object_recognition/detection/objects/visualization\n',
                   '/perception/object_recognition/objects\n',
                   '/perception/object_recognition/objects/visualization\n',
                   '/perception/object_recognition/prediction/objects_path_markers\n',
                   '/perception/object_recognition/tracking/objects\n',
                   '/perception/object_recognition/tracking/objects/visualization\n',
                   '/perception/traffic_light_recognition/traffic_light_states\n',
                   '/planning/mission_planning/route\n', '/planning/mission_planning/route_marker\n',
                   '/planning/scenario_planning/lane_driving/behavior_planning'
                   '/behavior_velocity_planner/debug/blind_spot\n',
                   '/planning/scenario_planning/lane_driving/behavior_planning/'
                   'behavior_velocity_planner/debug/crosswalk\n',
                   '/planning/scenario_planning/lane_driving/behavior_planning/'
                   'behavior_velocity_planner/debug/intersection\n',
                   '/planning/scenario_planning/lane_driving/behavior_planning/'
                   'behavior_velocity_planner/debug/path\n',
                   '/planning/scenario_planning/lane_driving/behavior_planning/'
                   'behavior_velocity_planner/debug/stop_line\n',
                   '/planning/scenario_planning/lane_driving/behavior_planning/'
                   'behavior_velocity_planner/debug/traffic_light\n',
                   '/planning/scenario_planning/lane_driving/behavior_planning/'
                   'lane_change_planner/debug/drivable_area\n',
                   '/planning/scenario_planning/lane_driving/behavior_planning/'
                   'lane_change_planner/debug/predicted_path_markers\n',
                   '/planning/scenario_planning/lane_driving/behavior_planning/'
                   'lane_change_planner/input/force_lane_change\n',
                   '/planning/scenario_planning/lane_driving/behavior_planning/path\n',
                   '/planning/scenario_planning/lane_driving/behavior_planning/path_with_lane_id\n',
                   '/planning/scenario_planning/lane_driving/lane_change_available\n',
                   '/planning/scenario_planning/lane_driving/lane_change_ready\n',
                   '/planning/scenario_planning/lane_driving/motion_planning/'
                   'obstacle_avoidance_planner/debug/clearance_map\n',
                   '/planning/scenario_planning/lane_driving/motion_planning/'
                   'obstacle_avoidance_planner/debug/marker\n',
                   '/planning/scenario_planning/lane_driving/motion_planning/'
                   'obstacle_avoidance_planner/debug/object_clearance_map\n',
                   '/planning/scenario_planning/lane_driving/motion_planning/'
                   'obstacle_avoidance_planner/enable_avoidance\n',
                   '/planning/scenario_planning/lane_driving/motion_planning/obstacle_avoidance_planner/trajectory\n',
                   '/planning/scenario_planning/lane_driving/motion_planning/obstacle_stop_planner/debug/marker\n',
                   '/planning/scenario_planning/lane_driving/trajectory\n',
                   '/planning/scenario_planning/motion_velocity_optimizer/closest_velocity\n',
                   '/planning/scenario_planning/motion_velocity_optimizer/'
                   'debug/trajectory_external_velocity_limitted\n',
                   '/planning/scenario_planning/motion_velocity_optimizer/debug/trajectory_lateral_acc_filtered\n',
                   '/planning/scenario_planning/motion_velocity_optimizer/debug/trajectory_raw\n',
                   '/planning/scenario_planning/motion_velocity_optimizer/debug/trajectory_time_resampled\n',
                   '/planning/scenario_planning/motion_velocity_optimizer/distance_to_stopline\n',
                   '/planning/scenario_planning/motion_velocity_optimizer/external_velocity_limit_mps\n',
                   '/planning/scenario_planning/motion_velocity_optimizer/parameter_descriptions\n',
                   '/planning/scenario_planning/motion_velocity_optimizer/parameter_updates\n',
                   '/planning/scenario_planning/parking/costmap_generator/grid_map\n',
                   '/planning/scenario_planning/parking/costmap_generator/occupancy_grid\n',
                   '/planning/scenario_planning/parking/freespace_planner/debug/partial_pose_array\n',
                   '/planning/scenario_planning/parking/freespace_planner/debug/pose_array\n',
                   '/planning/scenario_planning/parking/trajectory\n',
                   '/planning/scenario_planning/scenario\n',
                   '/planning/scenario_planning/scenario_selector/trajectory\n',
                   '/planning/scenario_planning/trajectory\n', '/rosout\n', '/rosout_agg\n',
                   '/sensing/lidar/no_ground/pointcloud\n', '/tf\n', '/tf_static\n', '/vehicle/engage\n',
                   '/vehicle/status/steering\n', '/vehicle/status/twist\n', '/vehicle/turn_signal_cmd\n',
                   '/web_controller/manual_overide_traffic_light_colour\n']


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

