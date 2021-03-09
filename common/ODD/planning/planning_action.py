#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import time
import re
import os
import subprocess
import pandas as pd
import logging
import common.ODD.auto_test_io as io
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped
from common.utils.ros2bag_pandas import *
logger = logging.getLogger()


def extrat_start_end_point(case_list, keyword):
    start_pose_list = []
    start_orientation_list = []
    end_pose_list = []
    end_orientation_list = []
    start_pose_list.append([case_list["start.position.x"], case_list["start.position.y"],
                            case_list["start.position.z"]])
    start_orientation_list.append([case_list["start.orientation.x"], case_list["start.orientation.y"],
                                   case_list["start.orientation.z"], case_list["start.orientation.w"]])
    end_pose_list.append([case_list["end.position.x"], case_list["end.position.y"], case_list["end.position.z"]])
    end_orientation_list.append([case_list["end.orientation.x"], case_list["end.orientation.y"],
                                 case_list["end.orientation.z"], case_list["end.orientation.w"]])
    if keyword == 'start_point':
        result = {'start.position.x': start_pose_list[0][0],
                  'start.position.y': start_pose_list[0][1],
                  'start.position.z': start_pose_list[0][2],
                  'start.orientation.x': start_orientation_list[0][0],
                  'start.orientation.y': start_orientation_list[0][1],
                  'start.orientation.z': start_orientation_list[0][2],
                  'start.orientation.w': start_orientation_list[0][3]}
        return result

    if keyword == 'end_point':
        result = {'end.position.x': end_pose_list[0][0],
                  'end.position.y': end_pose_list[0][1],
                  'end.position.z': end_pose_list[0][2],
                  'end.orientation.x': end_orientation_list[0][0],
                  'end.orientation.y': end_orientation_list[0][1],
                  'end.orientation.z': end_orientation_list[0][2],
                  'end.orientation.w': end_orientation_list[0][3]}
        return result


def read_jira_file(file_path, keyword):
    """
    Import JIRA CSV, read keywords and export relevant information
    JIRA CSV FILE COLUMNS:
        ['Jira ID', 'Priority', 'Story', 'title', 'start.position.x',
       'start.position.y', 'start.position.z', 'start.orientation.x',
       'start.orientation.y', 'start.orientation.z', 'start.orientation.w',
       'end.position.x', 'end.position.y', 'end.position.z',
       'end.orientation.x', 'end.orientation.y', 'end.orientation.z',
       'end.orientation.w', 'bag_name', 'duration']

    KEYWORD：['Jira ID', 'Priority', 'Story' ,'bag_name', 'duration']
       if keyword is 'start point' or 'end_point'  ->  return {'start/end_point':{'start/end.position.x',
       'start/end.position.y', 'start.position.z', 'start.orientation.x',
       'start/end.orientation.y', 'start.orientation.z', 'start.orientation.w'}}

       }
    """
    df = pd.read_csv(file_path)
    dict_df = df.to_dict()
    if 'Jira' in keyword:
        return dict_df["Jira ID"][0]
    if keyword == 'start_point':
        result = {'start.position.x': dict_df['start.position.x'][0],
                  'start.position.y': dict_df['start.position.y'][0],
                  'start.position.z': dict_df['start.position.z'][0],
                  'start.orientation.x': dict_df['start.orientation.x'][0],
                  'start.orientation.y': dict_df['start.orientation.y'][0],
                  'start.orientation.z': dict_df['start.orientation.z'][0],
                  'start.orientation.w': dict_df['start.orientation.w'][0]}
        return result
    if keyword == 'end_point':
        result = {'end.position.x': dict_df['end.position.x'][0],
                  'end.position.y': dict_df['end.position.y'][0],
                  'end.position.z': dict_df['end.position.z'][0],
                  'end.orientation.x': dict_df['end.orientation.x'][0],
                  'end.orientation.y': dict_df['end.orientation.y'][0],
                  'end.orientation.z': dict_df['end.orientation.z'][0],
                  'end.orientation.w': dict_df['end.orientation.w'][0]}
        return result
    else:
        return dict_df[keyword][0]


def local_planning_start():
    """
    [description]: 起planning_stimulator_launch， 子进程"
    :return: subprocess.Popen
    """
    logger.info(START_AUTOWARE_4_PLANNING)
    p1 = subprocess.Popen(START_AUTOWARE_4_PLANNING, stdout=subprocess.PIPE, shell=True)
    logger.info(p1.stdout)
    return p1


