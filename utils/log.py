# -*- coding:utf8 -*-
"""日志文件"""

import logging.config
from config import TEST_CASE_PATH
import os
import functools

# 定义三种日志输出格式 开始

standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'  # 其中name为getlogger指定的名字
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] %(message)s'
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束


def md_logger(log_path):
    logfile_path_staff = '{}/logs/{}.log'.format(TEST_CASE_PATH, log_path)
    # print(logfile_path_staff)
    log_path = '/'.join(logfile_path_staff.split('/')[:-1])
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    # log配置字典
    # LOGGING_DIC第一层的所有的键不能改变
    LOGGING_DIC = {
        'version': 1,  # 版本号
        'disable_existing_loggers': False,  # 固定写法
        'formatters': {
            'standard': {
                'format': standard_format
            },
            'simple': {
                'format': simple_format
            },
        },
        'filters': {},
        'handlers': {
            # 打印到终端的日志
            'sh': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',  # 打印到屏幕
                'formatter': 'simple'
            },
            # 打印到文件的日志,收集info及以上的日志
            'fh': {
                'level': 'INFO',
                'class': 'logging.handlers.TimedRotatingFileHandler',  # 按照日期分割
                'formatter': 'simple',
                'filename': logfile_path_staff,  # 日志文件
                'when': 'D',
                # 'maxBytes': 1024*1024*5,  # 日志大小 5M字节
                'interval': 1,
                'backupCount': 5,  # 轮转文件的个数
                'encoding': 'utf-8',  # 日志文件的编码
            },
        },
        'loggers': {
            # logging.getLogger(__name__)拿到的logger配置
            '': {
                'handlers': ['sh', 'fh'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
                'level': 'DEBUG',
                'propagate': True,  # 向上（更高level的logger）传递
            },
        },
    }
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置 通过字典方式去配置这个日志
    logger = logging.getLogger()  # 生成一个log实例  这里可以有参数 传给task_id
    return logger


def log(fun):
    """
    日志装饰器，日志按照层级存放
    :return:
    """
    @functools.wraps(fun)  # 为了保留被装饰函数的函数名和帮助文档信息
    def wrapper(*args, **kwargs):
        """这是一个wrapper函数"""
        # print(fun.__globals__)
        # print(fun.__globals__['__file__'])
        # 判断调用者是函数还是类中的函数
        dir_path = fun.__code__.co_filename.split('testcases/')[-1].split('.py')[0]  # 用例所在目录
        if args:
            # 被装饰的是类中的方法
            cls_name = args[0].__class__.__name__  # 用例类名
            # cls_file = args[0].__class__.__module__  # 用例所在模块
            case_name = fun.__name__  # 用例名称
            # print('cls_file: %s' % cls_file)
            log_path = '{}/{}/{}'.format(dir_path, cls_name, case_name)
        else:
            # 被装饰的函数
            case_name = fun.__name__  # 用例名称
            log_path = '{}/{}'.format(dir_path, case_name)
        # print('log_path: %s' % log_path)
        md_logger(log_path)
        return fun(*args, **kwargs)

    return wrapper

