# -*- coding:utf8 -*-
"""
Listening sdv pods state
"""
import os
import requests
import json
import logging
import sys
sys.path.append('../')
sys.path.append('../../')

from kubernetes import client, config, watch
from monitor.config import CENTER_DB_URL, NAMESPACE
from config import CURRENT_DIR
from monitor.log import my_logger

# CURRENT_DIR = './../'

# logging.basicConfig(level=logging.DEBUG, filename='%s/logs/monitor.log' % CURRENT_DIR, filemode='w',format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
log_path = '%s/logs' % CURRENT_DIR
logger = my_logger(log_path)

def monitor_sdv(namespace):
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    # config.load_kube_config()
    if os.getenv('KUBERNETES_SERVICE_HOST'):
        logger.info('load_incluster_config')
        config.load_incluster_config()
    else:
        config.load_kube_config()

    v1 = client.CoreV1Api()
    w = watch.Watch()
    
    # list all namespaces
    # print(v1.list_namespaced_pod(namespace))
    stream = w.stream(v1.list_namespaced_pod, namespace, timeout_seconds=10)
    err_container_dict = {}

    for event in stream:
        logger.info("Watch Event: %s %s" % (event['type'], event['object'].metadata.name))
        pod_name = event['object'].metadata.name
        
        containter_status_list = event['raw_object']['status']['containerStatuses']
        for con_status in containter_status_list:
            state = con_status['state']
            
            if 'running' not in state:
                desc = 'container[{name}] state: {state}'.format(name=con_status['name'], state=state) 
                err_container_dict[pod_name] = desc  # 具体信息待完善
                continue

            running_state = state['running']
            if not running_state:
                desc = 'container[{name}] state: {state}'.format(name=con_status['name'], state=state) 
                err_container_dict[pod_name] = desc  # 具体信息待完善

    return err_container_dict


def send_message_to_center_db(err_dict):
    url = CENTER_DB_URL
    try:
        ret = requests.post(url, headers={'Content-Type': 'application/json;'}, data=json.dumps(err_dict))
        logger.info('send to center db return: {}'.format(ret.json()))
    except Exception as e:
        logger.exception('send pods state to center db failed: {}'.format(e))


def main():
    count = 0

    logger.info('begin listen sdv pod ......')
    while True:
        err_dict = monitor_sdv(NAMESPACE)
        if err_dict:
            logger.info('listening sdv pod error message: {}'.format(err_dict))
            send_message_to_center_db(err_dict)
        count += 1
        logger.info('watch count: %d' % count)


if __name__ == '__main__':
    main()