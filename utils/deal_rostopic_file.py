# -*- coding:utf8 -*-
"""
rostopic 处理文件
生成CSV
"""

import csv


def deal(file_path_list, out_file_path='./'):
    header_list = ['第{0}次'.format(i+1) for i in range(len(file_path_list))]
    lines_list = []
    with open(out_file_path, 'w+') as topic_csv:
        w = csv.DictWriter(topic_csv, fieldnames=header_list)
        w.writeheader()

        for i, file_path in enumerate(file_path_list):
            with open(file_path, 'r') as topic:
                lines = topic.readlines()
                count = 0
                for line in lines:
                    if 'data' in line:
                        count += 1
                        if count > len(lines_list):
                            lines_list.append({header_list[i]: line.split(': ')[1].split('\n')[0]})
                        else:
                            lines_list[count-1][header_list[i]] = line.split(': ')[1].split('\n')[0]
        w.writerows(lines_list)


if __name__ == '__main__':
    deal(['/home/duan/TEST_DATA/Performance/pcl_2_reso_4/data/exec_1.txt',
          '/home/duan/TEST_DATA/Performance/pcl_2_reso_4/data/exec_2.txt',
          '/home/duan/TEST_DATA/Performance/pcl_2_reso_4/data/exec_3.txt',
          '/home/duan/TEST_DATA/Performance/pcl_2_reso_4/data/exec_4.txt',
          '/home/duan/TEST_DATA/Performance/pcl_2_reso_4/data/exec_5.txt',
          ], '/home/duan/TEST_DATA/Performance/pcl_2_reso_4/data/pcl_2_reso_4.csv')
