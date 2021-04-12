# -*- coding: utf-8 -*-
"""
Perception module case
"""

import time
import logging
import allure
import pytest
import gc

from common.generate_case_data import generate_case_data
from common.ODD.perception.compare_topics import compare_uuid, compare_semantic, compare_line, compare_position, \
    compare_shape, compare_orientation, compare_prediction_paths
import common.ODD.perception.perception_action as p_act
import common.ODD.perception.perception_conf as conf
import common.ODD.config as odd_conf
from common.utils.perception_bag_analysis import Analysis
logger = logging.getLogger()

case_dir = odd_conf.EXEC_CASE_SCENE[odd_conf.EXEC_CASE_TYPE]['case_dir']
CASE_LIST = generate_case_data('{case_path}/{case_dir}/perception_cases.csv'.format(case_path=odd_conf.ODD_CSV_CASES,
                                                                                    case_dir=case_dir))
bag_dir = odd_conf.EXEC_CASE_SCENE[odd_conf.EXEC_CASE_TYPE]['bag_dir']
BAG_BASE_PATH = '{bag_path}/{bag_dir}/perception'.format(bag_path=odd_conf.BAG_PATH, bag_dir=bag_dir)


def make_test_case(story, case_data, case_level, case_desc):
    """dynamic generate test case"""
    @allure.feature('perception')
    @pytest.mark.parametrize("case_data", case_data, ids=[case_desc])
    @allure.story(story)
    @allure.severity(case_level)
    def test_perception(env_opt, case_data):
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
            time.sleep(10)

            logger.info('{eq} {step} {eq}'.format(eq='='*20, step=step_desc))
            r_bool, ret = p_act.stop_record_bag()
            assert r_bool, ret

        step_desc = '4. analysis result bag data'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            logger.info('result bag path: {}'.format(perception_bag_result_path))
            bag_real = Analysis(perception_bag_result_path)
            logger.info('result bag msg count: {}'.format(bag_real.msg_count))
            assert bag_real.analysis(), 'analysis bag failed'
            bag_data = bag_real.data_dict
            logger.debug('object topic data: {}'.format(bag_data))
            allure.attach('{}'.format(bag_data), 'object topic data', allure.attachment_type.JSON)
            del bag_data

        step_desc = '5. get expect bag data'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            exp_bag_path = '{}/expect.bag'.format('/'.join(perception_bag_result_path.split('/')[:-1]))
            logger.info('expect object bag path: {}'.format(exp_bag_path))
            bag_exp = Analysis(exp_bag_path)
            logger.info('expect bag msg count: {}'.format(bag_exp.msg_count))
            assert bag_exp.analysis()
            bag_data_exp = bag_exp.data_dict
            logger.debug('expect object topic data: {}'.format(bag_data_exp))
            allure.attach('{}'.format(bag_data_exp), 'expect object topic data', allure.attachment_type.JSON)
            del bag_data_exp

        # compare with ground truth rosbag
        step_desc = '6. compare real bag with expect bag: 1. msg count'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            real_count = bag_real.msg_count
            exp_count = bag_exp.msg_count
            logger.info('expect: {}, real: {}'.format(exp_count, real_count))
            allure.attach('expect: {}, real: {}'.format(exp_count, real_count), 'compare msg count',
                          allure.attachment_type.TEXT)
            assert real_count in range(exp_count-conf.MSG_COUNT_STEP,
                                       exp_count+conf.MSG_COUNT_STEP), 'real object topic msg count is less or ' \
                                                                       'more than {step} then expect ' \
                                                                       'msg count'.format(step=conf.MSG_COUNT_STEP)

        # uuid compare
        bag_real_sum_dict = bag_real.sum_data()
        bag_exp_sum_dict = bag_exp.sum_data()
        logger.debug('expect bag topic summary: {}'.format(bag_exp_sum_dict))
        logger.debug('real bag topic summary: {}'.format(bag_real_sum_dict))

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
            logger.info('compare result of uuid msg: {}'.format(msg))
            assert r_bool, 'compare of uuid wrong, message: {}'.format(msg)
            # attach uuid png
            attach_mag = 'uuid count bar/per'
            allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)
            # compare std
            assert std_uuid < conf.UUID_STD_MAX, 'The standard deviation between the expected uuid and ' \
                                                 'the actual uuid is greater than {std_max}, ' \
                                                 'real std: {r_std:<8.2f}'.format(std_max=conf.UUID_STD_MAX,
                                                                                  r_std=std_uuid)
            del exp_uuid
            del real_uuid

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
                assert sem != 'UNKNOWN', 'Semantic is UNKNOWN, that is not allowed'
                assert std < conf.SEM_STD_MAX, 'Semantic-{sem}: The standard deviation between the expected position ' \
                                               'and the actual position is greater than {std_max}, std: {r_std:<8.2f}'.\
                    format(sem=sem, std_max=conf.SEM_STD_MAX, r_std=std)
            del exp_sem_dict
            del real_sem_dict

        step_desc = '9. compare real bag with expect bag: 3. position'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            exp_pos_dict = bag_exp_sum_dict['position']
            real_pos_dict = bag_real_sum_dict['position']
            exp_pos_all_dict = bag_exp_sum_dict['position_all']
            real_pos_all_dict = bag_real_sum_dict['position_all']
            logger.debug('expect position sum data: {}, real position sum data: {}'.format(exp_pos_dict, real_pos_dict))
            allure.attach('expect position sum data: {}\n'
                          'real position sum data: {}'.format(exp_pos_dict, real_pos_dict),
                          'expect and real position dict data', allure.attachment_type.TEXT)
            save_path = '{}/{}'.format(bag_dir, 'position.png')
            scatter_save_path = '{}/{}'.format(bag_dir, 'position_scatter.png')
            r_bool, pos_dict = compare_position(exp_pos_dict, real_pos_dict, exp_pos_all_dict, real_pos_all_dict,
                                                save_path, scatter_save_path, max_step=conf.PST_STEP)
            logger.debug('compare result of position: {}'.format(pos_dict))
            assert r_bool, 'compare of position is wrong, message: {}'.format(pos_dict)
            # attach position png
            attach_mag = 'per second count of position\'s  bar graph'
            allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)
            # attach position scatter png
            attach_mag = 'position scatter graph'
            allure.attach.file(scatter_save_path, attach_mag, allure.attachment_type.PNG)

            # compare position std
            for sem, dis_std_dict in pos_dict.items():
                # 1. compare of std
                std = dis_std_dict['std']
                logger.info('Position-{sem}: The standard deviation between the expected '
                            'with actual position is {std}'.format(sem=sem, std=std))
                assert std < conf.PST_STD_MAX, 'Position-{sem}: The standard deviation between the expected position ' \
                                               'and the actual position is greater than {std_max}, ' \
                                               'std: {r_std:<8.2f}'.format(sem=sem, std_max=conf.PST_STD_MAX, r_std=std)
                # 2. compare of distance between expect and actual, the distance should be less that 0.5m
                for dis in dis_std_dict['distance']:
                    assert dis < conf.PST_DIS_MAX, 'Position-{sem}: The distance between expect and actual is ' \
                                                   'more than {p_max}m, ' \
                                                   'distance: {dis}'.format(sem=sem, p_max=conf.PST_DIS_MAX, dis=dis)
            del exp_pos_dict
            del real_pos_dict
            del exp_pos_all_dict
            del real_pos_all_dict

        step_desc = '10. compare real bag with expect bag: 4. orientation'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            exp_ori_dict = bag_exp_sum_dict['orientation']
            real_ori_dict = bag_real_sum_dict['orientation']
            logger.debug('expect orientation sum data: {}, '
                         'real orientation sum data: {}'.format(exp_ori_dict, real_ori_dict))
            allure.attach('expect orientation sum data: {}\n'
                          'real orientation sum data: {}'.format(exp_ori_dict, real_ori_dict),
                          'expect and real orientation dict data', allure.attachment_type.TEXT)
            save_path = '{}/{}'.format(bag_dir, 'orientation.png')
            r_bool, ori_dict = compare_orientation(exp_ori_dict, real_ori_dict, save_path, max_step=conf.ORI_STEP)
            logger.debug('compare result of orientation: {}'.format(ori_dict))
            assert r_bool, 'compare of orientation is wrong, message: {}'.format(msg)
            # attach position png
            attach_mag = 'orientation\'s  line graph'
            allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)
            # compare position std
            for sem, dis_std_dict in ori_dict.items():
                # 1. compare of std
                std = dis_std_dict['std']
                logger.info('Orientation-{sem}: The standard deviation between the expected '
                            'with actual Orientation is {std}'.format(sem=sem, std=std))
                assert std < conf.ORI_STD_MAX, 'Orientation-{sem}: The standard deviation between the expected ' \
                                               'orientation and the actual orientation is greater than {o_max}, ' \
                                               'std: {r_std:<8.2f}'.format(sem=sem, o_max=conf.ORI_STD_MAX, r_std=std)
                # 2. compare of distance between expect and actual, the distance should be less that 0.5m
                for dis in dis_std_dict['yaw_diff']:
                    assert dis < conf.ORI_DIS_MAX, 'Orientation-{sem}: The distance between expect and ' \
                                                   'actual is more than {dis_max}, ' \
                                                   'yaw: {dis}'.format(sem=sem, dis_max=conf.ORI_DIS_MAX, dis=dis)
            del exp_ori_dict
            del real_ori_dict

        step_desc = '11. compare real bag with expect bag: 5. line speed'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            exp_line_dict = bag_exp_sum_dict['line']
            real_line_dict = bag_real_sum_dict['line']
            logger.debug('expect line sum data: {}, real line sum data: {}'.format(exp_line_dict, real_line_dict))
            allure.attach(
                'expect line sum data: {}\n real line sum data: {}'.format(exp_line_dict, real_line_dict),
                'expect and real line dict data', allure.attachment_type.TEXT)
            save_path = '{}/{}'.format(bag_dir, 'line.png')
            r_bool, line_dict = compare_line(exp_line_dict, real_line_dict, save_path, max_step=conf.LINE_STEP)
            logger.debug('compare result of line: {}'.format(line_dict))
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
                logger.info('Line-{sem}: The standard deviation between the expected '
                            'with actual line speed is {std}'.format(sem=sem, std=std))
                assert std < conf.LINE_STD_MAX, 'Line-{sem}: The standard deviation between the expected ' \
                                                'linear velocity and the actual velocity is greater than {std_max}, ' \
                                                'std: {r_std:<8.2f}'.format(sem=sem,
                                                                            std_max=conf.LINE_STD_MAX,
                                                                            r_std=std)
                # 2. compare of size between expect and actual, the size should be less that 1km/h
                for dis in line_std_dict['distance']:
                    assert dis < conf.LINE_DIS_MAX, 'Line-{sem}: The linear velocity difference between expect' \
                                                    ' and actual is more than {dis_max}km/h, ' \
                                                    'diff: {r_dis}'.format(sem=sem,
                                                                           dis_max=conf.LINE_DIS_MAX,
                                                                           r_dis=dis)
            del exp_line_dict
            del real_line_dict

        step_desc = '12. compare real bag with expect bag: 6. prediction'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            exp_pre_dict = bag_exp_sum_dict['prediction_paths']
            real_pre_dict = bag_real_sum_dict['prediction_paths']
            logger.debug('expect prediction_paths sum data: {}, '
                         'real prediction_paths sum data: {}'.format(exp_pre_dict, real_pre_dict))
            allure.attach(
                'expect prediction_paths sum data: {}\n'
                'real prediction_paths sum data: {}'.format(exp_pre_dict, real_pre_dict),
                'expect and real prediction_paths dict data', allure.attachment_type.TEXT)
            save_path = '{}/{}'.format(bag_dir, 'prediction_paths.png')
            r_bool, pre_dict = compare_prediction_paths(exp_pre_dict, real_pre_dict, save_path,
                                                        max_step=conf.PRE_PATH_STEP)
            logger.debug('compare result of prediction_paths: {}'.format(pre_dict))
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
                logger.info('Prediction-2th-{sem}: The standard deviation between the expected '
                            'with actual prediction path is {std}'.format(sem=sem, std=std_2th))
                assert std_2th < conf.PRE_PATH_STD_MAX, 'Prediction-2th-{sem}: The standard deviation between ' \
                                                        'the expected Prediction-2th and the actual Prediction-2th ' \
                                                        'is greater than {std_max}, ' \
                                                        'std: {r_std:<8.2f}'.format(sem=sem,
                                                                                    std_max=conf.PRE_PATH_STD_MAX,
                                                                                    r_std=std_2th)

                std_3th = pre_std_dict['paths_std_3th_xy']
                logger.info('Prediction-3th-{sem}: The standard deviation between the expected position '
                            'with actual position is {std}'.format(sem=sem, std=std_3th))
                assert std_3th < conf.PRE_PATH_STD_MAX, 'Prediction-3th-{sem}: The standard deviation between ' \
                                                        'the expected Prediction-3th and the actual Prediction-3th ' \
                                                        'is greater than {std_max}, ' \
                                                        'std: {r_std:<8.2f}'.format(sem=sem,
                                                                                    std_max=conf.PRE_PATH_STD_MAX,
                                                                                    r_std=std_3th)
                # 2. compare of size between expect and actual, the size should be less that 1km/h
                for dis in pre_std_dict['paths_eul_2th_xy']:
                    assert dis < conf.PRE_PATH_DIS_MAX, 'Prediction-2th-XY-{sem}: The Prediction-2th difference ' \
                                                        'between expect and actual is more than {dis_max}m, ' \
                                                        'diff: {r_dis}'.format(sem=sem, dis_max=conf.PRE_PATH_DIS_MAX,
                                                                               r_dis=dis)
                for ori in pre_std_dict['paths_eul_2th_ori']:
                    assert ori < conf.PRE_PATH_ORI_DIS_MAX, 'Prediction-2th-ori-{sem}: The Prediction-2th orientation' \
                                                            ' between expect and actual is more than {ori_dis_max}, ' \
                                                            'diff: {r_ori}'.format(sem=sem,
                                                                                   ori_dis_max=conf.PRE_PATH_ORI_DIS_MAX,
                                                                                   r_ori=ori)
                for dis in pre_std_dict['paths_eul_3th_xy']:
                    assert dis < conf.PRE_PATH_DIS_MAX, 'Prediction-3th-XY-{sem}: The Prediction-2th difference ' \
                                                        'between expect and actual is more than {dis_max}m, ' \
                                                        'diff: {r_dis}'.format(sem=sem, dis_max=conf.PRE_PATH_DIS_MAX,
                                                                               r_dis=dis)
                for ori in pre_std_dict['paths_eul_3th_ori']:
                    assert ori < conf.PRE_PATH_DIS_MAX, 'Prediction-2th-ori-{sem}: The Prediction-2th orientation ' \
                                                        'between expect and actual is more than {ori_dis_max}, ' \
                                                        'diff: {r_ori}'.format(sem=sem,
                                                                               ori_dis_max=conf.PRE_PATH_ORI_DIS_MAX,
                                                                               r_ori=ori)
            del exp_pre_dict
            del real_pre_dict

        step_desc = '13. compare real bag with expect bag: 7. shape'
        with allure.step(step_desc):
            logger.info('================= {} ================='.format(step_desc))
            exp_shape_dict = bag_exp_sum_dict['shape']
            real_shape_dict = bag_real_sum_dict['shape']
            ret_desc = 'expect shape sum data: {}, real shape sum data: {}'.format(exp_shape_dict, real_shape_dict)
            logger.debug(ret_desc)
            allure.attach(ret_desc, 'expect and real shape dict data', allure.attachment_type.TEXT)

            save_path = '{}/{}'.format(bag_dir, 'shape.png')
            r_bool, shape_dict = compare_shape(exp_shape_dict, real_shape_dict, save_path, max_step=conf.SHAPE_STEP)
            logger.debug('compare result of shape: {}'.format(shape_dict))
            assert r_bool, 'compare of shape got an error, message: {}'.format(shape_dict)
            # attach shape png
            attach_mag = 'shape size line chart'
            allure.attach.file(save_path, attach_mag, allure.attachment_type.PNG)
            # compare shape std
            for sem, s_dict in shape_dict.items():
                # 1. compare of size x std
                std_x = s_dict['std_x']
                logger.info('Shape-X-{sem}: The standard deviation between the expected '
                            'with actual shape is {std}'.format(sem=sem, std=std_x))
                assert std < conf.SHAPE_STD_X_MAX, 'Shape-{sem}: The standard deviation between the expected ' \
                                                   'size-x and the size-x is greater than {std_max}, ' \
                                                   'std: {r_std:<8.2f}'.format(sem=sem,
                                                                               std_max=conf.SHAPE_STD_X_MAX,
                                                                               r_std=std_x)

                # 2. compare of size y std
                std_y = s_dict['std_y']
                logger.info('Shape-Y-{sem}: The standard deviation between the expected '
                            'with actual shape is {std}'.format(sem=sem, std=std_y))
                assert std_y < conf.SHAPE_STD_Y_MAX, 'Shape-{sem}: The standard deviation between the expected ' \
                                                     'size-y and the size-y is greater than {std_max}, ' \
                                                     'std: {r_std:<8.2f}'.format(sem=sem,
                                                                                 std_max=conf.SHAPE_STD_Y_MAX,
                                                                                 r_std=std_y)
                # 3. compare of shape-x difference between expect and actual, the distance should be less that 0.5m
                for dis in s_dict['shape_diff_x']:
                    assert dis < conf.SHAPE_DIS_X_MAX, 'shape-x-{sem}: The shape-x difference between ' \
                                                       'expect and actual is more than {dis_max}m, ' \
                                                       'diff: {r_dis}'.format(sem=sem,
                                                                              dis_max=conf.SHAPE_DIS_X_MAX,
                                                                              r_dis=dis)

                # 4. compare of shape-y difference between expect and actual, the distance should be less that 0.5m
                for dis in s_dict['shape_diff_y']:
                    assert dis < conf.SHAPE_DIS_Y_MAX, 'shape-y-{sem}: The shape-y difference between ' \
                                                       'expect and actual is more than {dis_max}m, ' \
                                                       'diff: {r_dis}'.format(sem=sem,
                                                                              dis_max=conf.SHAPE_DIS_Y_MAX,
                                                                              r_dis=dis)
            del exp_shape_dict
            del real_shape_dict
        logger.info('case is finished, now to clean env')
        del bag_real_sum_dict
        del bag_exp_sum_dict
        gc.collect()
    # return fun
    return test_perception


for case_arg in CASE_LIST:
    # logger.info(case_arg)
    globals()[case_arg['CaseName']] = make_test_case(case_arg['Story'], [case_arg['test_case']],
                                                     case_arg['Priority'], case_arg['Desc'])


if __name__ == '__main__':
    # args = ['--allure-stories', 'child', '--alluredir', './allure_reports/allure']
    args = ['-s', '-v']
    pytest.main(args)