def local_docker_start():
    """
    [description]:
    """
    logger.info('start planning docker cmd: {}'.format(START_PLANNING_DOCKER))
    p2 = subprocess.Popen(START_PLANNING_DOCKER, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return p2


def planning_topics_test():
    # detect the process is on
    shown = subprocess.Popen("rostopic list", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = shown.communicate()
    # cmd = 'docker exec {} /bin/bash -c \'source /opt/ros/melodic/setup.bash && ' \
    # 'source /root/autoware4/devel/setup.bash && export ROS_IP={} && ' \
    # 'export ROS_MASTER_URI={} && rosnode list | grep perception\''.format(PERCEPTION_DOCKER_NAME,
    #                                                                       PERCEPTION_IP,
    #                                                                       PERCEPTION_ROS_MASTER_URI)
    # print("cmd in:", "rostopic list")
    if err.decode() is not None:
        logger.info("cmd out: ", err.decode())
    else:
        logger.info("cmd in:", out.decode("utf-8"))
    shown = subprocess.Popen("rostopic list", stdout=subprocess.PIPE, shell=True)
    topics = shown.stdout
    logger.info('start planning topics: {}'.format(topics))
    topic_list = topic_tolist()
    assert check_node_list(PLANNING_TOPICS, topic_list)
    # if 'perception' in topics and 'planning' in topics:
    #     return True
    # return False


def topic_tolist() -> list:
    shown = os.popen("rostopic list")
    topics = shown.readlines()
    return topics


def local_planning_end(p1):
    time.sleep(10)
    logger.info('kill -9 `ps -ef|grep "AutowareArchitectureProposal"|awk \'{{print $2}}\'`')
    logger.info("end local planning env")
    p1.terminate()


def local_docker_end(p2):
    time.sleep(10)
    p2.terminate()
    os.system("docker stop test_docker_sim")
    os.system('kill -9 `ps -ef|grep "docker"|awk \'{{print $2}}\'`')
    logger.info('kill -9 `ps -ef|grep "docker"|awk \'{{print $2}}\'`')


def add_start_end_point(start_postition, start_orientation, end_position, end_orientation):
    """

    :param start_postition: [x,y,z], orientation: [x,y,z,w]
    :param start_orientation: [x,y,z], orientation: [x,y,z,w]
    :param end_position: [x,y,z], orientation: [x,y,z,w]
    :param end_orientation: [x,y,z], orientation: [x,y,z,w]
    :return:
    """
    logger.info('enter add_start_end_point')
    try:
        io_class = io.AutoTestIO()
        logger.info(io_class)
        init_pose = PoseWithCovarianceStamped()  # 起点填充数据，事先用ros topic echo 记录下数据
        init_pose.pose.pose.position.x = start_postition[0]
        init_pose.pose.pose.position.y = start_postition[1]
        init_pose.pose.pose.position.z = start_postition[2]
        init_pose.pose.pose.orientation.x = start_orientation[0]
        init_pose.pose.pose.orientation.y = start_orientation[1]
        init_pose.pose.pose.orientation.z = start_orientation[2]
        init_pose.pose.pose.orientation.w = start_orientation[3]
        io_class.initialpose(init_pose)  # 发送起点
        logger.info("start_point sent")
        time.sleep(1)
        goal_pose = PoseStamped()
        goal_pose.pose.position.x = end_position[0]
        goal_pose.pose.position.y = end_position[1]
        goal_pose.pose.position.z = end_position[2]
        goal_pose.pose.orientation.x = end_orientation[0]
        goal_pose.pose.orientation.y = end_orientation[1]
        goal_pose.pose.orientation.z = end_orientation[2]
        goal_pose.pose.orientation.w = end_orientation[3]
        io_class.goal(goal_pose)  # 发送终点
        logger.info("end_point sent")
        time.sleep(10)
        io_class.engage_autoware(True)  # engage
        io_class.engage_vehicle(True)
        logger.info("engage auto")
        return True, ''
    except Exception as e:
        logger.exception(e)
        return False, "set start end point except, {}".format(e)


TOPICS_LIST = ["/planning/scenario_planning/trajectory",
               "/current_pose", "/vehicle/status/twist",
               "/vehicle/status/velocity"]

TOPICS = "/planning/scenario_planning/trajectory /current_pose " \
         "/vehicle/status/twist /vehicle/status/velocity /planning/mission_planning/route"


def start_record_bag(count_seconds, bag_name):
    """record bag,  放入当前目录"""
    # print(os.popen('env | grep ROS').read())
    # cmd = 'ros2 bag record -o {} {} --duration {}'.format(bag_name, TOPICS, str(count_seconds))
    # cmd = 'ros2 bag record {} -o {}  '.format(TOPICS, bag_name)
    # cmd = 'ros2 bag record {} -o {} -d 60'.format(TOPICS,"/home/autotest/Workspace/autotest/bags/aw4/planning/gt_01/gtt_01")
    cmd = 'ros2 bag record {} -o {}'.format(TOPICS,"/home/autotest/Workspace/autotest/bags/aw4/planning/gt_01/gteg_01")
    time.sleep(3)
    logger.info("the bag recorded address is {}".format(cmd))
    p = subprocess.Popen(cmd, shell=True)
    logger.info("start recording")

    return bag_name


def check_bag():
    count = 0
    logger.info("check bag")
    cmd = "ps -ef | grep record"
    result = os.popen(cmd)
    logger.info(cmd, "the result is {}".format(result))
    count += 1
    logger.info("count: {}".format(count))
    time.sleep(1)
    logger.info("waiting record files {}s".count)
    if "record" in result:
        return False, "waiting time is larger than count time"
    else:
        return True, ""


def check_dir(bag_dir):
    check_bag_dir = os.path.exists(bag_dir)
    if check_bag_dir:
        msg = ""
    else:
        msg = "Bag dir does not exists"
    return check_bag_dir, msg


def topic_csv(bag_name, topic_name,  path, result_file_name):
    # bag_name
    cmd = "ros2 topic echo -b %s -p %s >  %s/%s.csv" % (
        str(bag_name), topic_name, path, result_file_name)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stderr = p.stderr.read().decode('utf-8')
    stdout = p.stdout.read().decode('utf-8')
    logger.info('exec cmd: {}, stdout: {}, stderrr: {}'.format(cmd, stdout, stderr))
    if len(stderr) > 0:
        return False, stderr
    logger.info('CSV file loading complete: ' + topic_name)
    return True, ''


def save_csv_file(path, bag_name):
    for topic in TOPICS.split(" "):
        logger.info("Saving " + topic)
        keyw = topic.split("/")
        logger.info("saving " + keyw[-1] + " ...")
        assert topic_csv(bag_name + ".bag", topic, bag_name + "_" + keyw[-1],
                         path), topic + " could not saved to csv file"
        logger.info("saving address: " + path)
        time.sleep(2)


def compare_bag_sec(gt_bag_path,test_bag_path):
    cmd = "rosbag info {}".format(gt_bag_path)
    cmd1 = "rosbag info {}".format(test_bag_path)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    line = p.stdout.readlines()
    t_line = p1.stdout.readlines()
    pattern = re.compile(r'\d+')
    res = []
    res2 = []
    for i in line:
        ll = i.decode('utf-8')
        ll.strip('')
        if "duration" in ll:
            res = re.findall(pattern, ll)
    for j in t_line:
        t_ll = j.decode('utf-8')
        t_ll.strip('')
        if "duration" in t_ll:
            res2 = re.findall(pattern, t_ll)
    logger.info("gt bag sec: {}.{}s".format(res[0], res[1]))
    logger.info("test bag sec: {}.{}s".format(res2[0], res2[1]))
    sec_count = abs(int(res[0]) - int(res2[0]))
    if int(res2[0]) == 0:
        return False, "recorded bag sec is zero"
    if sec_count > 5:
        return False, "bag sec is not comparable"
    else:
        return True, ""

def db3_to_df(topic, db3_path):

    bag = Ros2bag(db3_path)
    cc = bag.dataframe(include=topic,seconds=True)
    return cc

if __name__ == '__main__':
    cc,dd = compare_bag_sec("~/workspace/autotest/bags/planning/gt_01/gt_01.bag", "~/workspace/autotest/bags/planning/gt_01/test_planning_01.bag")
    print(cc,dd)
