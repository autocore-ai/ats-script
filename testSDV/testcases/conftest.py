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
import time
import logging

import config
from testSDV.common.utils.log import md_logger
from testSDV.common.utils.local import check_process, stop_process
logger = logging.getLogger()


@pytest.fixture(autouse=True)
def log(get_case_log_path):
    """
    Dynamic logger
    :param get_case_log_path: cases log path
    :return:
    """
    return md_logger(get_case_log_path)  # Initial session log obj


@pytest.fixture(scope='function')
def get_case_log_path(request):
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
                log_path = '{}/logs/log_{}/{}/{}_JiraID_{}'.format(config.TEST_CASE_PATH, exec_time, case_path, case_name, case_id)
            else:
                log_path = '{}/logs/log_{}/{}/{}'.format(config.TEST_CASE_PATH, exec_time, case_path, case_name)
        else:
            log_path = '{}/logs/log_{}/{}/{}'.format(config.TEST_CASE_PATH, exec_time, case_path, case_name)
    else:
        cls_name = request.cls.__name__
        log_path = '{}/logs/log_{}/{}/{}/{}'.format(config.TEST_CASE_PATH, exec_time, case_path, cls_name, case_name)

    return log_path


@pytest.fixture(scope='function')
def sdv_env_opt(request, get_case_log_path):
    """
    future way environment
    
    setup:
    1. set domain info
    2. check remote docker environment
    
    teardown:
    1. check record rosbag process has been stopped 
    """
    fun_name = request.function.__name__
    logger.info('****************** exec case %s ******************' % fun_name)
    start_time = time.time()
    logger.info('****************** watch autoware %s ******************' % fun_name)

    yield

    logger.info('****************** teardown ******************')
    step_desc = 'tear down'
    logger.info('check ros2 bag already stopped')
    process_name = 'record'
    ret = check_process(process_name)
    logger.info('check result: {}'.format(ret))
    if ret:
        r_bool, ret = stop_process(process_name, signal='-9')
        if r_bool:
            logger.error("kill -9 record failed: %s" % ret)
    logger.info('test case[%s] exec finished' % fun_name)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    generate markdown report
    | Priority  | Yes  |
    :param item:
    :param call:
    :return:
    """
    out = yield

    report = out.get_result()
    result_path = config.TEST_CASE_PATH + '/result.txt'
    if report.when == "call":
        with open(result_path, 'a') as result:
            result.write('{case_name};{result}\n'.format(case_name=report.nodeid, result=report.outcome))
