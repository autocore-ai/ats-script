# -*- coding:utf8 -*-
import sys
sys.path.append('../')
sys.path.append('../../')
sys.path.append('../../../')
import time
import logging
import allure
import subprocess
import signal
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

    proc = subprocess.Popen(record_comm, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
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

    t = 0
    while not stop_record_sub.stop:
        time.sleep(1)
        t += 1
        logger.info('listen autoware state topic message, %ds ...' % t)
        if t > max_wait_time:
            logger.error('listen autoware state timeout: %d' % max_wait_time)
            return False, 'listen autoware state timeout: %d' % max_wait_time

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    stop_record_sub.destroy_node()
    rclpy.shutdown()
    return True, ''


def stop_reocrd_bag(proc):
    """
    stop record bag
    """
    proc.send_signal(signal.SIGINT)
    ret_code = proc.wait()
    logger.info('stop record bag process, return code: {}'.format(ret_code))
    return ret_code, ''


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
    msg_min_count = gt_bag_msg_count - 100
    msg_max_count = gt_bag_msg_count + 100
    if ret_bag_msg_count < msg_min_count or ret_bag_msg_count > msg_max_count:
        return False, 'result bag count[{ret_count}] not in [{min_count}, {max_count}]'.format(ret_count=ret_bag_msg_count, 
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
        min_count = count - 100
        max_count = count + 100
        ret_msg_count = ret_topic_count_dict[topic]
        if ret_msg_count < min_count or min_count > max_count:
            return False, 'result bag topic[{0}] msg count not in [{1}, {2}]'.format(topic, min_count, max_count)

    return True, ''


def check_autoware_state(gt_bag_path, bag_record_path):
    state_topic = conf.STATE
    gt_bag = Ros2bag(gt_bag_path)
    ret_bag = Ros2bag(bag_record_path)
    # read topic msg
    gt_dataframe = gt_bag.dataframe(include=[state_topic])
    ret_dataframe = ret_bag.dataframe(include=[state_topic])

    gt_state = [(content[0]) for _, content in gt_dataframe.iterrows()]
    ret_state = [(content[0]) for _, content in ret_dataframe.iterrows()]
   
    if gt_state != ret_state:
        return False, 'autoware state list are different, gt state: {gt}, real state: {ret}'.format(gt=gt_state, ret=ret_state)
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

    gt_route_id_list = [gt_dataframe[key].values.astype(int) for key in gt_dataframe.keys() if key.split('.')[-1] == 'lane_ids']
    ret_route_id_list = [ret_dataframe[key].values.astype(int) for key in ret_dataframe.keys() if key.split('.')[-1] == 'lane_ids']
    
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
    step = 20

    gt_bag = Ros2bag(gt_bag_path)
    ret_bag = Ros2bag(bag_record_path)
    
    # read topic msg
    gt_dataframe = gt_bag.dataframe(include=[current_post_topic])
    ret_dataframe = ret_bag.dataframe(include=[current_post_topic])
    

    # position check
    logger.info("*" * 20 + " check current pose position begin " + "*" * 20)
    gt_position_list = [(content[0], content[1], content[2]) for _, content in gt_dataframe.iterrows()]
    ret_position_list = [(content[0], content[1], content[2]) for _, content in ret_dataframe.iterrows()]

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
    max_euc_distance = 1
    for euc in euc_dis_ret:
        if euc > max_euc_distance:
            return False, 'current pose max euclidean distance[{}] > {}'.format(euc, max_euc_distance)

    logger.info("*" * 20 + " check current pose position end" + "*" * 20)

    # orientation check
    logger.info("*" * 20 + " check current pose orientation begin " + "*" * 20)
    gt_ori_list = [(content[3], content[4], content[5], content[6]) for _, content in gt_dataframe.iterrows()]
    ret_ori_list = [(content[3], content[4], content[5], content[6]) for _, content in ret_dataframe.iterrows()]

    r_bool,gt_ori_list, ret_ori_list, msg = deal_list(gt_ori_list, ret_ori_list, step)
    if not r_bool:
        return False, msg

    gt_yaw_list = [to_euler_angles(ori) for ori in gt_ori_list]
    ret_yaw_list = [to_euler_angles(ori) for ori in ret_ori_list]

    # make picture line row
    pic_current_pose_yaw_list = [( {'title': 'Current Pose Yaw', 'data': {'gt_yaw': gt_yaw_list, 'real_yaw': ret_yaw_list}}), 
                                 ( {'title': 'Current Pose gt', 'data': {'gt_yaw': gt_yaw_list}}),
                                 ( {'title': 'Current Pose real', 'data': {'real_yaw': ret_yaw_list}})]
    save_path = '%s/current_pose_yaw_lines.png' % bag_record_path
    r_bool, msg = generate_line_rows(pic_current_pose_yaw_list, save_path)
    if not r_bool:
        return False, msg
    attach_mag = 'Current Pose orientation graph'
    allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)

    r_bool, euc_dis_ret = cal_euc_distance(gt_position_list, ret_position_list)
    if not r_bool:
        return False, euc_dis_ret
    max_yaw = 10
    for dis in euc_dis_ret:
        if dis > max_yaw:
            return False, 'current pose max yaw [{}] > {}'.format(euc, max_yaw)

    logger.info("*" * 20 + " check current pose orientation end " + "*" * 20)

    return True, ''


def check_twist(gt_bag_path, bag_record_path):
    """
    ckeck twist and generate graph
    """
    twist_topic = conf.TWIST_TOPIC
    step = 20

    gt_bag = Ros2bag(gt_bag_path)
    ret_bag = Ros2bag(bag_record_path)
    
    # read topic msg
    gt_dataframe = gt_bag.dataframe(include=[twist_topic])
    ret_dataframe = ret_bag.dataframe(include=[twist_topic])

    logger.info("*" * 20 + " check line x begin " + "*" * 20)
    gt_line_x = [content[0] for _, content in gt_dataframe.iterrows()]
    ret_line_x = [content[0] for _, content in ret_dataframe.iterrows()]

    r_bool,gt_line_x, ret_line_x, msg = deal_list(gt_line_x, ret_line_x, step)
    if not r_bool:
        return False, msg

    # make picture line row
    pic_line_x_list = [( {'title': 'Twist Line X', 'data': {'gt_twist': gt_line_x, 'real_twist': ret_line_x}}), 
                                 ( {'title': 'Twist gt line x', 'data': {'gt_yaw': gt_line_x}}),
                                 ( {'title': 'Twist real line x', 'data': {'real_yaw': ret_line_x}})]
    save_path = '%s/twist_line_x.png' % bag_record_path
    r_bool, msg = generate_line_rows(pic_line_x_list, save_path)
    if not r_bool:
        return False, msg

    attach_mag = 'Twist line-x speed graph'
    allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)

    r_bool, euc_dis_ret = cal_euc_distance(gt_line_x, ret_line_x)
    if not r_bool:
        return False, euc_dis_ret
    max_dis = 2
    for dis in euc_dis_ret:
        if dis > max_dis:
            return False, 'Twist max distance [{}] > {}'.format(euc, max_dis)
        
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
    step = 20

    gt_bag = Ros2bag(gt_bag_path)
    ret_bag = Ros2bag(bag_record_path)
    
    # read topic msg
    gt_dataframe = gt_bag.dataframe(include=[vlty_topic])
    ret_dataframe = ret_bag.dataframe(include=[vlty_topic])

    logger.info("*" * 20 + " check velocity begin " + "*" * 20)
    gt_vlty = [content[0] for _, content in gt_dataframe.iterrows()]
    ret_vlty = [content[0] for _, content in ret_dataframe.iterrows()]

    r_bool,gt_vlty, ret_vlty, msg = deal_list(gt_vlty, ret_vlty, step)
    if not r_bool:
        return False, msg

    # make picture line row
    pic_vlty_list = [( {'title': 'Twist velocity', 'data': {'gt_velocity': gt_vlty, 'real_velocity': ret_vlty}}), 
                                 ( {'title': 'Twist gt velocity', 'data': {'gt_velocity': gt_vlty}}),
                                 ( {'title': 'Twist real velocity', 'data': {'real_velocity': ret_vlty}})]
    save_path = '%s/velocity.png' % bag_record_path
    r_bool, msg = generate_line_rows(pic_vlty_list, save_path)
    if not r_bool:
        return False, msg

    attach_mag = 'Velocity graph'
    allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)

    r_bool, euc_dis_ret = cal_euc_distance(gt_vlty, ret_vlty)
    if not r_bool:
        return False, euc_dis_ret
    max_dis = 2
    for dis in euc_dis_ret:
        if dis > max_dis:
            return False, 'Velocity max distance [{}] > {}'.format(euc, max_dis)
        
    r_bool, std, diff_list, msg = cal_std(gt_vlty, ret_vlty)
    allure.attach('ground truth velocity and real result velocity std:\n {}'.format(std),
                  'ground truth velocity and real result velocity std',
                   allure.attachment_type.TEXT)
    logger.info('Velocity std: {}'.format(std))

    logger.info("*" * 20 + " check velocity end " + "*" * 20)

    return True, ''
