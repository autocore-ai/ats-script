#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Bool
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped
import logging
logger = logging.getLogger()


class AutoTestIO(Node):
    """
    Automatic test data exchange interface class
    """
    def __init__(self):
       
        self.pub_initialpose = self.create_publisher(PoseWithCovarianceStamped, 'initialpose', 10)
        self.pub_goal = self.create_publisher(PoseStamped, 'planning/mission_planning/goal', 10)
        # self.pub_autoware_engage = self.create_publisher(Bool, 'autoware/put/engage', 1)

    def initialpose(self, position: list, orientation: list):
        """
        set init pise
        """
        init_pose = PoseWithCovarianceStamped()  # 起点填充数据，事先用ros topic echo 记录下数据
        init_pose.pose.pose.position.x = position[0]
        init_pose.pose.pose.position.y = position[1]
        init_pose.pose.pose.position.z = position[2]
        init_pose.pose.pose.orientation.x = orientation[0]
        init_pose.pose.pose.orientation.y = orientation[1]
        init_pose.pose.pose.orientation.z = orientation[2]
        init_pose.pose.pose.orientation.w = orientation[3]
        init_pose.header.frame_id = "viewer"
        self.pub_initialpose.publish(init_pose)

    def goal(self, position: list, orientation: list):
        """
        set goal
        """
        goal_pose = PoseStamped()
        goal_pose.pose.position.x = position[0]
        goal_pose.pose.position.y = position[1]
        goal_pose.pose.position.z = position[2]
        goal_pose.pose.orientation.x = orientation[0]
        goal_pose.pose.orientation.y = orientation[1]
        goal_pose.pose.orientation.z = orientation[2]
        goal_pose.pose.orientation.w = orientation[3]
        goal_pose.header.frame_id = "viewer"
        self.pub_goal.publish(goal_pose)

    def engage_autoware(self, data):
        """
        autoware engage true or false
        """
        b_data = Bool()
        b_data.data = data
        self.pub_autoware_engage.publish(b_data)


class AutowareStateSubscriber(Node):

    def __init__(self):
        super().__init__('autoware_state_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.stop = False

    def listener_callback(self, msg):
        logger.info('I heard: "%s"' % msg.data)
        if msg == 'ArrivedGoal':
            self.stop = True
