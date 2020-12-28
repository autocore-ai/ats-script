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
import config
import logging
from common.utils.log import md_logger
logger = logging.getLogger()


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
