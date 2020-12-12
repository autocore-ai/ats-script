# -*- coding:utf8 -*-
"""
The configuration file for storing fixture
Pytest loads and runs test functions before (or after) executing them
Pytest uses the yield keyword to divide the firmware into two parts. The code before yield belongs to preprocessing and will be executed before testing; the code after yield belongs to post-processing and will be executed after the test is completed.
For example, if each use case needs to be SSH to the PCU environment, you can put the fixture here
Pytest will read by default conftest.py All fixtures in
conftest.py Only all test cases under one package are valid
Different directories can have their own conftest.py
Test cases do not need to be imported manually conftest.py , pytest will find it by itself
When defining the firmware, declare the scope through the scope parameter. The options are:


Function: function level, each test function will execute firmware once;
Class: class level. Each test class is executed once, and all methods can be used;
Module: module level, each module is executed once, and the functions and methods in the module can be used;
Session: at the session level, a test is executed only once, and all the functions and methods found are available.
"""

import pytest
import allure
import time
from common.utils import remote
import config
import logging
from common.utils.log import md_logger
logger = logging.getLogger()


@allure.step('1. connect to pcu env')
@allure.title('1. connect to pcu env')
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
    """clean env"""
    remote_server.exec_comm('rm -rf /opt/autocore/test_data/map/*')
    # os.system('rm -rf {}/test_data/map/*'.format(config.TEST_CASE_PATH))
    logger.info('clean ok')


@allure.step('clean env')
@pytest.fixture
def clean_file(connect_pcu, name='connect to pcu'):
    """
    clean file
    :return:
    """
    remote_server = connect_pcu

    with allure.step('2. clean remote env'):
        logger.info('================= 2. clean env =================')
        clean_env(remote_server)

    yield

    with allure.step('15. clean remote env'):
        logger.info('================= 15. clean env =================')
        clean_env(remote_server)
    logger.info('=============== tear down test end ===============')


@pytest.fixture(autouse=True)
def log(get_case_path):
    """
    Dynamic logger
    :param get_case_path: case
    :return:
    """
    return md_logger(get_case_path)  # Initial session log obj


@pytest.fixture(scope='function')
def get_case_path(request):
    """
    get log path
    :param request:
    :return:
    """
    case_path = request.fspath.strpath.split('testcases/')[-1].split('.py')[0]
    case_name = request.function.__name__
    exec_time = time.strftime("%Y-%m-%d_%H:%M", time.localtime(time.time()))

    if request.cls is None:
        if 'case_data' in request.fixturenames:
            case_name = request.getfixturevalue('case_data')['CaseName']
            if 'Jira_ID' in request.getfixturevalue('case_data'):
                case_id = request.getfixturevalue('case_data')['Jira_ID']
                log_path = '{}/logs_{}/{}/{}_JiraID_{}'.format(config.TEST_CASE_PATH, exec_time, case_path, case_name, case_id)
            else:
                log_path = '{}/logs_{}/{}/{}'.format(config.TEST_CASE_PATH, exec_time, case_path, case_name)
        else:
            log_path = '{}/logs_{}/{}/{}'.format(config.TEST_CASE_PATH, exec_time, case_path, case_name)
    else:
        cls_name = request.cls.__name__
        log_path = '{}/logs_{}/{}/{}/{}'.format(config.TEST_CASE_PATH, exec_time, case_path, cls_name, case_name)

    return log_path
