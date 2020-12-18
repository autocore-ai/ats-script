# ====================== 1 ======================
import common.auto_test_io
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped
from common.action import *
import time
import pandas as pd
import os
import common.action as comm
import errno
from common.planning.command import *
import logging
import traceback
import config

logger = logging.getLogger()
io = common.auto_test_io


# def check_autoware

def extrat_start_end_point(case_list, keyword):
    start_pose_list = []
    start_orientation_list = []
    end_pose_list = []
    end_orientation_list = []
    start_pose_list.append([case_list["start.position.x"], case_list["start.position.y"], case_list["start.position.z"]])
    start_orientation_list.append([case_list["start.orientation.x"], case_list["start.orientation.y"],
                                  case_list["start.orientation.z"],case_list["start.orientation.w"]])
    end_pose_list.append([case_list["end.position.x"], case_list["end.position.y"], case_list["end.position.z"]])
    end_orientation_list.append([case_list["end.orientation.x"], case_list["end.orientation.y"],
                                  case_list["end.orientation.z"], case_list["end.orientation.w"]])
    if keyword == 'start_point':
        result = {'start.position.x': start_pose_list[0][0],
                      'start.position.y':  start_pose_list[0][1],
                      'start.position.z':  start_pose_list[0][2],
                      'start.orientation.x':  start_orientation_list[0][0],
                      'start.orientation.y':  start_orientation_list[0][1],
                      'start.orientation.z': start_orientation_list[0][2],
                      'start.orientation.w':  start_orientation_list[0][3]}
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
    print(df)
    dict_df = df.to_dict()
    print(dict_df)
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
    print('start planning docker cmd: {}'.format(START_PLANNING_DOCKER))
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
        print("cmd out: ", err.decode())
    else:
        print("cmd in:", out.decode("utf-8"))
    shown = subprocess.Popen("rostopic list",stdout=subprocess.PIPE, shell=True)
    topics = shown.stdout
    logger.info('start planning topics: {}'.format(topics))
    topic_list = topic_tolist()
    assert check_node_list(PLANNING_TOPICS, topic_list)
    # if 'perception' in topics and 'planning' in topics:
    #     return True
    # return False


def docker_start(aw_log_path):
    """
    for open branch:
    subprocess starts docker sh file
    """
    start_cmd = '{cmd} > {log_path}'.format(cmd=START_DOCKER_4_PLANNING, log_path=aw_log_path)
    if config.RVIZ == 1:
        start_cmd = '{cmd} > {log_path}'.format(cmd=START_DOCKER_4_PLANNING_RVIZ, log_path=aw_log_path)
    logger.info('start autoware cmd: {}'.format(start_cmd))
    r_bool, msg = comm.start_docker(start_cmd)
    return r_bool,msg
    # docker_content = subprocess.Popen(START_DOCKER_4_PLANNING, stdout=subprocess.PIPE, shell=True)
    # logger.info(docker_content.stdout)
    # return docker_content


