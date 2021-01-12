# -*- coding: utf-8 -*-
"""
Localization module case
"""

import logging
import allure
import pytest
import gc

from common.generate_case_data import generate_case_data
from common.cases_env_args import get_case_argv
logger = logging.getLogger()

case_argv = get_case_argv()
CASE_LIST = generate_case_data(case_argv['localization'])
BAG_BASE_PATH = case_argv['localization_bag_path']


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
                                                     case_arg['Priority'], case_arg['Title'])


if __name__ == '__main__':
    # args = ['--allure-stories', 'child', '--alluredir', './allure_reports/allure']
    args = ['-s', '-v']
    pytest.main(args)
