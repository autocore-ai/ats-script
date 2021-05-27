# -*- coding:utf8 -*-
import sys
sys.path.append('../')
sys.path.append('../../')
sys.path.append('../../../')
import time
import os
import logging
import allure
import subprocess
import threading
import signal
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import rclpy

import testSDV.common.sdv.config as conf
from testSDV.common.utils.ros2bag_pandas import Ros2bag
from testSDV.common.utils.calculate import cal_euc_distance, deal_list, to_euler_angles, cal_std
from testSDV.common.utils.generate_graph import generate_trace_rows, generate_line_rows
from testSDV.common.utils.auto_test_io import AutowareStateSubscriber

logger = logging.getLogger()


def record_bag(result_bag_path, bag_duration=None):
    """
    bag_name: according to bag_name to get record bag path
    """
    topic = ' '.join(conf.RECORD_TOPIC_LIST)
    record_comm = 'ros2 bag record {topic} -o {bag_name}'.format(topic=topic, bag_name=result_bag_path)
    logger.info('begin to record bag, command: {}'.format(record_comm))

    proc = subprocess.Popen(record_comm, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    time.sleep(2)  # give time to ready record
    
    return True, proc


def wait_stop_signal(max_wait_time=100):
    """
    wait stop signal topic
    subscription 
    """
    logger.info('wait max time: %d' % max_wait_time)
    rclpy.init()

    stop_record_sub = AutowareStateSubscriber()
    th = threading.Thread(target=rclpy.spin, args=(stop_record_sub,))
    th.start()

    wait_t = 0
    while wait_t > 0 and not stop_record_sub.running:
        time.sleep(1)
        wait_t += 1
        logger.info('waiting autoware start, waiting %ds ...' % wait_t)

    t = 0
    while not stop_record_sub.stop:
        time.sleep(1)
        t += 1
        logger.info('listening autoware state topic message, %ds ...' % t)
        if t > max_wait_time:
            logger.error('listening autoware state timeout: %d' % max_wait_time)
            return False, 'listening autoware state timeout: %d' % max_wait_time

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    # logger.info('++++++++++++++++ begin to destory node ++++++++++++++++++')
    # stop_record_sub.destroy_node()
    # logger.info('++++++++++++++++ destory node successfully ++++++++++++++++++')
    # rclpy.shutdown()
    # logger.info('++++++++++++++++ shut down ++++++++++++++++++')
    return True, ''


def stop_reocrd_bag(proc):
    """
    stop record bag
    """
    try:
        # proc.send_signal(signal.SIGINT)
        proc.send_signal(signal.SIGTERM)
        
        # ret_code = proc.wait()
        os.killpg(proc.pid, signal.SIGINT)
    except Exception as e:
        logger.exception(e)

    # logger.info('stop record bag process, return code: {}'.format(ret_code))
    time.sleep(2)
    logger.info('stop record finished')
    return True, ''


def check_bag_OK(gt_bag_path, ret_bag_path):
    """
    check record bag is Ok
    1. can read
    2. message count
    3. topics info
    """
    gt_bag = Ros2bag(gt_bag_path)
    gt_bag_info = gt_bag.bag_info

    ret_bag = Ros2bag(ret_bag_path)
    ret_bag_info = ret_bag.bag_info
    
    # check msg count
    gt_bag_msg_count = gt_bag_info['rosbag2_bagfile_information']['message_count']
    ret_bag_msg_count = ret_bag_info['rosbag2_bagfile_information']['message_count']
    msg_min_count = gt_bag_msg_count - 1000
    msg_max_count = gt_bag_msg_count + 1000
    if ret_bag_msg_count < msg_min_count or ret_bag_msg_count > msg_max_count:
        return False, 'result bag message counts[{ret_count}] not in [{min_count}, {max_count}]'.format(ret_count=ret_bag_msg_count, 
                                                                                                 min_count=msg_min_count,
                                                                                                 max_count=msg_max_count)

    # check topic
    gt_topic_info = gt_bag_info['rosbag2_bagfile_information']['topics_with_message_count']
    ret_topic_info = gt_bag_info['rosbag2_bagfile_information']['topics_with_message_count']
    gt_topic_count_dict = {detail['topic_metadata']['name']: detail['message_count'] for detail in gt_topic_info}
    ret_topic_count_dict = {detail['topic_metadata']['name']: detail['message_count'] for detail in ret_topic_info}

    for topic, count in gt_topic_count_dict.items():
        if topic not in ret_topic_count_dict.keys():
            return False, 'result bag don\'t have the topic %s' % topic
        min_count = count - 500
        max_count = count + 500
        ret_msg_count = ret_topic_count_dict[topic]
        if ret_msg_count < min_count or min_count > max_count:
            return False, 'result bag topic[{0}] msg count not in [{1}, {2}]'.format(topic, min_count, max_count)

    return True, ''


def check_autoware_state(gt_bag_path, bag_record_path):
    state_topic = conf.STATE
    ret_bag = Ros2bag(bag_record_path)
    # read topic msg
    ret_dataframe = ret_bag.dataframe(include=[state_topic])

    ret_state = set((content[0]) for _, content in ret_dataframe.iterrows())
    allure.attach('autoware state \nreal: {}'.format(ret_state),
                  'autoware state',
                   allure.attachment_type.TEXT)
    if not ('WaitingForRoute' in ret_state and 'Planning' in ret_state and 'WaitingForEngage' in ret_state and 'Driving' in ret_state and 'ArrivedGoal' in ret_state):
        return False, 'autoware state error, real state: {ret}'.format(ret=ret_state)
    return True, ''


def check_route_ids(gt_bag_path, bag_record_path):
    route_id_topic = conf.ROUTE_TOPIC

    gt_bag = Ros2bag(gt_bag_path)
    ret_bag = Ros2bag(bag_record_path)
    # read topic msg
    gt_dataframe = gt_bag.dataframe(include=[route_id_topic])
    gt_topic_keys = gt_dataframe.keys()

    ret_dataframe = ret_bag.dataframe(include=[route_id_topic])
    ret_topic_keys = ret_dataframe.keys()

    gt_route_id_list = [list(gt_dataframe[key].values.astype(int)) for key in gt_dataframe.keys() if key.split('.')[-1] == 'lane_ids']
    ret_route_id_list = [list(ret_dataframe[key].values.astype(int)) for key in ret_dataframe.keys() if key.split('.')[-1] == 'lane_ids']

    allure.attach('expect route ids: {}\nreal route ids: {}'.format(gt_route_id_list, ret_route_id_list), 'compare route ids',
                          allure.attachment_type.TEXT)
    
    if gt_route_id_list != ret_route_id_list:
        return False, 'result bag route ids are not equal ground truth, result ids: {}, gt ids: {}'.format(ret_route_id_list, gt_route_id_list)
    
    return True, ''


def check_current_pose(gt_bag_path, bag_record_path):
    """
    ckeck current posse and generate trace
    1. check position
    2. check orientation(yaw)
    """
    current_post_topic = conf.CURRENT_POSE_TOPIC
    step = 1000

    gt_bag = Ros2bag(gt_bag_path)
    ret_bag = Ros2bag(bag_record_path)
    
    # read topic msg
    gt_dataframe = gt_bag.dataframe(include=[current_post_topic])
    ret_dataframe = ret_bag.dataframe(include=[current_post_topic])
    
    # position check
    logger.info("*" * 20 + " check current pose position begin " + "*" * 20)
    gt_position_list = [(content[0], content[1], content[2]) for _, content in gt_dataframe.iterrows()]
    ret_position_list = [(content[0], content[1], content[2]) for _, content in ret_dataframe.iterrows()]

    # dtw
    distance, path = fastdtw(gt_position_list, ret_position_list, dist=euclidean)
    logger.info('dtw of position: {}'.format(distance))
    allure.attach('dtw of position: {}'.format(distance),
                  'position DTW',
                   allure.attachment_type.TEXT)
    if distance > 200:
        return False, 'position DTW[{}] > 200'.format(distance)

    r_bool,gt_position_list, ret_position_list, msg = deal_list(gt_position_list, ret_position_list, step)
    if not r_bool:
        return False, msg

    # make picture
    pic_current_pose_position_list = [{ 'trace_title': 'Current Pose trace', 
                                        'trace_dict': {
                                            'ground truth':[(position[0], position[1]) for position in gt_position_list],
                                            'real result': [(position[0], position[1]) for position in ret_position_list]
                                        }
                                    },
                                    { 'trace_title': 'Current Pose GT trace', 
                                        'trace_dict': {
                                            'ground truth':[(position[0], position[1]) for position in gt_position_list],
                                        }
                                    },
                                    { 'trace_title': 'Current Pose Real trace', 
                                        'trace_dict': {
                                            'real result': [(position[0], position[1]) for position in ret_position_list]
                                        }
                                    },
                                    ]
    save_path = '%s/current_pose_trace.png' % bag_record_path
    logger.info('current pose trace picture path: %s' % save_path)
    r_bool, msg = generate_trace_rows(pic_current_pose_position_list, save_path)
    if not r_bool:
        return False, msg
    attach_mag = 'Current Pose Trace'
    allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)
    
    r_bool, euc_dis_ret = cal_euc_distance(gt_position_list, ret_position_list)
    if not r_bool:
        return False, euc_dis_ret

    r_bool, std, diff_list, msg = cal_std(gt_position_list, ret_position_list)
    logger.info('cal current pose position std: {}'.format(std))

    allure.attach('ground truth position and real result position euclidean distance:\n {}'.format(euc_dis_ret),
                  'ground truth position and real result position euclidean distance',
                   allure.attachment_type.TEXT)
    # max_euc_distance = 5
    # for euc in euc_dis_ret:
    #     if euc > max_euc_distance:
    #         return False, 'current pose max euclidean distance[{}] > {}'.format(euc, max_euc_distance)

    logger.info("*" * 20 + " check current pose position end" + "*" * 20)

    # orientation check
    logger.info("*" * 20 + " check current pose orientation begin " + "*" * 20)
    gt_ori_list = [(content[3], content[4], content[5], content[6]) for _, content in gt_dataframe.iterrows()]
    ret_ori_list = [(content[3], content[4], content[5], content[6]) for _, content in ret_dataframe.iterrows()]

    # dtw
    distance, path = fastdtw(gt_ori_list, ret_ori_list, dist=euclidean)
    logger.info('dtw of orientation: {}'.format(distance))
    allure.attach('dtw of orientation: {}'.format(distance),
                  'orientation DTW',
                   allure.attachment_type.TEXT)
    if distance > 300:
        return False, 'orientation DTW[{}] > 300'.format(distance)

    r_bool,gt_ori_list, ret_ori_list, msg = deal_list(gt_ori_list, ret_ori_list, step)
    if not r_bool:
        return False, msg

    gt_yaw_list = [to_euler_angles(ori) for ori in gt_ori_list]
    ret_yaw_list = [to_euler_angles(ori) for ori in ret_ori_list]

    # make picture line row
    pic_current_pose_yaw_list = [( {'title': 'Current Pose Yaw', 'x_label': 'time', 'y_label': 'yaw', 'data': {'gt_yaw': gt_yaw_list, 'real_yaw': ret_yaw_list}}), 
                                 ( {'title': 'Current Pose gt', 'x_label': 'time', 'y_label': 'yaw', 'data': {'gt_yaw': gt_yaw_list}}),
                                 ( {'title': 'Current Pose real', 'x_label': 'time', 'y_label': 'yaw', 'data': {'real_yaw': ret_yaw_list}})]
    save_path = '%s/current_pose_yaw_lines.png' % bag_record_path
    r_bool, msg = generate_line_rows(pic_current_pose_yaw_list, save_path)
    if not r_bool:
        return False, msg
    attach_mag = 'Current Pose orientation graph'
    allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)

    r_bool, euc_dis_ret = cal_euc_distance(gt_position_list, ret_position_list)
    if not r_bool:
        return False, euc_dis_ret
    # max_yaw = 100
    # for dis in euc_dis_ret:
    #     if dis > max_yaw:
    #         return False, 'current pose max yaw [{}] > {}'.format(euc, max_yaw)

    logger.info("*" * 20 + " check current pose orientation end " + "*" * 20)

    return True, ''


