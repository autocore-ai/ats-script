# -*- coding:utf8 -*-

import logging.config
import os
import functools


def md_logger(log_path):
    standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                      '[%(levelname)s][%(message)s]'  # Where name is the name specified by getlogger
    simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] %(message)s'

    logfile_path_staff = '{}.log'.format(log_path)
    log_path = '/'.join(logfile_path_staff.split('/')[:-1])
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    # log Configuration dictionary
    # LOGGING_DIC All the keys in the first layer cannot be changed
    logging_dict = {
        'version': 1,
        'disable_existing_loggers': False,
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
            # print to client
            'sh': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            # Print to file log, collect info and above logs
            'fh': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',  # Split by date
                'formatter': 'simple',
                'filename': logfile_path_staff,  # log file
                'when': 'D',
                'interval': 1,
                'backupCount': 5,  # Number of rotation files
                'encoding': 'utf-8',
            },
        },
        'loggers': {
            '': {
                # Here we add the two handlers defined above, that is,
                # log data is written to the file and printed to the screen
                'handlers': ['sh', 'fh'],
                'level': 'DEBUG',
                'propagate': True,  # Pass up (higher level logger)
            },
        },
    }
    # Import the logging configuration defined above and configure the log by dictionary
    logging.config.dictConfig(logging_dict)
    logger = logging.getLogger()  # generate a log instance

    return logger


def log(fun):
    """
    Log decorator, the log is stored according to the level
    :return:
    """
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        # determine whether the caller is a function or a function in a class
        dir_path = fun.__code__.co_filename.split('testcases/')[-1].split('.py')[0]  # Use case directory

        if args:
            # What is decorated is the method in the class
            cls_name = args[0].__class__.__name__  # use case class name
            case_name = fun.__name__  # case name
            log_path = '{}/{}/{}'.format(dir_path, cls_name, case_name)
        else:
            case_name = fun.__name__  # case name
            log_path = '{}/{}'.format(dir_path, case_name)
        md_logger(log_path)
        return fun(*args, **kwargs)

    return wrapper
