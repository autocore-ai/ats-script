# -*- coding:utf8 -*-
"""
测试执行总入口
1. 解析参数
2. 根据参数生成 pytest 执行命令-- 参数相对应的case
3. 生成测试报告
4. 生成最后汇总的测试报告，可生成图片
5. 发送测试邮件
"""

import os
import sys
import time
import shutil
import subprocess
import pytest
import logging
from config import TEST_CASE_PATH, REMOTE_TEST_DATA, TEST_REPORT_LOG, TEST_CASE_LINK

SEVERITY = ['normal']

key = 'perception'  # 决定读取哪一个CSV
marker = 'CI'  # 挑选CSV中的用例

# 如果是整个的Perception用例都需要跑，该怎样区分？
# for循环CSV，获取符合条件的case，获取后的格式如下
"""blocker　 阻塞缺陷（功能未实现，无法下一步）
critical　　严重缺陷（功能点缺失）
normal　　 一般缺陷（边界情况，格式错误）
minor　 次要缺陷（界面错误与ui需求不符）
trivial　　 轻微缺陷（必须项无提示，或者提示不规范）
"""

if __name__ == "__main__":
    # args = ["-k", runConfig_dict["Project"], "-m", runConfig_dict["markers"],
    # "--maxfail=%s" % runConfig_dict["maxfail"],
    # "--durations=%s" % runConfig_dict["slowestNum"], "--reruns", reruns, "--reruns-delay", reruns_delay,
    #
    #         "--alluredir", xml_report_path, "--html=%s" % summary_report_path]

    args = sys.argv
    # args = ['-v', '-s', '--allure-features', 'perception', '--alluredir', './allure_reports/result']
    args = ['-v', '-s', '--allure-features', 'planning', '--alluredir', './allure_reports/result']
    # args = ['-v', '-s', '-k', 'child']
    print(args)
    # 根据参数生成执行命令，命令里包含了模块，用例等级等
    test_result = pytest.main(args)  # 全部通过，返回0；有失败或者错误，则返回1
    print(test_result)

    # 生成报告
    generate = 'allure generate ./allure_reports/result/ -o ./allure_reports/report/ --clean'
    print('generate allure_results: {}'.format(generate))
    os.system(generate)

