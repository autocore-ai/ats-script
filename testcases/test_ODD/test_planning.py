# -*- coding: utf-8 -*-
import allure
import pytest
import multiprocessing
import gc
from common.utils.process import *
from common.generate_case_data import generate_case_data
from common.ODD.planning.planning_action import *
from common.ODD.planning.planning_bag_analysis import *
import common.ODD.config as odd_conf
from common.ODD.aw4_action import *


logger = logging.getLogger()
case_dir = odd_conf.EXEC_CASE_SCENE[odd_conf.EXEC_CASE_TYPE]['case_dir']
CASE_LIST = generate_case_data('{case_path}/{case_dir}/planning_cases.csv'.format(case_path=odd_conf.ODD_CSV_CASES,
                                                                                  case_dir=case_dir))
bag_dir = odd_conf.EXEC_CASE_SCENE[odd_conf.EXEC_CASE_TYPE]['bag_dir']
BAG_BASE_PATH = '{bag_path}/{bag_dir}/planning/'.format(bag_path=odd_conf.BAG_PATH, bag_dir=bag_dir)


def make_test_case(story, case_data, case_level, case_desc):
    @allure.feature('planning')
    @pytest.mark.parametrize("case_data", case_data, ids=[case_desc])
    @allure.story(story)
    @allure.severity(case_level)
    def test_planning(env_opt, case_data):
        """
        1. Planning, local autoware setup.bash , roslaunch map
        It is expected that in this step, the interface will be written into docker

        2. Local docker (this will change in the future)

        3. Check whether the starting and ending points exist, do not exist or are abnormal,
        report an error and exit

        4. Engage / disengage, speed limit interface settings,
        whether the car speed changes, if not, report an error exit

        5. Start recording / planning / scenario of bag_ Planning / trajectory /,
        vehicle / status / twist, current pose given by the interface

        6. Detect the car arriving at the destination (traced position) and finish recording bag

        7. Check whether the bag message, size and message are abnormal
        """
        # name = case_data['CaseName']
        gt_name = case_data['gt_name']
        testcase_bag_path = BAG_BASE_PATH + gt_name + "/"  # /home/autotest/Workspace/autotest/bags/aw4/planning/gt_01/
        test_name = re.sub("gt", "test", gt_name)  # test_01
        test_bag_name = test_name + ".bag"  # test_01.bag
        gt_bag_name = gt_name + ".bag"  # gt_01.bag
        duration_secs = int(case_data['duration'])
        logger.info("planning bag path : {}".format(BAG_BASE_PATH))
        logger.info("planning bag record time: {}".format(str(duration_secs)))
        #
        # step_init = "check bags in bags path"
        # with allure.step(step_init):
        #     gt_dir_bool, gt_dir_msg = check_dir(testcase_bag_path)
        #     assert gt_dir_bool, gt_dir_msg
        #
        # step_info = "check ground truth has csv file or not"
        # with allure.step(step_info):
        #     gt_csv_file_name = ['{}_current_pose.csv\n'.format(gt_name),
        #                         '{}_route.csv\n'.format(gt_name),
        #                         '{}_trajectory.csv\n'.format(gt_name),
        #                         '{}_twist.csv\n'.format(gt_name),
        #                         '{}_velocity.csv\n'.format(gt_name)]
        #     shown = os.popen("cd {}; ls".format(testcase_bag_path))
        #     path_info = list(shown.readlines())
        #     exist_msg = [False for file_name in gt_csv_file_name if file_name not in path_info]
        #     if exist_msg:
        #         for topic in TOPICS.split(" "):
        #             logger.info("Downloading topic : {}".format(topic))
        #             hkey = topic.split("/")
        #             csv_bool, csv_msg = topic_csv(testcase_bag_path + gt_bag_name, topic, testcase_bag_path,
        #                                           gt_name + "_" + hkey[-1])
        #             # testcase_bag_path+gt_bag_name, topic, testcase_bag_path, gt_name + "_" + hkey[-1]
        #             assert csv_bool, csv_msg
        #             #
        #             # save_csv_file(BAG_BASE_PATH, gt_name)
        #             for i in range(3):
        #                 logger.info("Waiting.. {}s".format(i + 1))
        #                 time.sleep(1)
        #             #
        #             # for topic_one in TOPICS.split(" "):
        #             #     hkey = topic_one.split("/")
        #             #     csv_bool, csv_msg = topic_csv(BAG_BASE_PATH + gt_name + ".bag", topic_one,
        #             #                                   gt_name + "_" + hkey[-1], testcase_bag_path)
        #             #     assert csv_bool, csv_msg
        #             #     time.sleep(2)
        #     else:
        #         logger.info("csv files has already in bag file path: {}".format(gt_csv_file_name))

        step_3 = "start_record bag"
        with allure.step(step_3):
            # start_position_sample = [-815.500610352, -249.504760742, 0]
            # start_orientation_sample = [0, 0, -0.994364378898, 0.10601642316]
            # end_position_sample = [-1130.37866211, -401.696289062, 0]
            # end_orientation_sample = [0, 0, -0.771075397889, 0.636743850202]
            # bag_name_record = start_record_bag(duration_secs, testcase_bag_path + test_bag_name)

            bag_name_record = start_record_bag(duration_secs, testcase_bag_path + test_bag_name)
            logger.info("recording bag address {}".format(bag_name_record))
            # assert check_bag(bag_path+name+".bag"), "bag has not recorded successfully"

        step_4 = "add start end point， and engage"
        with allure.step(step_4):
            logger.info(step_4)
            time.sleep(2)
            dict_start = extrat_start_end_point(case_data, "start_point")
            dict_end = extrat_start_end_point(case_data, "end_point")
            start_point_info = list(dict_start.values())
            logger.info("start_point is {}".format(start_point_info))
            end_point_info = list(dict_end.values())
            logger.info("end_point is {}".format(end_point_info))
            start_position_sample = start_point_info[0:3]
            start_orientation_sample = start_point_info[3:]
            end_position_sample = end_point_info[0:3]
            end_orientation_sample = end_point_info[3:]
            # add_start_end_point(start_position_sample, start_orientation_sample,
            #                                      end_position_sample, end_orientation_sample)
            proc = multiprocessing.Process(target=add_start_end_point,
                                           args=(start_position_sample, start_orientation_sample,
                                                 end_position_sample, end_orientation_sample))
            proc.start()
            proc.join()
            proc.terminate()
            time.sleep(2)
            logger.info("auto engage")

        step_6 = "6. end recording manually"
        with allure.step(step_6):
            logger.info(step_6)
            logger.info('record end, ready to kill -2')
            time.sleep(3)
            for i in range(int(case_data['duration']) + 6):
                # for i in range(10):
                time.sleep(1)
                logger.info("waiting planning bag record finished {}s".format(i))
            stop_cmd = 'kill {} "ps -ef|grep "{}"|awk \'{{print $2}}\'"'.format("-2", 'record')

            # stop_cmd = 'ps -ef |grep "record" |awk '\''{print $2}'\'' '

            logger.info("waiting finished , check the bag duration ")
            cc = MyContainer("runtime-ros2")
            cc.exec_run(stop_cmd)
            # logger.info(r_bool)
            # logger.info(msg)
            logger.info("end recording ")
            time.sleep(10)


        # step_add = "check bag sec is approximately  close to gt_bag"
        # with allure.step(step_add):
        #     logger.info(testcase_bag_path + test_bag_name)
        #     logger.info(testcase_bag_path + gt_bag_name)
        #     sec_bool, sec_msg = compare_bag_sec(testcase_bag_path + test_bag_name, testcase_bag_path + gt_bag_name)
        #     assert sec_bool, sec_msg


        step_db3 = "return db3 to df"
        with allure.step(step_db3):
            bag = Ros2bag("/home/autotest/Workspace/autotest/bags/aw4/planning/gt_01/gteg_01")
            gt_df_dict = {}
            for topic in TOPICS_LIST:
                cc = bag.dataframe(include=topic)
                gt_df_dict[topic] = cc



            print(gt_df_dict)

        test_dict={}
        step_following = "get gt bag dataframe"
        with allure.step(step_following):
            bag = Ros2bag("/home/autotest/Workspace/autotest/bags/aw4/planning/gt_01/test_01")
            df_dict = {}
            for topic in TOPICS_LIST:
                cc = bag.dataframe(include=topic)
                test_dict[topic] = cc



            print(test_dict)

        # os.system("docker stop runtime-ros2")



        # test_csv_name = re.sub("gt", "test", gt_name)
        # step_5 = "collect data"
        # with allure.step(step_5):
        #     for topic in TOPICS.split(" "):
        #         hkey = topic.split("/")
        #         t_csv_bool, t_csv_msg = topic_csv(testcase_bag_path + test_bag_name, topic, testcase_bag_path,
        #                                           test_csv_name + "_" + hkey[-1])
        #         assert t_csv_bool, t_csv_msg
        #         time.sleep(2)
        #     for i in range(3):
        #         logger.info("Waiting bag record.. {}s".format(i + 1))
        #         time.sleep(1)
        # # test_csv_name = gt_name.replace("gt","test")
        # gt_pose_path = testcase_bag_path + "{}_current_pose.csv".format(gt_name)
        # t_v_path = testcase_bag_path + "{}_twist.csv".format(test_csv_name)
        # logger.info("BAG VELOCITY bag path : {}".format(t_v_path))
        # gt_v_path = testcase_bag_path + "{}_twist.csv".format(gt_name)
        #
        # t_pose_path = testcase_bag_path + "{}_current_pose.csv".format(test_csv_name)
        # gt_pose_file = testcase_bag_path + "{}_current_pose.csv".format(gt_name)
        #
        # gt_tra_path = testcase_bag_path + "{}_trajectory.csv".format(gt_name)
        # t_tra_path = testcase_bag_path + "{}_trajectory.csv".format(test_csv_name)
        # logger.info("trajectory bag path {}".format(t_tra_path))            # add_start_end_point(start_position_sample, start_orientation_sample,
        #     #                     end_position_sample, end_orientation_sample)

        with allure.step("1. /current_twist is always zero  -> not pass"):
            # a_df = pd.read_csv(t_v_path)
            a_df = test_dict["/vehicle/status/twist"]
            # allure.attach.file(gt_v_path, "gt velocity ")
            # allure.attach.file(t_v_path, "test velocity")
            assert velocity_not_zero(a_df), "current twist shows to zero, record unsuccessfully"

        with allure.step("2. current_pose value has not changed -> not pass"):
            # b_df = pd.read_csv(t_pose_path)
            test_pose_df =test_dict["/current_pose"]
            gt_current_pose_df = gt_df_dict["/current_pose"]
            assert current_pose_change(test_pose_df ), "current pose has not changed , record seccessfully "

        with allure.step("Data analysis"):
            with allure.step("3.current_pose: gt/test comparison： 1.eur distance larger than one range， not pass "):
                # df1, df2 = csv_to_df(gt_pose_file, t_pose_path)
                # test_current_pose = test_dict["/current_pose"]
                df1_shape_count= test_pose_df.shape[0]
                df2_shape_count= gt_current_pose_df.shape[0]
                logger.info(df1_shape_count)
                logger.info(df2_shape_count)
                if df1_shape_count> df2_shape_count:
                    count = df1_shape_count - df2_shape_count
                    test_pose_df.drop(test_pose_df.tail(count).index, inplace=True)
                if df1_shape_count < df2_shape_count:
                    count = df2_shape_count - df1_shape_count
                    gt_current_pose_df.drop(gt_current_pose_df.tail(count).index, inplace=True)
                else:
                    logger.info("count shape is same")
                logger.info("cut the extra columns , "
                            "now the  columns are {} , {}".format(test_pose_df.shape[0], gt_current_pose_df.shape[0]))

            yaw_range = 100
            with allure.step("4.current pose: comparison： 2. yaw angle is larger ont certain range， not pass "):
                result, c_yaw_list = current_pose_analysis_yaw(yaw_range, test_pose_df, gt_current_pose_df)
                assert result, "current pose yaw caculation is out of range: {}".format(yaw_range)
                with open(testcase_bag_path+ '1.txt', 'w') as file_pose:
                    for i in range(len(c_yaw_list)):
                        file_pose.write(str(c_yaw_list[i]))
                logger.info("current pose list: {}".format(c_yaw_list))

                fig, ax = plt.subplots(1, 1, figsize=(10, 6))
                ax.plot(c_yaw_list)
                plt.savefig(testcase_bag_path + "current_pose.png")
                logger.info("current pose pic address: {}".format(testcase_bag_path+ "current_pose.png"))
                allure.attach.file(testcase_bag_path + "1.txt", "current_pose txt file ")
                allure.attach.file(testcase_bag_path + "current_pose.png", "current_pose pic")

            with allure.step("5. current twist comparison： ×3.6 plot"):
                # dfc, dfd = csv_to_df(gt_v_path, t_v_path)
                dfc, dfd =gt_df_dict["/vehicle/status/twist"],test_dict["/vehicle/status/twist"]
                add = testcase_bag_path + "twist.png"
                plot_twist(dfc, dfd, add)
                allure.attach.file(add, "current_twist")

            with allure.step("6. plot pose"):
                df1, df2 = gt_df_dict["/current_pose"], test_pose_df
                pose_pic_add = testcase_bag_path + "pose.png"
                pic_loc = plot_pose(df1, df2, pose_pic_add)
                allure.attach.file(pose_pic_add, "plot pose for two bags")
                assert pic_loc, "fail to plot current pose"

            with allure.step("7.trajectory eur distance ，first 40 points"):
                trajectory_pic_add = testcase_bag_path + "trajectory.png"
                dfa,dfb= gt_df_dict["/planning/scenario_planning/trajectory"], test_dict["/planning/scenario_planning/trajectory"]
                logger.info('------------------------{}'.format(dfa))
                logger.info("---------------------{}".format(dfb))
                logger.info(dfa['planning.scenario_planning.trajectory.points[1].pose.position.y'])
                plot_eu(dfa, dfb, trajectory_pic_add)
                logger.info(trajectory_pic_add)
                allure.attach.file(trajectory_pic_add, "trajectory_eu")
                allure.attach.file(trajectory_pic_add, "trajectory_eu_01")

            with allure.step("8.trajectory yaw angle，first 40 points"):
                gt_tra_df = dfa
                t_tra_df = dfb
                tr_yaw_add = testcase_bag_path + "delta_yaw.png"
                tr_yaw_add1 = testcase_bag_path + "delta_yaw1.png"
                count = gt_tra_df.shape[0] - t_tra_df.shape[0]
                gt_tra_df.drop(gt_tra_df.tail(count).index, inplace=True)
                trajectory_yaw_plot(gt_tra_df, t_tra_df, tr_yaw_add, tr_yaw_add1)
                allure.attach.file(tr_yaw_add, "trajectory_delta_yaw")
                allure.attach.file(tr_yaw_add1, "trajectory_delta_yaw_01")
        #
        #     with allure.step("9. /planning/mission_planning/route   info comparison"):
        #         gt_route = testcase_bag_path + "{}_route.csv".format(gt_name)
        #         t_route = testcase_bag_path + "{}_route.csv".format(test_csv_name)
        #         allure.attach.file(gt_route, "gt route info")
        #         allure.attach.file(t_route, "test route info")
        #
        #         assert route_same(gt_route, t_route), "planning_route msg is not the same "

        gc.collect()

    return test_planning


for case_arg in CASE_LIST:
    globals()[case_arg['CaseName']] = make_test_case(case_arg['Story'], [case_arg['test_case']],
                                                     case_arg['Priority'], case_arg['Desc'], )

if __name__ == '__main__':
    pass
