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
import common.action as comm

logger = logging.getLogger()


@pytest.fixture
def perception_open_env(get_case_path):
    """
    1. set up
        check autoware4 docker status, if running, stop it, then check docker stopped
        start autoware4 docker
        check autoware4 docker started successful

    2. tear down
        stop docker
        check docker stopped
    """
    start_time = time.time()

    step_desc = '1. check Autoware4 status, if running, stop it, autoware.4 env: {}'.format(
        p_conf.PERCEPTION_AUTOWARE4_IP)
    with allure.step(step_desc):
        logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
        r_bool, status = p_env.check_autoware_open_status()
        logger.info('check_autoware_open_status, return: {}, {}'.format(r_bool, status))
        assert r_bool, status
        if status in [2, 3]:
            step_desc = '1.1 {}, stop it'.format(p_conf.AUTOWARE_RUN_STATUS)
            with allure.step(step_desc):
                logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
                r_bool, status = p_env.stop_autoware_open()
                logger.info('stop autoware result: {}, {}'.format(r_bool, status))
                assert r_bool, status

    step_desc = '2. start Autoware4'
    with allure.step(step_desc):
        logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
        log_path = get_case_path
        aw_log_path = '{}/logs/{}_autoware.log'.format(TEST_CASE_PATH, log_path)
        logger.info('autoware log path: {}'.format(aw_log_path))
        r_bool, msg = p_env.start_autoware_open(aw_log_path)
        assert r_bool, msg

    wait_time = 80
    step_desc = '3. check autoware start ok, and waiting autoware to start until start successful, ' \
                'max wait time: {w_t}s'.format(w_t=wait_time)
    with allure.step(step_desc):
        logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step=step_desc))
        t = 0
        while t < wait_time:
            time.sleep(1)
            logger.info('waiting autoware start, wait {}s ......'.format(t+1))
            r_bool, status = p_env.check_autoware_open_status()
            assert r_bool, status
            if status == 2:
                logger.info('autoware started successfully')
                break
            t += 1
        assert t < wait_time, 'autoware didn\'t start in {}s'.format(wait_time)

    yield

    step_desc = '1. stop autoware'
    with allure.step(step_desc):
        logger.info('{eq} {step} {eq}'.format(eq='=' * 20, step=step_desc))
        r_bool, msg = p_env.stop_autoware_open()
        assert r_bool, msg

    end_time = time.time()
    allure.attach('Case exec time: {}'.format(end_time - start_time), 'Case exec time', allure.attachment_type.TEXT)