def check_twist(gt_bag_path, bag_record_path):
    """
    ckeck twist and generate graph
    """
    twist_topic = conf.TWIST_TOPIC
    step = 1000

    gt_bag = Ros2bag(gt_bag_path)
    ret_bag = Ros2bag(bag_record_path)
    
    # read topic msg
    gt_dataframe = gt_bag.dataframe(include=[twist_topic])
    ret_dataframe = ret_bag.dataframe(include=[twist_topic])

    logger.info("*" * 20 + " check line x begin " + "*" * 20)
    gt_line_x = [content[0] for _, content in gt_dataframe.iterrows()]
    ret_line_x = [content[0] for _, content in ret_dataframe.iterrows()]

    distance, _ = fastdtw(gt_line_x, ret_line_x, dist=euclidean)
    logger.info('DTW of twist: {}'.format(distance))
    allure.attach('dtw of twist: {}'.format(distance),
                  'twist DTW',
                   allure.attachment_type.TEXT)
    # dtw
    if distance > 50:
        return False, 'twist DTW[{}] > 50'.format(distance)

    r_bool,gt_line_x, ret_line_x, msg = deal_list(gt_line_x, ret_line_x, step)
    if not r_bool:
        return False, msg

    # make picture line row
    pic_line_x_list = [( {'title': 'Twist Line X', 'x_label': 'time', 'y_label': 'line-x speed', 'data': {'gt_twist': gt_line_x, 'real_twist': ret_line_x}}), 
                                 ( {'title': 'Twist gt line x', 'x_label': 'time', 'y_label': 'line-x speed', 'data': {'gt_yaw': gt_line_x}}),
                                 ( {'title': 'Twist real line x', 'x_label': 'time', 'y_label': 'line-x speed', 'data': {'real_yaw': ret_line_x}})]
    save_path = '%s/twist_line_x.png' % bag_record_path
    r_bool, msg = generate_line_rows(pic_line_x_list, save_path)
    if not r_bool:
        return False, msg

    attach_mag = 'Twist line-x speed graph'
    allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)

    r_bool, euc_dis_ret = cal_euc_distance(gt_line_x, ret_line_x)
    if not r_bool:
        return False, euc_dis_ret
    # max_dis = 5
    # for dis in euc_dis_ret:
    #     if dis > max_dis:
    #         return False, 'Twist max distance [{}] > {}'.format(euc, max_dis)
        
    r_bool, std, diff_list, msg = cal_std(gt_line_x, ret_line_x)
    allure.attach('ground truth line-x and real result line-x std:\n {}'.format(std),
                  'ground truth line-x and real result line-x std',
                   allure.attachment_type.TEXT)
    logger.info('twist std: {}'.format(std))

    logger.info("*" * 20 + " check line x end " + "*" * 20)

    return True, ''


