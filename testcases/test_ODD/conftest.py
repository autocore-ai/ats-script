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
import time
import pytest
import allure
import logging
import common.ODD.aw4_env as aw4_env
import common.ODD.config as aw4_conf
logger = logging.getLogger()


@pytest.fixture(scope='function')
def env_opt(request, get_case_log_path):
    """startup case run environment"""
    logger.info('execute cases: %s' % aw4_conf.EXEC_CASE_SCENE[aw4_conf.EXEC_CASE_TYPE]['desc'])
    fun_name = request.function.__name__
    logger.info('case function is %s' % fun_name)
    logger.info('startup run environment...')
    start_time = time.time()

    # according to case function, get environment information
    env_ip = aw4_conf.TEST_MODULE_INFO[fun_name]['ros1_docker_ip']
    wait_aw4_time = 80

    if aw4_conf.EXEC_CASE_TYPE in [1, 3]:  # open source
        """
        1. set up
            check autoware4 docker status, if running, stop it, then check docker stopped
            start autoware4 docker
            check autoware4 docker started successful

        2. tear down
            stop docker
        """
        step_desc = '1. check aw4 status, if running, stop it. aw4 env: {}'.format(env_ip)
        aw4_env.check_aw4(env_ip, fun_name, step_desc)

        step_desc = '2. start aw4. aw4 env: {}'.format(env_ip)
        aw4_env.start_aw4(get_case_log_path, fun_name, step_desc)

        step_desc = '3. check aw4 start ok, and waiting aw4 to start until start successfully, ' \
                    'max wait time: {w_t}s'.format(w_t=wait_aw4_time)
        aw4_env.wait_aw4_start(env_ip, fun_name, wait_aw4_time, step_desc)
        time.sleep(2)
        logger.info('aw4 environment is ok, now exec cases')

        yield

        step_desc = 'stop aw4'
        aw4_env.stop_aw4(fun_name, step_desc)

    else:
        """
        TO DO
        other startup modes 
        1. set up
        Default export 了ROS_IP,ROS_MASTER_URI,source /opt/ros/melodic/setup.bash, source ~/AutowareArchitectureProposal/devel/setup.bash
        start perception env
            1. start Autoware.4, command：START_AUTOWARE_4
            2. start perception

        1. tear down
            1. close perception
            2. close Autoware.4
        """

    end_time = time.time()
    allure.attach('Case exec time: {}'.format(end_time - start_time), 'Case exec time', allure.attachment_type.TEXT)


if __name__ == '__main__':
    pass
