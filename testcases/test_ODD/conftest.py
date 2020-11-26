# -*- coding:utf8 -*-
"""
专门存放fixture的配置文件
pytest 会在执行测试函数之前（或之后）加载运行它们
Pytest 使用 yield 关键词将固件分为两部分，yield 之前的代码属于预处理，会在测试前执行；yield 之后的代码属于后处理，将在测试完成后执行。
比如每个用例都要ssh到PCU环境上，就可以把fixture放到这里
pytest会默认读取conftest.py中的所有fixture
conftest.py只有一个package下的所有测试用例生效
不同目录可以有自己的conftest.py
测试用例不需要手动导入conftest.py，pytest会自己找
在定义固件时，通过 scope 参数声明作用域，可选项有：

    function: 函数级，每个测试函数都会执行一次固件；
    class: 类级别，每个测试类执行一次，所有方法都可以使用；
    module: 模块级，每个模块执行一次，模块内函数和方法都可使用；
    session: 会话级，一次测试只执行一次，所有被找到的函数和方法都可用。

"""

import pytest
import allure
import os
from utils import remote
from common.command import START_AUTOWARE_4, START_PERCEPTION
from common.process import *
import common.perception_action as p_env
import config
import common.perception_conf as p_conf
import logging
from utils.log import md_logger
logger = logging.getLogger()


@allure.step('1. 连接PCU环境')
@allure.title('1. 连接PCU环境')
@pytest.fixture
def connect_pcu():
    logger.info('================= 1. connect to PCU env =================')
    logger.info('IP: {}, USER: {}, PWD: {}'.format(config.PCU_IP, config.PCU_USER, config.PCU_PWD))
    remote_server = remote.Remote(config.PCU_IP, config.PCU_USER, config.PCU_PWD)
    r_bool, desc = remote_server.check_is_connect()
    assert r_bool, desc
    logger.info('=============== set up connect PCU OK ===============')
    return remote_server


def clean_env(remote_server):
    """清理环境"""
    remote_server.exec_comm('rm -rf /opt/autocore/test_data/map/*')
    # os.system('rm -rf {}/test_data/map/*'.format(config.TEST_CASE_PATH))
    logger.info('clean ok')


