# -*- coding:utf8 -*-
import pytest

if __name__ == '__main__':
    import time
    import os
    from config import TEST_CASE_PATH

    report_html_dir = '{}/{}'.format(TEST_CASE_PATH, time.strftime("report_%Y-%m-%d_%H:%M:%S", time.localtime()))
    print('exec testcases')
    pytest.main(['-s', '-v', '--alluredir', '{}/allure_results/'.format(TEST_CASE_PATH)])
    print('generate allure_results')
    os.system('allure generate {}/allure_results/ -o {}/ --clean'.format(TEST_CASE_PATH, report_html_dir))
    print('mv log')
    os.system('cp -r {}/logs {}/data/attachments'.format(TEST_CASE_PATH, report_html_dir))