@pytest.fixture
def perception_env():
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
    start_time = time.time()
    step_desc = '1. check Autoware4 status, if running, stop it, autoware.4 env: {}'.format(p_conf.PERCEPTION_AUTOWARE4_IP)
    with allure.step(step_desc):
        logger.info('='*20 + step_desc + '='*20)
        r_bool, status = p_env.check_autoware_status()
        logger.info('check_autoware_status, return: {}, {}'.format(r_bool, status))
        assert r_bool, str(status)
        if status:
            step_desc = 'Autoware4 is running...now to stop it'
            with allure.step(step_desc):
                logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
                s_bool, s_ret = p_env.stop_autoware4()
                assert s_bool, s_ret
                time.sleep(3)  # wait killed success
            step_desc = 'Autoware4 stopped, now to check status'
            with allure.step(step_desc):
                logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
                r_bool, status = p_env.check_autoware_status()
                assert r_bool, status
                assert not status, 'Autoware4 stopped failed, please check ...'

    step_desc = '2. To start Autoware4'
    with allure.step(step_desc):
        logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
        r_bool, msg = p_env.start_autoware4()
        assert r_bool, msg
        wait_time = 0
        while wait_time < 20:
            time.sleep(1)
            wait_time += 1
            step_desc = 'waiting Autoware4 to start, {}s'.format(wait_time)
            with allure.step(step_desc):
                logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
                r_bool, status = p_env.check_autoware_status()
                if r_bool and status:
                    logger.info('Autoware started OK')
                    break

    step_desc = '3. Check Autoware4 started ok'
    with allure.step(step_desc):
        logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
        r_bool, status = p_env.check_autoware_status()
        logger.info('check autoware status, return: {}, {}'.format(r_bool, status))
        assert r_bool, status
        assert status, 'Autoware is not running after wait {}s'.format(wait_time)

    # need to enter docker to check
    step_desc = '4. Check perception status, if running, stop it'
    with allure.step(step_desc):
        logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
        r_bool, ret = p_env.check_perception()
        assert r_bool, ret
        if ret:
            step_desc = 'Perception is running, to kill it.'
            with allure.step(step_desc):
                logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
                r_bool, msg = p_env.stop_perception()
                assert r_bool, msg
                wait_time = 10
                for i in range(1, wait_time+1):
                    time.sleep(1)
                    logger.info('waiting perception stop, {}s...'.format(i))
            step_desc = 'check perception is stopped'
            with allure.step(step_desc):
                logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
                r_bool, ret = p_env.check_perception()
                assert r_bool, ret
                assert not ret, 'Perception is stopped once, now it is running still, return'

    step_desc = '5. Start perception ...'
    with allure.step(step_desc):
        logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
        r_bool, msg = p_env.start_perception()
        assert r_bool, msg
        wait_time = 0
        while wait_time < 60:
            time.sleep(1)
            wait_time += 1
            step_desc = 'waiting perception to start, {}s'.format(wait_time)
            with allure.step(step_desc):
                logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
                r_bool, status = p_env.check_perception()
                if r_bool and status:
                    logger.info('Perception started OK')
                    break

    # 6. check perception is ok
    step_desc = '6. Check start perception OK'
    with allure.step(step_desc):
        logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
        r_bool, msg = p_env.check_perception()
        assert r_bool, msg
        assert msg, 'perception is not running, start env failed, return'

    logger.info('Test env for autoware4 perception is ready, let\'s to do test...')
    time.sleep(5)

    yield

    step_desc = '1. Stop perception'
    with allure.step(step_desc):
        logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
        r_bool, ret = p_env.stop_perception()
        assert r_bool, ret
        wait_time = 30
        for i in range(1, wait_time+1):
            logger.info('waiting perception to stop, {}s ...'.format(i))
            time.sleep(1)

    step_desc = '2. Check perception has stopped'
    with allure.step(step_desc):
        logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
        r_bool, ret = p_env.check_perception()
        assert r_bool, ret
        assert not ret, 'perception stopped failed, return'

    step_desc = '3. Stop autoware4'
    with allure.step(step_desc):
        logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
        r_bool, ret = p_env.stop_autoware4()
        assert r_bool, ret
        wait_time = 10
        for i in range(1, wait_time + 1):
            logger.info('waiting autoware4 to stop, {}s ...'.format(i))
            time.sleep(1)

    step_desc = '4.Check autoware4 has stopped'
    with allure.step(step_desc):
        logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
        r_bool, ret = p_env.check_autoware_status()
        assert r_bool, ret
        assert not ret, 'autoware4 stopped failed, return'

    end_time = time.time()
    allure.attach('Case exec time: {}'.format(end_time - start_time), 'Case exec time', allure.attachment_type.TEXT)


@pytest.fixture
def planning_env(scope='function'):
    step_1 = "start environment "
    with allure.step(step_1):
        logger.info(step_1)
        p1 = local_planning_start()
        logger.info(p1)
        logging.info('waiting autoware start ...')
        time.sleep(5)
        assert local_planning_start_test(), 'local planning env started fail'

    step_2 = "start docker"
    with allure.step(step_2):
        logger.info(step_2)
        time.sleep(5)
        p2 = local_docker_start()
        time.sleep(10)
        assert pid_exists(p2.pid), "local docker env started fail"

    yield

    with allure.step("stop environment"):
        time.sleep(5)
        logger.info("stop env")
        local_planning_end(p1)
        time.sleep(5)
        local_docker_end(p2)


if __name__ == '__main__':
    pass
