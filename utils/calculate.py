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
    if l1_len > l2_len and l1_len == l2_len+step:
        l1 = l1[step:]
    elif l1_len < l2_len and l1_len+step == l2_len:
        l2 = l2[step:]
    elif l1_len == l2_len:
        pass
    else:
        return False, 0, [], '{}\'s len is not equal {}\'s len'.format(l1, l2)

    diff = np.array(l1)-np.array(l2)
    std = np.std(diff)
    return True, std, list(diff), ''
