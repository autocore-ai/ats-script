# -*- coding:utf8 -*-
import time
import logging
import subprocess
from common.perception.command import START_AUTOWARE_4, START_PERCEPTION, CHECK_AUTOWARE_4, AUTOWARE_SCREEN_NAME, STOP_AUTOWARE_4,\
    CHECK_PERCEPTION_DOCKER, CHECK_PERCEPTION_NODE, STOP_PERCEPTION, ROSBAG_RECORD_O, ROSBAG_RECORD_O_REMOTE, \
    ROSBAG_PLAY, ROSBAG_PLAY_REMOTE, PERCEPTION_DOCKER_NAME, CHECK_AUTOWARE_4_NODES, AUTOWARE_4_NODES_LIST, \
    PERCEPTION_NODES_LIST
from utils.remote import RemoteP
import common.perception.perception_conf as p_conf
import utils.local as loc
import config
logger = logging.getLogger()


# def check_autoware_status():
#     """
#     check autoware running status
#     1. judge: Is autoware and test env same env?
#     2. if same, local check
#     3. if not, remote to autoware and check
#     return:
#     True, True: first true, check
#     """
#     check_cmd_autoware = 'ps -ef| grep {} | grep -v grep'.format('Autoware')
#     check_cmd_ros = 'ps -ef| grep {} | grep -v grep'.format('ros')
#     if config.TEST_IP == config.PERCEPTION_AUTOWARE4_IP:
#         pass
#     else:
#         logger.info('check remote autoware.4 status: {}'.format(check_cmd_autoware))
#         logger.info('check remote ros status: {}'.format(check_cmd_ros))
#         server = RemoteP(config.PERCEPTION_AUTOWARE4_IP, config.PERCEPTION_AUTOWARE4_PWD, config.PERCEPTION_AUTOWARE4_PWD)
#         r_bool_autoware4, ret_autoware4 = server.exec_comm(check_cmd_autoware)
#         logger.info('check remote autoware4-Autoware, result: {}, msg: {}'.format(r_bool_autoware4, ret_autoware4))
#         if not r_bool_autoware4:
#             return False, ret_autoware4
#         r_bool_ros, ret_ros = server.exec_comm(check_cmd_ros)
#         logger.info('check remote autoware4-ros, result: {}, {}'.format(r_bool_ros, ret_ros))
#         if not r_bool_ros:
#             return False, ret_ros
#
#         run_status = False
#         if 'Autoware' in ret_autoware4 or 'ros' in ret_ros:
#             run_status = True
#         return True, run_status


# def stop_autoware4(signal='-15'):
#     """
#     stop autoware4
#     1. judge:  Is autoware and test env same env?
#     2. if same, local stop
#     3. if not, remote to autoware, to stop
#     """
#     stop_cmd_autoware = 'kill {} `ps -ef|grep "Autoware"|awk \'{{print $2}}\'`'.format(signal)
#     stop_cmd_ros = 'kill {} `ps -ef|grep "ros"|awk \'{{print $2}}\'`'.format(signal)
#     if config.TEST_IP == config.PERCEPTION_AUTOWARE4_IP:
#         pass
#     else:
#         logger.info('stop remote autoware4 command: {}'.format(stop_cmd_autoware))
#         logger.info('stop remote ros command: {}'.format(stop_cmd_ros))
#         server = RemoteP(config.PERCEPTION_AUTOWARE4_IP, config.PERCEPTION_AUTOWARE4_PWD,
#                          config.PERCEPTION_AUTOWARE4_PWD)
#         r_bool_autoware4, ret_autoware4 = server.exec_comm(stop_cmd_autoware)
#         logger.info('stop remote autoware4, result: {}, msg: {}'.format(r_bool_autoware4, ret_autoware4))
#         if not r_bool_autoware4:
#             return False, ret_autoware4
#         r_bool_ros, ret_ros = server.exec_comm(stop_cmd_ros)
#         logger.info('stop remote autoware4, result: {}, msg: {}'.format(r_bool_ros, ret_autoware4))
#         if not r_bool_ros:
#             return False, ret_ros
#         return True, ''


