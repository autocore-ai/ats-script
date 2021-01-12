#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@Project ：autotest 
@File    ：command.py
@Date    ：2021/1/8 上午11:01 
"""

GET_ROS_NODE_LIST = 'docker exec %s /bin/bash -c \'cd %s && ' \
                    'source install/setup.bash && export ROS_IP=%s && ' \
                    'export ROS_MASTER_URI=%s && rosnode list\''
