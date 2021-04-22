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
import subprocess
import threading
import argparse
import pytest
import config
import monitor.sdv_monitor as s_m


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-pt', '--pytest', help="pytest params, such as '-m marker --count=5'")
    args = parser.parse_args()

    p_args = ['-v', '-s', '--html=./allure_reports/report.html', '--self-contained-html',
              '--alluredir', './allure_reports/result']

    # pytest params
    if args.pytest:
        p_args.extend(args.pytest.split(' '))

    print('start monitor ......')
    t = threading.Thread(target=s_m.main)
    t.start()
    time.sleep(2)

    print('test ego car ......')
    test_result = pytest.main(p_args)  # All pass, return 0; failure or error, return 1
    print('cases exec result: {}'.format(test_result))

    t.join()
    

if __name__ == "__main__":
    main()