def check_autoware_status():
    """
    check autoware running status by screen
    1. judge: Is autoware and test env same env?
    2. if same, local check
    3. if not, remote to autoware and check
    return:
    True, True: first true, check
    """
    check_cmd_autoware = CHECK_AUTOWARE_4
    logger.info('check autoware4 status, command: {}'.format(check_cmd_autoware))
    check_cmd_node = CHECK_AUTOWARE_4_NODES
    logger.info('check autoware4 nodes status, command: {}'.format(check_cmd_node))

    if config.TEST_IP == p_conf.PERCEPTION_AUTOWARE4_IP:
        p = subprocess.Popen(check_cmd_autoware, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stderr = p.stderr.read().decode('utf-8')
        ret = p.stdout.read().decode('utf-8')
        logger.info('check autoware result, stdout:{}, stderr: {}'.format(ret, stderr))
        if len(stderr) > 1:
            return False, stderr

        if len(ret) == 0:
            return True, False

        # check nodes are all ok
        p = subprocess.Popen(check_cmd_node, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stderr = p.stderr.read().decode('utf-8')
        ret_nodes = p.stdout.read().decode('utf-8')
        logger.info('check Autoware nodes result, stdout: {}, stderr: {}'.format(ret_nodes, stderr))
        # if len(stderr) > 1:
        #     return False, stderr
    else:
        server = RemoteP(p_conf.PERCEPTION_AUTOWARE4_IP, p_conf.PERCEPTION_AUTOWARE4_PWD, p_conf.PERCEPTION_AUTOWARE4_PWD)
        r_bool, ret = server.exec_comm(check_cmd_autoware)
        logger.info('check remote autoware4-Autoware, exec result: {}, autoware status: {}'.format(r_bool, ret))
        if not r_bool:
            return False, ret
        if len(ret) == 0:
            return True, False

        r_bool, ret_nodes = server.exec_comm(check_cmd_node)
        logger.info('check remote autoware4-Autoware nodes, exec result: {}, autoware status: {}'.format(r_bool, ret))
        if not r_bool:
            return False, ret

    if AUTOWARE_SCREEN_NAME not in ret:
        return True, False

    # loop auto other nodes
    for node in AUTOWARE_4_NODES_LIST:
        if node not in ret_nodes:
            return True, False

    return True, True


def start_autoware4():
    """
    start autowate4 by screen
    1. judge:  Is autoware and test env same env?
    2. if same, local start
    3. if not, remote to autoware, to start
    """
    start_cmd_autoware = START_AUTOWARE_4
    logger.info('start autoware4, command: {}'.format(START_AUTOWARE_4))
    if config.TEST_IP == p_conf.PERCEPTION_AUTOWARE4_IP:
        subprocess.Popen(start_cmd_autoware, shell=True)
        # stderr = p.stderr.read().decode('utf-8')
        # if len(stderr) > 1:
        #     logger.error('start autoware failed: {}'.format(stderr))
        #     return False, stderr
        return True, ''
    else:
        server = RemoteP(p_conf.PERCEPTION_AUTOWARE4_IP, p_conf.PERCEPTION_AUTOWARE4_PWD,
                         p_conf.PERCEPTION_AUTOWARE4_PWD)
        r_bool_autoware4, ret_autoware4 = server.exec_comm(start_cmd_autoware)
        logger.info('start remote autoware4, exec result: {}, msg: {}'.format(r_bool_autoware4, ret_autoware4))
        if not r_bool_autoware4:
            return False, ret_autoware4

        return True, ''


def stop_autoware4():
    """
    stop autoware4 by screen
    1. judge:  Is autoware and test env same env?
    2. if same, local stop
    3. if not, remote to autoware, to stop
    """
    stop_cmd_autoware = STOP_AUTOWARE_4
    logger.info('stop autoware4 command: {}'.format(stop_cmd_autoware))
    if config.TEST_IP == p_conf.PERCEPTION_AUTOWARE4_IP:
        subprocess.Popen(stop_cmd_autoware, shell=True, stderr=subprocess.PIPE)
        return True, ''
    else:
        server = RemoteP(p_conf.PERCEPTION_AUTOWARE4_IP, p_conf.PERCEPTION_AUTOWARE4_PWD,
                         p_conf.PERCEPTION_AUTOWARE4_PWD)
        r_bool, ret = server.exec_comm(stop_cmd_autoware)
        logger.info('stop remote autoware4, exec result: {}, msg: {}'.format(r_bool, ret))
        if not r_bool:
            return False, ret
        return True, ''


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


#
# def check_perception_docker_status():
#     """
#     check perception docker status
#     """
#     if PERCEPTION_ENV_REMOTE:
#         remote = RemoteP(config.PERCEPTION_IP, config.PERCEPTION_USER, config.PERCEPTION_PWD)
#         cmd = 'docker ps | grep devel'
#         logger.info('exec remote command, check perception docker status: {}'.format(cmd))
#         r_bool, ret = remote.exec_comm(cmd)
#         logger.info('check perception result:{} {}'.format(r_bool, ret))
#         if not r_bool:
#             return False, ret
#         if not ret:
#             return False, 'docker stopped already.'
#     return True, ''
#
#
# def stop_perception_docker():
#     """
#     stop perception docker
#     """
#     if PERCEPTION_ENV_REMOTE:
#         remote = RemoteP(config.PERCEPTION_IP, config.PERCEPTION_USER, config.PERCEPTION_PWD)
#         cmd = 'docker stop devel'
#         logger.info('exec remote command, stop perception docker: {}'.format(cmd))
#         r_bool, ret = remote.exec_comm(cmd)
#         if not r_bool:
#             return False, ret
#         logger.info('exec remote command , stop perception docker result: {}'.format(ret))
#     return True, ''
#
#
# def check_perception_ok():
#     """
#     check perception is ok by rosnode list
#     """
#     r_bool, node_list = get_perception_node_list()
#     if not r_bool:
#         return False, node_list
#
#     logger.info('check perception in node list')
#     if '/perception/object_recognition/detection/roi_cluster_fusion' not in node_list:
#         return False, 'start failed.'
#     return True, 'start success'
#
#
# def get_perception_node_list():
#     """get perception env rosnode list"""
#     cmd = 'rosnode list'
#     if PERCEPTION_ENV_REMOTE:
#         # cmd = 'export ROS_IP={};export ROS_MASTER_URI={};source /opt/ros/melodic/setup.bash;rosnode list | grep perception'.format(PERCEPTION_IP, PERCEPTION_ROS_MASTER_URI)
#         cmd = 'export ROS_IP={};export ROS_MASTER_URI={};source /home/nv/NVME/aw_debug/perception/perception_radar_v2/autoware4-xavier/devel/setup.bash;rosnode list | grep perception'.format(PERCEPTION_IP, PERCEPTION_ROS_MASTER_URI)
#         logger.info('exec remote command: {}'.format(cmd))
#         remote = RemoteP(config.PERCEPTION_IP, config.PERCEPTION_USER, config.PERCEPTION_PWD)
#         r_bool, ret = remote.exec_comm(cmd)
#     else:  # local operations
#         pass
#     if not r_bool:
#         return False, 'get remote rosnode error: {}'.format(ret)
#     rosnode_list = [node for node in ret.split('\n') if node]
#     logger.info('remote rosnode list: {}'.format(ret))
#     return True, rosnode_list
#
#
# def stop_perception_node_list(node_list):
#     """
#     To stop node list by rosnode kill
#     """
#     node_str = ' '.join(node_list)
#     cmd = 'rosnode kill {}'.format(node_str)
#     if PERCEPTION_ENV_REMOTE:
#         # cmd = 'export ROS_IP={};export ROS_MASTER_URI={};source /opt/ros/melodic/setup.bash;rosnode kill {}'.format(
#         #     PERCEPTION_IP, PERCEPTION_ROS_MASTER_URI, node_str)
#         cmd = 'export ROS_IP={};export ROS_MASTER_URI={};source /home/nv/NVME/aw_debug/perception/perception_radar_v2/autoware4-xavier/devel/setup.bash;rosnode kill {}'.format(
#             PERCEPTION_IP, PERCEPTION_ROS_MASTER_URI, node_str)
#         remote = RemoteP(config.PERCEPTION_IP, config.PERCEPTION_USER, config.PERCEPTION_PWD)
#         r_bool, ret = remote.exec_comm(cmd)
#         print(ret)
#         logger.info('rosnode kill result: {}'.format(ret))
#         # stop screen
#         screen_stop = 'screen -X -S perception-test quit'
#         r_bool, ret = remote.exec_comm(screen_stop)
#         logger.info('screen kill result: {}'.format(ret))
#     else:  # local operations
#         pass
#     if not r_bool:
#         return False, 'get remote rosnode error: {}'.format(ret)
#
#     return True, 'killed.'


def record_bag(result_bag_path, bag_duration):
    """
    record bag
    1. if local record bag, just record to local dir
    2. if need to remote record bag, record bag at remote, than download to local dir
    bag_name: according to bag_name to get record bag path
    """
    topic = '/perception/object_recognition/objects'
    if p_conf.PERCEPTION_BAG_REMOTE:
        ip, user, pwd = p_conf.PERCEPTION_BAG_REMOTE_IP, p_conf.PERCEPTION_BAG_REMOTE_USER, p_conf.PERCEPTION_BAG_REMOTE_PWD
        logger.info('need to record bag at remote, env: {}:{}/{}'.format(ip, user, pwd))
        remote = RemoteP(ip, user, pwd)
        record_command = ROSBAG_RECORD_O_REMOTE.format(name=result_bag_path, t=bag_duration, topic=topic)
        logger.info('begin to record bag, remote command: {}'.format(record_command))
        r_bool, ret = remote.exec_comm(record_command)
        logger.info('remote record bag, exec result: {} status: {}'.format(r_bool, ret))
        if not r_bool:
            return False, ret
    else:
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
    if p_conf.PERCEPTION_BAG_REMOTE:
        play_cmd = ROSBAG_PLAY_REMOTE.format(bag_path=bag_path)
        ip, user, pwd = p_conf.PERCEPTION_BAG_REMOTE_IP, p_conf.PERCEPTION_BAG_REMOTE_USER, p_conf.PERCEPTION_BAG_REMOTE_PWD
        logger.info('need to play bag at remote, env: {}:{}/{}'.format(ip, user, pwd))
        remote = RemoteP(ip, user, pwd)
        logger.info('play command: {}'.format(play_cmd))
        r_bool, ret = remote.exec_comm(play_cmd)
        logger.info('play return: {}, msg: {}'.format(r_bool, ret))
        if not r_bool:
            return False, ret
    else:
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

    if p_conf.PERCEPTION_BAG_REMOTE:
        ip, user, pwd = p_conf.PERCEPTION_BAG_REMOTE_IP, p_conf.PERCEPTION_BAG_REMOTE_USER, p_conf.PERCEPTION_BAG_REMOTE_PWD
        logger.info('to check record bag at remote, env: {}:{}/{}'.format(ip, user, pwd))
        remote = RemoteP(ip, user, pwd)
        r_bool, ret = remote.exec_comm(check_cmd)
        logger.info('check record stauts, exec result: {} status: {}'.format(r_bool, ret))
        if not r_bool:
            return False, ret
        record_status = False  # record status
        if 'result.bag' in ret:
            record_status = True
    else:
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
    if p_conf.PERCEPTION_BAG_REMOTE:
        ip, user, pwd = p_conf.PERCEPTION_BAG_REMOTE_IP, p_conf.PERCEPTION_BAG_REMOTE_USER, p_conf.PERCEPTION_BAG_REMOTE_PWD
        logger.info('need to stop record bag at remote, env: {}:{}/{}'.format(ip, user, pwd))
        remote = RemoteP(ip, user, pwd)
        r_bool, ret = remote.exec_comm(stop_cmd)
        logger.info('stop remote record, return: {}, msg: {}'.format(r_bool, ret))
        if not r_bool:
            return False, ret
    else:
        r_bool, ret = loc.stop_process('result.bag', '-2', 5)
        if not r_bool:
            return False, ret
    return True, ''


if __name__ == '__main__':
    r_bool, 