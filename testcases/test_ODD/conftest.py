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
from common.process import check_process, local_stop_process, local_start_process, remote_start_process
import config
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
def start_perception_env():
    """
    默认当前环境已经export了ROS_IP,ROS_MASTER_URI,source /opt/ros/melodic/setup.bash, source ~/AutowareArchitectureProposal/devel/setup.bash
    启动perception环境
        1. 启动 Autoware 4, 对应命令：START_AUTOWARE_4
        2. 启动 perception
    """
    # 1. 检查Autoware是否没有运行
    logger.info('check Autoware status is stop')
    process_name = 'Autoware'  # autoware 当前环境中，只有Autoware启动的进程所含有的关键字
    r_bool = check_process(process_name)
    if not r_bool:
        logger.warning('Autoware.4 is running still, now to kill it.')
        # 2. Autoware4 正在运行，去杀它一次，如杀不成功，则退出，为了保证环境的干净
        r_bool, msg = local_stop_process(process_name, kill_cmd='-9', stop_time=5)
        assert r_bool, msg  # 停止失败，不再继续进行

    # 3. 启动 Autoware 4
    r_bool, msg = local_start_process(START_AUTOWARE_4, 'Autoware', start_time=30)
    assert r_bool, msg

    # 4. 启动 Perception
    logger.info('connect remote perception: IP: {}, USER: {}, PWD: {}'.
                format(config.PERCEPTION_IP, config.PERCEPTION_USER, config.PERCEPTION_PWD))
    perc_server = remote.Remote(config.PERCEPTION_IP, config.PERCEPTION_USER, config.PERCEPTION_PWD)
    r_bool, desc = perc_server.check_is_connect()
    assert r_bool, desc
    # 启动
    r_bool, msg = remote_start_process(perc_server, START_PERCEPTION, 'autoware_launch', start_time=30)
    assert r_bool, msg
    logger.info('Test env for autoware4 perception is ready, let\'s go')