def check_velocity(gt_bag_path, bag_record_path):
    """
    check velocity
    """
    vlty_topic = conf.VELOCITY_TOPIC
    step = 1000

    gt_bag = Ros2bag(gt_bag_path)
    ret_bag = Ros2bag(bag_record_path)
    
    # read topic msg
    gt_dataframe = gt_bag.dataframe(include=[vlty_topic])
    ret_dataframe = ret_bag.dataframe(include=[vlty_topic])

    logger.info("*" * 20 + " check velocity begin " + "*" * 20)
        
    gt_vlty = [content[2] for _, content in gt_dataframe.iterrows()]
    ret_vlty = [content[2] for _, content in ret_dataframe.iterrows()]
    distance, _ = fastdtw(gt_vlty, ret_vlty, dist=euclidean)
    allure.attach('dtw of velocity: {}'.format(distance),
                  'velocity DTW',
                   allure.attachment_type.TEXT)
    logger.info('DTW of velocity: {}'.format(distance))
    # dtw
    if distance > 50:
        return False, 'velocity DTW[{}] > 50'.format(distance)

    r_bool, gt_vlty, ret_vlty, msg = deal_list(gt_vlty, ret_vlty, step)
    if not r_bool:
        return False, msg

    # make picture line row
    pic_vlty_list = [( {'title': 'Twist velocity', 'x_label': 'time', 'y_label': 'velocity', 'data': {'gt_velocity': gt_vlty, 'real_velocity': ret_vlty}}), 
                                 ( {'title': 'Twist gt velocity', 'x_label': 'time', 'y_label': 'velocity', 'data': {'gt_velocity': gt_vlty}}),
                                 ( {'title': 'Twist real velocity','x_label': 'time', 'y_label': 'velocity', 'data': {'real_velocity': ret_vlty}})]
    save_path = '%s/velocity.png' % bag_record_path
    r_bool, msg = generate_line_rows(pic_vlty_list, save_path)
    if not r_bool:
        return False, msg

    attach_mag = 'Velocity graph'
    allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)

    r_bool, euc_dis_ret = cal_euc_distance(gt_vlty, ret_vlty)
    if not r_bool:
        return False, euc_dis_ret
    # max_dis = 5
    # for dis in euc_dis_ret:
    #     if dis > max_dis:
    #         return False, 'Velocity max distance [{}] > {}'.format(dis, max_dis)
        
    r_bool, std, diff_list, msg = cal_std(gt_vlty, ret_vlty)
    allure.attach('ground truth velocity and real result velocity std:\n {}'.format(std),
                  'ground truth velocity and real result velocity std',
                   allure.attachment_type.TEXT)
    logger.info('Velocity std: {}'.format(std))

    logger.info("*" * 20 + " check velocity end " + "*" * 20)

    return True, ''
