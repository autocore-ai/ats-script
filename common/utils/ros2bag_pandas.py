"""
ROS2 bag generator
ros2 bag format sqlite3, serialization_format cdr
"""

import six
import re
import warnings

import rosbag2_py as rospy
import pandas as pd
import yaml
import numpy as np

from rclpy.serialization import deserialize_message
from rosidl_runtime_py.utilities import get_message


class Ros2bag:

    def __init__(self, bag_path):
        serialization_format = 'cdr'
        self.bag_path = bag_path
        self.storage_options = rospy.StorageOptions(uri=bag_path, storage_id='sqlite3')
        self.converter_options = rospy.ConverterOptions(
            input_serialization_format=serialization_format,
            output_serialization_format=serialization_format)
        with open('%s/metadata.yaml' % self.bag_path) as bag_file:
            self.bag_info = yaml.load(bag_file, Loader=yaml.FullLoader)

    def dataframe(self, include=None, exclude=None, parse_header=False, seconds=False, prefix_topic=True):
        """
        Read in a ros2bag file and create a pandas data frame that
        is indexed by the time the message was recorded in the bag.
        :include: None, String, or List  Topics to include in the dataframe
                   if None all topics added, if string it is used as regular
                       expression, if list that list is used.
        :exclude: None, String, or List  Topics to be removed from those added
                using the include option using set difference.  If None no topics
                removed. If String it is treated as a regular expression. A list
                removes those in the list.
        :seconds: time index is in seconds
        :prefix_topic: data name include topic or not
        :returns: a pandas dataframe object
        """
        reader = rospy.SequentialReader()
        reader.open(self.storage_options, self.converter_options)

        topic_types = reader.get_all_topics_and_types()
        topic_type_map = {topic.name: topic.type for topic in topic_types}
        bag_topics = self.prune_topics(topic_type_map.keys(), include, exclude)
        # print(bag_topics)
        prefix_key_dict = {topic: self.get_key_name(topic) for topic in bag_topics}
        # print(prefix_key_dict)
        storage_filter = rospy.StorageFilter(topics=bag_topics)
        reader.set_filter(storage_filter)
        msg_len = self.get_length(bag_topics)
        datastore = {}
        # create the index
        index = []
        count = 0
        while reader.has_next():
            (topic, msg, t) = reader.read_next()
            msg_type = get_message(topic_type_map[topic])
            # print(topic)
            msg = deserialize_message(msg, msg_type)
            # print(topic)
            topic_prefix = prefix_key_dict[topic] if prefix_topic else ''
            if seconds:
                index.append(str(msg.header.stamp.sec))
            else:
                try:
                    index.append(msg.header.stamp.nanosec)
                except:
                    index.append("")

            if hasattr(msg, '__slots__'):
                msg_dict = self.get_base_fields(msg, prefix=topic_prefix, parse_header=parse_header)
                for field, value in msg_dict.items():
                    if field not in datastore:
                        datastore[field] = np.empty(msg_len)
                    datastore[field][count] = value

            else:
                if topic_prefix not in datastore:
                    datastore[topic_prefix] = np.empty(msg_len)
                datastore[topic_prefix][count] = msg
            # for slot in msg
            # message counter
            count += 1

        if not seconds:
            index = pd.to_datetime(index, unit='ns')
        return pd.DataFrame(data=datastore, index=index)

    def get_length(self, topics=None):
        """
        Find the length (# of rows) in the created dataframe
        """
        msg_count = 0
        if not topics:
            msg_count = self.bag_info['rosbag2_bagfile_information']['message_count']
        for topic_count in self.bag_info['rosbag2_bagfile_information']['topics_with_message_count']:
            if topic_count['topic_metadata']['name'] in topics:
                msg_count += topic_count['message_count']
        return msg_count

    @staticmethod
    def get_key_name(name):
        """fix up topic to key names to make them a little prettier"""
        if name[0] == '/':
            name = name[1:]
        name = name.replace('/', '.')
        return name

    @staticmethod
    def prune_topics(bag_topics, include, exclude):
        """
        prune the topics.  If include is None add all to the set of topics to
        use if include is a string regex match that string,
        if it is a list use the list
        If exclude is None do nothing, if string remove the topics with regex,
        if it is a list remove those topics
        """

        topics_to_use = set()
        # add all of the topics
        if include is None:
            for t in bag_topics:
                topics_to_use.add(t)
        elif isinstance(include, six.string_types):
            check = re.compile(include)
            for t in bag_topics:
                if re.match(check, t) is not None:
                    topics_to_use.add(t)
        else:
            try:
                # add all of the includes if it is in the topic
                for topic in include:
                    if topic in bag_topics:
                        topics_to_use.add(topic)
            except:
                warnings.warn('Error in topic selection Using All!')
                topics_to_use = set()
                for t in bag_topics:
                    topics_to_use.add(t)

        to_remove = set()
        # now exclude the exclusions
        if exclude is None:
            pass
        elif isinstance(exclude, six.string_types):
            check = re.compile(exclude)
            for t in list(topics_to_use):
                if re.match(check, t) is not None:
                    to_remove.add(t)
        else:
            for remove in exclude:
                if remove in exclude:
                    to_remove.add(remove)

        # final set stuff to get topics to use
        topics_to_use = topics_to_use - to_remove
        # return a list for the results
        return list(topics_to_use)

    @classmethod
    def get_base_fields(self, msg, prefix='', parse_header=True):
        """
        function to get the full names of every message field in the message
        planning.scenario_planning.trajectory_points[0].point.pose.position.x
        """
        slots = msg.__slots__
        msg_value = dict()
        msg_arr_list = msg.get_fields_and_field_types().keys()
        if prefix:
            prefix += '.'
        for i, m in enumerate(msg_arr_list):
            slot_msg = getattr(msg, slots[i])
            if not parse_header and m == 'header':
                continue

            if isinstance(slot_msg, list):
                for j, s in enumerate(slot_msg):
                    if hasattr(s, '__slots__'):
                        sub_msg_value = self.get_base_fields(
                            s, prefix=prefix + m + '[%d]' % j,
                            parse_header=parse_header,
                        )
                        msg_value.update(sub_msg_value)
                    else:
                        msg_value[prefix + s] = s
            elif hasattr(slot_msg, '__slots__'):
                sub_msg_value = self.get_base_fields(
                    slot_msg, prefix=prefix + m,
                    parse_header=parse_header,
                )
                msg_value.update(sub_msg_value)
            else:
                msg_value[prefix + m] = slot_msg
        return msg_value

if __name__ == '__main__':
    # Ros2bag.dataframe("home/Workspace/autotest/rosbag2_2021_03_03-15_57_27/02.bag/02.bag_0.db3")
    TOPICS_LIST = ["/planning/scenario_planning/trajectory",
                   "/vehicle/status/twist",
                   "/vehicle/status/velocity",
                   "/current_pose"
                   ]
    bag= Ros2bag("/home/autotest/Workspace/autotest/bags/aw4/planning/gt_01/gteg_01")
    # cc = bag.dataframe(include='/vehicle/status/velocity')
    # print(cc)
    count = 0
    for i in TOPICS_LIST:
        cc = bag.dataframe(include=i)
        cc.to_excel(str(count)+".xlsx")
        count = count+1

    print(cc)
