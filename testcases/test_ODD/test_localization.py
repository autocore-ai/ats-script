# -*- coding: utf-8 -*-
"""
Localization module case
"""

import logging
import allure
import pytest

from common.generate_case_data import generate_case_data
import common.ODD.config as odd_conf

logger = logging.getLogger()

case_dir = odd_conf.EXEC_CASE_SCENE[odd_conf.EXEC_CASE_TYPE]['case_dir']
CASE_LIST = generate_case_data('{case_path}/{case_dir}/localization_cases.csv'.format(case_path=odd_conf.ODD_CSV_CASES,
                                                                                      case_dir=case_dir))
bag_dir = odd_conf.EXEC_CASE_SCENE[odd_conf.EXEC_CASE_TYPE]['bag_dir']
BAG_BASE_PATH = '{bag_path}/{bag_dir}/localization'.format(bag_path=odd_conf.BAG_PATH, bag_dir=bag_dir)


def make_test_case(story, case_data, case_level, case_desc):
    """dynamic generate test case"""
    @allure.feature('localization')
    @pytest.mark.parametrize("case_data", case_data, ids=[case_desc])
    @allure.story(story)
    @allure.severity(case_level)
    def test_localization(env_opt, case_data):
        """
        Step：
        1. start environment
        2. ready to record bag
        3. play bag
        4. analysis expect and test result bag
        5. compare two bags
        6. clean env
        """

    # return fun
    return test_localization


for case_arg in CASE_LIST:
    # logger.info(case_arg)
    globals()[case_arg['CaseName']] = make_test_case(case_arg['Story'], [case_arg['test_case']],
                                                     case_arg['Priority'], case_arg['Desc'])


if __name__ == '__main__':
    # args = ['--allure-stories', 'child', '--alluredir', './allure_reports/allure']
    args = ['-s', '-v']
    pytest.main(args)
