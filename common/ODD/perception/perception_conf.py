# -*- coding:utf8 -*-
from config import TEST_CASE_PATH
# master info
PERCEPTION_IP = '127.0.0.1'
# if perception docker is same with test code, user and pwd can be empty
PERCEPTION_USER = ''
PERCEPTION_PWD = ''
# aw4 perception workspace
PERCEPTION_WORKSPACE = ''
# if perception startup by docker, it will be invalid
PERCEPTION_ROS_MASTER_URI = 'http://{}:11311'.format(PERCEPTION_IP)

# test perception node list
PERCEPTION_NODE_LIST = [
    '/aggregator_node',
    '/control/remote_cmd_converter',
    '/control/shift_decider',
    '/control/trajectory_follower/latlon_muxer',
    '/control/trajectory_follower/mpc_follower',
    '/control/trajectory_follower/velocity_controller',
    '/control/vehicle_cmd_gate',
    '/localization/pose_estimator/ndt_scan_matcher',
    '/localization/pose_twist_fusion_filter/ekf_localizer',
    '/localization/relay',
    '/localization/twist_estimator/gyro_odometer',
    '/localization/util/crop_box_filter_mesurement_range',
    '/localization/util/pose_initializer',
    '/localization/util/voxel_grid_filter',
    '/map/lanelet2_map_loader',
    '/map/lanelet2_map_visualization',
    '/map/map_tf_generator',
    '/map/pointcloud_map_loader',
    '/perception/object_recognition/detection/dynamic_object_visualization',
    '/perception/object_recognition/detection/lidar_apollo_instance_segmentation',
    '/perception/object_recognition/detection/shape_estimation',
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
    '/robot_state_publisher',
    '/rosapi',
    '/rosbridge_websocket',
    '/rosout',
    '/roswww',
    '/sensing/camera/traffic_light/tl_camera_info_relay',
    '/sensing/camera/traffic_light/tl_compressed_image_relay',
    '/sensing/gnss/gnss_poser',
    '/sensing/imu/relay',
    '/sensing/lidar/concatenate_data',
    '/sensing/lidar/crop_box_filter',
    '/sensing/lidar/left/velodyne_nodelet_manager',
    '/sensing/lidar/left/velodyne_nodelet_manager_cloud',
    '/sensing/lidar/left/velodyne_nodelet_manager_crop_box_filter_mirror',
    '/sensing/lidar/left/velodyne_nodelet_manager_crop_box_filter_self',
    '/sensing/lidar/left/velodyne_nodelet_manager_fix_distortion',
    '/sensing/lidar/left/velodyne_nodelet_manager_ring_outlier_filter',
    '/sensing/lidar/lidar_nodelet_manager',
    '/sensing/lidar/ray_ground_filter',
    '/sensing/lidar/rear/velodyne_nodelet_manager',
    '/sensing/lidar/rear/velodyne_nodelet_manager_cloud',
    '/sensing/lidar/rear/velodyne_nodelet_manager_crop_box_filter_mirror',
    '/sensing/lidar/rear/velodyne_nodelet_manager_crop_box_filter_self',
    '/sensing/lidar/rear/velodyne_nodelet_manager_fix_distortion',
    '/sensing/lidar/rear/velodyne_nodelet_manager_ring_outlier_filter',
    '/sensing/lidar/relay',
    '/sensing/lidar/right/velodyne_nodelet_manager',
    '/sensing/lidar/right/velodyne_nodelet_manager_cloud',
    '/sensing/lidar/right/velodyne_nodelet_manager_crop_box_filter_mirror',
    '/sensing/lidar/right/velodyne_nodelet_manager_crop_box_filter_self',
    '/sensing/lidar/right/velodyne_nodelet_manager_fix_distortion',
    '/sensing/lidar/right/velodyne_nodelet_manager_ring_outlier_filter',
    '/sensing/lidar/top/velodyne_nodelet_manager',
    '/sensing/lidar/top/velodyne_nodelet_manager_cloud',
    '/sensing/lidar/top/velodyne_nodelet_manager_crop_box_filter_mirror',
    '/sensing/lidar/top/velodyne_nodelet_manager_crop_box_filter_self',
    '/sensing/lidar/top/velodyne_nodelet_manager_fix_distortion',
    '/sensing/lidar/top/velodyne_nodelet_manager_ring_outlier_filter',
    '/system/autoware_error_monitor',
    '/system/autoware_state_monitor',
    '/system/emergency_handler'
]

# compare standard deviation and euclidean distance config
MSG_COUNT_STEP = 1000  # rosbag msg count step
UUID_STD_MAX = 1000
SEM_STD_MAX = 1000
PST_STEP = 500  # position point max step
PST_STD_MAX = 1000  # position max std
PST_DIS_MAX = 1000  # position max distance
ORI_STEP = 500  # orientation point max step
ORI_STD_MAX = 1000
ORI_DIS_MAX = 1000
LINE_STEP = 1000  # line speed point max step
LINE_STD_MAX = 1000
LINE_DIS_MAX = 1000
PRE_PATH_STEP = 1000  # prediction point max step
PRE_PATH_STD_MAX = 1000
PRE_PATH_DIS_MAX = 1000
PRE_PATH_ORI_DIS_MAX = 1000
SHAPE_STEP = 1000
SHAPE_STD_X_MAX = 1000
SHAPE_STD_Y_MAX = 1000
SHAPE_DIS_X_MAX = 1000
SHAPE_DIS_Y_MAX = 1000
