# -*- coding:utf8 -*-
"""
Read CSV to generate test case data
"""
import pandas as pd
import logging
logger = logging.getLogger()


def generate_case_data(csv_case_path):
    """
    According to the use case path, the use case data of the specified tag is generated
    """
    data_list = []
    df = pd.read_csv(csv_case_path)

    # Check the uniqueness of the case
    case_name = df.CaseName.duplicated()
    if case_name.any():
        raise Exception('duplicated case name, must be unique')

    # check case name start with test_
    wrong_name = df[~ df['CaseName'].str.contains('test_')]
    if wrong_name.CaseName.count():
        raise Exception('CaseName column must start with \'test_\'')

    for index, d in df.iterrows():
        case_name = d['CaseName']
        case_dict = {'Title': d['Title'], 'Priority': d['Priority'], 'Story': d['Story'],
                     'CaseName': d['CaseName']}
        jira_id = ''
        if 'Jira_ID' in d:
            jira_id = d['Jira_ID']
            case_dict['Jira_ID'] = jira_id
            d.drop('Jira_ID', inplace=True)

        d.drop('Title', inplace=True)
        d.drop('Priority', inplace=True)
        d.drop('Story', inplace=True)
        d.drop('CaseName', inplace=True)
        case_dict['test_case'] = d
        case_dict['test_case']['CaseName'] = case_name
        if jira_id:
            case_dict['test_case']['Jira_ID'] = jira_id
        data_list.append(case_dict)
    logger.info('read cases count: {}'.format(len(data_list)))
    logger.info('read cases: {}'.format(data_list))
    return data_list


if __name__ == '__main__':
    generate_case_data('/home/duan/PycharmProjects/auto_test/testcases/test_ODD/cases/perception_cases.csv')