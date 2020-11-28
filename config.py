# -*- coding:utf8 -*-
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

PCU_IP = '192.168.1.102'
PCU_USER = 'user'
PCU_PWD = 'user'
LOCAL_IP = '192.168.1.33'

REMOTE_TEST_DATA = '/opt/autocore/test_data/'  # PCU存放测试数据的路径
# TEST_CASE_PATH = '/home/duan/PycharmProjects/auto_test/'  # 测试用例所在目录
TEST_CASE_PATH = '{}'.format(CURRENT_DIR)  # test script path

TEST_REPORT_LOG = 'data/attachments/logs/'  # 测试日志在报告中的位置，相对路径
TEST_CASE_LINK = 'https://gitlab.com/autocore/AutoTest/autotest/-/tree/master'

TEST_IP = '127.0.0.1'

SEVERITY = ['normal', 'minor']  # 设置需要执行的用例级别

