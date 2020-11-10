# -*- coding:utf8 -*-
import allure
import os, sys

sys.path.append('./../../')
print(sys.path)
from config import TEST_CASE_PATH, REMOTE_TEST_DATA, TEST_REPORT_LOG, TEST_CASE_LINK
from common.command import *
import logging
import time
import pytest
from common.process import *

logger = logging.getLogger()
CASE_CURRENT_DIR = os.getcwd().split('testcases/')[-1]
CASE_FILE_NAME = os.path.split(__file__)[-1].split('.')[0]
CASE_PATH = '{}{}/{}'.format(TEST_REPORT_LOG, CASE_CURRENT_DIR, CASE_FILE_NAME)

# con = pytest.importorskip('requests',  minversion='3')
# @con
def test_3(image_file):
    # pytest.importorskip('requests', minversion='3')
    logger.info('123123')
    logger.info(image_file)
    logger.info(sys.path[0])
    logger.info(os.getcwd())
    logger.info(__file__)
    logger.info('test3')
    assert 1 == 1


# 从下向上做笛卡尔积
@pytest.mark.parametrize('test_input', [1, 2, 3])
@pytest.mark.parametrize('test_output, expected', [(1, 2), (3, 4)])
def test_multi(test_input, test_output, expected):
    pass


@allure.feature('毫米波雷达')
class TestMap:
    """测试地图"""

    @allure.link('{}/{}/{}.log'.format(CASE_PATH, 'TestMap', 'test_a'), name='用例日志')
    def test_a(self):
        logger.info(os.getcwd())
        logger.info(CASE_CURRENT_DIR)
        logger.info('{}/logs/{}/{}'.format(TEST_CASE_PATH, CASE_CURRENT_DIR, self.__class__.__module__, self.__class__.__name__))
        logger.info('log_path: {}{}/{}/{}/'.format(TEST_REPORT_LOG, CASE_CURRENT_DIR, self.__class__.__module__,
                                                  self.__class__.__name__, sys._getframe().f_code.co_name))

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('毫米波雷达生成地图')
    @allure.link('{}/{}/{}.log'.format(CASE_PATH, 'TestMap', 'test_radar_to_map'), name='用例日志')
    @allure.testcase(TEST_CASE_LINK, '测试用例地址')
    @allure.title("radar生成点云地图")
    def test_radar_to_map(self, log_path, connect_pcu, clean_file):
        """
        测试radar输出点云地图
        1. SDK环境启动
        2. 清理环境,远程和本地的pcd,utm文件
        3. 测试脚本环境source,启动 radar_mapping
        4. play 带有毫米波雷达信息的rosbag
        5. 播放30s
        6. kill -9 bag
        7. kill -2 radar_mapping
        8. 检查远程文件是否生成
        9. 下载远程文件到本地
        10. 检查文件是否存在
        11. 检查utm文件是否正确
        12. 启动 radar_pf_localizer，sleep 1
        13. 停止 radar_pf_localizer
        14. 检测地图加载是否成功
        """
        logger.info('log_path: {}'.format(log_path))
        remote = connect_pcu

        # 3. 测试脚本环境source,启动 radar_mapping
        with allure.step('3. 测试脚本环境source,启动 radar_mapping'):
            logger.info('================= 3. PCU start radar_mapping =================')
            r_bool, desc = remote_start_process(remote, RADAR_MAPPING, 'radar_mapping', 3)
            assert r_bool, desc

        # 4. play 带有毫米波雷达信息的rosbag
        with allure.step('4. play 带有毫米波雷达信息的rosbag'):
            logger.info('================= 4. play bag with radar topic =================')
            r_bool, desc = local_start_process(ROS_PLAY_BAG_MAP, 'bag', 3)
            assert r_bool, desc

        # 5. 播放30s
        with allure.step('5. 播放30s'):
            logger.info('================= 5. play bag 30s =================')
            time.sleep(30)

        # 6. kill bag
        with allure.step('6. 停止播放 bag'):
            logger.info('================= 6. stop play bag =================')
            r_bool, desc = local_stop_process('bag', kill_cmd='-9', stop_time=1)
            assert r_bool, desc

        # 7. kill radar mapping
        with allure.step('7. kill radar mapping'):
            logger.info('================= 7. kill radar mapping =================')
            r_bool, desc = remote_stop_process(remote, 'radar_mapping', kill_cmd='-2', stop_time=20)
            assert r_bool, desc

        # 8. 检查文件是否生成
        with allure.step('8. 检查文件是否生成'):
            logger.info('================= 8. check map pcd and pcd.utm file =================')
            ret = remote.exec_comm('ls -l {}/map'.format(REMOTE_TEST_DATA)).stdout
            logger.info('stdout: {}'.format(ret))
            assert '.pcd' in ret, 'pcd file not exist'
            assert '.pcd.utm' in ret, 'utm file not exist'

        # 9. 下载文件
        with allure.step('9. 下载地图pcd和utm文件'):
            logger.info('================= 8. download pcd and pcd.utm file to local =================')
            r_bool, desc = remote.get('{}/map'.format(REMOTE_TEST_DATA), '{}/'.format(log_path))
            assert r_bool, desc
            logger.info(' download successfully')

        # 10. 检查文件
        pcd_file = ''
        utm_file = ''
        with allure.step('10. 检查文件'):
            logger.info('================= 9. local check pcd/utm file =================')
            for file_name in os.listdir('{}/map'.format(log_path)):
                assert '.pcd' in file_name
                if file_name[-4:] == '.pcd':
                    pcd_file = '{}/map/{}'.format(REMOTE_TEST_DATA, file_name)
                elif file_name[-8:] == '.pcd.utm':
                    utm_file = '{}/map/{}'.format(REMOTE_TEST_DATA, file_name)
                else:
                    assert False, 'abnormal file: {}'.format(file_name)

                if '.pcd.utm' in file_name:
                    # 11. 检查utm文件
                    with allure.step('11. 检查utm文件'):
                        logger.info('================= 11. check utm content =================')
                        utm_path = '{}/map/{}'.format(log_path, file_name)
                        allure.attach.file(utm_path, 'utm文件',
                                           allure.attachment_type.TEXT)
                        with open(utm_path, 'r') as f:
                            info_list = f.readline().split(' ')
                            logger.info('utm file: {}'.format(info_list))
                            assert info_list
                            assert '50' == info_list[2], info_list
                            assert 'R\n' == info_list[3], info_list
            assert pcd_file, 'pcd is not exist'
            assert utm_file, 'utm is not exist'

        # 12. 启动 radar_pf_localizer
        with allure.step('12. 启动 radar_pf_localizer'):
            logger.info('================= 12. start radar_pf_localizer =================')
            temp_file = '{}/map/temp.txt'.format(REMOTE_TEST_DATA)
            r_bool, ret = remote_start_process(remote, RADAR_PF_LOCALIZER % (utm_file, pcd_file, temp_file), 'radar_pf_localizer')
            assert r_bool, ret

        # 13. 停止 radar_pf_localizer
        with allure.step('13. 停止 radar_pf_localizer'):
            logger.info('================= 13. stop radar_pf_localizer =================')
            r_bool, ret = remote_stop_process(remote, 'radar_pf_localizer', '-9', 2)
            assert r_bool, ret

        # 14. 检测是否地图是否加载成功
        with allure.step('14. 检测是否地图是否加载成功'):
            logger.info('================= 14. check map loader =================')
            temp_local_file = '{}/map/temp.txt'.format(log_path)
            remote.get(temp_file, temp_local_file)
            allure.attach.file(temp_local_file, 'radar_pf_localizer启动日志', allure.attachment_type.TEXT)
            with open(temp_local_file, 'r') as f:
                assert 'PCL_MAP......OK......' in f.read(), 'radar_pf_localizer load map failed'


