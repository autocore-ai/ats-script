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
import argparse
import pytest
import config

CASE_TYPE = 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', help="exec cases type, 1: open source cases 2: home cases, default 1",
                        type=int, choices=[1, 2])
    parser.add_argument('-f', '--features', help="tested features, such as perception,planning")
    parser.add_argument('-s', '--stories',  help="tested stories, such as adult,car")
    parser.add_argument('-l', '--level', type=int,  choices=[0, 1, 2, 3, 4],
                        help="tested cases level, 0: trivial, 1: minor, 2: normal, 3: critical, 4: blocker")
    parser.add_argument('-m', '--mark', help="cases marker")
    parser.add_argument('-r', '--rviz', help="show rviz, default False", action="store_true")
    parser.add_argument('-sv', '--serve', help="after executed cases finished, open test results in Browse;"
                                               " default False", action="store_true")
    args = parser.parse_args()
    print(args)
    if args.type == 2:
        config.EXEC_CASE_TYPE = 2
        print('exec home cases')
    else:
        config.EXEC_CASE_TYPE = 1
        print('exec open source cases')

    if args.rviz:
        print('show rviz')
        config.RVIZ = True

    p_args = ['-v', '-s',  '--alluredir', './allure_reports/result']
    if args.features:
        p_args.append('--allure-features')
        p_args.append(args.features)
    if args.stories:
        p_args.append('--allure-stories')
        p_args.append(args.stories)

    test_result = pytest.main(p_args)  # All pass, return 0; failure or error, return 1
    print('cases exec result: {}'.format(test_result))
    if args.serve:
        gen = 'allure serve ./allure_reports/result'
    else:
        gen = 'allure generate ./allure_reports/result/ -o ./allure_reports/report/ --clean'
    print('generate allure_results: {}'.format(gen))
    os.system(gen)


if __name__ == "__main__":
    main()
