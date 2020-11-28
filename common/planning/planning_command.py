"""

1.起planning，本地AutowareA. setup.bash , roslaunch map
预计在这一步骤里头加上起点终点接口    会写进docker里面

2.起本地docker （这块以后会有变动）
docker run --rm -i --gpus=all --net=host --name=test_docker_sim --privileged -v
/tmp/.X11-unix:/tmp/.X11-unix:rw -v $HOME/.Xauthority:$HOME/.Xauthority:rw -e ROS_MASTER_URI=${ROS_MASTER_URI} -e ROS_IP=${ROS_IP} -e DISPLAY=${DISPLAY} -e XAUTHORITY=${XAUTH} autocore/simulator_for_sdk

3.起点终点检测是否存在， 不存在或者异常，报错， 退出

4.engage/ disengage ， 速度限速接口设置， 小车是否发生速度变动，若无， 报错退出

5.开始录bag 的/planning/scenario_planning/trajectory/ , vehicle/status/twist, 接口给的current pose

6.检测小车到达终点（追踪出来的位置）， 结束录bag
7.查看bag 信息， 大小， message 是否有异常


planning 验证过程：（先提条件：已经拿到ground truth bag和待验证的bag）


1.两个bags 的/planning/scenario_planning/trajectory,vehicle/status/twist, 接口给的current pose 存入csv文件里
eg:
export ROS_IP=192.168.50.113;export ROS_MASTER_URI=http://192.168.50.113:11311;source /home/minwei/AutowareArchitectureProposal/devel/setup.bash; rostopic echo -b 1.bag -p /planning/scenario_planning/trajectory >  record_trajectory.csv

2.取出pose 进行比较， 计算方差
3.得出vehicle/status/twist结果来测试规划模块速度， 方位是否一致
"""
# ====================== 1 ======================
import subprocess
import auto_io.auto_test_io
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped
import time
import os
import common.planning.planning_conf as conf
import errno
from common.command import *
import logging

logger = logging.getLogger()

