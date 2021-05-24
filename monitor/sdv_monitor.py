# -*- coding:utf8 -*-
"""
Listening sdv pods state
"""
import os
import requests
import json
import logging
import sys

from kubernetes import client, config, watch
from monitor.config import CENTER_DB_PATH, NAMESPACE, WATCH_INTEVAL
from config import CURRENT_DIR
from monitor.log import my_logger

log_path = '%s/logs' % CURRENT_DIR
logger = my_logger(log_path)

def monitor_sdv(namespace):
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    # config.load_kube_config()
    if os.getenv('KUBERNETES_SERVICE_HOST'):
        logger.info('load incluster config')
        config.load_incluster_config()
    else:
        config.load_kube_config()

    v1 = client.CoreV1Api()
    w = watch.Watch()
    
    timeout = WATCH_INTEVAL
    stream = w.stream(v1.list_namespaced_pod, namespace, timeout_seconds=timeout)

    container_state_dict = {}
    pods_count = 0
    for event in stream:
        pods_count += 1
        try:
            logger.info("Watch Event: %s %s" % (event['type'], event['object'].metadata.name))
            pod_name = event['object'].metadata.name
            pod_ip = event['object'].status.pod_ip
            container_state_dict[pod_name] = {'ip': pod_ip, 'container': []}

            containter_status_list = event['raw_object']['status']['containerStatuses']
            for con_status in containter_status_list:
                container_name = con_status['name']
                state = list(con_status['state'].keys())[0]
                container_state_dict[pod_name]['container'].append({container_name: state})
        except Exception as e:
            logger.exception(e)
            logger.error('event: {}'.format(event))

    logger.info('watch %d pods' % pods_count)

    return container_state_dict


def send_message_to_center_db(container_state_dict):
    logger.info('pod state: {}'.format((container_state_dict)))
    url = 'http://{ip}:8000{path}'.format(ip=os.getenv('HOST_IP'), path=CENTER_DB_PATH)
    logger.info('pod state center db url: %s' % url)

    try:
        ret = requests.put(url, headers={'Content-Type': 'application/json;'}, data=json.dumps(container_state_dict))
        logger.info('send to center db return, state: {}, {}'.format(ret.status_code, ret.text))
    except Exception as e:
        logger.exception('send pods state to center db failed: {}'.format(e))


def main():
    count = 0

    logger.info('beginning to listen sdv pod state ......')
    while True:
        err_dict = monitor_sdv(NAMESPACE)
        # if err_dict:
        logger.info('listening sdv pod message: {}'.format(err_dict))
        send_message_to_center_db(err_dict)
        count += 1
        logger.info('watch counts: %d' % count)


if __name__ == '__main__':
    main()