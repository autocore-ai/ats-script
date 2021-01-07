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
from common.process import *
import common.perception.perception_action as p_env
import common.perception.perception_conf as p_conf
from common.planning.planning_action import *
import config
logger = logging.getLogger()
wait_aw4_time = 80


@pytest.fixture
def perception_env(get_case_path):
    start_time = time.time()

    if config.EXEC_CASE_TYPE == 1:
        """
        1. set up
            check autoware4 docker status, if running, stop it, then check docker stopped
            start autoware4 docker
            check autoware4 docker started successful

        2. tear down
            stop docker
            check docker stopped
        """
        check_aw4_open()
        start_aw4_open(get_case_path)
        wait_aw4_start_open()
        time.sleep(2)
        logger.info('aw4 env is ok, now to exec cases')
        yield
        stop_aw4_open()
    else:
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
        check_aw4_home()
        start_aw4_home()
        check_aw4_ok_home()
        check_perception_home()
        start_perception_home()
        check_perception_ok_home()
        time.sleep(2)
        logger.info('aw4 env is ok, now to exec cases')
        yield
        stop_perception_home()
        check_perception_stop_home()
        stop_aw4_home()
        check_aw4_stop_home()

    end_time = time.time()
    allure.attach('Case exec time: {}'.format(end_time - start_time), 'Case exec time', allure.attachment_type.TEXT)


@allure.step('1. check Autoware4 status, if running, stop it, aw4 env: {}'.format(p_conf.PERCEPTION_AUTOWARE4_IP))
def check_aw4_open():
    logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step='1. check aw4 status, if running, stop it, '
                                                            'aw4 env: {}'.format(p_conf.PERCEPTION_AUTOWARE4_IP)))
    r_bool, status = p_env.check_autoware_open_status()
    logger.info('check_autoware_open_status, return: {}, {}'.format(r_bool, status))
    assert r_bool, status
    if status in [2, 3]:
        step_desc = '1.1 {}, stop it'.format(p_conf.AUTOWARE_RUN_STATUS)
        with allure.step(step_desc):
            logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step=step_desc))
            r_bool, status = p_env.stop_autoware_open()
            logger.info('stop autoware result: {}, {}'.format(r_bool, status))
            assert r_bool, status


@allure.step('2. start aw4')
def start_aw4_open(case_path):
    logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step='2. start aw4'))
    aw_log_path = '{}_autoware.txt'.format(case_path)
    logger.info('autoware log path: {}'.format(aw_log_path))
    r_bool, msg = p_env.start_autoware_open(aw_log_path)
    assert r_bool, msg


@allure.step('3. check aw4 start ok, and waiting aw4 to start until start successful, '
             'max wait time: {w_t}s'.format(w_t=wait_aw4_time))
def wait_aw4_start_open():
    logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step='3. check aw4 start ok, and waiting aw4 to start until '
                                                            'start successful, '
                                                            'max wait time: {w_t}s'.format(w_t=wait_aw4_time)))
    t = 0
    while t < wait_aw4_time:
        time.sleep(1)
        logger.info('waiting autoware start, wait {}s ......'.format(t+1))
        r_bool, status = p_env.check_autoware_open_status()
        assert r_bool, status
        if status == 2:
            logger.info('autoware started successfully')
            break
        t += 1
    assert t < wait_aw4_time, 'autoware didn\'t start in {}s'.format(wait_aw4_time)


@allure.step('1. stop autoware')
def stop_aw4_open():
    logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step='1. stop autoware'))
    r_bool, msg = p_env.stop_autoware_open()
    assert r_bool, msg


@allure.step('1. check Autoware4 status, if running, stop it, aw4 env: {}'.format(p_conf.PERCEPTION_AUTOWARE4_IP))
def check_aw4_home():
    logger.info('=' * 20 + '1. check Autoware4 status, if running, stop it, '
                           'aw4 env: {}'.format(p_conf.PERCEPTION_AUTOWARE4_IP) + '=' * 20)
    r_bool, status = p_env.check_autoware_status()
    logger.info('check_autoware_status, return: {}, {}'.format(r_bool, status))
    assert r_bool, str(status)
    if status:
        step_desc = 'Autoware4 is running...now to stop it'
        with allure.step(step_desc):
            logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step=step_desc))
            s_bool, s_ret = p_env.stop_autoware4()
            assert s_bool, s_ret
            time.sleep(3)  # wait killed success
        step_desc = 'Autoware4 stopped, now to check status'
        with allure.step(step_desc):
            logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step=step_desc))
            r_bool, status = p_env.check_autoware_status()
            assert r_bool, status
            assert not status, 'Autoware4 stopped failed, please check ...'


@allure.step('2. start aw4')
def start_aw4_home():
    logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step='2. start aw4'))
    r_bool, msg = p_env.start_autoware4()
    assert r_bool, msg
    wait_time = 0
    while wait_time < 20:
        time.sleep(1)
        wait_time += 1
        step_desc = 'waiting Autoware4 to start, {}s'.format(wait_time)
        with allure.step(step_desc):
            logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step=step_desc))
            r_bool, status = p_env.check_autoware_status()
            if r_bool and status:
                logger.info('Autoware started OK')
                break


