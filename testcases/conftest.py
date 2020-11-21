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


@allure.step('清理环境')
@pytest.fixture
def clean_file(connect_pcu, name='连接PCU环境'):
    """
    清理文件
    :return:
    """
    remote_server = connect_pcu

    with allure.step('2. 清理远程环境'):
        logger.info('================= 2. clean env =================')
        clean_env(remote_server)

    yield

    with allure.step('15. 清理远程环境'):
        logger.info('================= 15. clean env =================')
        clean_env(remote_server)
    logger.info('=============== tear down test end ===============')


@allure.step('生成日志层级对象')
@pytest.fixture(autouse=True)
def log(request, name='日志'):
    """
    动态日志路径
    :param request:
    :param name:
    :return:
    """
    case_path = request.fspath.strpath.split('testcases/')[-1].split('.py')[0]  # 用例所在目录
    case_name = request.function.__name__
    if request.cls is None:
        if 'case_data' in request.fixturenames:
            case_id = request.getfixturevalue('case_data')['Jira_ID']
            log_path = '{}/{}_JiraID_{}'.format(case_path, case_name, case_id)
        else:
            log_path = '{}/{}'.format(case_path, case_name)
    else:
        cls_name = request.cls.__name__
        log_path = '{}/{}/{}'.format(case_path, cls_name, case_name)
    return md_logger(log_path)  # 初始话日志路径


@pytest.fixture(scope='function')
def log_path(request, name='日志路径'):
    """
    获取日志路径
    :param request:
    :param name:
    :return:
    """
    case_path = request.fspath.strpath.split('testcases/')[-1].split('.py')[0]  # 用例所在目录
    case_name = request.function.__name__
    """
    request
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
     '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
     '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
     '_addfinalizer', '_arg2fixturedefs', '_arg2index', '_check_scope', '_compute_fixture_value', '_factorytraceback', 
     '_fillfixtures', '_fixture_defs', '_fixturedef', '_fixturemanager', '_get_active_fixturedef', '_get_fixturestack', 
     '_getnextfixturedef', '_getscopeitem', '_parent_request', '_pyfuncitem', '_schedule_finalizers', 'addfinalizer', 
     'applymarker', 'cls', 'config', 'fixturename', 'fixturenames', 'fspath', 'function', 'getfixturevalue', 'instance',
      'keywords', 'module', 'node', 'param_index', 'raiseerror', 'scope', 'session']
    """
    if request.cls is None:
        if 'case_data' in request.fixturenames:
            case_id = request.getfixturevalue('test_data')['jira_id']
            real_log_path = '{}logs/{}/{}_JiraID_{}'.format(config.TEST_CASE_PATH, case_path, case_name, case_id)
        else:
            real_log_path = '{}logs/{}/{}'.format(config.TEST_CASE_PATH, case_path, case_name)
    else:
        cls_name = request.cls.__name__
        real_log_path = '{}logs/{}/{}/{}'.format(config.TEST_CASE_PATH, case_path, cls_name, case_name)

    return real_log_path  # 日志路径


@pytest.fixture(scope="session")
def image_file(tmpdir_factory):
    # img = compute_expensive_image()
    fn = tmpdir_factory.mktemp("data").join("img.png")
    return str(fn)


@pytest.fixture(scope="session")
def test_f(request,):
    print(request)
    return 1

