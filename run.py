# -*- coding:utf8 -*-
"""
General entrance of test execution
1. Analytical parameters
2. Generate pytest execution command according to the parameter -- the case corresponding to the parameter
3. Generate test report
4. Generate the final summary test report and generate pictures
5. Send test email
"""

import os
import time
import json
import subprocess
import threading
import argparse
import requests
import pytest
import logging
import config
import monitor.sdv_monitor as s_m
logger = logging.getLogger()


def exec_case(p_args):
    host_ip = os.getenv('HOST_IP')

    test_result = pytest.main(p_args)  # All pass, return 0; failure or error, return 1
    logger.info('cases exec result: {}'.format(test_result))

    gen = 'allure generate ./allure_reports/result/ -o ./allure_reports/report/ --clean'
    logger.info('generate allure_results: {}'.format(gen))
    os.system(gen)

    # post exec result to zenoh db test
    test_result_url = 'http://%s:8111/report/index.html' % host_ip
    url = 'http://{ip}:8000/rsu/autotest/result_url/'.format(ip=host_ip)
    logger.info('test result center db url: %s' % url)

    try:
        ret = requests.put(url, data=test_result_url)
        logger.info('send test result to center db state: {}, return: {}'.format(ret.status_code, ret.text))
    except Exception as e:
        logger.exception('send test result to center db failed: {}'.format(e))

    open_server = 'allure open ./allure_reports -p 8111'
    logger.info(open_server)
    os.system(open_server)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-pt', '--pytest', help="pytest params, such as '-m marker --count=5'")
    args = parser.parse_args()

    p_args = ['-v', '-s', '--html=./allure_reports/report.html', '--self-contained-html',
              '--alluredir', './allure_reports/result']

    if args.pytest:
        p_args.extend(args.pytest.split(' '))

    logger.info('start monitor ......')
    t = threading.Thread(target=s_m.main)
    t.start()
    time.sleep(1)

    logger.info('test ego car ......')
    case_th = threading.Thread(target=exec_case, args=(p_args,))
    case_th.start()
    case_th.join()

    t.join()
    

if __name__ == "__main__":
    main()