@allure.step('启动Autoware4和perception环境')
@allure.title('启动Autoware4和perception环境')
@pytest.fixture
def perception_env(timer_function_scope, log, scope='function'):
    """
    1. set up
    Default export 了ROS_IP,ROS_MASTER_URI,source /opt/ros/melodic/setup.bash, source ~/AutowareArchitectureProposal/devel/setup.bash
    start perception env
        1. start Autoware.4, command：START_AUTOWARE_4
        2. start perception

    1. tear down
    1. close perception
    2. close Autoware.4
    """
    step_desc = '1. check Autoware4 status, if running, to stop it, autoware.4 env: {}'.format(p_conf.PERCEPTION_AUTOWARE4_IP)
    with allure.step(step_desc):
        logger.info('='*20 + step_desc + '='*20)
        r_bool, status = p_env.check_autoware_status()
        logger.info('check_autoware_status, return: {}, {}'.format(r_bool, status))
        assert r_bool, str(status)
        if status:
            step_desc = 'Autoware4 is running...now to stop it'
            with allure.step(step_desc):
                logger.info('=' * 20 + step_desc + '=' * 20)
                s_bool, s_ret = p_env.stop_autoware4()
                assert s_bool, s_ret
                time.sleep(3)  # wait killed success
            step_desc = 'Autoware4 stopped, now to check status'
            with allure.step(step_desc):
                logger.info('=' * 20 + step_desc + '=' * 20)
                r_bool, status = p_env.check_autoware_status()
                assert r_bool, status
                assert not status, 'Autoware4 stopped failed, please check ...'

    step_desc = '2. To start Autoware4'
    with allure.step(step_desc):
        logger.info('=' * 20 + step_desc + '=' * 20)
        r_bool, msg = p_env.start_autoware4()
        assert r_bool, msg
        wait_time = 10
        for i in range(1, wait_time+1):
            time.sleep(1)
            logger.info('Waiting autoware to start, wait {}s, {}s ...'.format(wait_time, i))

    step_desc = '3. Check Autoware4 is running'
    with allure.step(step_desc):
        logger.info('=' * 20 + step_desc + '=' * 20)
        r_bool, status = p_env.check_autoware_status()
        logger.info('check autoware status, return: {}, {}'.format(r_bool, status))
        assert r_bool, status
        assert status, 'Autoware is not running after wait {}s'.format(wait_time)

    # need to enter docker to check
    step_desc = '4. Check perception status, if running, to stop it'
    with allure.step(step_desc):
        logger.info('=' * 20 + step_desc + '=' * 20)
        r_bool, ret = p_env.check_perception()
        assert r_bool, ret
        if ret:
            step_desc = 'Perception is running, to kill it.'
            with allure.step(step_desc):
                logger.info('=' * 20 + step_desc + '=' * 20)
                r_bool, msg = p_env.stop_perception()
                assert r_bool, msg
                wait_time = 10
                for i in range(1, wait_time+1):
                    time.sleep(1)
                    logger.info('waiting perception stop, {}s...'.format(i))
            step_desc = 'check perception is stopped'
            with allure.step(step_desc):
                logger.info('=' * 20 + step_desc + '=' * 20)
                r_bool, ret = p_env.check_perception()
                assert r_bool, ret
                assert not ret, 'Perception is stopped once, now it is running still, return'

    step_desc = '5. Start perception ...'
    with allure.step(step_desc):
        logger.info('=' * 20 + step_desc + '=' * 20)
        r_bool, msg = p_env.start_perception()
        assert r_bool, msg
        wait_time = 60
        for i in range(1, wait_time+1):
            time.sleep(1)
            logger.info('Waiting perception to start, wait {}s, {}s ...'.format(wait_time, i))

    # 6. check perception is ok
    step_desc = '6. Check start perception OK'
    with allure.step(step_desc):
        logger.info('=' * 20 + step_desc + '=' * 20)
        r_bool, msg = p_env.check_perception()
        assert r_bool, msg
        assert msg, 'perception is not running, start env failed, return'

    logger.info('Test env for autoware4 perception is ready, let\'s to do test...')

    yield

    step_desc = '1. Stop perception'
    with allure.step(step_desc):
        logger.info('=' * 20 + step_desc + '=' * 20)
        r_bool, ret = p_env.stop_perception()
        assert r_bool, ret
        wait_time = 30
        for i in range(1, wait_time+1):
            logger.info('waiting perception to stop, {}s ...'.format(i))
            time.sleep(1)

    step_desc = '2. Check perception has stopped'
    with allure.step(step_desc):
        logger.info('=' * 20 + step_desc + '=' * 20)
        r_bool, ret = p_env.check_perception()
        assert r_bool, ret
        assert not ret, 'perception stopped failed, return'

    step_desc = '3. Stop autoware4'
    with allure.step(step_desc):
        logger.info('=' * 20 + step_desc + '=' * 20)
        r_bool, ret = p_env.stop_autoware4()
        assert r_bool, ret
        wait_time = 10
        for i in range(1, wait_time + 1):
            logger.info('waiting autoware4 to stop, {}s ...'.format(i))
            time.sleep(1)

    step_desc = '4.Check autoware4 has stopped'
    with allure.step(step_desc):
        logger.info('=' * 20 + step_desc + '=' * 20)
        r_bool, ret = p_env.check_autoware_status()
        assert r_bool, ret
        assert not ret, 'autoware4 stopped failed, return'

    # to clean autoware env
    # msg = 'tear down: stop perception'
    # logger.info(msg)
    # with allure.step(msg):
    #     logger.info(msg)
    #     r_bool, node_list = get_perception_node_list()
    #     assert r_bool, node_list
    #     assert node_list, 'perception quit expectedly'
    #     r_bool, msg = stop_perception_node_list(node_list)
    #     assert r_bool, msg
    #
    #
    # # to stop autoware
    # msg = 'To stop Autoware'
    # with allure.step(msg):
    #     logger.info(msg)
    #     r_bool, msg = local_stop_process(key_autoware, kill_cmd='-9', stop_time=5)
    #     assert r_bool, msg  # stop failed, stop
    #     r_bool, msg = local_stop_process(key_ros, kill_cmd='-9', stop_time=5)
    #     assert r_bool, msg  # stop failed, stop


if __name__ == '__main__':
    # r_bool, msg = local_start_process(START_AUTOWARE_4, 'AutowareArchitectureProposa', start_time=30)
    # perc_server = remote.Remote(config.PERCEPTION_IP, config.PERCEPTION_USER, config.PERCEPTION_PWD)
    # r_bool, desc = perc_server.check_is_connect()
    # perc_key = 'ros'
    # perc_key2 = 'autoware'
    # perc_bool = remote_check_process(perc_server, perc_key)
    # perc_bool2 = remote_check_process(perc_server, perc_key2)
    # print(r_bool)
    # print(desc)
    # r_bool, msg = remote_start_process(perc_server, START_PERCEPTION, 'autoware', start_time=30)

    perc_server = remote.Remote(config.PERCEPTION_IP, config.PERCEPTION_USER, config.PERCEPTION_PWD)
    perc_key = 'ros'
    perc_key2 = 'autoware'
    perc_bool = remote_check_process(perc_server, perc_key)
    perc_bool2 = remote_check_process(perc_server, perc_key2)
    if perc_bool or perc_bool2:
        logger.warning('Perception is running still, now to kill it.')
        c_bool, msg = remote_stop_process(perc_server, perc_key, stop_time=5)
        assert c_bool, msg
        c_bool, msg = remote_stop_process(perc_server, perc_key2, stop_time=5)
        assert c_bool, msg
    r_bool, msg = remote_start_process(perc_server, START_PERCEPTION, 'autoware', start_time=30)
    assert r_bool, msg

