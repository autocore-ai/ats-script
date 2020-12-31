# -*- coding:utf8 -*-
"""
General calculation method
"""
import logging
import numpy as np
import traceback
logger = logging.getLogger()


def deal_list(list_1, list_2, step):
    """
    compare two lists, and return equal length list
    :param list_1:
    :param list_2:
    :param step:
    :return:
    """
    len_list_1, len_list_2 = len(list_1), len(list_2)
    if len_list_1 in [len_list_2+1, len_list_2+step]:
        step = len_list_1 - len_list_2
        list_1 = list_1[step:]
    elif len_list_2 in [len_list_1+1, len_list_1+step]:
        step = len_list_2 - len_list_1
        list_2 = list_2[step:]
    elif len_list_1 == len_list_2:
        pass
    else:
        return False, list_1, list_2, 'step: {}, {}\'s len: {} is not equal {}\'s len: {}'.format(step, len_list_1,
                                                                                                  list_1, len_list_2,
                                                                                                  list_2)
    return True, list_1, list_2, ''

def cal_std(list_1, list_2):
    """
    Calculate the standard deviation of two arrays
    1. Calculate whether the length of two arrays is consistent. If not, remove the element
    2. Array subtraction
    3. Calculate the standard deviation
    """
    diff = np.array(list_1)-np.array(list_2)
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
