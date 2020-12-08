"""
planning 模块 case

1. 一条路段，有拐弯， 无障碍， 无红绿灯
2. 一条路段， 无拐弯， 无障碍, 无红绿灯
"""
import allure
from common.process import *
import pytest
import common.planning.planning_conf as conf
from common.planning.planning_bag_analysis import *
from common.generate_case_data import generate_case_data
import logging
from common.action import *
logger = logging.getLogger()
CASE_LIST = generate_case_data('{}/testcases/test_ODD/cases/planning_cases.csv'.format(TEST_CASE_PATH))


def make_test_case(story, case_data, case_level, case_desc):

    @allure.feature('planning')
    @pytest.mark.parametrize("case_data", case_data, ids=[case_desc])
    @allure.story(story)
    @allure.severity(case_level)
    def test_planning(planning_env, case_data):
        """
        1. Planning, local autowarea setup.bash , roslaunch map
        It is expected that in this step, the interface will be written into docker

        2. Local docker (this will change in the future)



        3. Check whether the starting and ending points exist, do not exist or are abnormal, report an error and exit



        4. Engage / disengage, speed limit interface settings,
        whether the car speed changes, if not, report an error exit



        5. Start recording / planning / scenario of bag_ Planning / trajectory /,
        vehicle / status / twist, current pose given by the interface



        6. Detect the car arriving at the destination (traced position) and finish recording bag

        7. Check whether the bag message, size and message are abnormal
        """
        name = case_data['CaseName']
        gt_name = case_data['gt_name']
        bag_path = '{}/bags/planning_bags/{}/'.format(TEST_CASE_PATH, gt_name)
        # with allure.step("collect ground_truth bag data"):
        #     #
        #     # for topic in TOPICS.split(" "):
        #     #     print(topic)
        #     #     keyw = topic.split("/")
        #     #     assert topic_csv(gt_name+".bag", topic,
        #     "gt_"+keyw[-1],conf.LOCAL_GT_BAG_PATH), topic+" could not saved to csv file"
        #     #     time.sleep(2)
        #     #
        #     # save_csv_file(bag_path,gt_name)
        #     for i in range(3):
        #         logger.info("Waiting.. {}s".format(i+1))
        #         time.sleep(1)
        #
        #
        #     for topic in TOPICS.split(" "):
        #         print(topic)
        #         keyw = topic.split("/")
        #         assert topic_csv(bag_path+gt_name+".bag", topic,
        #         "gt_01_"+keyw[-1],bag_path), topic+" could not saved to csv file"
        #         time.sleep(2)
        #
        step_3 = "start_record bag"
        with allure.step(step_3):
            # start_position_sample = [-815.500610352, -249.504760742, 0]
            # start_orientation_sample = [0, 0, -0.994364378898, 0.10601642316]
            # end_position_sample = [-1130.37866211, -401.696289062, 0]
            # end_orientation_sample = [0, 0, -0.771075397889, 0.636743850202]
            bag_name_record = start_record_bag(90, bag_path+name)
            logger.info("recording bag address".format(bag_name_record))
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
        #     /home/adlink/workspace/autotest/common/script/run_docker_sim.sh
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
                logger.info("waitting {}s".format(i))
            # r_bool, msg = local_stop_process(bag_path+name, '-2')
            # logger.info(r_bool)
            # logger.info(msg)
            logger.info("end recording ")

            time.sleep(10)

        step_5 = "collect data"
        with allure.step(step_5):
            for topic in TOPICS.split(" "):
                print(topic)
                keyw = topic.split("/")
                assert topic_csv(bag_path+name+".bag", topic, "test_01_"+keyw[-1], bag_path), topic + " could not saved to csv file"
                time.sleep(2)
            for i in range(3):
                logger.info("Waiting bag record.. {}s".format(i+1))
                time.sleep(1)

        gt_pose_path = bag_path+"gt_01_current_pose.csv"
        t_v_path = bag_path+"test_01_twist.csv"
        logger.info("BAG VELOCITY bag path : {}".format(t_v_path))
        gt_v_path = bag_path+"gt_01_twist.csv"

        t_pose_path = bag_path + "test_01_current_pose.csv"
        gt_pose_file = bag_path + "gt_01_current_pose.csv"

        gt_tra_path = bag_path + "gt_01_trajectory.csv"
        t_tra_path = bag_path + "test_01_trajectory.csv"
        logger.info("trajectory bag path {}".format(t_tra_path))

        with allure.step("Data analysis"):
            with allure.step("1. /current_twist is always zero  -> not pass"):
                a_df = pd.read_csv(t_v_path)
                allure.attach.file(gt_v_path, "gt velocity ")
                allure.attach.file(t_v_path, "test velocity")
                assert velocity_not_zero(a_df)

            with allure.step("2. current_pose value has not changed -> not pass"):
                b_df = pd.read_csv(t_pose_path)
                assert current_pose_change(b_df)

            with allure.step("3.current_pose: gt/test comparison： 1.eur distance larger than one range， not pass "):
                df1, df2 = csv_to_df(gt_pose_file, t_pose_path)
                c = df1.shape[0]
                d = df2.shape[0]
                logger.info(c)
                logger.info(d)
                if c > d:
                    count = df1.shape[0]-df2.shape[0]
                    df1.drop(df1.tail(count).index, inplace=True)
                else:
                    count = df2.shape[0] - df1.shape[0]
                    df2.drop(df2.tail(count).index, inplace=True)

                logger.info("columns are {} , {}".format(df1.shape[0], df2.shape[0]))

            with allure.step("4.current pose: comparison： 2. yaw angle is larger ont certain range， not pass "):
                result, c_yaw_list = current_pose_analysis_yaw(100, df1, df2)
                # assert result
                with open(bag_path+'1.txt', 'w') as f:
                    for i in range(len(c_yaw_list)):
                        f.write(str(c_yaw_list[i]))
                logger.info("current pose list: {}".format(c_yaw_list))

                fig, ax = plt.subplots(1, 1, figsize=(10, 6))
                ax.plot(c_yaw_list)
                plt.savefig(bag_path+"current_pose.png")
                logger.info("current pose pic address: {}".format(bag_path+"current_pose.png"))
                allure.attach.file(bag_path+"1.txt", "current_pose txt file ")
                allure.attach.file(bag_path+"current_pose.png", "current_pose pic")

            with allure.step("5. current twist comparison： ×3.6 plot"):
                dfc, dfd = csv_to_df(gt_v_path, t_v_path)
                add = bag_path+"twist.png"
                plot_twist(dfc, dfd, add)
                allure.attach.file(add, "current_twist")

            with allure.step("6. plot pose"):
                df1, df2 = csv_to_df(gt_pose_path, t_pose_path)
                pose_pic_add = bag_path+"pose.png"
                pic_loc = plot_pose(df1, df2, pose_pic_add)
                assert pic_loc, "fail to plot current pose"
                allure.attach.file(pose_pic_add, "plot pose for two bags")

            with allure.step("7.trajectory eur distance ，first 40 points"):
                trajectory_pic_add = bag_path + "trajectory.png"
                plot_eu(gt_tra_path, t_tra_path, trajectory_pic_add)
                logger.info(trajectory_pic_add)
                allure.attach.file(trajectory_pic_add, "trajectory_eu")
                allure.attach.file(trajectory_pic_add, "trajectory_eu_01")

            with allure.step("8.trajectory yaw angle，first 40 points"):
                gt_tra_df = pd.read_csv(gt_tra_path)
                t_tra_df = pd.read_csv(t_tra_path)
                tr_yaw_add = bag_path + "delta_yaw.png"
                tr_yaw_add1 = bag_path + "delta_yaw1.png"
                count = gt_tra_df.shape[0] - t_tra_df.shape[0]
                gt_tra_df.drop(gt_tra_df.tail(count).index, inplace=True)
                trajectory_yaw_plot(gt_tra_df, t_tra_df, tr_yaw_add, tr_yaw_add1)
                allure.attach.file(tr_yaw_add, "trajectory_delta_yaw")
                allure.attach.file(tr_yaw_add1, "trajectory_delta_yaw_01")

            with allure.step("9. /planning/mission_planning/route   info comparison"):
                gt_route = bag_path + "gt_01_route.csv"
                t_route = bag_path + "test_01_route.csv"
                allure.attach.file(gt_route, "gt route info")
                allure.attach.file(t_route, "test route info")

                assert route_same(gt_route, t_route), "planning_route msg is not the same "

    # 把生成的函数返回
    return test_planning


for case_arg in CASE_LIST:
    logger.info(case_arg)
    print(case_arg)
    globals()[case_arg['CaseName']] = make_test_case(case_arg['Story'], [case_arg['test_case']],
                                                     case_arg['Priority'], case_arg['Title'],
                                                     )

#  局限于只有一条路经， 无障碍物
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
    # generate = 'allure generate /home/minwei/autotest/allure_rep
    # orts/result/ -o /home/minwei/autotest/allure_reports/report/ --clean'
    # print('generate allure_results: {}'.format(generate))
    # os.system(generate)
