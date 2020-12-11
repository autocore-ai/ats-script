# -*- coding:utf8 -*-
"""
General calculation method
"""
import numpy as np
import traceback
import logging
logger = logging.getLogger()


def cal_std(l1, l2, step=1):
    """
    Calculate the standard deviation of two arrays
    1. Calculate whether the length of two arrays is consistent. If not, remove the element
    2. Array subtraction
    3. Calculate the standard deviation
    """
    l1_len = len(l1)
    l2_len = len(l2)
    if l1_len > l2_len and l1_len in [l2_len, l2_len+step]:
        l1 = l1[step:]
    elif l1_len < l2_len and l2_len in [l1_len, l1_len+step]:
        l2 = l2[step:]
    elif l1_len == l2_len:
        pass
    else:
        return False, 0, [], '{}\'s len: {} is not equal {}\'s len: {}'.format(l1, l1_len, l2, l2_len)

    diff = np.array(l1)-np.array(l2)
    std = np.std(diff)
    return True, std, list(diff), ''


def cal_euc_distance(array1, array2):
    """Calculate the Euclidean distance between the points of two vectors and return the array"""
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
