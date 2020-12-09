# -*- coding:utf8 -*-
"""
看下数据多的时候，计算多个欧氏距离的时间
"""

import numpy as np
import random
import time

# n = 30
# x_list = [round(random.uniform(1, x), 4) for x in range(n)]
# y_list = [round(random.uniform(1, y), 4) for y in range(n)]
# z_list = [round(random.uniform(1, z), 4) for z in range(n)]
#
# real_x_list = [round(random.uniform(1, x), 4) for x in range(n)]
# real_y_list = [round(random.uniform(1, y), 4) for y in range(n)]
# real_z_list = [round(random.uniform(1, z), 4) for z in range(n)]
#
#
# exp_p = np.array([(x, y, z) for x in x_list
#                    for y in y_list
#                    for z in z_list
#          ])
#
# real_val = np.array([(x, y, z) for x in real_x_list
#                       for y in real_y_list
#                       for z in real_z_list
#          ])
#
# ret_list = []
# t = time.time()
# for index, val in enumerate(exp_p):
#     ret_list.append(np.linalg.norm(val - real_val[index]))
#
# print(time.time() - t)
# print(len(ret_list))
# # print(ret_list)
#
# n_fit = 0
# for ret in ret_list:
#     n_fit += 1 if ret < 1 else 0
#
# # print(n_fit)
# # print(n_fit*0.1/len(ret_list))
#
#
# def cos_sim(vector_a, vector_b):
#     """
#     计算两个向量之间的余弦相似度
#     :param vector_a: 向量 a
#     :param vector_b: 向量 b
#     :return: sim
#     """
#     vector_a = np.mat(vector_a)
#     vector_b = np.mat(vector_b)
#     num = float(vector_a * vector_b.T)
#     denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
#     cos = num / denom
#     sim = 0.5 + 0.5 * cos
#     return sim
#
#
# cos_list = []
# t = time.time()
# for index, val in enumerate(exp_p):
#     cos_list.append(cos_sim(val, real_val[index]))
# print(time.time() - t)

# print(cos_list)
a = ['红', '黄', '绿']
b = [[x, y, z] for x in a
       for y in a
       for z in a]

for i in b:
    print('距离箭头形红绿灯较远（50m左右），三个红绿灯依次为： {}，{}，{}'.format(i[0], i[1], i[2]))
for i in b:
    print('距离箭头形红绿灯较近（5m左右），三个红绿灯依次为： {}，{}，{}'.format(i[0], i[1], i[2]))

