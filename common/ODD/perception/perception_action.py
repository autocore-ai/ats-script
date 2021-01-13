# -*- coding:utf8 -*-
"""
perception environment and others funcs
"""
import time
import logging
import subprocess
from common.ODD.perception.command import *
from common.utils.remote import RemoteP
import common.ODD.perception.perception_conf as p_conf
import common.utils.local as loc
import config
logger = logging.getLogger()


def start_perception():
    """
    start perception
    1. judge:  Is perception and test env same env?
    2. if same, local start
    3. if not, remote to autoware, to start
    """
    cmd = START_PERCEPTION
    logger.info('start perception, command: {}'.format(cmd))
    if config.TEST_IP == p_conf.PERCEPTION_IP:
        subprocess.Popen(cmd, shell=True)
        return True, ''
    else:
        remote = RemoteP(p_conf.PERCEPTION_IP, p_conf.PERCEPTION_USER, p_conf.PERCEPTION_PWD)
        # cmd = 'export ROS_IP={};export ROS_MASTER_URI={};source /opt/ros/melodic/setup.bash;{}'.\
        #     format(PERCEPTION_IP, PERCEPTION_ROS_MASTER_URI, START_PERCEPTION)
        # cmd = 'sh ~/workspace/run_autoware4_perception.sh'
        r_bool, ret = remote.exec_comm(cmd)
        logger.info('start remote perception, exec result: {} msg: {}'.format(r_bool, ret))
        if not r_bool:
            return False, ret
    return True, ''


def stop_perception():
    """
    stop perception
    1. judge:  Is perception and test env same env?
    2. if same, local start
    3. if not, remote to autoware, to start
    """
    cmd = STOP_PERCEPTION
    if config.TEST_IP == p_conf.PERCEPTION_IP:
        logger.info('stop local perception, command: {}'.format(cmd))
        subprocess.Popen(cmd, shell=True)
        return True, ''
    else:
        remote = RemoteP(p_conf.PERCEPTION_IP, p_conf.PERCEPTION_USER, p_conf.PERCEPTION_PWD)
        logger.info('stop remote perception, command: {}'.format(cmd))
        r_bool, ret = remote.exec_comm(cmd)
        logger.info('stop remote perception, exec result: {} msg: {}'.format(r_bool, ret))
        if not r_bool:
            return False, ret
    return True, ''


def check_perception():
    """
    start perception
    1. judge:  Is perception and test env same env?
    2. if same, local start
    3. if not, remote to autoware, to start
    check step:
    1. check docker is exist?
    2. rosnodes are exist?
    """
    cmd_docker = CHECK_PERCEPTION_DOCKER
    cmd_rosnodes = CHECK_PERCEPTION_NODE
    docker_name = PERCEPTION_DOCKER_NAME
    if config.TEST_IP == p_conf.PERCEPTION_IP:
        # check docker
        logger.info('check perception docker, cmd: {}'.format(cmd_docker))
        p = subprocess.Popen(cmd_docker, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stderr = p.stderr.read().decode('utf-8')
        stdout = p.stdout.read().decode('utf-8')
        logger.info('check perception docker, stdout: {}, stderr: {}'.format(stdout, stderr))
        if len(stderr) > 0:
            return False, stderr
        if len(stdout) == 0:  # docker is not exist, return
            return True, False
        logger.info('perception docker is running...')

        # check node
        logger.info('check perception node, cmd: {}'.format(cmd_rosnodes))
        p = subprocess.Popen(cmd_rosnodes, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stderr = p.stderr.read().decode('utf-8')
        stdout = p.stdout.read().decode('utf-8')
        logger.info('check perception nodes, \nstdout: {}, \nstderr: {}'.format(stdout, stderr))
        if len(stderr) > 0:
            return False, stderr

        for node in PERCEPTION_NODES_LIST:
            if node not in stdout:
                return True, False
    else:
        remote = RemoteP(p_conf.PERCEPTION_IP, p_conf.PERCEPTION_USER, p_conf.PERCEPTION_PWD)
        logger.info('check remote perception docker, command: {}'.format(cmd_docker))
        r_bool, ret = remote.exec_comm(cmd_docker)
        logger.info('check remote perception docker, exec result: {} status: {}'.format(r_bool, ret))
        if not r_bool:
            return False, ret
        if docker_name not in ret:  # docker is not running, return
            return True, False

        logger.info('check remote perception nodes, command: {}'.format(cmd_rosnodes))
        r_bool, ret = remote.exec_comm(cmd_rosnodes)
        logger.info('check remote perception nodes, exec result: {}, status: {}'.format(r_bool, ret))
        if not r_bool:
            return False, ret
        for node in PERCEPTION_NODES_LIST:
            if node not in ret:
                return True, False
    logger.info('perception is running')
    return True, True


def record_bag(result_bag_path, bag_duration):
    """
    record bag
    1. if local record bag, just record to local dir
    2. if need to remote record bag, record bag at remote, than download to local dir
    bag_name: according to bag_name to get record bag path
    """
    topic = p_conf.OBJECTS_TOPIC
    record_comm = ROSBAG_RECORD_O.format(name=result_bag_path, t=bag_duration, topic=topic)
    logger.info('begin to record bag, command: {}'.format(record_comm))
    subprocess.Popen(record_comm, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    time.sleep(2)  # give time to ready record
    return True, 'begin to record bag'


def play_bag(bag_path):
    """
    play rosbag
    bag_path: need to play bag's path
    """
    play_cmd = ROSBAG_PLAY.format(bag_path=bag_path)
    logger.info('play command: {}'.format(play_cmd))
    proc = subprocess.Popen(play_cmd, shell=True, stderr=subprocess.PIPE)
    proc.wait()
    stderr = proc.stderr.read().decode('utf-8')
    logger.info('rosbag play result: {}'.format(stderr))
    if len(stderr) > 0:
        return False, stderr
    return True, ''


def check_record_bag():
    """
    Is check record action running?
    """
    check_cmd = 'ps -ef| grep result.bag | grep -v grep'
    logger.info('check record status, command: {}'.format(check_cmd))

    r_bool, ret = loc.check_process('result.bag')
    if not r_bool:
        return False, ret
    record_status = ret
    return True, record_status


def stop_record_bag():
    """
    stop record bag
    """
    stop_cmd = 'kill -2 `ps -ef|grep "result.bag"|awk \'{{print $2}}\'`'
    logger.info('stop record command: {}'.format(stop_cmd))
    r_bool, ret = loc.stop_process('result.bag', '-2', 5)
    if not r_bool:
        return False, ret
    return True, ''
