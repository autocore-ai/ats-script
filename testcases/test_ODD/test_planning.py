"""
planning 模块 case

1. 一条路段，有拐弯， 无障碍， 无红绿灯
2. 一条路段， 无拐弯， 无障碍, 无红绿灯
"""
import allure
from common.process import *
import pytest
from common.planning.planning_command import *
import common.planning.planning_conf as conf
from common.planning.planning_bag_analysis import *
from common.generate_case_data import generate_case_data
import logging
logger = logging.getLogger()
import pandas as pd
CASE_LIST = generate_case_data('{}/testcases/test_ODD/cases/planning_cases.csv'.format(TEST_CASE_PATH))


def make_test_case(story, case_data, case_level, case_desc, jira_id):

    @allure.feature('planning')
    @pytest.mark.parametrize("case_data", case_data, ids=[case_desc])
    @allure.story(story)
    @allure.severity(case_level)
    def test_planning(planning_env, case_data):
    # def test_planning(case_data):
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
        name = case_data['CaseName']
        gt_name = case_data['gt_name']
        bag_path= '{}/bags/planning_bags/{}/'.format(TEST_CASE_PATH,gt_name)
        # with allure.step("collect ground_truth bag data"):
        #     #
        #     # for topic in TOPICS.split(" "):
        #     #     print(topic)
        #     #     keyw = topic.split("/")
        #     #     assert topic_csv(gt_name+".bag", topic, "gt_"+keyw[-1],conf.LOCAL_GT_BAG_PATH), topic+" could not saved to csv file"
        #     #     time.sleep(2)
        #     #
        #     save_csv_file(bag_path,gt_name)
        #     for i in range(5):
        #         logger.info("Waiting.. {}s".format(i+1))
        #         time.sleep(1)

        step_3 = "start_record bag"
        with allure.step(step_3):
            # start_position_sample = [-815.500610352, -249.504760742, 0]
            # start_orientation_sample = [0, 0, -0.994364378898, 0.10601642316]
            # end_position_sample = [-1130.37866211, -401.696289062, 0]
            # end_orientation_sample = [0, 0, -0.771075397889, 0.636743850202]
            bag_name_record = start_record_bag(90, bag_path+name)
            # assert check_bag(bag_path+name+".bag"), "bag has not recorded successfully"

        step_4 = "add start end point， and engage"
        with allure.step(step_4):
            logger.info(step_4)
            time.sleep(1)
            dict_start = read_jira_file(conf.LOCAL_JIRA_PLANNING_FILE_PATH, "start_point")
            dict_end = read_jira_file(conf.LOCAL_JIRA_PLANNING_FILE_PATH, "end_point")
            a_l = list(dict_start.values())
            logger.info("start_point is {}".format(a_l))
            b_l = list(dict_end.values())
            logger.info("end_point is {}".format(b_l))
            start_position_sample = a_l[0:3]
            start_orientation_sample = a_l[3:]
            end_position_sample = b_l[0:3]
            end_orientation_sample = b_l[3:]
            add_start_end_point(start_position_sample, start_orientation_sample, end_position_sample,
                                end_orientation_sample)
            time.sleep(1)
            logger.info("auto engage")

            # assert r_bool, msg

        # step_check="check bag finished or not"
        # with allure.step(step_check):
        #     logger.info("step_check")
        #     print('step check')
        #     """
        #     cd ~/workspace/test_autoware/AutowareArchitectureProposal;./start_planning_test.sh
        #     export ROS_IP=127.0.0.1;export ROS_MASTER_URI=http://127.0.0.1:11311;/home/adlink/workspace/autotest/common/script/run_docker_sim.sh
        #     """
        #     check_result, msg = check_bag(90,bag_path+name)
        #     logger.info(check_result,msg)
        #     assert check_result, msg

        step_6 = "6. end recording maunally"
        with allure.step(step_6):
            logger.info(step_6)
            logger.info('record end, ready to kill -2')
            # time.sleep(90)
            for i in range(int(case_data['duration'])):
                time.sleep(1)
                logger.info("waitting 1s")
            r_bool, msg = local_stop_process(bag_path+name, '-2')
            logger.info(r_bool)
            logger.info(msg)
            logger.info("end recording ")

            time.sleep(3)

        # step_5 = "collect data"
        # with allure.step(step_5):
        #
        #     for topic in TOPICS.split(" "):
        #         print(topic)
        #         keyw = topic.split("/")
        #         assert topic_csv(bag_path+name+".bag", topic, keyw[-1],bag_path), topic+" could not saved to csv file"
        #         time.sleep(2)


        BAG_VELOCITY_FILE_PATH = bag_path+"test_01_twist.csv"
        GROUNDTRUTH_VELOCITY_FILE_PATH =  bag_path+"/"+"gt_01_twist.csv"

        BAG_POSE_FILE_PATH = bag_path+"test_01_current_pose.csv"
        GROUNDTRUTH_FILE_PATH = bag_path+"gt_01_current_pose.csv"


        BAG_VELOCITY_FILE_PATH = bag_path+"test_01_twist.csv"
        logger.info("BAG VELOCITY bag path : {}".format(BAG_VELOCITY_FILE_PATH))
        GROUNDTRUTH_VELOCITY_FILE_PATH =  bag_path+"gt_01_twist.csv"

        BAG_POSE_FILE_PATH = bag_path+"test_01_current_pose.csv"
        GROUNDTRUTH_FILE_PATH = bag_path+"gt_01_current_pose.csv"


        GROUNDTRUTH_TRAJECTORY = bag_path+ "gt_01_trajectory.csv"
        TEST_TRAJECTORY = bag_path+ "test_01_trajectory.csv"
        logger.info("trajectory bag path {}".format(TEST_TRAJECTORY))

        GROUNDTRUTH_ROUTE = bag_path +"gt_01_route.csv"
        TEST_ROUTE = bag_path+ "test_01_route.csv"

        with allure.step("Data analysis"):
            with allure.step("1. 如果输出文档速度一直为 0   -> not pass"):
                a = pd.read_csv(BAG_VELOCITY_FILE_PATH )
                assert velocity_not_zero(a)

            with allure.step("2. current_pose 值一直没有变 -> not pass"):
                b = pd.read_csv(BAG_POSE_FILE_PATH)
                assert current_pose_change(b)

            with allure.step("3.current_pose: 两值比较： 1.欧式距离之差 -》 超过一个range， 不pass "):
                df1, df2 = csv_to_df(GROUNDTRUTH_FILE_PATH, BAG_POSE_FILE_PATH)
                logger.info(df1.shape[0])
                logger.info(df2.shape[0])
                count = df1.shape[0]-df2.shape[0]
                df1.drop(df1.tail(count).index, inplace=True)
                logger.info(df1.shape[0])
                logger.info("columns are {} , {}".format(df1.shape[0],df2.shape[0]))
                # result, key_name, df_all , er_msg= current_pose_analysis_eur(50, df1, df2)
                # df_all.to_csv("./1.csv")
                # allure.attach.file(TEST_CASE_PATH+"/1.csv")
                # assert result, er_msg

            with allure.step("4.current pose: 两值比较： 2. 偏航角之差  -》 超过一个range， 不pass "):
                result, c_yaw_list = current_pose_analysis_yaw(100, df1, df2)
                assert result
                with open(bag_path+'1.txt', 'w') as f:
                    for i in range(len(c_yaw_list)):
                        f.write(str(c_yaw_list[i]))
                allure.attach.file(bag_path+"1.txt","current_pose")

            with allure.step("5. current twist 两值比较： ×3.6 画图"):
                dfc, dfd = csv_to_df(GROUNDTRUTH_VELOCITY_FILE_PATH, BAG_VELOCITY_FILE_PATH)
                plot_twist(dfc, dfd)
                allure.attach.file("./twist.png","current_twist")

            with allure.step("6.trajectory 欧式距离之差 做图，前40的points"):
                plot_eu(GROUNDTRUTH_TRAJECTORY,TEST_TRAJECTORY)
                logger.info(TEST_CASE_PATH+"/trajectory.png")
                allure.attach.file(TEST_CASE_PATH + "/trajectory.png")
                allure.attach.file(TEST_CASE_PATH+"/trajectory1.png","trajectory_eu")

            with allure.step("6.trajectory 偏航角之差 做图，前40的points"):
                a = pd.read_csv(GROUNDTRUTH_TRAJECTORY)
                b = pd.read_csv(TEST_TRAJECTORY)
                count = a.shape[0] - b.shape[0]
                a.drop(a.tail(count).index, inplace=True)
                trajectory_yaw_plot(a,b)
                allure.attach.file(TEST_CASE_PATH + "/delta_yaw.png")
                allure.attach.file(TEST_CASE_PATH+"/delta_yaw1.png","trajectory_delta_yaw")

            with allure.step("7. plot pose"):
                pic_loc = plot_pose(df1, df2)
                allure.attach.file(pic_loc)

            with allure.step("8. /planning/mission_planning/route   信息匹配"):
                GROUNDTRUTH_ROUTE = conf.LOCAL_PLANNING_BAG_PATH+gt_name+"/"+ "gt_01_route.csv"
                TEST_ROUTE = conf.LOCAL_PLANNING_BAG_PATH+gt_name+"/"+ "test_01_route.csv"
                assert route_same(GROUNDTRUTH_ROUTE,TEST_ROUTE), "planning_route msg is not the same "

    # 把生成的函数返回
    return test_planning



for case_arg in CASE_LIST:
    logger.info(case_arg)
    print(case_arg)
    globals()[case_arg['CaseName']] = make_test_case(case_arg['Story'], [case_arg['test_case']],
                                                     case_arg['Priority'], case_arg['Title'],
                                                     case_arg['Jira_ID'])



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
