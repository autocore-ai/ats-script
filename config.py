# -*- coding:utf8 -*-

PCU_IP = '192.168.1.102'
PCU_USER = 'user'
PCU_PWD = 'user'
LOCAL_IP = '192.168.1.33'

REMOTE_TEST_DATA = '/opt/autocore/test_data/'  # PCU存放测试数据的路径
TEST_CASE_PATH = '/home/duan/PycharmProjects/auto_test/'  # 测试用例所在目录

TEST_REPORT_LOG = 'data/attachments/logs/'  # 测试日志在报告中的位置，相对路径
TEST_CASE_LINK = 'https://gitlab.com/autocore/AutoTest/autotest/-/tree/master'

# ====================== Perception ENV ======================
# master info
PERCEPTION_ROS_MASTER_URI = 'http://192.168.10.29:11311'

# perception server info
PERCEPTION_IP = '192.168.10.64'
PERCEPTION_USER = 'ac'
PERCEPTION_PWD = 'a'

# ====================== Planning ENV ======================



SEVERITY = ['normal', 'minor']  # 设置需要执行的用例级别
