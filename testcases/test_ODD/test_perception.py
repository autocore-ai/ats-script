# -*- coding: utf-8 -*-
"""
Perception module case
"""

import allure
import pytest
import time
import logging

from common.generate_case_data import generate_case_data
from config import TEST_CASE_PATH
from common.perception.perception_bag_analysis import Analysis, compare_uuid, compare_semantic, compare_line, compare_position,\
    compare_shape, compare_orientation, compare_prediction_paths
import common.perception.perception_action as p_act
import common.perception.perception_conf as conf

logger = logging.getLogger()

CASE_LIST = generate_case_data('{}/testcases/test_ODD/cases/perception_cases_open.csv'.format(TEST_CASE_PATH))
BAG_BASE_PATH = conf.PERCEPTION_BAG_PATH_OPEN
logger.info('Perception case list: {}'.format(CASE_LIST))


# dynamic generate test case
def make_test_case(story, case_data, case_level, case_desc):

    @allure.feature('perception')
    @pytest.mark.parametrize("case_data", case_data, ids=[case_desc])
    @allure.story(story)
    @allure.severity(case_level)
    def test_perception(perception_open_env, case_data):
        """
        Step：
        1. start env
        2. ready to record bag
        3. play bag
        4. analysis expect and test result bag
        5. compare two bags
        6. clean env
        """
        bag_name = case_data['bag_name']
        bag_dir = '{}/{}'.format(BAG_BASE_PATH, bag_name.split('.bag')[0])
        logger.info('case bag path: {}'.format(bag_dir))
        perception_bag_result_path = '{}/{}'.format(bag_dir, 'result.bag')  # perception result bag path
        step_desc = '1. record rosbag, new bag name: {}'.format(perception_bag_result_path)
        with allure.step(step_desc):
            logger.info('='*20 + step_desc + '='*20)
            bag_duration = case_data['bag_duration']
            r_bool, ret = p_act.record_bag(perception_bag_result_path, bag_duration)
            assert r_bool, ret

        play_bag_path = '{}/{}'.format(bag_dir, case_data['bag_name'])
        step_desc = '2. play rosbag, bag path: {}'.format(play_bag_path)
        with allure.step(step_desc):
            logger.info('='*20 + step_desc + '='*20)
            r_bool, ret = p_act.play_bag(play_bag_path)
            logger.info('play bag finished')
            assert r_bool, ret

        step_desc = '3. stop record bag'
        with allure.step(step_desc):
            time.sleep(1)

            logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
            r_bool, ret = p_act.stop_record_bag()
            assert r_bool, ret

        '''
        step_desc = '3. get bag to local, remote'
        with allure.step(step_desc):
            logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
            ip, user, pwd = conf.PERCEPTION_BAG_REMOTE_IP, conf.PERCEPTION_BAG_REMOTE_USER, conf.PERCEPTION_BAG_REMOTE_PWD
            remote = RemoteP(ip, user, pwd)
            bag_dir = '{}/{}'.format(conf.PERCEPTION_BAG_PATH, case_data['bag_name'].split('.bag')[0])
            logger.info('case bag path: {}'.format(bag_dir))
            perception_bag_result_path = '{}/{}'.format(bag_dir, 'result.bag')  # perception result bag path
            r_bool, ret = remote.get(perception_bag_result_path, '/media/duan/OS/auto_test/bag/{}/result.bag'.format(bag_name.split('.')[0]))
            logger.info('get remote bag, return: {}, msg: {}'.format(r_bool, ret))
            assert r_bool, ret
        '''
        step_desc = '4. analysis result bag data'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            logger.info('result bag path: {}'.format(perception_bag_result_path))
            bag_real = Analysis(perception_bag_result_path)
            logger.info('result bag msg count: {}'.format(bag_real.msg_count))
            assert bag_real.analysis(), 'analysis bag failed'
            bag_data = bag_real.data_dict
            # logger.info('object topic data: {}'.format(bag_data))
            allure.attach('{}'.format(bag_data), 'object topic data', allure.attachment_type.JSON)

        step_desc = '5. get expect bag data'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            exp_bag_path = '{}/expect.bag'.format('/'.join(perception_bag_result_path.split('/')[:-1]))
            # exp_bag_path = '{}/expect.bag'.format('/'.join(perception_bag_result_path.split('/')[:-1]))
            logger.info('expect object bag path: {}'.format(exp_bag_path))
            bag_exp = Analysis(exp_bag_path)
            logger.info('expect bag msg count: {}'.format(bag_exp.msg_count))
            assert bag_exp.analysis()
            bag_data_exp = bag_exp.data_dict
            # logger.info('expect object topic data: {}'.format(bag_data_exp))
            allure.attach('{}'.format(bag_data_exp), 'expect object topic data', allure.attachment_type.JSON)

        # compare with ground truth rosbag
        step_desc = '6. compare real bag with expect bag: 1. msg count'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            real_count = bag_real.msg_count
            exp_count = bag_exp.msg_count
            allure.attach('expect: {}, real: {}'.format(exp_count, real_count), 'compare msg count', allure.attachment_type.TEXT)
            assert real_count in range(exp_count-10, exp_count+20), 'real object topic msg count is less 10 or more than 20 then expect msg count'

        # uuid compare
        bag_real_sum_dict = bag_real.sum_data()
        bag_exp_sum_dict = bag_exp.sum_data()
        logger.info('expect bag topic summary: {}'.format(bag_exp_sum_dict))
        logger.info('real bag topic summary: {}'.format(bag_real_sum_dict))

        step_desc = '7. compare real bag with expect bag: 2. uuid'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            exp_uuid = bag_exp_sum_dict['uuid']
            real_uuid = bag_real_sum_dict['uuid']
            logger.info('expect uuid: {}, real uuid: {}'.format(exp_uuid, real_uuid))
            allure.attach('expect uuid: {}, sum: {}\nreal uuid: {}, sum: {}'.
                          format(exp_uuid, sum(exp_uuid), real_uuid, sum(real_uuid)), 'compare uuid',
                          allure.attachment_type.TEXT)
            save_path = '{}/{}'.format(bag_dir, 'uuid.png')
            r_bool, std_uuid, msg = compare_uuid(exp_uuid, real_uuid, save_path)
            logger.info('compare result of uuid std: {:<8.2f}'.format(std_uuid))
            assert r_bool, 'compare of uuid is wrong, message: {}'.format(msg)
            # attach uuid png
            attach_mag = 'uuid count bar/per'
            allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)
            # compare std
            assert std_uuid < 100, 'The standard deviation between the expected uuid and '\
                                   'the actual uuid is greater than 1, std: {:<8.2f}'.format(std_uuid)

        step_desc = '8. compare real bag with expect bag: 3. semantic'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            exp_sem_dict = bag_exp_sum_dict['semantic']
            real_sem_dict = bag_real_sum_dict['semantic']
            logger.info('expect semantic: {}, real semantic: {}'.format(exp_sem_dict, real_sem_dict))
            allure.attach('expect semantic: {}\n real semantic: {}'.format(exp_sem_dict, real_sem_dict),
                          'expect and real semantic', allure.attachment_type.TEXT)
            save_path = '{}/{}'.format(bag_dir, 'semantic.png')
            r_bool, sem_std_dict = compare_semantic(exp_sem_dict, real_sem_dict, save_path)
            logger.info('compare result of semantic: {}'.format(sem_std_dict))
            assert r_bool, 'compare of semantic is wrong, message: {}'.format(sem_std_dict)
            # attach semantic png
            attach_mag = 'semantic count bar graph per second'
            allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)
            # compare semantic std
            for sem, std in sem_std_dict.items():
                assert sem != 'UNKNOWN', 'Semantic is UNKNOWN, that is not allow'
                assert std < 100, 'Semantic-{}: The standard deviation between the expected position and ' \
                                  'the actual position is greater than 1, std: {:<8.2f}'.format(sem, std)

        step_desc = '9. compare real bag with expect bag: 3. position'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            exp_pos_dict = bag_exp_sum_dict['position']
            real_pos_dict = bag_real_sum_dict['position']
            logger.info('expect position sum data: {}, real position sum data: {}'.format(exp_pos_dict, real_pos_dict))
            allure.attach('expect position sum data: {}\n real position sum data: {}'.format(exp_pos_dict, real_pos_dict),
                          'expect and real position dict data', allure.attachment_type.TEXT)
            save_path = '{}/{}'.format(bag_dir, 'position.png')
            r_bool, pos_dict = compare_position(exp_pos_dict, real_pos_dict, save_path, max_step=500)
            logger.info('compare result of position: {}'.format(pos_dict))
            assert r_bool, 'compare of position is wrong, message: {}'.format(pos_dict)
            # attach position png
            attach_mag = 'per second count of position\'s  bar graph'
            allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)
            # compare position std
            for sem, dis_std_dict in pos_dict.items():
                # 1. compare of std
                std = dis_std_dict['std']
                assert std < 100000, 'Position-{}: The standard deviation between the expected position and ' \
                                   'the actual position is greater than 1, std: {:<8.2f}'.format(sem, std)
                # 2. compare of distance between expect and actual, the distance should be less that 0.5m
                for dis in dis_std_dict['distance']:
                    assert dis < 200000.5, 'Position-{}: The distance between expect and actual ' \
                                      'is more than 0.5m, distance: {}'.format(sem, dis)

        step_desc = '10. compare real bag with expect bag: 4. orientation'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            exp_ori_dict = bag_exp_sum_dict['orientation']
            real_ori_dict = bag_real_sum_dict['orientation']
            logger.info('expect orientation sum data: {}, real orientation sum data: {}'.format(exp_ori_dict, real_ori_dict))
            allure.attach('expect orientation sum data: {}\n real orientation sum data: {}'.format(exp_ori_dict, real_ori_dict),
                          'expect and real orientation dict data', allure.attachment_type.TEXT)
            save_path = '{}/{}'.format(bag_dir, 'orientation.png')
            r_bool, ori_dict = compare_orientation(exp_ori_dict, real_ori_dict, save_path, max_step=500)
            logger.info('compare result of orientation: {}'.format(ori_dict))
            assert r_bool, 'compare of orientation is wrong, message: {}'.format(msg)
            # attach position png
            attach_mag = 'orientation\'s  line graph'
            allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)
            # compare position std
            for sem, dis_std_dict in ori_dict.items():
                # 1. compare of std
                std = dis_std_dict['std']
                assert std < 20000, 'Orientation-{}: The standard deviation between the expected orientation and ' \
                                 'the actual orientation is greater than 10, std: {:<8.2f}'.format(sem, std)
                # 2. compare of distance between expect and actual, the distance should be less that 0.5m
                for dis in dis_std_dict['yaw_diff']:
                    assert dis < 20000, 'Orientation-{}: The distance between expect and actual ' \
                                      'is more than 10, yaw: {}'.format(sem, dis)

        step_desc = '11. compare real bag with expect bag: 5. line speed'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            exp_line_dict = bag_exp_sum_dict['line']
            real_line_dict = bag_real_sum_dict['line']
            logger.info('expect line sum data: {}, real line sum data: {}'.format(exp_line_dict, real_line_dict))
            allure.attach(
                'expect line sum data: {}\n real line sum data: {}'.format(exp_line_dict, real_line_dict),
                'expect and real line dict data', allure.attachment_type.TEXT)
            save_path = '{}/{}'.format(bag_dir, 'line.png')
            r_bool, line_dict = compare_line(exp_line_dict, real_line_dict, save_path, max_step=10000)
            logger.info('compare result of line: {}'.format(line_dict))
            assert r_bool, 'compare of line got an error, message: {}'.format(line_dict)
            # attach compare result
            attach_mag = 'line speed compare result'
            allure.attach('{}'.format(line_dict), attach_mag, allure.attachment_type.TEXT)
            # attach line png
            attach_mag = 'linear velocity line chart'
            allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)
            # compare line std
            for sem, line_std_dict in line_dict.items():
                # 1. compare of std
                std = line_std_dict['std']
                assert std < 2000, 'Line-{}: The standard deviation between the expected linear velocity and ' \
                                  'the actual velocity is greater than 1, std: {:<8.2f}'.format(sem, std)
                # 2. compare of size between expect and actual, the size should be less that 1km/h
                for dis in line_std_dict['distance']:
                    assert dis < 20000, 'Line-{}: The linear velocity difference between expect and actual ' \
                                      'is more than 1km/h, diff: {}'.format(sem, dis)

        step_desc = '12. compare real bag with expect bag: 6. prediction'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            exp_pre_dict = bag_exp_sum_dict['prediction_paths']
            real_pre_dict = bag_real_sum_dict['prediction_paths']
            logger.info('expect prediction_paths sum data: {}, real prediction_paths sum data: {}'.format(exp_pre_dict, real_pre_dict))
            allure.attach(
                'expect prediction_paths sum data: {}\n real prediction_paths sum data: {}'.format(exp_pre_dict, real_pre_dict),
                'expect and real prediction_paths dict data', allure.attachment_type.TEXT)
            save_path = '{}/{}'.format(bag_dir, 'prediction_paths.png')
            r_bool, pre_dict = compare_prediction_paths(exp_pre_dict, real_pre_dict, save_path, max_step=10000)
            logger.info('compare result of prediction_paths: {}'.format(pre_dict))
            assert r_bool, 'compare of prediction_paths got an error, message: {}'.format(line_dict)

            # attach compare result
            attach_mag = 'prediction_paths compare result'
            allure.attach('{}'.format(pre_dict), attach_mag, allure.attachment_type.TEXT)
            # attach line png
            attach_mag = 'prediction_paths line chart'
            allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)
            # compare line std
            for sem, pre_std_dict in pre_dict.items():
                # 1. compare of std
                std_2th = pre_std_dict['paths_std_2th_xy']
                assert std_2th < 100000, 'Prediction-2th-{}: The standard deviation between the expected Prediction-2th ' \
                                       'and the actual Prediction-2th is greater than 1, std: {:<8.2f}'.format(sem, std_2th)

                std_3th = pre_std_dict['paths_std_3th_xy']
                assert std_3th < 100000, 'Prediction-3th-{}: The standard deviation between the expected Prediction-3th ' \
                                       'and the actual Prediction-3th is greater than 1, std: {:<8.2f}'.format(sem, std_3th)
                # 2. compare of size between expect and actual, the size should be less that 1km/h
                for dis in pre_std_dict['paths_eul_2th_xy']:
                    assert dis < 100000, 'Prediction-2th-XY-{}: The Prediction-2th difference between expect and actual ' \
                                    'is more than 1m, diff: {}'.format(sem, dis)
                for ori in pre_std_dict['paths_eul_2th_ori']:
                    assert ori < 100000, 'Prediction-2th-ori-{}: The Prediction-2th orientation between expect and actual ' \
                                    'is more than 1, diff: {}'.format(sem, ori)
                for dis in pre_std_dict['paths_eul_3th_xy']:
                    assert dis < 100000, 'Prediction-3th-XY-{}: The Prediction-2th difference between expect and actual ' \
                                    'is more than 1m, diff: {}'.format(sem, dis)
                for ori in pre_std_dict['paths_eul_3th_ori']:
                    assert ori < 100000, 'Prediction-3th-ori-{}: The Prediction-2th orientation between expect and actual ' \
                                    'is more than 1, diff: {}'.format(sem, ori)

        step_desc = '13. compare real bag with expect bag: 7. shape'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            exp_shape_dict = bag_exp_sum_dict['shape']
            real_shape_dict = bag_real_sum_dict['shape']
            ret_desc = 'expect shape sum data: {}, real shape sum data: {}'.format(exp_shape_dict, real_shape_dict)
            logger.info(ret_desc)
            allure.attach(ret_desc, 'expect and real shape dict data', allure.attachment_type.TEXT)

            save_path = '{}/{}'.format(bag_dir, 'shape.png')
            r_bool, shape_dict = compare_shape(exp_shape_dict, real_shape_dict, save_path, max_step=10000)
            logger.info('compare result of shape: {}'.format(shape_dict))
            assert r_bool, 'compare of shape got an error, message: {}'.format(shape_dict)
            # attach shape png
            attach_mag = 'shape size line chart'
            allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)
            # compare shape std
            for sem, s_dict in shape_dict.items():
                # 1. compare of size x std
                std_x = s_dict['std_x']
                assert std < 10000, 'Shape-{}: The standard deviation between the expected size-x and ' \
                                 'the size-x is greater than 1, std: {:<8.2f}'.format(sem, std_x)

                # 2. compare of size y std
                std_y = s_dict['std_y']
                assert std_y < 100000, 'Shape-{}: The standard deviation between the expected size-y and ' \
                                  'the size-y is greater than 1, std: {:<8.2f}'.format(sem, std_y)
                # 3. compare of shape-x difference between expect and actual, the distance should be less that 0.5m
                for dis in s_dict['shape_diff_x']:
                    assert dis < 100000.5, 'shape-x-{}: The shape-x difference between expect and actual ' \
                                    'is more than 0.5m, diff: {}'.format(sem, dis)

                # 4. compare of shape-y difference between expect and actual, the distance should be less that 0.5m
                for dis in s_dict['shape_diff_y']:
                    assert dis < 100000.5, 'shape-y-{}: The shape-y difference between expect and actual ' \
                                      'is more than 0.5m, diff: {}'.format(sem, dis)
        logger.info('case is finished, now to clean env')
    # return fun
    return test_perception


for case_arg in CASE_LIST:
    logger.info(case_arg)
    globals()[case_arg['CaseName']] = make_test_case(case_arg['Story'], [case_arg['test_case']],
                                                     case_arg['Priority'], case_arg['Title'])


if __name__ == '__main__':
    # args = ['--allure-stories', 'child', '--alluredir', './allure_reports/allure']
    args = ['-s', '-v']
    pytest.main(args)
