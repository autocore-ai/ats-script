# -*- coding: utf-8 -*-
import datetime
import allure
import pytest
import gc
import logging

from testSDV.common.utils.generate_case_data import generate_case_data
import testSDV.common.sdv.action as act
import testSDV.common.sdv.config as conf


logger = logging.getLogger('sdv_test')
CASE_LIST = generate_case_data('{case_path}/sdv_cases.csv'.format(case_path=conf.PATH_CSV_CASES))
BAG_BASE_PATH = '{bag_path}/'.format(bag_path=conf.BAG_PATH)


def make_test_case(story, case_data, case_level, case_desc):
    
    @allure.feature('sdv')
    @pytest.mark.parametrize("case_data", case_data, ids=[case_desc])
    @allure.story(story)
    @allure.severity(case_level)
    def test_future_way(sdv_env_opt, case_data):
        """
        1. record bag
        2. stop record bagbag
        3. check bag
        """
        bag_dir_path = '{bag_path}/{test_name}'.format(bag_path=BAG_BASE_PATH, test_name=case_data['CaseName'])
        logger.info('case bag path: {}'.format(bag_dir_path))
        case_gt_path = '{b_dir}/gt'.format(b_dir=bag_dir_path)
        case_bag_record_path = '{b_dir}/result_{d}'.format(b_dir=bag_dir_path, 
                                                            d=str(datetime.datetime.now())[:19].replace(' ', '_').replace('-', '_').replace(':', '_'))
        logger.info('ground truth path: %s' % case_gt_path)
        logger.info('record bag path: %s' % case_bag_record_path)

        step_desc = ' 1. record ros2 bag, new bag path and name: %s' % case_bag_record_path
        with allure.step(step_desc):
            logger.info('='*20 + step_desc + '='*20)
            
            r_bool, proc = act.record_bag(case_bag_record_path)
            logger.info('record bag return: {}, info: {}'.format(r_bool, proc))
            assert r_bool, ret

        step_desc = ' 2. waiting record bag stop signal'
        with allure.step(step_desc):
            logger.info('='*20 + step_desc + '='*20)
            runtime = int(case_data['runtime'])
            r_bool, ret = act.wait_stop_signal(runtime+10)
            logger.info('waiting record bag stop signal return: {}, info: {}'.format(r_bool, ret))
            assert r_bool, ret
        
        step_desc = ' 3. stop record bag '
        with allure.step(step_desc):
            logger.info('='*20 + step_desc + '='*20)
            r_bool, ret = act.stop_reocrd_bag(proc)
            logger.info('stop record bag return: {}, info: {}'.format(r_bool, ret))
            assert r_bool, ret
        
        step_desc = ' 4. check record bag OK '
        with allure.step(step_desc):
            logger.info('='*20 + step_desc + '='*20)
            r_bool, ret = act.check_bag_OK(case_gt_path, case_bag_record_path)
            logger.info('check record bag stop return: {}, info: {}'.format(r_bool, ret))
            assert r_bool, ret

        step_desc = ' 5. check autoware state '
        with allure.step(step_desc):
            logger.info('='*20 + step_desc + '='*20)
            r_bool, ret = act.check_autoware_state(case_gt_path, case_bag_record_path)
            logger.info('check autoware state return: {}, info: {}'.format(r_bool, ret))
            assert r_bool, ret
        
        step_desc = ' 6. check route id '
        with allure.step(step_desc):
            logger.info('='*20 + step_desc + '='*20)
            r_bool, ret = act.check_route_ids(case_gt_path, case_bag_record_path)
            logger.info('check_route_ids return: {}, info: {}'.format(r_bool, ret))
            assert r_bool, ret

        step_desc = ' 7. check current_pose '
        with allure.step(step_desc):
            logger.info('='*20 + step_desc + '='*20)
            r_bool, ret = act.check_current_pose(case_gt_path, case_bag_record_path)
            logger.info('check_current_pose return: {}, info: {}'.format(r_bool, ret))
            assert r_bool, ret
            
        step_desc = ' 8. check twist '
        with allure.step(step_desc):
            logger.info('='*20 + step_desc + '='*20)
            r_bool, ret = act.check_twist(case_gt_path, case_bag_record_path)
            logger.info('check_twist return: {}, info: {}'.format(r_bool, ret))
            assert r_bool, ret
        
        step_desc = ' 9. check velocity '
        with allure.step(step_desc):
            logger.info('='*20 + step_desc + '='*20)
            r_bool, ret = act.check_velocity(case_gt_path, case_bag_record_path)
            logger.info('check_velocity return: {}, info: {}'.format(r_bool, ret))
            assert r_bool, ret
        
    return test_future_way


for case_arg in CASE_LIST:
    globals()[case_arg['CaseName']] = make_test_case(case_arg['Story'], [case_arg['test_case']],
                                                     case_arg['Priority'], case_arg['Desc'], )

if __name__ == '__main__':
    pass
