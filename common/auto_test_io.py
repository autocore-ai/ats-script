import _thread
import time
import rospy
from std_msgs.msg import Bool
from std_msgs.msg import Float32
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped
import copy
import logging
logger = logging.getLogger()


class AutoTestIO:
    """
    Automatic test data exchange interface class
    """
    def __init__(self, args=None):
        self.current_pose = None
        try:

            my_handlers = copy.copy(logger.handlers)
            rospy.init_node('io', argv=args, anonymous=True)
            logger.handlers = my_handlers
            rospy.Subscriber('current_pose', PoseStamped,
                             self.callback_current_pose)
            self.pub_initialpose = rospy.Publisher(
                'initialpose', PoseWithCovarianceStamped, queue_size=1, latch=True)
            self.pub_goal = rospy.Publisher(
                'planning/mission_planning/goal', PoseStamped, queue_size=1, latch=True)
            self.pub_autoware_engage = rospy.Publisher(
                'autoware/engage', Bool, queue_size=1, latch=True)
            self.pub_vehicle_engage = rospy.Publisher(
                'vehicle/engage', Bool, queue_size=1, latch=True)
            self.pub_velocity_limit = rospy.Publisher(
                'planning/scenario_planning/max_velocity', Float32, queue_size=1)
            _thread.start_new_thread(rospy.spin, ())
        except Exception as e:
            logger.exception(e)
            raise e

    def callback_current_pose(self, msg):
        self.current_pose = msg

    @property
    def pose(self):
        """
        get current pose
        """
        # return (self.current_pose.pose.position.x, self.current_pose.pose.position.y)

    def initialpose(self, data):
        """
        set init pise
        """
        data.header.frame_id = "viewer"
        self.pub_initialpose.publish(data)

    def goal(self, data):
        """
        set goal
        """
        data.header.frame_id = "viewer"
        data.header.stamp = rospy.get_rostime()
        self.pub_goal.publish(data)

    def engage_autoware(self, data):
        """
        autoware engage true or false
        """
        self.pub_autoware_engage.publish(data)

    def engage_vehicle(self, data):
        """
        vehicle engage true or false
        """
        self.pub_vehicle_engage.publish(data)

    def velocity_limit(self, data):
        """
        set max speed km/h
        """
        self.pub_velocity_limit.publish(data / 3.6)

    def add_pedestrian(self, pose, speed):
        """
        TODO add pedestrian
        """
        pass

    def add_car(self, pose, speed):
        """
        TODO add car
        """
        pass

    def remove_obstacle(self, id=None):
        """
        TODO remove object, if argv is empty, remove all移除obstacle, 参数空则移除所有
        """
        pass


if __name__ == '__main__':
    io = AutoTestIO()
    init_pose = PoseWithCovarianceStamped()
    init_pose.pose.pose.position.x = 0
    init_pose.pose.pose.position.y = 1
    init_pose.pose.pose.position.z = 2
    init_pose.pose.pose.orientation.x = 0
    init_pose.pose.pose.orientation.y = 0
    init_pose.pose.pose.orientation.z = 0
    init_pose.pose.pose.orientation.w = 1
    io.initialpose(init_pose)
    goal_pose = PoseStamped()
    goal_pose.pose.position.x = 5
    goal_pose.pose.position.x = 0
    goal_pose.pose.position.x = 0
    goal_pose.pose.orientation.x = 0
    goal_pose.pose.orientation.y = 0
    goal_pose.pose.orientation.z = 0
    goal_pose.pose.orientation.w = 1
    io.goal(goal_pose)
    io.engage_autoware(True)
    time.sleep(3)
