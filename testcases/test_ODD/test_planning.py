"""
planning 模块 case

1. 一条路段，有拐弯， 无障碍， 无红绿灯
2. 一条路段， 无拐弯， 无障碍, 无红绿灯
"""
import allure
from common.process import *
import time
import logging
import os
import subprocess
import pytest
import re
import json
from common.planning_command import *
from common.planning_bag_analysis import *

logger = logging.getLogger()
import pandas as pd


@allure.feature('planning')
def test_planning_testcase(name="test_01"):
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
    """
    step_1 = "start environment "
    with allure.step(step_1):
        logger.info(step_1)
        time.sleep(10)
        p1 = local_planning_start()
        logger.info(p1)
        assert local_planning_start_test(), 'local planning env started fail'

    step_2 = "start docker"
    with allure.step(step_2):
        logger.info(step_2)
        time.sleep(10)
        p2 = local_docker_start()
        time.sleep(20)
        assert pid_exists(p2.pid), "local docker env started fail"

    step_3 = "start_record bag"
    with allure.step(step_3):
        # start_position_sample = [-815.500610352, -249.504760742, 0]
        # start_orientation_sample = [0, 0, -0.994364378898, 0.10601642316]
        # end_position_sample = [-1130.37866211, -401.696289062, 0]
        # end_orientation_sample = [0, 0, -0.771075397889, 0.636743850202]
        bag_name = start_record_bag(90, name)
        assert check_bag(name+".bag"), "bag has not recorded successfully"

    step_4 = "add start end point， and engage"
    with allure.step(step_4):
        logger.info(step_4)
        time.sleep(1)
        dict_start= read_jira_file(LOCAL_JIRA_PLANNING_FILE_PATH,"start_point")
        dict_end= read_jira_file(LOCAL_JIRA_PLANNING_FILE_PATH,"end_point")
        a_l = list(dict_start.values())
        b_l = list(dict_end.values())
        start_position_sample = a_l[0:3]
        start_orientation_sample = a_l[3:]
        end_position_sample = b_l[0:3]
        end_orientation_sample = b_l[3:]
        add_start_end_point(start_position_sample, start_orientation_sample, end_position_sample,
                            end_orientation_sample)
        time.sleep(1)
        engage_auto()

    step_6 = "6. end recording maunally"
    with allure.step(step_6):
        logger.info(step_6)
        logger.info('record end, ready to kill -2')
        r_bool, msg = local_stop_process(bag_name, '-2')
        logger.info(r_bool)
        logger.info(msg)
        logger.info("end recording ")
        time.sleep(3)


    with allure.step("stop environment"):
        time.sleep(5)
        logger.info("stop env")
        local_planning_end(p1)
        time.sleep(10)
        local_docker_end(p2)

    step_5 = "collect data"
    with allure.step(step_5):
        for topic in TOPICS.split(" "):
            print(topic)
            keyw = topic.split("/")
            assert topic_csv(name+".bag", topic, keyw[-1]), topic+" could not saved to csv file"
            time.sleep(2)

    BAG_VELOCITY_FILE_PATH = "/bags/record_vehiclewist1.csv"
    GROUNDTRUTH_VELOCITY_FILE_PATH = "/bags/record_vehiclewist1.csv"
    BAG_POSE_FILE_PATH = "/bags/record_current_pose1.csv"
    GROUNDTRUTH_FILE_PATH = "/bags/record_current_pose.csv"

    with allure.step("Data analysis"):
        with allure.step("1. 如果输出文档速度一直为 0   -> not pass"):
            a = pd.read_csv(BAG_VELOCITY_FILE_PATH)
            assert velocity_not_zero(a)

        with allure.step("2. current_pose 值一直没有变 -> not pass"):
            b = pd.read_csv(BAG_POSE_FILE_PATH)
            assert current_pose_change(b)

        with allure.step("3.current_pose: 两值比较： 1.欧式距离之差 -》 超过一个range， 不pass "):
            df1, df2 = csv_to_df(GROUNDTRUTH_FILE_PATH, BAG_POSE_FILE_PATH)
            df2.drop(df2.tail(3).index, inplace=True)
            result, key_name, df_all = current_pose_analysis_eur(50, df1, df2)
            df_all.to_csv("./1.csv")
            allure.attach.file("/home/minwei/autotest/1.csv")
            assert result

        with allure.step("4.current pose: 两值比较： 2. 偏航角之差  -》 超过一个range， 不pass "):
            result, c_yaw_list = current_pose_analysis_yaw(100, df1, df2)
            assert result
            with open('1.txt', 'w') as f:
                for i in range(len(c_yaw_list)):
                    f.write(str(c_yaw_list[i]))
            allure.attach.file("/home/minwei/autotest/1.txt")

        with allure.step("5. current twist 两值比较： ×3.6 画图"):
            dfc, dfd = csv_to_df(GROUNDTRUTH_VELOCITY_FILE_PATH, BAG_VELOCITY_FILE_PATH)
            plot_twist(dfc, dfd)
            allure.attach.file("/home/minwei/autotest/common/twist.png")

        with allure.step("6. /planning/mission_planning/route   不为空"):
            pass

        with allure.step("7. plot pose"):
            pic_loc = plot_pose(df1, df2)
            allure.attach.file(pic_loc)




# 局限于只有一条路经， 无障碍物

if __name__ == '__main__':
    # logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # logger = logging.getLogger(__name__)
    #
    # logger.info("Start print log")
    # logger.debug("Do something")
    # logger.warning("Something maybe fail.")
    # logger.info("Finish")
    # args = ['-v', '--alluredir', '~/autotest/allure_reports/allure']
    # pytest.main(args)

    # test_make_planning_testcase()

    args = ['-v', '-s', '--alluredir', '/home/minwei/autotest/allure_reports/result']
    # args = ['-v', '-s', '-k', 'child']
    print(args)
    # 根据参数生成执行命令，命令里包含了模块，用例等级等
    test_result = pytest.main(args)  # 全部通过，返回0；有失败或者错误，则返回1
    print(test_result)

    # 生成报告
    print('=' * 20)
    # generate = 'allure generate /home/minwei/autotest/allure_reports/result/ -o /home/minwei/autotest/allure_reports/report/ --clean'
    # print('generate allure_results: {}'.format(generate))
    # os.system(generate)