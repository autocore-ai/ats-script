# -*- coding: utf-8 -*-
"""
Perception 模块 case
"""

import allure
import pytest
import time
import logging
import os
import subprocess
from rosbag import rosbag_main

from common.generate_case_data import generate_case_data
from common.command import ROSBAG_RECORD_O
from run import SEVERITY
from config import TEST_CASE_PATH, REMOTE_TEST_DATA, TEST_REPORT_LOG, TEST_CASE_LINK
from common.perception_bag_analysis import Analysis

logger = logging.getLogger()

CASE_LIST = generate_case_data('{}/testcases/test_ODD/cases/perception.csv'.format(TEST_CASE_PATH))
BAG_BASE_PATH = '{}bag'.format(TEST_CASE_PATH)
CASE_CURRENT_DIR = os.path.split(__file__)[0].split('testcases/')[-1]
CASE_FILE_NAME = os.path.split(__file__)[-1].split('.')[0]
CASE_PATH = '{}{}/{}'.format(TEST_REPORT_LOG, CASE_CURRENT_DIR, CASE_FILE_NAME)
print(CASE_LIST)


# 动态生成测试用例
def make_test_case(story, case_data, case_level, case_desc, jira_id):
    print('用例日志连接：{}/{}/{}_JiraID_{}.log'.format(CASE_PATH, 'test_perception', 'test_perception', jira_id))

    # 此处可以用变量装饰了
    @allure.feature('perception')
    @pytest.mark.parametrize("case_data", case_data, ids=[case_desc])
    @allure.story(story)
    @allure.severity(case_level)
    @allure.link('{}/{}/{}_JiraID_{}.log'.format(CASE_PATH, 'test_perception', 'test_perception', jira_id), name='用例日志地址')
    # @allure.testcase("https://autocore.atlassian.net/plugins/servlet/ac/com.infostretch.QmetryTestManager/qtm4j-test-management?project.key=AO&project.id=10005")  # 用例连接地址
    def test_perception(start_perception_env, case_data):
        """
        测试步骤：
        1. 启动环境
        2. 准备记录bag, bag存放路径在bag目录下，具体bag名字对应的目录下
        3. 播放bag
        4. 分析bag
        5. 比较结果
        6. 关闭环境
        """
        bag_dir = '{}/{}'.format(BAG_BASE_PATH,  case_data['bag_name'].split('.bag')[0])

        # 记录障碍物的输出的bag
        perception_bag_result_path = '{}/{}'.format(bag_dir, 'result.bag')
        step_desc = 'record rosbag, new bag name: {}'.format(perception_bag_result_path)
        # 开始记录bag
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            # 记录bag 时间比原有播放时间长20s
            bag_record_time = int(case_data['bag_duration']) + 20
            record_comm = ROSBAG_RECORD_O.format(perception_bag_result_path, bag_record_time)
            logger.info('rosbag record command: {}'.format(record_comm))
            record_proc = subprocess.Popen(record_comm, shell=True)

        # 开始播放bag
        play_bag_path = '{}{}'.format(bag_dir, case_data['bag_name'])
        step_desc = 'play rosbag, bag path:{}'.format(play_bag_path)
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            # 播放bag，此命令会等待bag播完
            rosbag_main.play_cmd([play_bag_path, '--clock'])

        # 停止记录 rosbag
        step_desc = 'stop record rosbag'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            record_proc.terminate()

        # 分析记录的rosbag信息
        step_desc = 'analysis object bag data'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            bag_an = Analysis(perception_bag_result_path)
            assert bag_an.analysis()
            bag_data = bag_an.data_dict
            logger.info('object topic data: {}'.format(bag_data))
            allure.attach(bag_data, 'object topic data', allure.attachment_type.JSON)

        # 读取 groundtruth bag 数据
        step_desc = 'analysis expect object bag data'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            exp_bag_path = '{}/expect.bag'.format(perception_bag_result_path.split('/')[:-1])
            logger.info('expect object bag path: {}'.format(exp_bag_path))
            bag_an_exp = Analysis(perception_bag_result_path)
            assert bag_an_exp.analysis()
            bag_data_exp = bag_an_exp.data_dict
            logger.info('expect object topic data: {}'.format(bag_data_exp))
            allure.attach(bag_data_exp, 'expect object topic data', allure.attachment_type.JSON)

        # 和 groundtruth rosbag 作比较，消息数量
        step_desc = 'compare real bag with expect bag: msg count'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            real_count = bag_an.msg_count
            exp_count = bag_an_exp.msg_count
            allure.attach('expect: {}, real: {}'.format(exp_count, real_count), 'compare msg count', allure.attachment_type.TEXT)
            assert real_count in range(exp_count-10, exp_count+20), 'real object topic msg count is less 10 or more than 20 then expect msg count'

        # uuid compare
        step_desc = 'compare real bag with expect bag: uuid'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            real_count = bag_an.msg_count
            exp_count = bag_an_exp.msg_count
            allure.attach('expect: {}, real: {}'.format(exp_count, real_count), 'compare msg count',
                          allure.attachment_type.TEXT)
            assert real_count in range(exp_count - 10,
                                       exp_count + 20), 'real object topic msg count is less 10 or more than 20 then expect msg count'

    # 关闭环境

    # 把生成的函数返回
    return test_perception


for case_arg in CASE_LIST:
    globals()[case_arg['fun_name']] = make_test_case(case_arg['Story'], [case_arg['test_data']],
                                                     case_arg['Priority'], case_arg['Title'],
                                                     case_arg['Jira_ID'])


if __name__ == '__main__':

    args = ['--allure-stories', 'child', '--alluredir', './allure_reports/allure']
    pytest.main(args)
