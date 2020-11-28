# -*- coding:utf8 -*-
"""
命令
"""
from config import PCU_IP, LOCAL_IP, TEST_IP, TEST_CASE_PATH
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