io = auto_io.auto_test_io
import pandas as pd


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
       if keyword is 'start/end_point'  ->  return {'start/end_point':{'start/end.position.x',
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
    "起planning_stimulator_launch， 子进程"
    p1 = subprocess.Popen(START_AUTOWARE_4_PLANNING, stdout=subprocess.PIPE, shell=True)
    logger.info(p1.stdout)
    return p1


def local_planning_start_test():
    # 检测进程起来了
    shown = os.popen("rostopic list")
    topics = shown.read()
    logger.info('start planning topics: {}'.format(topics))
    if 'perception' in topics and 'planning' in topics:
        return True
    return False



def local_docker_start():
    "起planning_stimulator_launch"
    time.sleep(30)
    logger.info('start planning docker cmd: {}'.format(START_PLANNING_DOCKER))
    p2 = subprocess.Popen(START_PLANNING_DOCKER, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    logger.info(p2.stdout)
    return p2


def pid_exists(pid):
    """Check whether pid exists in the current process table.
    """
    if pid < 0:
        return False
    if pid == 0:
        raise ValueError('invalid PID 0')
        return False
    try:
        os.kill(pid, 0)
    except OSError as err:
        if err.errno == errno.ESRCH:
            return False
        elif err.errno == errno.EPERM:
            return True
    else:
        return True


def local_planning_end(p1):
    "结束local planning子进程"
    time.sleep(10)
    ll = os.system('kill -9 `ps -ef|grep "AutowareArchitectureProposal"|awk \'{{print $2}}\'`')
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
    io_class = io.AutoTestIO()
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

def engage_auto():
    io_class = io.AutoTestIO()
    io_class.engage_autoware(True)  # engage
    logger.info("engage auto")

TOPICS_LIST = ["/planning/scenario_planning/trajectory", "/current_pose", "/vehicle/status/twist",
               "/vehicle/status/velocity"]
TOPICS = "/planning/scenario_planning/trajectory /current_pose /vehicle/status/twist /vehicle/status/velocity /planning/mission_planning/route"

def start_record_bag(count_seconds, bag_name):
    """record bag,  放入当前目录"""
    # print(os.popen('env | grep ROS').read())
    cmd = 'rosbag record -O {} {} --duration {}'.format(bag_name, TOPICS, str(count_seconds))
    print("start recording")
    logger.info(cmd)
    subprocess.Popen(cmd, shell=True)
    logger.info("start recording")
    return bag_name

def check_bag(bag_name):
    # rosbag.rosbag_main.info_cmd("/home/minwei/autotest/common/08.bag")
    try:
        result = os.popen("rosbag info /home/minwei/autotest/" + bag_name)
        print(result.read())
        return True
    except:
        print(Exception)
        return False


def topic_csv(bag_name, topic_name, result_file_name, path):
    # bag_name

    process = len(os.popen(
        "rostopic echo -b %s -p %s >  %s/%s.csv" % (
            str(path + bag_name), topic_name, path, result_file_name)
    ).readlines())
    logger.info("the process=" + str(process))
    if process == 0:
        logger.info('CSV file loading complete: '+ topic_name)
        print('CSV file loading complete: '+ topic_name)
        return True
    else:
        return False


def bag_demo():
    # 录取一个含有/planning/scenario_planning/trajectory， /current_pose，/vehicle/status/twist，  /vehicle/status/velocity的bag
    time.sleep(10)
    p1 = local_planning_start()
    time.sleep(30)
    p2 = local_docker_start()
    time.sleep(30)
    start_position_sample = [-815.500610352, -249.504760742, 0]
    start_orientation_sample = [0, 0, -0.994364378898, 0.10601642316]
    end_position_sample = [-1130.37866211, -401.696289062, 0]
    end_orientation_sample = [0, 0, -0.771075397889, 0.636743850202]
    add_start_end_point(start_position_sample, start_orientation_sample, end_position_sample, end_orientation_sample)
    time.sleep(45)
    # topic_csv("/home/minwei/autotest/bags/05.bag", "/planning/scenario_planning/trajectory", "record_result")
    # time.sleep(10)
    local_planning_end(p1)
    time.sleep(10)
    local_docker_end(p2)


#     complete
def save_csv_file(path,bag_name):
    for topic in TOPICS.split(" "):
        logger.info("Saving "+ topic)
        keyw = topic.split("/")
        logger.info("saving "+ keyw[-1] + " ...")
        assert topic_csv(bag_name + ".bag", topic, "test_" + keyw[-1],
                         path), topic + " could not saved to csv file"
        logger.info("saving address: "+ path)
        time.sleep(2)
if __name__ == '__main__':
    # save_csv_file(conf.LOCAL_TEST_BAG_PATH,"test_01")
    save_csv_file(conf.LOCAL_GT_BAG_PATH, "gt_01")
    # /home/minwei/autotest/bags/planning_bags/test_bags/test_01.bag
    # time.sleep(10)
    # p1 = local_planning_start()
    # for i in range(1, 31):
    #     time.sleep(1)
    #     print('sleep {}s'.format(i))
    # # time.sleep(30)
    # p2 = local_docker_start()
    # for i in range(1, 31):
    #     time.sleep(1)
    #     print('sleep {}s'.format(i))
    # start_position_sample = [-815.500610352, -249.504760742, 0]
    # start_orientation_sample = [0, 0, -0.994364378898, 0.10601642316]
    # end_position_sample = [-1130.37866211, -401.696289062, 0]
    # end_orientation_sample = [0, 0, -0.771075397889, 0.636743850202]
    # add_start_end_point(start_position_sample, start_orientation_sample, end_position_sample, end_orientation_sample)
    # # time.sleep(30)
    # # record_bag(60,"08",TOPICS)
    # record_bag(60, "08")
    # time.sleep(4)
    # local_planning_end(p1)
    # time.sleep(3)
    # local_docker_end(p2)
    #
    #
    # check_bag("08")
    # bag_demo()
    # time.sleep(10)
    # topic_csv("/home/minwei/autotest/common/2020-11-18-15-47-44.bag", "/planning/scenario_planning/trajectory", "record_result")
    # time.sleep(10)
    # topic_csv("/home/minwei/autotest/common/2020-11-18-15-47-44.bag", "/current_pose", "record_current_pose")
    # time.sleep(10)
    # topic_csv("/home/minwei/autotest/common/2020-11-18-15-47-44.bag", "/vehicle/status/twist", "record_vehiclewist")
    # time.sleep(10)
    # topic_csv("/home/minwei/autotest/common/2020-11-18-15-47-44.bag", "/vehicle/status/velocity", "record_vehiclevelocity")
    #
