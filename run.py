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
import subprocess
import argparse
import pytest
import config

CASE_TYPE = 1


def sum_md_report():
    """
    sum markdown report
    :return:
    """
    result_dict = {'passed': 0, 'skipped': 0, 'failed': 0, 'errors': 0,
                   'expected failures': 0, 'unexpected passes': 0}

    # summary test result
    with open(config.TEST_CASE_MD_REPORT, 'r') as md_r:
        all_con = md_r.readlines()

    for result in all_con:
        if len(result.split('|')) < 3:
            continue
        result = result.split('|')[-2].strip()
        if result in result_dict.keys():
            result_dict[result] += 1

    insert_content = '# Test Report\n' \
                     '##Summary\n\n' \
                     '{} passed, {} skipped, {} failed, {} errors, {} expected failures, {} unexpected passes\n'.format(
        result_dict['passed'], result_dict['skipped'], result_dict['failed'], result_dict['errors'],
        result_dict['expected failures'], result_dict['unexpected passes'])
    # 写如文件
    with open(config.TEST_CASE_MD_REPORT, 'w') as md_r:
        md_r.write(insert_content)
        md_r.writelines(all_con)
    print('generate markdown report successfully')


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

    p_args = ['-v', '-s', '--alluredir', './allure_reports/result']
    if args.features:
        p_args.append('--allure-features')
        p_args.append(args.features)
    if args.stories:
        p_args.append('--allure-stories')
        p_args.append(args.stories)

    # source ros setup.bash
    proc = subprocess.Popen('source {ros1}'.format(ros1=config.ROS1_SETUP), shell=True, stderr=subprocess.PIPE)
    stderr = proc.stderr.read()
    if stderr:
        print(stderr)
        return

    # clean report
    with open(config.TEST_CASE_MD_REPORT, 'w') as md_r:
        md_r.write('## Detail\n\n|  TestCase   | Result  |\n|  ----  | ----  |\n')

    test_result = pytest.main(p_args)  # All pass, return 0; failure or error, return 1
    print('cases exec result: {}'.format(test_result))
    sum_md_report()

    if args.serve:
        gen = 'allure serve ./allure_reports/result'
    else:
        gen = 'allure generate ./allure_reports/result/ -o ./allure_reports/report/ --clean'
    print('generate allure_results: {}'.format(gen))
    os.system(gen)


if __name__ == "__main__":
    main()