def check_docker():
    cmd_docker = 'docker ps | grep %s' % PLANNING_DOCKER_NAME
    logger.info('check planning docker, cmd: {}'.format(cmd_docker))
    p = subprocess.Popen(cmd_docker, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stderr = p.stderr.read().decode('utf-8')
    stdout = p.stdout.read().decode('utf-8')
    logger.info('check planning docker, stdout: {}, stderr: {}'.format(stdout, stderr))
    if len(stderr) > 0:
        return False, stderr
    if len(stdout) == 0:  # docker is not exist, return
        return True, False
    logger.info('planning docker is running...')


def docker_end():
    """
    for open branch:
    subprocess ends docker sh file
    """
    r_bool, s_bool = comm.stop_docker(PLANNING_DOCKER_NAME)
    return r_bool, s_bool


def topic_tolist() -> list:
    shown = os.popen("rostopic list")
    topics = shown.readlines()
    return topics


def local_planning_end(p1):
    "结束local planning子进程"
    time.sleep(10)
    ll = os.system('kill -9 `ps -ef|grep "AutowareArchitectureProposal"|awk \'{{print $2}}\'`')
    ll_ros = os.system('kill -9 `ps -ef|grep "ros"|awk \'{{print $2}}\'`')
    logger.info('kill -9 `ps -ef|grep "AutowareArchitectureProposal"|awk \'{{print $2}}\'`')
    logger.info("end local planning env")
    p1.terminate()


def local_docker_end(p2):
    "结束docker进程"
    time.sleep(10)
    p2.terminate()
    print("local docker end")
    os.system("docker stop test_docker_sim")
    os.system('kill -9 `ps -ef|grep "docker"|awk \'{{print $2}}\'`')
    logger.info('kill -9 `ps -ef|grep "docker"|awk \'{{print $2}}\'`')


def add_start_end_point(start_postition, start_orientation, end_position, end_orientation):
    "position: [x,y,z], orientation: [x,y,z,w]"
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
        print("end_point sent")
        time.sleep(10)
        io_class.engage_autoware(True)  # engage
        io_class.engage_vehicle(True)
        logger.info("engage auto")
        print("engage auto")
        return True, ''
    except Exception as e:
        traceback.print_exc()
        logger.exception(e)
        return False, "set start end point except, {}".format(e)


# def engage_auto():
#     io_class = io.AutoTestIO()
#     io_class.engage_autoware(True)  # engage
#     logger.info("engage auto")

TOPICS_LIST = ["/planning/scenario_planning/trajectory",
               "/current_pose", "/vehicle/status/twist",
               "/vehicle/status/velocity"]

TOPICS = "/planning/scenario_planning/trajectory /current_pose " \
         "/vehicle/status/twist /vehicle/status/velocity /planning/mission_planning/route"


def start_record_bag(count_seconds, bag_name):
    """record bag,  放入当前目录"""
    # print(os.popen('env | grep ROS').read())
    cmd = 'rosbag record -O {} {} --duration {}'.format(bag_name, TOPICS, str(count_seconds))
    print("start recording")
    logger.info("the bag recorded address is {}".format(cmd))
    p = subprocess.Popen(cmd, shell=True)
    # # check record bag has finished or not
    # time.sleep(count_seconds)
    logger.info("start recording")

    return bag_name


def check_bag(wait_time, bag_name):
    # rosbag.rosbag_main.info_cmd("/home/minwei/autotest/common/08.bag")
    count = 0
    logger.info("checkbag")

    # result = os.popen("rosbag info " + bag_name)
    # logger.info(result.read())
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


def topic_csv(bag_name, topic_name, result_file_name, path):
    # bag_name
    cmd = "rostopic echo -b %s -p %s >  %s/%s.csv" % (
        str(bag_name), topic_name, path, result_file_name)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stderr = p.stderr.read().decode('utf-8')
    stdout = p.stdout.read().decode('utf-8')
    logger.info('exec cmd: {}, stdout: {}, stderrr: {}'.format(cmd, stdout, stderr))
    if len(stderr) > 0:
        return False, stderr
    logger.info('CSV file loading complete: ' + topic_name)
    return True, ''
    # process = len(os.popen(
    #     "rostopic echo -b %s -p %s >  %s/%s.csv" % (
    #         str(path + bag_name), topic_name, path, result_file_name)
    # ).readlines())
    # logger.info("the process=" + str(process))
    # if process == 0:
    #     logger.info('CSV file loading complete: '+ topic_name)
    #     print('CSV file loading complete: '+ topic_name)
    #     return True
    # else:
    #     return False


#     complete
def save_csv_file(path, bag_name):
    for topic in TOPICS.split(" "):
        logger.info("Saving " + topic)
        keyw = topic.split("/")
        logger.info("saving " + keyw[-1] + " ...")
        assert topic_csv(bag_name + ".bag", topic, bag_name + "_" + keyw[-1],
                         path), topic + " could not saved to csv file"
        logger.info("saving address: " + path)
        time.sleep(2)


def check_save_csv():
    pass

if __name__ == '__main__':

    pass

    # import common.planning.planning_conf as conf
    # name = "test_planning_01"
    # gt_name = "gt_01"
    # bag_path = '{}/bags/planning/'.format(TEST_CASE_PATH)
    # p2 = subprocess.Popen(START_DOCKER_4_PLANNING, stdout=subprocess.PIPE, shell=True)
    # time.sleep(20)
    # # bag_path = "/home/minwei/autotest/bags/planning/"
    # print(bag_path+name)
    # bag_name_record = start_record_bag(60, bag_path + name)
    # time.sleep(1)
    # dict_start = read_jira_file(conf.LOCAL_JIRA_PLANNING_FILE_PATH, "start_point")
    # time.sleep(1)
    # dict_end = read_jira_file(conf.LOCAL_JIRA_PLANNING_FILE_PATH, "end_point")
    # a_l = list(dict_start.values())
    # print("start_point is {}".format(a_l))
    # b_l = list(dict_end.values())
    # print("end_point is {}".format(b_l))
    # start_position_sample = a_l[0:3]
    # start_orientation_sample = a_l[3:]
    # end_position_sample = b_l[0:3]
    # end_orientation_sample = b_l[3:]
    # add_start_end_point(start_position_sample, start_orientation_sample, end_position_sample,
    #                     end_orientation_sample)
    # time.sleep(10)
    # print("auto engage")
    # for i in range(int(60)):
    #     time.sleep(1)
    #     print("waitting {}s".format(i))
    # # r_bool, msg = local_stop_process(bag_path+name, '-2')
    # # logger.info(r_bool)
    # # logger.info(msg)
    # print("end recording ")
    #
    # time.sleep(10)
    #
    # for topic in TOPICS.split(" "):
    #     print(topic)
    #     keyw = topic.split("/")
    #     assert topic_csv(bag_path + name + ".bag", topic, "test_01_" + keyw[-1],
    #                      bag_path), topic + " could not saved to csv file"
    #     time.sleep(2)
    # for i in range(3):
    #     logger.info("Waiting bag record.. {}s".format(i + 1))
    #     time.sleep(1)

