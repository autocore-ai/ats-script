# -*- coding: utf-8 -*-
import datetime
import allure
import pytest
import multiprocessing
import gc
from common.utils.process import *
from common.generate_case_data import generate_case_data
import common.ODD.futur_eway.fw_action as fw_act


logger = logging.getLogger()
case_dir = odd_conf.EXEC_CASE_SCENE[odd_conf.EXEC_CASE_TYPE]['case_dir']
CASE_LIST = generate_case_data('{case_path}/{case_dir}/fwg_cases.csv'.format(case_path=odd_conf.ODD_CSV_CASES,
                                                                                  case_dir=case_dir))
bag_dir = odd_conf.EXEC_CASE_SCENE[odd_conf.EXEC_CASE_TYPE]['bag_dir']
BAG_BASE_PATH = '{bag_path}/{bag_dir}/fw/'.format(bag_path=odd_conf.BAG_PATH, bag_dir=bag_dir)


def make_test_case(story, case_data, case_level, case_desc):
    
    @allure.feature('future_way')
    @pytest.mark.parametrize("case_data", case_data, ids=[case_desc])
    @allure.story(story)
    @allure.severity(case_level)
    def test_future_way(fw_env_opt, case_data):
        """
        1. record bag
        2. stop record bagbag
        3. check bag
        """
        bag_dir_path = '{bag_path}/{test_name}'.formant(bag_path=BAG_BASE_PATH, test_name=case_data['CaseName'])
        logger.info('case bag path: {}'.format(bag_dir_path))
        case_gt_path = '{b_dir}/gt'.format(b_dir=bag_dir_path)
        case_bag_record_path = '{b_dir}/retsult_{d}'.format(b_dir=bag_dir_path, 
                                                            d=str(datetime.datetime.now())[:19].replace(' ', '_').replace('-', '_'))
        logger.info('ground truth path: %s' % case_gt_path)
        logger.info('record bag path: %s' % case_bag_record_path)
        

        step_desc = '1. record ros2 bag, new bag path and name: %s' % case_bag_record_path
        with allure.step(step_desc):
            logger.info('='*20 + step_desc + '='*20)
            # bag_duration = case_data['bag_duration']
            r_bool, ret = fw_act.record_bag(case_bag_record_path)
            assert r_bool, ret

        step_desc = '2. waiting to record bag'
        with allure.step(step_desc):
            logger.info('='*20 + step_desc + '='*20)
        
        step_desc = '3. stop record bag'
        with allure.step(step_desc):
            logger.info('='*20 + step_desc + '='*20)
        
        step_desc = '4. check record bag OK'
        with allure.step(step_desc):
            logger.info('='*20 + step_desc + '='*20)
            r_bool, ret = fw_act.check_bag_OK(case_gt_path, case_bag_record_path)
            assert r_bool, ret

        step_desc = '5. check route id'
        with allure.step():
            logger.info('='*20 + step_desc + '='*20)
            r_bool, ret = fw_act.check_route_ids(case_gt_path, case_bag_record_path)
            assert r_bool, ret

        step_desc = '6. check current_pose'
        with allure.step():
            logger.info('='*20 + step_desc + '='*20)
            r_bool, ret = fw_act.check_current_pose(case_gt_path, case_bag_record_path)
            assert r_bool, ret
            
        step_desc = '7. check twist'
        with allure.step():
            logger.info('='*20 + step_desc + '='*20)
            r_bool, ret = fw_act.check_twist(case_gt_path, case_bag_record_path)
            assert r_bool, ret
        
        step_desc = '8. check velocity'
        with allure.step():
            logger.info('='*20 + step_desc + '='*20)
            r_bool, ret = fw_act.check_velocity(case_gt_path, case_bag_record_path)
            assert r_bool, ret
        
        step_desc = '8. check trajectory'
        with allure.step():
            logger.info('='*20 + step_desc + '='*20)

    return test_future_way


for case_arg in CASE_LIST:
    globals()[case_arg['CaseName']] = make_test_case(case_arg['Story'], [case_arg['test_case']],
                                                     case_arg['Priority'], case_arg['Desc'], )

if __name__ == '__main__':
    pass
