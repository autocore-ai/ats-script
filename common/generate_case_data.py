# -*- coding:utf8 -*-
"""
读取 CSV 生成测试用例数据
"""
import csv
import pandas as pd
import traceback
import logging
logger = logging.getLogger()


def generate_case_data(csv_case_path):
    """
    根据用例路径，生成指定标签的用例数据
    severity: 标志着这个story的用例整体级别，有 normal 等值
    level: 用例级别，比如1,2,3，
    根据story 获取用例数据

    [
        {
            'story': 'adult', 'case_level': 'normal', 'case_desc': '静止成人站在静态车前'， 'jira_id': 1,
            'test_data' : {}
        },normal
        ...
    ]

    """
    data_list = []
    df = pd.read_csv(csv_case_path)
    for index, d in df.iterrows():
        jira_id = d['Jira_ID']
        case_dict = {'Jira_ID': jira_id, 'Title': d['Title'], 'Priority': d['Priority'], 'Story': d['Story']}
        d.drop('Jira_ID', inplace=True)
        d.drop('Title', inplace=True)
        d.drop('Priority', inplace=True)
        d.drop('Story', inplace=True)
        case_dict['test_case'] = d
        case_dict['test_case']['Jira_ID'] = jira_id
        data_list.append(case_dict)
    logger.info('read cases count: {}'.format(len(data_list)))
    return data_list


if __name__ == '__main__':
    generate_case_data('/home/duan/PycharmProjects/auto_test/testcases/test_ODD/cases/perception_cases.csv')