if __name__ == '__main__':
    import pytest
    """
    1. 直接执行pytest.main() 【自动查找当前目录下，以test_开头的文件或者以_test结尾的py文件】
    2. 设置pytest的执行参数 pytest.main(['--html=./allure_results.html','test_login.py'])【执行test_login.py文件，并生成html格式的报告】
    3. 运行目录及子包下的所有用例  pytest.main(['目录名'])
    4. 运行指定模块所有用例  pytest.main(['test_reg.py'])
    5. 运行指定模块指定类指定用例  pytest.main(['test_reg.py::TestClass::test_method'])  冒号分割
    6.  -m=xxx: 运行打标签的用例
        -reruns=xxx，失败重新运行

        -q: 安静模式, 不输出环境信息
        -v: 丰富信息模式, 输出更详细的用例执行信息
        -s: 显示程序中的print/logging输出
        --resultlog=./log.txt 生成log
        --junitxml=./log.xml 生成xml报告
    """
    import time
    from pathlib import Path
    # 清理日志
    # os.system('rm -rf {}/logs/*'.format(TEST_CASE_PATH))
    # report_html_dir = '{}allure_reports/{}'.format(TEST_CASE_PATH, time.strftime("report_%Y-%m-%d_%H:%M:%S", time.localtime()))
    # print('exec testcases')
    # pytest.main(['-s', '-v', '--alluredir', '{}/allure_results/'.format(TEST_CASE_PATH)])
    #
    # # 生成报告
    # generate = 'allure generate {}allure_results/ -o {}/ --clean'.format(TEST_CASE_PATH, report_html_dir)
    # print('generate allure_results: {}'.format(generate))
    # os.system(generate)
    #
    # # 移动日志
    # mv_log = 'cp -r {}/logs {}/data/attachments'.format(TEST_CASE_PATH, report_html_dir)
    # print('mv log: {}'.format(mv_log))
    # os.system(mv_log)
    print(Path('asd.txt').exists)
    pytest.mark.parametrize()








