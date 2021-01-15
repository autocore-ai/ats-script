#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@Project ：autotest 
@File    ：my_docker.py
@Date    ：2021/1/11 上午11:21

docker operation
"""
import docker
import logging
import subprocess
from weakref import WeakValueDictionary

logger = logging.getLogger()


def start_container(cmd: str) -> (bool, str):
    """
    start docker
    :param cmd: start command
    :return:
    """
    # p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # stdout = p.stdout.read().decode('utf-8')
    # stderr = p.stderr.read().decode('utf-8')
    # logger.info('start docker result, stdout: {}, stderr: {}'.format(stdout, stderr))
    # if stderr:
    #     logger.error(stderr)
    #    return False, stderr
    subprocess.Popen(cmd, shell=True)
    return True, ''


class Singleton(type):
    _instances = WeakValueDictionary()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # This variable declaration is required to force a
            # strong reference on the instance.
            instance = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class MyContainer(metaclass=Singleton):
    """
    my container api
    """

    def __init__(self, name_or_id):
        try:
            self.client = docker.client.from_env()
            self.name_or_id = name_or_id
            self.container = self.client.containers.get(name_or_id)
            logger.info('get container successfully')
        except Exception as e:
            logger.error(e)
            raise e

    def stop(self):
        """
        container status
        return
        True: container is running
        False: container stop or something is wrong
        """
        try:
            self.container.stop()
            return True, ''
        except Exception as e:
            logger.exception(e)
            return False, 'stop container except: %s' % e.__str__()

    def exec_run(self, cmd):
        """
        Run a /bin/bash command inside this container. Similar to
        ``docker exec /bin/bash -c``.
        ``demux=True``, a tuple of two bytes: stdout and stderr.
        """
        try:
            command = '/bin/bash -c \'{cmd}\''.format(cmd=cmd)
            exit_code, output = self.container.exec_run(command, demux=True)
            if exit_code == 0:
                return True, output
            logger.error('exec cmd inside container[%s], exit code: %d, output: %s' % (self.name_or_id,
                                                                                       exit_code, str(output)))
            return False, str(output)
        except Exception as e:
            return False, 'exec command in container[%s] exception: %s' % (self.name_or_id, e.__str__())

    def status(self):
        """
        container status
        """
        return self.container.status
