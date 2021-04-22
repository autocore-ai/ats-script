# -*- coding:utf8 -*-

import logging.config
import os
import functools


def my_logger(log_path):
    standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                      '[%(levelname)s][%(message)s]'  # Where name is the name specified by getlogger
    simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] %(message)s'

    logfile_path_staff = '{}/monitor.log'.format(log_path)
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
            'monitor': {
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
            'monitor': {
                # Here we add the two handlers defined above, that is,
                # log data is written to the file and printed to the screen
                'handlers': ['sh', 'monitor'],
                'level': 'DEBUG',
                'propagate': True,  # Pass up (higher level logger)
            },
        },
    }
    # Import the logging configuration defined above and configure the log by dictionary
    logging.config.dictConfig(logging_dict)
    logger = logging.getLogger('monitor')  # generate a log instance

    return logger