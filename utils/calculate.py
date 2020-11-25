# -*- coding:utf8 -*-
"""
通用计算方法
"""
import numpy as np
import traceback
import logging
logger = logging.getLogger()


def cal_std(l1, l2, step=1):
    """
    计算两个数组的标准差
    1. 计算两个数组的长度是否一致，不一致，则去除元素
    2. 数组相减
    3. 计算标准差
    """
    l1_len = len(l1)
    l2_len = len(l2)
    if l1_len > l2_len and l1_len == l2_len+step:
        l1 = l1[step:]
    elif l1_len < l2_len and l1_len+step == l2_len:
        l2 = l2[step:]
    elif l1_len == l2_len:
        pass
    else:
        return False, 0, [], '{}\'s len is not equal {}\'s len'.format(l1, l2)

    # 数组相减
    diff = np.array(l1)-np.array(l2)
    std = np.std(diff)
    return True, std, list(diff), ''


def cal_euc_distance(array1, array2):
    """计算两个向量各个点之间的欧式距离，返回数组"""
    ret_list = []
    if len(array1) != len(array2):
        return False, 'two array\'s length is not equal, {} != {}'.format(len(array1), len(array2))
    try:
        for i, d in enumerate(array1):
            dist = np.linalg.norm(np.array(d)-np.array(array2[i]))
            ret_list.append(dist)
        return True, ret_list
    except Exception as e:
        logger.error(array1)
        logger.error(array2)
        logger.exception(e)
        return False, '%s' % traceback.format_exc()


if __name__ == '__main__':
    print(cal_euc_distance([np.array([1, 2]), np.array([2,3])], [np.array([2, 1]), np.array([2,3])]))