@allure.step('3. check aw4 start ok, and waiting aw4 to start until start successful, '
             'max wait time: {w_t}s'.format(w_t=wait_aw4_time))
def check_aw4_ok_home():
    logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step='3. check aw4 start ok, and waiting aw4 to start until'
                                                            ' start successful,'
                                                            ' max wait time: {w_t}s'.format(w_t=wait_aw4_time)))
    r_bool, status = p_env.check_autoware_status()
    logger.info('check autoware status, return: {}, {}'.format(r_bool, status))
    assert r_bool, status
    assert status, 'Autoware is not running after wait {}s'.format(wait_aw4_time)


@allure.step('4. Check perception status, if running, stop it')
def check_perception_home():
    logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step='4. Check perception status, if running, stop it'))
    r_bool, ret = p_env.check_perception()
    assert r_bool, ret
    if ret:
        step_desc = 'Perception is running, to kill it.'
        with allure.step(step_desc):
            logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step=step_desc))
            r_bool, msg = p_env.stop_perception()
            assert r_bool, msg
            wait_time = 10
            for i in range(1, wait_time + 1):
                time.sleep(1)
                logger.info('waiting perception stop, {}s...'.format(i))
        step_desc = 'check perception is stopped'
        with allure.step(step_desc):
            logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step=step_desc))
            r_bool, ret = p_env.check_perception()
            assert r_bool, ret
            assert not ret, 'Perception is stopped once, now it is running still, return'


@allure.step('5. Start perception ...')
def start_perception_home():
    logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step='5. Start perception ...'))
    r_bool, msg = p_env.start_perception()
    assert r_bool, msg
    wait_time = 0
    while wait_time < 60:
        time.sleep(1)
        wait_time += 1
        step_desc = 'waiting perception to start, {}s'.format(wait_time)
        with allure.step(step_desc):
            logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step=step_desc))
            r_bool, status = p_env.check_perception()
            if r_bool and status:
                logger.info('Perception started OK')
                break


@allure.step('6. Check start perception OK')
def check_perception_ok_home():
    logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step='6. Check start perception OK'))
    r_bool, msg = p_env.check_perception()
    assert r_bool, msg
    assert msg, 'perception is not running, start env failed, return'


@allure.step('1. Stop perception')
def stop_perception_home():
    logger.info('{eq} {step} {eq}'.format(eq='='*20, step='1. Stop perception'))
    r_bool, ret = p_env.stop_perception()
    assert r_bool, ret
    wait_time = 30
    for i in range(1, wait_time+1):
        logger.info('waiting perception to stop, {}s ...'.format(i))
        time.sleep(1)


@allure.step('2. Check perception has stoppedc')
def check_perception_stop_home():
    logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step='2. Check perception has stopped'))
    r_bool, ret = p_env.check_perception()
    assert r_bool, ret
    assert not ret, 'perception stopped failed, return'


@allure.step('3. Stop autoware4')
def stop_aw4_home():
    logger.info('{eq} {step} {eq}'.format(eq='='*20, step='3. Stop autoware4'))
    r_bool, ret = p_env.stop_autoware4()
    assert r_bool, ret
    wait_time = 10
    for i in range(1, wait_time + 1):
        logger.info('waiting autoware4 to stop, {}s ...'.format(i))
        time.sleep(1)


@allure.step('4.Check autoware4 has stopped')
def check_aw4_stop_home():
    logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step='4.Check autoware4 has stopped'))
    r_bool, ret = p_env.check_autoware_status()
    assert r_bool, ret
    assert not ret, 'autoware4 stopped failed, return'


@pytest.fixture
def planning_open_env(get_case_path):
    step_0 = "check environment status , if status open, close it , if not , follow next step"
    with allure.step(step_0):
        time.sleep(5)
        check_aw4_open()
        time.sleep(2)
        logger.info('aw4 env is ok, now to exec cases')

    step_1 = "1. start docker"
    with allure.step(step_1):
        logger.info(step_1)
        time.sleep(5)
        logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step='2. start aw4'))
        aw_log_path = '{}_autoware.txt'.format(get_case_path)
        logger.info('autoware log path: {}'.format(aw_log_path))
        r_bool, msg = docker_start(aw_log_path)
        assert r_bool, msg
        count_sec = 0
        wait_time = 80
        for count_sec in range(wait_time):
            time.sleep(1)
            process_bol, aw4_status_bool = comm.check_docker(PLANNING_DOCKER_NAME)
            if process_bol and aw4_status_bool:
                logger.info("aw4 plannnig is runnning successfully")
                break
            if process_bol and not aw4_status_bool:
                continue
            if not process_bol:
                assert False, aw4_status_bool
        if count_sec == 79 and process_bol and not aw4_status_bool:
            assert False, "exceed waiting time {} , aw4 starts failed".format(wait_time)
        time.sleep(3)
        # assert planning_topics_test(), "all planning related topics are ready"
    yield

    with allure.step("stop environment"):
        logger.info("stop env")
        time.sleep(5)
        r_bool, s_bool = docker_end()
        if not r_bool:
            logger.error('stop autoware failed, msg: {}'.format(s_bool))
            return False, s_bool

        if not s_bool:
            return True, 'stop autoware failed'
        return True, ''


if __name__ == '__main__':
    pass
