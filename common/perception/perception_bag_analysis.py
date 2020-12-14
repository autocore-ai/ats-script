# -*- coding:utf8 -*-
"""
1. Number of obstacles UUID_ The detection rate was UUID_ Count / T, give the number of UUIDs detected per second, and draw a line graph
2. The correct semantic, the type and number of semantics, the percentage of correct semantics, the semantic pie chart, the line chart of semantics per second, and the broken line chart with different semantics
3. Position of obstacles, take x, Y values, form a two-dimensional list in chronological order, and draw a broken line diagram
List and draw the angle of the obstacle according to the time order
5. The linear velocity line of obstacles, only the values of X and y are taken. The x-axis data forms a list according to the time sequence and draws a broken line graph. The y-axis data forms a list according to the time order, and draws the broken line diagram, and gives the average speed of X and Y
6. The second value of prediction information of each point is taken out from the prediction data of obstacles. The second value predicts the position and direction of the current obstacle after 0.5s. Get the list like the second and third, and then draw a line chart comparing with 3 and 4. The starting point of X axis is 0.5s later than that of 3 and 4.
In the later stage, Euclidean distance and cosine similarity processing can be done for the predicted data and the data of 3 and 4, and the standard deviation can be calculated for data reference
7. The shape of the obstacle, the shape type and corresponding number, the percentage of the correct type, and the shape pie chart. The list of X and Y is formed in chronological order, and a broken line chart is drawn. Calculate the standard deviation of X and Y respectively
"""

import rosbag
import math
import os
import numpy as np
import matplotlib.path as mpath
import matplotlib.pyplot as plt
from common.utils.generate_graph import generate_bar, generate_bar_rows, generate_trace_rows, generate_line_rows, generate_pre_path_row
from common.utils.calculate import cal_std, cal_euc_distance
import logging
logger = logging.getLogger()

SEMANTIC = {
    0: 'UNKNOWN',
    1: 'CAR',
    2: 'TRUCK',
    3: 'BUS',
    4: 'BICYCLE',
    5: 'MOTORBIKE',
    6: 'PEDESTRIAN',
    7: 'ANIMAL',
}

SHAPE = {
    0: 'BOUNDING_BOX',
    1: 'CYLINDER',
    2: 'POLYGON'
}


class Analysis:
    def __init__(self, b_path):
        self.bag_path = b_path
        self._sect_len = 0
        self.bag = rosbag.Bag(self.bag_path)
        self.msg_count = self.bag.get_message_count()
        start_time = self.bag.get_start_time()
        end_time = self.bag.get_end_time()
        # self.time_list = np.linspace(start_time, end_time, num=1).data
        self.time_list = []
        self.time_split(start_time, end_time)  # Slice the time
        self.data_dict = {}  # key: uuid, value: object's sum data

    def analysis(self):
        """
        return dict:
        {
            'uuid_0': {
                        'uuid_sec': [2, 3, 4, 5],  # uuid count per second for checking out object percent
                        'semantic': {'CAR': [1, 2, 3, 1], 'BUS': [1, 2, 3, 1] },  # semantic dict, key: semantic, value: count per second
                        'position': {'t1': (x, y), 't2': (x, y)},   # t: x and y's position
                        'orientation': {t1: yaw1, t2: yaw2} # t: yaw
                        'line': {'t1: (x, y), 't2': (x, y)},   # t: x and y's line speed
                        'prediction_paths': {t1: [(x11, y11, yaw11), (x12, y12, yaw12)], t2: [(x21, y21, yaw21), (x22, y22, yaw22)]},   # position and orientation of prediction
                        'shape': {type_0: {sect: [1, 2, 3], t_size: {t: (x, y)}}, type_1: {sect: [1, 2, 3], t_size: {t: (x, y)}}},  # shape's type and count per second
                        },
        'uuid_1': {......},
        ......
        }

        """
        ans_list = []
        for idx, (topic, msg, mt) in enumerate(self.bag.read_messages()):
            if not msg.objects:
                continue
            sect = self.time_section(mt.to_sec())  # 看当前时间所处的时间段位
            for obj in msg.objects:
                ans_list.append(self.obj_deal(obj, sect, mt.to_sec()))
        return True

    def time_split(self, start, end):
        """
        The start time and end time are divided with an interval of 1 s
        """
        num = end-start
        self._sect_len = math.ceil(num)
        for i in range(self._sect_len):
            self.time_list.append(end - i)

    def time_section(self, t):
        """
        Judge where the current time is in
        Time divided in seconds, with segments starting from 0
        """
        l = len(self.time_list) - 1
        sect = 0
        for i, val in enumerate(self.time_list):
            if t > val:
                sect = l-i
                break
        return sect

    def obj_deal(self, obj, sect, mt):
        """
        obj: message obj
        sect: message's part
        mt: message obj's time
        message deal data struct:
        'uuid_0': {
                    'uuid_sec': [2, 3, 4, 5],  # uuid count per second for checking out object percent
                    'semantic': {'CAR': [1, 2, 3, 1], 'BUS': [1, 2, 3, 1] },  # semantic dict, key: semantic, value: count per second
                    'position': {'t1': (x, y), 't2': (x, y)},   # t: x and y's position
                    'orientation': {t1: yaw1, t2: yaw2} # t: yaw
                    'line': {'t1: (x, y), 't2': (x, y)},   # t: x and y's line speed
                    'prediction_paths': {t1: [(x11, y11, yaw11), (x12, y12, yaw12)], t2: [(x21, y21, yaw21), (x22, y22, yaw22)]},   # position and orientation of prediction
                    'shape': {type_0: {sect: [1, 2, 3], t_size: {t: (x, y)}}, type_1: {sect: [1, 2, 3], t_size: {t: (x, y)}}},  # shape's type and count per second
                    }
        """
        uuid = obj.id.uuid
        if uuid not in self.data_dict:  # init data struct
            data_struct = {'uuid_sec': [0] * self._sect_len,
                           'semantic': {},
                           'position': {},
                           'orientation': {},
                           'line': {},
                           'prediction_paths': {},
                           'shape': {}
                           }

            # semantic init struct
            semantic = SEMANTIC[obj.semantic.type]
            semantic_dict = {semantic: [0] * self._sect_len}

            # shape init
            shape = SHAPE[obj.shape.type]
            # shape_dict = {shape: {'sect': [0] * self._sect_len, 'x': [], 'y': []}}
            shape_dict = {shape: {'sect': [0] * self._sect_len, 't_size': {}}}

        else:
            # Handling the existing UUID
            data_struct = self.data_dict[uuid]

            # semantic 处理 'semantic': {'type_1': [1, 2, 3, 1], 'type_2': [1, 2, 3, 1] },  # uuid对应的语义，以及每秒出现的次数
            semantic = SEMANTIC[obj.semantic.type]
            semantic_dict = data_struct['semantic']
            if semantic not in semantic_dict:
                semantic_dict[semantic] = [0] * self._sect_len

            # shape
            shape = SHAPE[obj.shape.type]
            shape_dict = data_struct['shape']
            if shape not in shape_dict:
                shape_dict[shape] = {'sect': [0] * self._sect_len, 't_size': {}}

        # uuid
        data_struct['uuid_sec'][sect] += 1

        # semantic
        semantic_dict[semantic][sect] += 1
        data_struct['semantic'] = semantic_dict

        # position
        data_struct['position'][mt] = (obj.state.pose_covariance.pose.position.x, obj.state.pose_covariance.pose.position.y)
        # data_struct['position'].append((obj.state.pose_covariance.pose.position.x, obj.state.pose_covariance.pose.position.y))

        # orientation
        data_struct['orientation'][mt] = self.to_euler_angles(obj.state.pose_covariance.pose.orientation)

        # line
        data_struct['line'][mt] = (obj.state.twist_covariance.twist.linear.x, obj.state.twist_covariance.twist.linear.y)
        # data_struct['line']['x'].append(obj.state.twist_covariance.twist.linear.x)
        # data_struct['line']['y'].append(obj.state.twist_covariance.twist.linear.y)

        data_struct['prediction_paths'][mt] = []
        for i, path in enumerate(obj.state.predicted_paths[0].path):
            path_obj = path.pose
            data_struct['prediction_paths'][mt].append((path_obj.pose.position.x, path_obj.pose.position.y, self.to_euler_angles(path_obj.pose.orientation)))

        shape_dict[shape]['sect'][sect] += 1
        shape_dict[shape]['t_size'][mt] = (obj.shape.dimensions.x, obj.shape.dimensions.y)
        data_struct['shape'] = shape_dict

        self.data_dict[uuid] = data_struct

    def to_euler_angles(self, orientation):
        """w、x、y、z to euler angles"""
        # angles = {'pitch': 0.0, 'roll': 0.0, 'yaw': 0.0}
        # print(orientation)
        w = orientation.w
        x = orientation.x
        y = orientation.y
        z = orientation.z
        # r = math.atan2(2 * (w * x + y * z), 1 - 2 * (x * x + y * y))
        # p = math.asin(2 * (w * y - z * z))
        y = math.atan2(2 * (w * z + x * y), 1 - 2 * (z * z + y * y))
        # angles['roll'] = r * 180 / math.pi
        # angles['pitch'] = p * 180 / math.pi
        # angles['yaw'] = y * 180 / math.pi
        return y * 180 / math.pi

    def sum_data(self, cat_type=1):
        """
        At present, it only supports semantic classification
        Summarize the analyzed data
        1. UUID is the total number of UUIDs detected per second, regardless of obstacles
        2. Semantics are summarized as the number of semantics per second
        3. Position the obstacle position array obtained according to the trajectory diagram. Manual operation is required here to classify the obstacles, objects, shapes and positions. The specific values need to be passed into cat_ Type = 1, shape, 2, position, currently only 1 is supported
        4. Orientation will not be decomposed for the time being
        5. Line divide the speed into arrays according to the classification (the same as 3)
        6. Shape summarizes the shape type and size corresponding to each semantics per second
        'uuid_0': {
                        'uuid_sec': [2, 3, 4, 5],  # uuid count per second for checking out object percent
                        'semantic': {'CAR': [1, 2, 3, 1], 'BUS': [1, 2, 3, 1] },  # semantic dict, key: semantic, value: count per second
                        'position': {'t1': (x, y), 't2': (x, y)},   # t: x and y's position
                        'orientation': {t1: yaw1, t2: yaw2} # t: yaw
                        'line': {'t1: (x, y), 't2': (x, y)},   # t: x and y's line speed
                        'prediction_paths': {t1: [(x11, y11, yaw11), (x12, y12, yaw12)], t2: [(x21, y21, yaw21), (x22, y22, yaw22)]},   # position and orientation of prediction
                        'shape': {type_0: {sect: [1, 2, 3], t_size: {t: (x, y)}}, type_1: {sect: [1, 2, 3], t_size: {t: (x, y)}}},  # shape's type and count per second
                        },
        return data_struct
        {
            'uuid': np.array([0]*self._sect_len),  Sum up the number of all UUIDs detected per second, regardless of obstacles
            'semantic': {},  Sum up to the number of each semantic per second
            'position': {'CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}},
            'orientation': {t1: yaw1, t2: yaw2} # t: yaw
            'line':{CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}},
            'shape': {CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}}
        }
        """
        if cat_type == 1:  # according to semantic
            ret_dict = {'uuid': np.array([0]*self._sect_len), 'semantic': {}, 'position': {}, 'line': {}, 'shape': {},
                        'orientation': {}, 'prediction_paths': {}}
        else:
            ret_dict = {}

        for uuid, data in self.data_dict.items():
            ret_dict['uuid'] += np.array(data['uuid_sec'])
            # sum data by semantic
            for sem, sec_data in data['semantic'].items():
                if sem in ret_dict['semantic']:
                    ret_dict['semantic'][sem] += np.array(sec_data)
                    ret_dict['position'][sem].update(data['position'])
                    ret_dict['orientation'][sem].update(data['orientation'])
                    ret_dict['line'][sem].update(data['line'])
                    ret_dict['prediction_paths'][sem].update(data['prediction_paths'])
                    for shape, shape_data in data['shape'].items():
                        ret_dict['shape'][sem].update(data['shape'][shape]['t_size'])

                else:
                    ret_dict['semantic'][sem] = np.array(sec_data)
                    # print(data_dict['position'][sem])
                    ret_dict['position'][sem] = data['position']
                    ret_dict['orientation'][sem] = data['orientation']
                    ret_dict['line'][sem] = data['line']
                    ret_dict['prediction_paths'][sem] = data['prediction_paths']

                    ret_dict['shape'][sem] = {}
                    for shape, shape_data in data['shape'].items():
                        ret_dict['shape'][sem].update(data['shape'][shape]['t_size'])

        return ret_dict

    def show_graph(self):
        """
        1. Number of obstacles UUID_ The detection rate was UUID_ Count / T, give the number of UUIDs detected per second, and draw a line graph
        2. The correct semantic, the type and number of semantics, the percentage of correct semantics, the semantic pie chart, the line chart of semantics per second, and the broken line chart with different semantics
        3. Position of obstacles, take x, Y values, form a two-dimensional list in chronological order, and draw a broken line diagram
        List and draw the angle of the obstacle according to the time order
        5. The linear velocity line of obstacles, only the values of X and y are taken. The x-axis data forms a list according to the time sequence and draws a broken line graph. The y-axis data forms a list according to the time order, and draws the broken line diagram, and gives the average speed of X and Y
        6. The second value of prediction information of each point is taken out from the prediction data of obstacles. The second value predicts the position and direction of the current obstacle after 0.5s. Get the list like the second and third, and then draw a line chart comparing with 3 and 4. The starting point of X axis is 0.5s later than that of 3 and 4.
            In the later stage, Euclidean distance and cosine similarity processing can be done for the predicted data and the data of 3 and 4, and the standard deviation can be calculated for data reference
        7. The shape of the obstacle, the shape type and corresponding number, the percentage of the correct type, and the shape pie chart. The list of X and Y is formed in chronological order, and a broken line chart is drawn. Calculate the standard deviation of X and Y respectively
        """
        graph_path_dir = self.bag_path.split('.bag')[0]
        os.makedirs(graph_path_dir, exist_ok=True)

        # analysis data and make pic
        t_x = range(1, self._sect_len + 1)
        fig_line, ax_line = plt.subplots(figsize=(10, 5))
        uuid_line_path = '{}/uuid.png'.format(graph_path_dir)

        fig_se, (ax0_se, ax1_se) = plt.subplots(2, 1, figsize=(10, 16))
        semantic_count_dict = {}   # semantic sum
        semantic_path = '{}/semantic.png'.format(graph_path_dir)

        # position trace
        fig_position, ax_position = plt.subplots(figsize=(10, 5))
        position_path = '{}/position.png'.format(graph_path_dir)

        # twist line
        fig_t, (axx_t, axy_t) = plt.subplots(2, 1, figsize=(10, 16))
        twist_path = '{}/twist.png'.format(graph_path_dir)

        # shape
        fig_shape, (ax_sec, ax_x, ax_y) = plt.subplots(3, 1, figsize=(10, 24))
        shape_path = '{}/shape.png'.format(graph_path_dir)

        for uuid, data in self.data_dict.items():
            label_semantic_list = []  # semantic
            for s_type, sec_data in data['semantic'].items():
                ax0_se.plot(range(1, self._sect_len + 1), sec_data, label=s_type)
                if s_type in semantic_count_dict:
                    semantic_count_dict[s_type] += sum(data['semantic'][s_type])
                else:
                    semantic_count_dict[s_type] = sum(data['semantic'][s_type])
                if s_type not in label_semantic_list:
                    label_semantic_list.append(s_type)

            # label
            label_semantic = '_'.join(label_semantic_list)

            uuid_sec_list = data['uuid_sec']
            # uuid
            ax_line.plot(t_x, uuid_sec_list, label='{}_{}'.format(uuid, label_semantic))

            # position trace
            Path = mpath.Path
            path_data = []
            c_f = 0
            # make path
            for t in sorted(data['position'].keys()):
                x = data['position'][t][0]
                y = data['position'][t][1]
                if c_f == 0:
                    path_data.append((Path.MOVETO, (x, y)))
                elif c_f == len(data['position']):
                    path_data.append((Path.CLOSEPOLY, (x, y)))
                elif c_f == 2:
                    path_data.append((Path.LINETO, (x, y)))
                else:
                    path_data.append((Path.CURVE4, (x, y)))
                c_f += 1

            # print(path_data)
            codes, verts = zip(*path_data)
            path = mpath.Path(verts, codes)
            # patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
            # ax_position.add_patch(patch)
            x, y = zip(*path.vertices)
            ax_position.plot(x, y, marker=mpath.Path(verts, codes), label=label_semantic)
            ax_position.text(x[-1], y[-1], label_semantic)

            # speed
            twist_x = [data['line'][item][0] for item in sorted(data['line'].keys())]
            twist_y = [data['line'][item][1] for item in sorted(data['line'].keys())]
            # twist_y = data['line']['y']
            line_x = [i for i in range(0, len(twist_x))]
            axx_t.plot(line_x, twist_x, label=label_semantic)
            axy_t.plot(line_x, twist_y, label=label_semantic)
            axx_t.text(line_x[-1], twist_x[-1], label_semantic)
            axy_t.text(line_x[-1], twist_y[-1], label_semantic)

            # ax_sec, ax_x, ax_y
            for shape, dt in data['shape'].items():
                ax_sec.plot(t_x, dt['sect'], label='{}_{}'.format(shape, label_semantic))
                x_size = [size[0] for t, size in dt['t_size'].items()]
                y_size = [size[1] for t, size in dt['t_size'].items()]
                x_v = len(x_size)
                ax_x.plot([i for i in range(x_v)], x_size, label='{}_{}'.format(shape, label_semantic))
                ax_y.plot([i for i in range(x_v)], y_size, label='{}_{}'.format(shape, label_semantic))

        ax_line.set_title('uuid sec graph')
        ax_line.legend()
        fig_line.savefig(uuid_line_path, dpi=600)

        labels = semantic_count_dict.keys()
        semantic_sum = sum(semantic_count_dict.values())
        semantic_per_dict = {key: val/semantic_sum*0.1*100 for key, val in semantic_count_dict.items()}
        sizes = semantic_per_dict.values()
        explode = [0.01] * len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
        ax1_se.pie(sizes, explode=explode, labels=labels, autopct='%1.01f%%',
                   shadow=False, startangle=90)
        ax1_se.axis('equal')
        ax1_se.set_title('semantic pie graph')
        ax1_se.legend()
        ax0_se.axis('equal')
        ax0_se.legend()
        ax0_se.set_title('semantic sec graph')
        fig_se.savefig(semantic_path, dpi=600)

        ax_position.grid()
        ax_position.axis('equal')
        ax_position.set_title('position line graph')
        ax_position.legend()
        fig_position.savefig(position_path, dpi=600)

        axx_t.set_title('twist line x graph')
        axx_t.legend()
        axy_t.set_title('twist line y graph')
        axy_t.legend()
        fig_t.savefig(twist_path, dpi=600)

        ax_sec.set_title('shape second count graph')
        ax_x.set_title('shape size x')
        ax_y.set_title('shape size y')
        ax_sec.legend()
        ax_x.legend()
        ax_y.legend()

        fig_shape.savefig(shape_path, dpi=600)


def compare_uuid(uuid_exp, uuid_rel, save_path, step=2):
    """
    Compare the UUID of two bags and generate pictures
    uuid_ Exp: [2,4], expected UUIDs per second
    uuid_ Rel: [3, 5], the actual number of UUIDs per second
    generate uuid compare graph
    Return bool, standard deviation, description information
    """
    # cal std
    r_bool, std_uuid, diff_list, msg = cal_std(uuid_exp, uuid_rel, 2)
    if not r_bool:
        return False, 0, msg
    logger.info('expect and real uuid diff: {}'.format(std_uuid))

    # per count
    data_list = [{'data': uuid_exp, 'label': 'expect uuid, sum: {}'.format(sum(uuid_exp))},
                 {'data': uuid_rel, 'label': 'real uuid, sum: {}'.format(sum(uuid_rel))}]
    r_bool, msg = generate_bar(data_list, save_path, y_label='Count',
                               title='Expect and real uuid count per second, std: {:<8.2f}'.format(std_uuid))
    if not r_bool:
        logger.error(msg)
        return False, 0, msg
    return True, std_uuid, ''


def compare_semantic(sem_dict_exp, sem_dict_rel, save_path):
    """
    Compare the semantic of the two bags and generate images
    Sum up to the number of each semantic per second
    sem_ dict_ exp: {type_ 1: [1,1,1], type_ 1: [2,2,2]}, the expected number of semantics per second
    sem_ dict_ rel: {type_ 1: [1,1,1], type_ 1: [2,2,2]}, the actual number of semantics per second
    Return bool, standard deviation, description information
    """
    exp_category = sem_dict_exp.keys()
    real_category = sem_dict_rel.keys()
    if not sorted(exp_category) == sorted(real_category):
        return False, 'semantic category is not equal, expect val: {}, real val: {}'.format(exp_category, real_category)

    sem_std_dict = {key: 0 for key in exp_category}
    # The standard deviation of each kind is calculated in a cycle, and the bar chart of each kind of semantic is drawn
    sem_list = []  # Store the drawing information corresponding to each semantic
    for key, value in sem_dict_exp.items():
        r_bool, std, diff_list, msg = cal_std(value, sem_dict_rel[key], 1)
        if not r_bool:
            return False, msg
        sem_std_dict[key] = std
        sem_list.append({'data': {'expect semantic': value, 'real semantic': sem_dict_rel[key]}, 'x_label': 'Second',
                         'y_label': 'Count per second', 'title': 'Semantic: {} expect and real, std: {:<8.2f}'.format(key, std)})

    # Draw a bar chart
    r_bool, msg = generate_bar_rows(sem_list, save_path)
    if not r_bool:
        logger.error(msg)
        return False, msg
    return True, sem_std_dict


def compare_position(position_dict_exp, position_dict_real, save_path, max_step=5):
    """
    The position of the two bags is compared and the trajectory is generated
    The keys of the two must be equal
    position_ dict_ Exp: {car ': {T1: (x, y), T2: (x, y)},'bus': {T1: (x, y), T2: (x, y)}, # position values in X and Y directions
    position_ dict_ Real: {car ': {T1: (x, y), T2: (x, y)},'bus': {T1: (x, y), T2: (x, y)}, # position values in X and Y directions
    max_ Step: the number of elements with the most difference between the two groups of data
        0. Judge the number of two location data, and the difference should not be too large
        1. Calculate the Euclidean distance of the corresponding time point and return to list
        2. Calculate the standard deviation of the above list
        3. Draw the trajectory of the two
    Return bool, position distance difference list, standard deviation, description information
    """
    exp_semantic_list = position_dict_exp.keys()
    real_semantic_list = position_dict_real.keys()
    if sorted(exp_semantic_list) != sorted(real_semantic_list):
        return False, 'expect position\'s semantic is not equal real\'s semantic: expect semantic {}, real semantic {}'.format(exp_semantic_list, real_semantic_list)

    ret_dict = {semantic: {} for semantic in exp_semantic_list}
    data_list = []
    for semantic, exp_position_dict in position_dict_exp.items():
        real_position_dict = position_dict_real[semantic]

        # 0. Judge the number of two location data, can not be too big difference
        exp_len = len(exp_position_dict.keys())
        real_len = len(real_position_dict.keys())
        max_len = exp_len + max_step
        min_len = exp_len - max_step
        if real_len not in range(min_len, max_len+1):
            logger.info('shape: {}\nposition elements count is not in normal range\nexpect len: {} - {}, real len: {}'.format(semantic, min_len, max_len, real_len))
            return False, 'shape: {},position elements count is not in normal range, expect len: {} - {}, real len: {}'.format(semantic, min_len, max_len, real_len)

        # 1. Calculate the Euclidean distance of the corresponding time point and return to list
        exp_data_list = [exp_position_dict[t] for t in sorted(exp_position_dict.keys())]
        real_data_list = [real_position_dict[t] for t in sorted(real_position_dict.keys())]
        if exp_len > real_len:
            exp_data_list = exp_data_list[:real_len]
        elif exp_len < real_len:
            real_data_list = real_data_list[:exp_len]
        r_bool, ret_list = cal_euc_distance(exp_data_list, real_data_list)
        if not r_bool:
            logger.error('cal euc distance error msg: {}'.format(ret_list))
            return False, ret_list

        ret_dict[semantic]['distance'] = ret_list  # Distance under the same semantic

        # 2. cal std
        std = np.std(ret_list)

        ret_dict[semantic]['std'] = std

        # trace data
        data_list.append({'trace_title': '{} Trace, std: {:<8.2f}'.format(semantic, std),
                          'trace_dict': {'{}_exp'.format(semantic): exp_data_list, '{}_real'.format(semantic): real_data_list},
                          })
    # 3. draw two trace
    r_bool, msg = generate_trace_rows(data_list, save_path)

    if not r_bool:
        logger.error('generate trace rows failed: {}'.format(msg))
        return False, msg
    return True, ret_dict


def compare_orientation(ori_dict_expt, ori_dict_real, save_path, max_step=5):
    """
    compare orientation
    'orientation': {'CAR': {1602578285.9338055: -175.59981964547225}}}
    ori_dict_expt and ori_dict_real: key -> semantic, value->t:yaw
    save_path: orientation graph save path
    max_step: value list max step
    return: bool, dict->{'CAR': {yaw_diff: [], std: 1}}
    """
    # semantic compare
    exp_ori_list = ori_dict_expt.keys()
    real_ori_list = ori_dict_real.keys()
    if sorted(exp_ori_list) != sorted(real_ori_list):
        return False, 'expect orientation\'s semantic is not equal real\'s semantic: expect semantic {}, real semantic {}'.format(
            exp_ori_list, real_ori_list)

    # get yaw diff and std
    ret_dict = {semantic: {'yaw_diff': [], 'std': 0} for semantic in exp_ori_list}
    data_list = []  # for graph
    for semantic, exp_ori_dict in ori_dict_expt.items():
        real_ori_dict = ori_dict_real[semantic]

        # 0. semantic's data length compare
        exp_len = len(exp_ori_dict.keys())
        real_len = len(real_ori_dict.keys())
        max_len = exp_len + max_step
        min_len = exp_len - max_step
        if real_len not in range(min_len, max_len + 1):
            logger.error('semantic: {}\norientation elements count is not in normal range\n '
                         'expect len: {} - {}, real len: {}'.format(semantic, min_len, max_len, real_len))
            return False, 'semantic: {} orientation elements count is not in normal range expect len: {} - {}, real len: {}'.format(semantic, min_len, max_len, real_len)

        # 1. Calculate expect orientation the difference with real orientation
        exp_data_list = [exp_ori_dict[t] for t in sorted(exp_ori_dict.keys())]
        real_data_list = [real_ori_dict[t] for t in sorted(real_ori_dict.keys())]
        if exp_len > real_len:
            exp_data_list = exp_data_list[:real_len]
        elif exp_len < real_len:
            real_data_list = real_data_list[:exp_len]
        r_bool, ret_list = cal_euc_distance(exp_data_list, real_data_list)
        if not r_bool:
            return False, ret_list

        # 2. cal std
        ret_dict[semantic]['yaw_diff'] = ret_list
        std = np.std(ret_list)
        ret_dict[semantic]['std'] = std

        data_list.append(
            (
                {
                    'title': '{}_Orientation, std: {:<8.2f}'.format(semantic, std),
                    'data': {'ori_exp': exp_data_list, 'ori_real_x': real_data_list, 'ori_diff_x': ret_list}
                }
            )
        )

        # Draw the bottom shape X and Y and the three line graph of the difference
        r_bool, msg = generate_line_rows(data_list, save_path)

        if not r_bool:
            logger.error(msg)
            return False, msg

    return True, ret_dict


def compare_line(line_dict_exp, line_dict_real, save_path, max_step=5):
    """
    Compare linear velocity
    'line': {car ': {T1: (x, y), T2: (x, y)},'bus': {T1: (x, y), T2: (x, y)}. According to the classification (same as 3), the speed is divided into arrays
    The keys of the two must be equal
    line_dict_exp: {car ': {T1: (x, y), T2: (x, y)},'bus': {T1: (x, y), T2: (x, y)}, # position values in X and Y directions
    line_dict_real: {car ': {T1: (x, y), T2: (x, y)},'bus': {T1: (x, y), T2: (x, y)}, # position values in X and Y directions
    max_step: the number of elements with the most difference between the two groups of data
        0. Judge the number of two linear velocity data, and the difference should not be too large
        1. Calculate the Euclidean distance of the line velocity at the corresponding time point and return to list
        2. Calculate the standard deviation of the above list
        3. Draw the trajectory of the two
    Return bool, linear velocity, distance difference, list, standard deviation, description information
    """
    exp_semantic_list = line_dict_exp.keys()
    real_semantic_list = line_dict_real.keys()
    if sorted(exp_semantic_list) != sorted(real_semantic_list):
        return False, 'expect line\'s semantic is not equal real\'s semantic: expect semantic {}, real semantic {}'.format(
            exp_semantic_list, real_semantic_list)

    ret_dict = {semantic: {} for semantic in exp_semantic_list}
    data_list = []
    for semantic, exp_line_dict in line_dict_exp.items():
        real_line_dict = line_dict_real[semantic]

        exp_len = len(exp_line_dict.keys())
        real_len = len(real_line_dict.keys())
        max_len = exp_len + max_step
        min_len = exp_len - max_step
        if real_len not in range(min_len, max_len + 1):
            return False, 'shape: {}\nline elements count is not in normal range\nexpect len: {} - {}, real len: {}'.format(
                semantic, min_len, max_len, real_len)

        # 1. Calculate the Euclidean distance of the corresponding time point and return to list
        exp_data_list = [exp_line_dict[t] for t in sorted(exp_line_dict.keys())]
        real_data_list = [real_line_dict[t] for t in sorted(real_line_dict.keys())]
        if exp_len > real_len:
            exp_data_list = exp_data_list[:real_len]
        elif exp_len < real_len:
            real_data_list = real_data_list[:exp_len]
        r_bool, ret_list = cal_euc_distance(exp_data_list, real_data_list)
        if not r_bool:
            return False, ret_list

        ret_dict[semantic]['distance'] = ret_list

        # 2. cal std
        std = np.std(ret_list)
        ret_dict[semantic]['std'] = std

        # cal x, y
        exp_data_list_x = [d[0] for d in exp_data_list]
        exp_data_list_y = [d[1] for d in exp_data_list]
        real_data_list_x = [d[0] for d in real_data_list]
        real_data_list_y = [d[1] for d in real_data_list]
        r_bool, ret_list_x = cal_euc_distance(exp_data_list_x, real_data_list_x)
        if not r_bool:
            return False, ret_list_x
        ret_dict[semantic]['distance_x'] = ret_list_x

        r_bool, ret_list_y = cal_euc_distance(exp_data_list_y, real_data_list_y)
        if not r_bool:
            return False, ret_list_y
        ret_dict[semantic]['distance_y'] = ret_list_y
        # cal std
        std_x = np.std(ret_list_x)
        ret_dict[semantic]['std_x'] = std_x
        std_y = np.std(ret_list_y)
        ret_dict[semantic]['std_y'] = std_y

        data_list.append((
            {'title': '{}_X Line Speed, std: {:<8.2f}'.format(semantic, std_x),
             'data': {'{}_exp_x'.format(semantic): exp_data_list_x, '{}_real_x'.format(semantic): real_data_list_x,
                      '{}_distance_x'.format(semantic): ret_list_x}
             },
            {'title': '{}_Y Line Speed, std: {:<8.2f}'.format(semantic, std_y),
             'data': {'{}_exp_y'.format(semantic): exp_data_list_y, '{}_real_y'.format(semantic): real_data_list_y,
                      '{}_distance_y'.format(semantic): ret_list_y}
             },
        ))

    # 3. make line graph
    r_bool, msg = generate_line_rows(data_list, save_path)

    if not r_bool:
        logger.error(msg)
        return False, msg
    return True, ret_dict


def compare_prediction_paths(pre_dict_exp, pre_dict_real, save_path, max_step=5):
    """
    compare prediction
    compare 2th, 3th point of prediction path
    {'CAR': {t1: [(x11, y11, yaw11), (x12, y12, yaw12)], t2: [(x21, y21, yaw21), (x22, y22, yaw22)]}}
    """
    # compare semantic
    exp_pre_list = pre_dict_exp.keys()
    real_pre_list = pre_dict_real.keys()
    if sorted(exp_pre_list) != sorted(real_pre_list):
        return False, 'expect prediction_paths\'s semantic is not equal real\'s semantic: expect prediction_paths semantic {},' \
                      ' real prediction_paths semantic {}'.format(exp_pre_list, real_pre_list)

    # compare  2th, 3th point of prediction path
    graph_data = {}  # for graph data
    ret_dict = {}
    for semantic, exp_pre_dict in pre_dict_exp.items():
        real_pre_dict = pre_dict_real[semantic]

        # 0. compare same semantic , prediction element count
        exp_len = len(exp_pre_dict.keys())
        real_len = len(real_pre_dict.keys())
        max_len = exp_len + max_step
        min_len = exp_len - max_step
        if real_len not in range(min_len, max_len + 1):
            return False, 'semantic: {}\n' \
                          'prediction paths elements count is not in normal range\n' \
                          'expect len: {} - {}, real len: {}'.format(
                semantic, min_len, max_len, real_len)

        # get same count element
        exp_data_list = [exp_pre_dict[t] for t in sorted(exp_pre_dict.keys())]
        real_data_list = [real_pre_dict[t] for t in sorted(real_pre_dict.keys())]
        if exp_len > real_len:
            exp_data_list = exp_data_list[:real_len]
        elif exp_len < real_len:
            real_data_list = real_data_list[:exp_len]

        # 1. get 2th and 3th element
        paths_exp_2th, paths_exp_3th, paths_real_2th, paths_real_3th = [], [], [], []
        for i, paths_list in enumerate(exp_data_list):
            if len(paths_list) < 2:
                continue
            paths_exp_2th.append(paths_list[1])
            paths_exp_3th.append(paths_list[2])
            paths_real_2th.append(real_data_list[i][1])
            paths_real_3th.append(real_data_list[i][2])

        # 2. x,y position eul distance
        exp_2th_xy = [(data[0], data[1]) for data in paths_exp_2th]
        real_2th_xy = [(data[0], data[1]) for data in paths_real_2th]
        exp_3th_xy = [(data[0], data[1]) for data in paths_exp_3th]
        real_3th_xy = [(data[0], data[1]) for data in paths_real_3th]
        exp_2th_ori = [data[2] for data in paths_exp_2th]
        real_2th_ori = [data[2] for data in paths_real_2th]
        exp_3th_ori = [data[2] for data in paths_exp_3th]
        real_3th_ori = [data[2] for data in paths_real_3th]
        r_boo, paths_diff_2th_xy = cal_euc_distance(exp_2th_xy, real_2th_xy)  # line
        r_boo, paths_diff_3th_xy = cal_euc_distance(exp_3th_xy, real_3th_xy)  # line
        r_boo, paths_diff_2th_ori = cal_euc_distance(exp_2th_ori, real_2th_ori)
        r_boo, paths_diff_3th_ori = cal_euc_distance(exp_3th_ori, real_3th_ori)

        # 3. cal xy std
        paths_std_2th_xy = np.std(paths_diff_2th_xy)
        paths_std_3th_xy = np.std(paths_diff_3th_xy)
        paths_std_2th_ori = np.std(paths_diff_2th_ori)
        paths_std_3th_ori = np.std(paths_diff_3th_ori)
        ret_dict[semantic] = {'paths_eul_2th_xy': paths_diff_2th_xy, 'paths_eul_3th_xy': paths_diff_3th_xy,
                              'paths_std_2th_xy': paths_std_2th_xy, 'paths_std_3th_xy': paths_std_3th_xy,
                              'paths_eul_2th_ori': paths_diff_2th_ori, 'paths_eul_3th_ori': paths_diff_3th_ori,
                              'paths_std_2th_ori': paths_std_2th_ori, 'paths_std_3th_ori': paths_std_3th_ori,
                              }

        # logger.info('paths_std_2th_xy: {}'.format(paths_std_2th_xy))
        # make graph, 2 row, 3 col
        # the 1st row, xy trace, xy eul, ori(exp, real, diff)
        # the 2nd row, xy trace, xy eul, ori(exp, real, diff)
        graph_data_s = [
            # the 2nd pre path
            (
                # xy trace
                {
                    'title': 'The 2nd xy trace of {}\'s Prediction Path'.format(semantic),
                    'trace_dict': {'{}_xy_exp'.format(semantic): exp_2th_xy,
                                   '{}_xy_real'.format(semantic): real_2th_xy
                                   }
                 },
                # xy eul line graph
                {
                    'title': 'The 2nd xy eul of {}\'s, std: {:<8.2f}'.format(semantic, paths_std_2th_xy),
                    'line_data': {'{}_xy_eul'.format(semantic): paths_diff_2th_xy}
                },
                # ori line (exp, real, diff)
                {
                    'title': 'The 2nd orientation of {}\'s, std: {:<8.2f}'.format(semantic, paths_std_2th_ori),
                    'line_data': {'{}_ori_exp'.format(semantic): exp_2th_ori,
                                  '{}_ori_real'.format(semantic): real_2th_ori,
                                  '{}_ori_diff'.format(semantic): paths_diff_2th_ori}
                }
            ),
            # the 3rd pre path
            (
                # xy trace
                {
                    'title': 'The 3rd xy trace of {}\'s Prediction Path'.format(semantic),
                    'trace_dict': {'{}_xy_exp'.format(semantic): exp_3th_xy,
                                   '{}_xy_real'.format(semantic): real_3th_xy
                                   }
                },
                # xy eul line graph
                {
                    'title': 'The 3rd xy eul of {}\'s, std: {:<8.2f}'.format(semantic, paths_std_3th_xy),
                    'line_data': {'{}_xy_eul'.format(semantic): paths_diff_3th_xy}
                },
                # ori line (exp, real, diff)
                {
                    'title': 'The 3rd orientation of {}\'s, std: {:<8.2f}'.format(semantic, paths_std_3th_ori),
                    'line_data': {'{}_ori_exp'.format(semantic): exp_3th_ori,
                                  '{}_ori_real'.format(semantic): real_3th_ori,
                                  '{}_ori_diff'.format(semantic): paths_diff_3th_ori}
                }
            ),
        ]
        graph_data[semantic] = graph_data_s
    # make graph
    logger.debug('prediction graph data: {}'.format(graph_data))
    r_bool, msg = generate_pre_path_row(graph_data, save_path)

    if not r_bool:
        logger.error(msg)
        return False, msg
    return True, ret_dict


def compare_shape(shape_dict_exp, shape_dict_real, save_path, max_step=5):
    """
    Compare shape size
    'shape ': {car': {T1: (x, y), T2: (x, y)},'bus': {T1: (x, y), T2: (x, y)}}. According to the classification (same as 3), shape is divided into arrays
    The keys of the two must be equal
    shape_dict_exp: {car ': {T1: (x, y), T2: (x, y)},'bus': {T1: (x, y), T2: (x, y)}, # position values in X and Y directions
    shape_dict_real: {car ': {T1: (x, y), T2: (x, y)},'bus': {T1: (x, y), T2: (x, y)}, # position values in X and Y directions
    max_ Step: the number of elements with the most difference between the two groups of data
    0. Judge the number of two shape data, and the difference between left and right should not exceed max_ step
    1. Calculate the difference of different semantic shape x at corresponding time points and return to list
    2. Calculate the difference of different semantic shape y at corresponding time points and return to list
    3. Calculate the standard deviation of the list above
    4. Draw the broken line graph of X and y of each semantics
    Return bool, linear velocity, distance difference, list, standard deviation, description information
    """
    exp_semantic_list = shape_dict_exp.keys()
    real_semantic_list = shape_dict_real.keys()
    if sorted(exp_semantic_list) != sorted(real_semantic_list):
        return False, 'expect shape\'s semantic is not equal real\'s semantic: expect semantic {}, real semantic {}'.format(
            exp_semantic_list, real_semantic_list)

    ret_dict = {semantic: {'shape_diff_x': [], 'shape_diff_y': [], 'std_x': 0, 'std_y': 0} for semantic in exp_semantic_list}

    data_list = []
    for semantic, exp_shape_dict in shape_dict_exp.items():
        real_shape_dict = shape_dict_real[semantic]

        # 0. The number of two shape data should not be too different
        exp_len = len(exp_shape_dict.keys())
        real_len = len(real_shape_dict.keys())
        max_len = exp_len + max_step
        min_len = exp_len - max_step
        if real_len not in range(min_len, max_len + 1):
            return False, 'semantic: {}\nshape elements count is not in normal range\nexpect len: {} - {}, real len: {}'.format(
                semantic, min_len, max_len, real_len)

        # get same count element
        exp_data_list = [exp_shape_dict[t] for t in sorted(exp_shape_dict.keys())]
        real_data_list = [real_shape_dict[t] for t in sorted(real_shape_dict.keys())]
        if exp_len > real_len:
            exp_data_list = exp_data_list[:real_len]
        elif exp_len < real_len:
            real_data_list = real_data_list[:exp_len]
        # 1. Calculate the difference of different semantic shape x at the corresponding time point, and return to list
        shape_exp_x = [t[0] for t in exp_data_list]
        shape_real_x = [t[0] for t in real_data_list]
        # cal std
        r_bool, std, diff_list, msg = cal_std(shape_exp_x, shape_real_x)
        if not r_bool:
            return False, msg
        ret_dict[semantic]['shape_diff_x'] = diff_list
        ret_dict[semantic]['std_x'] = std

        shape_exp_y = [t[1] for t in exp_data_list]
        shape_real_y = [t[1] for t in real_data_list]
        r_bool_y, std_y, diff_list_y, msg_y = cal_std(shape_exp_y, shape_real_y)
        if not r_bool_y:
            return False, msg_y
        ret_dict[semantic]['shape_diff_y'] = diff_list_y
        ret_dict[semantic]['std_y'] = std_y
        data_list.append(
            (
                {
                    'title': '{}_Shape_X, std: {:<8.2f}'.format(semantic, std),
                    'data': {'shape_exp_x': shape_exp_x, 'shape_real_x': shape_real_x, 'shape_diff_x': diff_list}
                },
                {
                    'title': '{}_Shape_Y, std: {:<8.2f}'.format(semantic, std_y),
                    'data': {'shape_exp_y': shape_exp_y, 'shape_real_y': shape_real_y, 'shape_diff_y': diff_list_y}
                },
            )
        )

    # Draw the bottom shape X and Y and the three line graph of the difference
    r_bool, msg = generate_line_rows(data_list, save_path)

    if not r_bool:
        logger.error(msg)
        return False, msg
    return True, ret_dict


if __name__ == '__main__':
    bag_path = '/home/adlink/workspace/autotest/bags/moving_p_inner_front_2020-10-13-16-37-15/result.bag'
    ans = Analysis(bag_path)
    # print(ans.msg_count)
    ans.analysis()
    # # print(ans.data_dict)
    ret = ans.sum_data()
    print(ret['line'])

    # print(ans.sum_data()['position'])
    # for key, data in ans.sum_data().items():
    #     print(key)
        # print(data)
    #     for i, v in data.items():
    #         print(i)
    #         print(v)
    # ans.show_graph()
    # print(compare_uuid([2, 3, 7, 3], [2, 3, 7, 3], './uuid.png'))
    # print(compare_semantic({'CAR': [10, 2, 1], 'BUS': [1, 3, 4]}, {'CAR': [1, 2, 1], 'BUS': [1, 3, 4]}, './semantic.png'))
    # position_dict_exp = {'CAR': {1: (1, 1), 2: (3, 4)}, 'BUS': {1: (5, 5), 2: (5, 6)}}
    # position_dict_real = {'CAR': {1: (1, 1), 2: (3, 4)}, 'BUS': {1: (5, 5), 2: (9, 6)}}
    # print(compare_position(position_dict_exp, position_dict_real, './position.png', max_step=5))
    # shape_dict_exp = {'CAR': {1: (1, 1), 2: (3, 4)}, 'BUS': {1: (5, 5), 2: (5, 6)}}
    # shape_dict_real = {'CAR': {1: (1, 1), 2: (3, 4)}, 'BUS': {1: (5, 5), 2: (9, 6)}}
    # compare_shape(shape_dict_exp, shape_dict_real, './shape.png')
    # dd = {1602578276.902625: (4.0, 1.9012241724724643), 1602578277.003378: (4.0, 1.8611870255553147), 1602578277.0940807: (4.0, 1.8611870255553147), 1602578277.1948392: (4.0, 1.8611870255553147), 1602578277.2955287: (4.0, 1.8611870255553147), 1602578277.3963366: (4.0, 1.8611870255553147), 1602578277.4970963: (4.0, 1.8611870255553147), 1602578277.597924: (4.0, 1.8611870255553147), 1602578277.6988087: (4.0, 1.8611870255553147), 1602578278.2938702: (4.0, 1.932743545048103), 1602578278.394774: (4.0, 1.9516897201538086), 1602578278.4955842: (4.0, 1.9516897201538086), 1602578278.5964937: (4.0, 1.9516897201538086), 1602578278.6972759: (4.0, 1.9516897201538086), 1602578278.798119: (4.0, 1.9516897201538086), 1602578278.8988903: (4.0, 1.9516897201538086), 1602578278.9997034: (4.0, 1.9516897201538086), 1602578284.0017586: (4.0, 1.934133305741003), 1602578284.102574: (4.0, 1.934133305741003), 1602578284.2035189: (4.0, 1.9619409603384197), 1602578284.2945945: (4.0, 1.8460990018663195), 1602578284.3952541: (4.0, 1.8460990018663195), 1602578284.4959126: (4.0, 1.8460990018663195), 1602578284.5967326: (4.0, 1.8460990018663195), 1602578284.6975965: (4.0, 1.8460990018663195), 1602578284.798365: (4.0, 1.8460990018663195), 1602578284.8991723: (4.0, 1.8460990018663195), 1602578285.000005: (4.0, 1.703336661360954), 1602578285.1007302: (4.0, 1.8203452887695413), 1602578285.2014105: (4.0, 1.8436425336869766), 1602578285.3022187: (4.0, 1.7359323480584008), 1602578285.40313: (4.0, 1.7359323480584008), 1602578285.5038974: (4.0, 1.8282361996594914), 1602578285.5946462: (4.0, 1.8282361996594914), 1602578285.695476: (4.0, 1.8282361996594914), 1602578285.7962615: (4.0, 1.9164736154748236), 1602578285.8969688: (4.0, 1.9164736154748236), 1602578285.9976995: (4.0, 1.9164736154748236), 1602578286.0985882: (4.0, 1.9164736154748236), 1602578286.1994066: (4.0, 1.9164736154748236), 1602578286.300808: (4.0, 1.9164736154748236), 1602578286.4016323: (4.0, 1.9164736154748236)}
    # shape_real_x = [exp_shape_dict[t][0] for t in sorted(real_shape_dict.keys())]
    # exp = {'CAR': {1602578274.3316307: [(-145.10251167119918, -118.79853700831981, 0.0), (-154.71197616483303, -122.76208723686281, 0.0), (-164.32144065846688, -126.72563746540581, 0.0), (-173.93090515210073, -130.6891876939488, 0.0), (-183.5403696457346, -134.6527379224918, 0.0), (-193.14983413936844, -138.61628815103484, 0.0), (-202.7592986330023, -142.57983837957784, 0.0), (-212.3687631266361, -146.54338860812084, 0.0), (-221.97822762027, -150.50693883666383, 0.0), (-231.58769211390384, -154.47048906520683, 0.0), (-241.1971566075377, -158.43403929374983, 0.0), (-250.80662110117154, -162.39758952229283, 0.0), (-260.4160855948054, -166.36113975083583, 0.0), (-270.0255500884392, -170.32468997937883, 0.0), (-279.63501458207304, -174.28824020792183, 0.0), (-289.244479075707, -178.25179043646486, 0.0), (-298.8539435693408, -182.21534066500786, 0.0), (-308.4634080629746, -186.17889089355083, 0.0), (-318.0728725566085, -190.14244112209386, 0.0), (-327.6823370502424, -194.10599135063686, 0.0), (-337.2918015438762, -198.06954157917986, 0.0)], 1602578274.4324296: [(-147.6106181100128, -119.83588564910151, 0.0), (-158.4396488542488, -124.30854448301005, 0.0), (-169.26867959848477, -128.7812033169186, 0.0), (-180.09771034272075, -133.25386215082713, 0.0), (-190.92674108695672, -137.72652098473566, 0.0), (-201.75577183119267, -142.1991798186442, 0.0), (-212.58480257542865, -146.67183865255276, 0.0), (-223.41383331966463, -151.1444974864613, 0.0), (-234.2428640639006, -155.61715632036982, 0.0), (-245.0718948081366, -160.08981515427837, 0.0), (-255.90092555237254, -164.56247398818692, 0.0), (-266.7299562966085, -169.03513282209545, 0.0), (-277.5589870408445, -173.507791656004, 0.0), (-288.3880177850805, -177.98045048991253, 0.0), (-299.21704852931646, -182.45310932382105, 0.0), (-310.04607927355244, -186.92576815772958, 0.0), (-320.8751100177884, -191.39842699163813, 0.0), (-331.7041407620244, -195.8710858255467, 0.0), (-342.5331715062604, -200.34374465945524, 0.0), (-353.36220225049635, -204.81640349336377, 0.0), (-364.19123299473233, -209.2890623272723, 0.0)], 1602578274.533182: [(-149.79271519281488, -120.73714597648915, 0.0), (-160.62174593705086, -125.20980481039769, 0.0), (-171.45077668128684, -129.6824636443062, 0.0), (-182.2798074255228, -134.15512247821476, 0.0), (-193.10883816975877, -138.62778131212332, 0.0), (-203.93786891399475, -143.10044014603184, 0.0), (-214.76689965823073, -147.5730989799404, 0.0), (-225.5959304024667, -152.04575781384892, 0.0), (-236.42496114670269, -156.51841664775748, 0.0), (-247.25399189093866, -160.991075481666, 0.0), (-258.08302263517464, -165.46373431557453, 0.0), (-268.9120533794106, -169.93639314948308, 0.0), (-279.7410841236466, -174.40905198339163, 0.0), (-290.5701148678826, -178.88171081730016, 0.0), (-301.39914561211856, -183.35436965120869, 0.0), (-312.22817635635454, -187.82702848511724, 0.0), (-323.0572071005905, -192.2996873190258, 0.0), (-333.8862378448265, -196.77234615293432, 0.0), (-344.7152685890625, -201.24500498684284, 0.0), (-355.5442993332984, -205.7176638207514, 0.0), (-366.3733300775344, -210.19032265465995, 0.0)], 1602578274.6340094: [(-151.97644373407277, -121.63908013676605, 0.0), (-162.80547447830875, -126.1117389706746, 0.0), (-173.63450522254473, -130.58439780458315, 0.0), (-184.46353596678068, -135.05705663849167, 0.0), (-195.29256671101666, -139.5297154724002, 0.0), (-206.12159745525264, -144.00237430630875, 0.0), (-216.95062819948862, -148.4750331402173, 0.0), (-227.7796589437246, -152.94769197412583, 0.0), (-238.60868968796058, -157.42035080803436, 0.0), (-249.43772043219656, -161.8930096419429, 0.0), (-260.26675117643254, -166.36566847585146, 0.0), (-271.0957819206685, -170.83832730976, 0.0), (-281.9248126649045, -175.31098614366854, 0.0), (-292.7538434091405, -179.78364497757707, 0.0), (-303.58287415337645, -184.2563038114856, 0.0), (-314.41190489761243, -188.72896264539412, 0.0), (-325.2409356418484, -193.20162147930267, 0.0), (-336.0699663860844, -197.67428031321123, 0.0), (-346.89899713032037, -202.14693914711978, 0.0), (-357.7280278745563, -206.6195979810283, 0.0), (-368.55705861879227, -211.09225681493683, 0.0)], 1602578274.7247033: [(-153.94070046084366, -122.45036698307337, 0.0), (-164.76973120507964, -126.9230258169819, 0.0), (-175.59876194931562, -131.39568465089044, 0.0), (-186.42779269355157, -135.868343484799, 0.0), (-197.25682343778755, -140.34100231870752, 0.0), (-208.08585418202352, -144.81366115261608, 0.0), (-218.9148849262595, -149.2863199865246, 0.0), (-229.74391567049548, -153.75897882043313, 0.0), (-240.57294641473146, -158.23163765434168, 0.0), (-251.40197715896744, -162.70429648825024, 0.0), (-262.2310079032034, -167.17695532215876, 0.0), (-273.0600386474394, -171.6496141560673, 0.0), (-283.8890693916753, -176.12227298997584, 0.0), (-294.7181001359113, -180.5949318238844, 0.0), (-305.5471308801473, -185.06759065779292, 0.0), (-316.37616162438326, -189.54024949170145, 0.0), (-327.20519236861924, -194.01290832561, 0.0), (-338.0342231128552, -198.48556715951855, 0.0), (-348.8632538570912, -202.95822599342708, 0.0), (-359.6922846013272, -207.4308848273356, 0.0), (-370.52131534556315, -211.90354366124416, 0.0)], 1602578274.8254862: [(-156.12346147152067, -123.3519015291741, 0.0), (-166.95249221575665, -127.82456036308264, 0.0), (-177.78152295999263, -132.2972191969912, 0.0), (-188.6105537042286, -136.76987803089972, 0.0), (-199.4395844484646, -141.24253686480824, 0.0), (-210.26861519270054, -145.7151956987168, 0.0), (-221.09764593693652, -150.18785453262535, 0.0), (-231.9266766811725, -154.66051336653388, 0.0), (-242.75570742540847, -159.1331722004424, 0.0), (-253.58473816964445, -163.60583103435096, 0.0), (-264.4137689138804, -168.0784898682595, 0.0), (-275.2427996581164, -172.55114870216804, 0.0), (-286.07183040235236, -177.0238075360766, 0.0), (-296.90086114658834, -181.49646636998511, 0.0), (-307.7298918908243, -185.96912520389364, 0.0), (-318.5589226350603, -190.44178403780217, 0.0), (-329.3879533792963, -194.91444287171072, 0.0), (-340.21698412353226, -199.38710170561927, 0.0), (-351.04601486776824, -203.85976053952783, 0.0), (-361.8750456120042, -208.33241937343635, 0.0), (-372.7040763562402, -212.80507820734488, 0.0)], 1602578274.9263375: [(-158.30770406686798, -124.25404800656585, 0.0), (-169.13673481110396, -128.72670684047438, 0.0), (-179.96576555533994, -133.19936567438293, 0.0), (-190.79479629957592, -137.67202450829149, 0.0), (-201.6238270438119, -142.1446833422, 0.0), (-212.45285778804785, -146.61734217610854, 0.0), (-223.28188853228383, -151.0900010100171, 0.0), (-234.1109192765198, -155.56265984392562, 0.0), (-244.9399500207558, -160.03531867783417, 0.0), (-255.76898076499177, -164.5079775117427, 0.0), (-266.5980115092277, -168.98063634565125, 0.0), (-277.4270422534637, -173.4532951795598, 0.0), (-288.2560729976997, -177.92595401346833, 0.0), (-299.08510374193565, -182.39861284737685, 0.0), (-309.91413448617163, -186.8712716812854, 0.0), (-320.7431652304076, -191.34393051519393, 0.0), (-331.5721959746436, -195.8165893491025, 0.0), (-342.40122671887957, -200.289248183011, 0.0), (-353.23025746311555, -204.76190701691957, 0.0), (-364.0592882073515, -209.23456585082812, 0.0), (-374.8883189515875, -213.70722468473664, 0.0)], 1602578276.8317118: [(-219.01955619351568, -91.72554482353189, 0.0), (-218.17142213300554, -76.03111509783596, 0.0), (-215.0465881221402, -60.57609178528943, 0.0), (-201.692835035629, -52.88595435073953, 0.0), (-186.45137024716482, -49.02704589473295, 0.0), (-171.20358717578688, -45.18802798080956, 0.0), (-155.95454939227002, -41.35386051588435, 0.0), (-140.70434169591965, -37.52432158510094, 0.0), (-125.45318310926922, -33.69854147819277, 0.0), (-110.20135557808426, -29.87540572680866, 0.0), (-94.94918306753985, -26.053633687618298, 0.0), (-79.69701055699551, -22.231861648427724, 0.0), (-64.44518302580724, -18.40872589705307, 0.0), (-49.19402443936034, -14.582945790072745, 0.0), (-33.94381673509817, -10.753406821590142, 0.0), (-18.694778808551177, -6.919243691996043, 0.0), (-3.447045499366103, -3.0799233767311747, 0.0), (11.79935342266474, 0.7646718049512727, 0.0), (27.044514271574762, 4.614161121223243, 0.0)], 1602578276.9324372: [(-221.45370069375645, -88.57813500880354, 0.0), (-220.45913419670634, -70.95027956334361, 0.0), (-211.76926479144078, -53.34605588070572, 0.0), (-194.1348096127646, -48.337013268859906, 0.0), (-177.11463903378498, -44.12818047079051, 0.0), (-160.07983970428538, -39.959604312506684, 0.0), (-143.034778468698, -35.83152018602954, 0.0), (-125.98052756857442, -31.73976403304659, 0.0), (-108.91880642456998, -27.677537953562734, 0.0), (-91.85182996959435, -23.636086252200727, 0.0), (-74.78214331498776, -19.605348039028645, 0.0), (-57.7124566603812, -15.57460982585658, 0.0), (-40.64548020540543, -11.533158124494436, 0.0), (-23.583759061388747, -7.470932045017499, 0.0), (-6.5295081630547855, -3.379175894031854, 0.0), (10.515552819779842, 0.7489082270602458, 0.0), (27.550364570508304, 4.917507823795041, 0.0)], 1602578277.0332596: [(-223.53036445681505, -85.86507408414724, 0.0)], 1602578277.134072: [(-225.65256548631666, -83.2378945251208, 0.0)], 1602578277.2247467: [(-227.58952989011505, -81.01725306676052, 0.0), (-238.29084019805072, -67.90323267700892, 0.0), (-248.99215050598636, -54.7892122872573, 0.0), (-259.693460813922, -41.67519189750569, 0.0), (-270.3947711218577, -28.56117150775409, 0.0), (-281.09608142979334, -15.447151118002466, 0.0), (-291.797391737729, -2.3331307282508646, 0.0), (-302.4987020456647, 10.780889661500723, 0.0), (-313.2000123536003, 23.89491005125234, 0.0), (-323.90132266153597, 37.008930441003955, 0.0), (-334.60263296947164, 50.122950830755585, 0.0), (-345.30394327740726, 63.236971220507186, 0.0), (-356.005253585343, 76.35099161025879, 0.0), (-366.7065638932786, 89.46501200001039, 0.0), (-377.40787420121427, 102.57903238976196, 0.0), (-388.10918450914994, 115.6930527795136, 0.0), (-398.81049481708556, 128.8070731692652, 0.0), (-409.5118051250213, 141.9210935590168, 0.0), (-420.2131154329569, 155.0351139487684, 0.0), (-430.91442574089257, 168.14913433852007, 0.0), (-441.61573604882824, 181.26315472827167, 0.0)], 1602578277.3253732: [(-229.76204813729697, -78.67078663927197, 0.0), (-240.49235060024114, -66.00708646496149, 0.0), (-251.22265306318528, -53.34338629065101, 0.0), (-261.9529555261294, -40.67968611634053, 0.0), (-272.6832579890736, -28.01598594203005, 0.0), (-283.41356045201775, -15.352285767719579, 0.0), (-294.1438629149619, -2.688585593409087, 0.0), (-304.874165377906, 9.97511458090139, 0.0), (-315.6044678408502, 22.638814755211868, 0.0), (-326.33477030379436, 35.302514929522346, 0.0), (-337.0650727667385, 47.96621510383281, 0.0), (-347.7953752296827, 60.6299152781433, 0.0), (-358.5256776926268, 73.29361545245379, 0.0), (-369.25598015557097, 85.95731562676426, 0.0), (-379.98628261851513, 98.62101580107475, 0.0), (-390.7165850814593, 111.28471597538524, 0.0), (-401.44688754440347, 123.9484161496957, 0.0), (-412.1771900073476, 136.61211632400617, 0.0), (-422.90749247029174, 149.27581649831666, 0.0), (-433.6377949332359, 161.93951667262712, 0.0), (-444.36809739618, 174.60321684693758, 0.0)], 1602578277.4262154: [(-231.92618395314827, -76.11671444950184, 0.0), (-242.65648641609243, -63.453014275191364, 0.0), (-253.38678887903657, -50.78931410088089, 0.0), (-264.1170913419807, -38.1256139265704, 0.0), (-274.8473938049249, -25.461913752259925, 0.0), (-285.57769626786904, -12.798213577949454, 0.0), (-296.3079987308132, -0.13451340363896236, 0.0), (-307.0383011937573, 12.529186770671515, 0.0), (-317.7686036567015, 25.192886944981993, 0.0), (-328.49890611964565, 37.85658711929247, 0.0), (-339.2292085825898, 50.520287293602934, 0.0), (-349.959511045534, 63.183987467913425, 0.0), (-360.6898135084781, 75.84768764222392, 0.0), (-371.42011597142226, 88.51138781653438, 0.0), (-382.15041843436643, 101.17508799084487, 0.0), (-392.8807208973106, 113.83878816515536, 0.0), (-403.61102336025476, 126.50248833946583, 0.0), (-414.3413258231989, 139.1661885137763, 0.0), (-425.07162828614304, 151.82988868808678, 0.0), (-435.8019307490872, 164.49358886239725, 0.0), (-446.5322332120313, 177.1572890367077, 0.0)], 1602578277.5269804: [(-234.08866017749943, -73.56460087825548, 0.0), (-244.8189626404436, -60.900900703945, 0.0), (-255.54926510338774, -48.23720052963452, 0.0), (-266.2795675663319, -35.573500355324036, 0.0), (-277.00987002927604, -22.90980018101356, 0.0), (-287.7401724922202, -10.246100006703088, 0.0), (-298.4704749551644, 2.4176001676074037, 0.0), (-309.2007774181085, 15.081300341917881, 0.0), (-319.93107988105265, 27.74500051622836, 0.0), (-330.6613823439968, 40.408700690538836, 0.0), (-341.391684806941, 53.0724008648493, 0.0), (-352.12198726988515, 65.73610103915979, 0.0), (-362.85228973282926, 78.39980121347028, 0.0), (-373.58259219577343, 91.06350138778075, 0.0), (-384.3128946587176, 103.72720156209124, 0.0), (-395.04319712166176, 116.39090173640173, 0.0), (-405.77349958460593, 129.0546019107122, 0.0), (-416.50380204755004, 141.71830208502266, 0.0), (-427.2341045104942, 154.38200225933315, 0.0), (-437.9644069734384, 167.0457024336436, 0.0), (-448.6947094363825, 179.70940260795408, 0.0)], 1602578277.6276731: [(-236.2495918821141, -71.0143101200122, 0.0), (-246.97989434505826, -58.35060994570172, 0.0), (-257.7101968080024, -45.68690977139124, 0.0), (-268.44049927094653, -33.02320959708076, 0.0), (-279.1708017338907, -20.35950942277028, 0.0), (-289.90110419683486, -7.69580924845981, 0.0), (-300.63140665977903, 4.967890925850682, 0.0), (-311.36170912272314, 17.63159110016116, 0.0), (-322.0920115856673, 30.295291274471637, 0.0), (-332.8223140486115, 42.958991448782115, 0.0), (-343.55261651155564, 55.62269162309258, 0.0), (-354.2829189744998, 68.28639179740307, 0.0), (-365.0132214374439, 80.95009197171356, 0.0), (-375.7435239003881, 93.61379214602402, 0.0), (-386.47382636333225, 106.27749232033452, 0.0), (-397.2041288262764, 118.94119249464501, 0.0), (-407.9344312892206, 131.60489266895547, 0.0), (-418.6647337521647, 144.26859284326594, 0.0), (-429.39503621510886, 156.93229301757643, 0.0), (-440.125338678053, 169.5959931918869, 0.0), (-450.85564114099714, 182.25969336619735, 0.0)], 1602578277.7284436: [(-238.41218598956812, -68.46205742535572, 0.0), (-249.14248845251228, -55.798357251045246, 0.0), (-259.87279091545645, -43.13465707673477, 0.0), (-270.60309337840056, -30.470956902424284, 0.0), (-281.3333958413447, -17.807256728113806, 0.0), (-292.0636983042889, -5.143556553803336, 0.0), (-302.79400076723306, 7.520143620507156, 0.0), (-313.5243032301772, 20.183843794817633, 0.0), (-324.25460569312133, 32.84754396912811, 0.0), (-334.9849081560655, 45.51124414343859, 0.0), (-345.71521061900967, 58.17494431774905, 0.0), (-356.44551308195383, 70.83864449205954, 0.0), (-367.175815544898, 83.50234466637004, 0.0), (-377.9061180078421, 96.1660448406805, 0.0), (-388.6364204707863, 108.82974501499099, 0.0), (-399.36672293373044, 121.49344518930148, 0.0), (-410.09702539667455, 134.15714536361196, 0.0), (-420.8273278596188, 146.82084553792242, 0.0), (-431.5576303225629, 159.4845457122329, 0.0), (-442.287932785507, 172.14824588654335, 0.0), (-453.0182352484512, 184.8119460608538, 0.0)], 1602578278.2323167: [(-232.473033802788, -53.14912424631823, 0.0), (-231.4397420489885, -44.48840578759015, 0.0), (-230.40645029518905, -35.827687328862076, 0.0), (-229.37315854138956, -27.166968870133996, 0.0), (-228.33986678759007, -18.506250411405922, 0.0), (-227.30657503379058, -9.845531952677845, 0.0), (-226.27328327999112, -1.1848134939497612, 0.0), (-225.23999152619163, 7.475904964778316, 0.0), (-224.20669977239214, 16.136623423506386, 0.0), (-223.17340801859265, 24.79734188223447, 0.0), (-222.1401162647932, 33.45806034096254, 0.0), (-221.1068245109937, 42.118778799690624, 0.0), (-220.07353275719422, 50.77949725841871, 0.0), (-219.04024100339473, 59.44021571714678, 0.0), (-218.00694924959527, 68.10093417587487, 0.0), (-216.97365749579578, 76.76165263460294, 0.0), (-215.9403657419963, 85.42237109333101, 0.0), (-214.90707398819683, 94.0830895520591, 0.0), (-213.87378223439734, 102.74380801078718, 0.0), (-212.84049048059785, 111.40452646951525, 0.0), (-211.80719872679836, 120.06524492824332, 0.0)], 1602578278.333125: [(-232.246063412455, -50.61808381340709, 0.0), (-231.17296345946602, -40.281237798333166, 0.0), (-230.09986350647702, -29.944391783259242, 0.0), (-229.02676355348805, -19.607545768185318, 0.0), (-227.95366360049908, -9.270699753111394, 0.0), (-226.8805636475101, 1.0661462619625297, 0.0), (-225.80746369452112, 11.402992277036454, 0.0), (-224.73436374153215, 21.739838292110385, 0.0), (-223.66126378854318, 32.0766843071843, 0.0), (-222.58816383555418, 42.41353032225822, 0.0), (-221.51506388256522, 52.75037633733215, 0.0), (-220.44196392957625, 63.08722235240608, 0.0), (-219.36886397658725, 73.42406836748, 0.0), (-218.29576402359828, 83.76091438255392, 0.0), (-217.2226640706093, 94.09776039762787, 0.0), (-216.14956411762032, 104.43460641270178, 0.0), (-215.07646416463135, 114.7714524277757, 0.0), (-214.00336421164238, 125.10829844284962, 0.0), (-212.93026425865338, 135.44514445792353, 0.0), (-211.8571643056644, 145.78199047299748, 0.0), (-210.78406435267544, 156.1188364880714, 0.0)], 1602578278.4339306: [(-232.34005197955437, -48.11921320566747, 0.0), (-231.82265772492138, -37.03951910630453, 0.0), (-231.30526347028842, -25.959825006941596, 0.0), (-230.78786921565543, -14.88013090757866, 0.0), (-230.27047496102247, -3.8004368082157214, 0.0), (-229.75308070638948, 7.279257291147211, 0.0), (-229.23568645175652, 18.35895139051015, 0.0), (-228.71829219712353, 29.43864548987309, 0.0), (-228.20089794249054, 40.51833958923603, 0.0), (-227.68350368785758, 51.59803368859897, 0.0), (-227.1661094332246, 62.67772778796189, 0.0), (-226.64871517859163, 73.75742188732482, 0.0), (-226.13132092395864, 84.83711598668776, 0.0), (-225.61392666932565, 95.9168100860507, 0.0), (-225.0965324146927, 106.99650418541364, 0.0), (-224.5791381600597, 118.07619828477658, 0.0), (-224.06174390542674, 129.15589238413952, 0.0), (-223.54434965079375, 140.23558648350246, 0.0), (-223.0269553961608, 151.3152805828654, 0.0), (-222.5095611415278, 162.3949746822283, 0.0), (-221.9921668868948, 173.47466878159125, 0.0)], 1602578278.5247188: [(-232.55538721447908, -45.886874143936765, 0.0), (-232.5435793096778, -34.44667809234077, 0.0), (-232.5317714048765, -23.00648204074477, 0.0), (-232.5199635000752, -11.566285989148774, 0.0), (-232.5081555952739, -0.1260899375527771, 0.0), (-232.49634769047262, 11.31410611404322, 0.0), (-232.48453978567133, 22.754302165639217, 0.0), (-232.47273188087004, 34.19449821723522, 0.0), (-232.46092397606876, 45.63469426883121, 0.0), (-232.44911607126744, 57.074890320427215, 0.0), (-232.43730816646615, 68.5150863720232, 0.0), (-232.42550026166487, 79.95528242361921, 0.0), (-232.41369235686358, 91.3954784752152, 0.0), (-232.4018844520623, 102.83567452681119, 0.0), (-232.39007654726097, 114.27587057840721, 0.0), (-232.3782686424597, 125.7160666300032, 0.0), (-232.3664607376584, 137.15626268159917, 0.0), (-232.3546528328571, 148.59645873319516, 0.0), (-232.34284492805583, 160.0366547847912, 0.0), (-232.33103702325454, 171.4768508363872, 0.0), (-232.31922911845322, 182.9170468879832, 0.0)], 1602578278.6254845: [(-232.8508158628276, -43.442037178240234, 0.0), (-233.30282168232628, -31.784923970338866, 0.0), (-233.75482750182496, -20.127810762437502, 0.0), (-234.20683332132361, -8.470697554536137, 0.0), (-234.6588391408223, 3.1864156533652306, 0.0), (-235.11084496032097, 14.843528861266606, 0.0), (-235.56285077981966, 26.50064206916796, 0.0), (-236.01485659931834, 38.157755277069334, 0.0), (-236.46686241881702, 49.814868484970695, 0.0), (-236.91886823831567, 61.47198169287207, 0.0), (-237.37087405781435, 73.12909490077345, 0.0), (-237.82287987731303, 84.7862081086748, 0.0), (-238.2748856968117, 96.44332131657615, 0.0), (-238.7268915163104, 108.10043452447752, 0.0), (-239.17889733580907, 119.7575477323789, 0.0), (-239.63090315530775, 131.41466094028024, 0.0), (-240.0829089748064, 143.07177414818162, 0.0), (-240.53491479430508, 154.72888735608302, 0.0), (-240.98692061380376, 166.38600056398437, 0.0), (-241.43892643330244, 178.04311377188574, 0.0), (-241.89093225280112, 189.70022697978712, 0.0)], 1602578278.7262921: [(-232.34632796983078, -39.20689840054577, 0.0), (-231.8828037843862, -24.652519555111077, 0.0), (-231.4192795989416, -10.098140709676382, 0.0), (-230.95575541349706, 4.456238135758319, 0.0), (-230.49223122805247, 19.010616981193003, 0.0), (-230.0287070426079, 33.564995826627694, 0.0), (-229.5651828571633, 48.119374672062406, 0.0), (-229.10165867171875, 62.67375351749709, 0.0), (-228.63813448627417, 77.22813236293177, 0.0), (-228.17461030082958, 91.78251120836647, 0.0), (-227.711086115385, 106.33689005380116, 0.0), (-227.24756192994042, 120.89126889923587, 0.0), (-226.78403774449586, 135.44564774467057, 0.0), (-226.32051355905128, 150.00002659010522, 0.0), (-225.8569893736067, 164.55440543553993, 0.0), (-225.3934651881621, 179.10878428097465, 0.0), (-224.92994100271753, 193.6631631264093, 0.0), (-224.46641681727297, 208.217541971844, 0.0), (-224.0028926318284, 222.77192081727873, 0.0), (-223.5393684463838, 237.32629966271338, 0.0), (-223.07584426093922, 251.8806785081481, 0.0)], 1602578278.827104: [(-231.84169682033647, -35.20981113826058, 0.0), (-230.74434587359255, -19.017454998277724, 0.0), (-229.6469949268486, -2.825098858294872, 0.0), (-228.5496439801047, 13.367257281687976, 0.0), (-227.45229303336075, 29.559613421670832, 0.0), (-226.35494208661683, 45.75196956165368, 0.0), (-225.2575911398729, 61.94432570163653, 0.0), (-224.16024019312897, 78.13668184161938, 0.0), (-223.06288924638503, 94.32903798160224, 0.0), (-221.9655382996411, 110.52139412158509, 0.0), (-220.86818735289717, 126.71375026156794, 0.0), (-219.77083640615325, 142.9061064015508, 0.0), (-218.6734854594093, 159.09846254153365, 0.0), (-217.5761345126654, 175.2908186815165, 0.0), (-216.47878356592145, 191.48317482149935, 0.0), (-215.38143261917753, 207.6755309614822, 0.0), (-214.2840816724336, 223.86788710146504, 0.0), (-213.18673072568967, 240.06024324144784, 0.0), (-212.08937977894573, 256.25259938143074, 0.0), (-210.9920288322018, 272.4449555214136, 0.0), (-209.8946778854579, 288.63731166139644, 0.0)], 1602578278.9278867: [(-231.5007114372406, -31.518305673177075, 0.0), (-230.21752765497047, -14.66251536368559, 0.0), (-228.93434387270034, 2.1932749458058964, 0.0), (-227.6511600904302, 19.049065255297386, 0.0), (-226.3679763081601, 35.90485556478887, 0.0), (-225.08479252588998, 52.76064587428035, 0.0), (-223.80160874361985, 69.61643618377184, 0.0), (-222.51842496134972, 86.47222649326332, 0.0), (-221.2352411790796, 103.3280168027548, 0.0), (-219.95205739680947, 120.18380711224628, 0.0), (-218.66887361453936, 137.03959742173777, 0.0), (-217.38568983226924, 153.89538773122925, 0.0), (-216.1025060499991, 170.75117804072076, 0.0), (-214.81932226772898, 187.60696835021224, 0.0), (-213.53613848545885, 204.46275865970372, 0.0), (-212.25295470318872, 221.31854896919523, 0.0), (-210.96977092091862, 238.1743392786867, 0.0), (-209.6865871386485, 255.0301295881782, 0.0), (-208.40340335637836, 271.8859198976697, 0.0), (-207.12021957410823, 288.7417102071612, 0.0), (-205.8370357918381, 305.59750051665264, 0.0)], 1602578279.0287137: [(-231.29032080269033, -28.081498955844967, 0.0), (-230.08251072718122, -11.166850549045346, 0.0), (-228.8747006516721, 5.747797857754275, 0.0), (-227.66689057616298, 22.662446264553896, 0.0), (-226.45908050065387, 39.57709467135352, 0.0), (-225.25127042514475, 56.491743078153135, 0.0), (-224.04346034963564, 73.40639148495276, 0.0), (-222.83565027412652, 90.3210398917524, 0.0), (-221.6278401986174, 107.235688298552, 0.0), (-220.42003012310832, 124.15033670535162, 0.0), (-219.2122200475992, 141.06498511215122, 0.0), (-218.0044099720901, 157.97963351895086, 0.0), (-216.79659989658097, 174.89428192575048, 0.0), (-215.58878982107186, 191.80893033255012, 0.0), (-214.38097974556274, 208.72357873934976, 0.0), (-213.17316967005362, 225.63822714614938, 0.0), (-211.9653595945445, 242.55287555294896, 0.0), (-210.7575495190354, 259.46752395974863, 0.0), (-209.54973944352628, 276.3821723665482, 0.0), (-208.34192936801716, 293.29682077334786, 0.0), (-207.13411929250805, 310.21146918014745, 0.0)], 1602578279.1294706: [(-231.1768291180459, -24.84609943312688, 0.0), (-230.171874391839, -8.201824997646455, 0.0), (-229.16691966563212, 8.442449437833972, 0.0), (-228.16196493942522, 25.086723873314398, 0.0), (-227.1570102132183, 41.730998308794824, 0.0), (-226.1520554870114, 58.37527274427525, 0.0), (-225.14710076080453, 75.01954717975568, 0.0), (-224.14214603459763, 91.6638216152361, 0.0), (-223.13719130839073, 108.30809605071653, 0.0), (-222.13223658218385, 124.95237048619694, 0.0), (-221.12728185597695, 141.59664492167738, 0.0), (-220.12232712977004, 158.2409193571578, 0.0), (-219.11737240356314, 174.88519379263823, 0.0), (-218.11241767735626, 191.52946822811867, 0.0), (-217.10746295114936, 208.17374266359909, 0.0), (-216.10250822494245, 224.8180170990795, 0.0), (-215.09755349873558, 241.46229153455994, 0.0), (-214.09259877252867, 258.1065659700404, 0.0), (-213.08764404632177, 274.75084040552076, 0.0), (-212.08268932011487, 291.3951148410012, 0.0), (-211.077734593908, 308.03938927648164, 0.0)], 1602578279.2302604: [(-230.97425101765677, -21.490957744086607, 0.0), (-229.96929629144987, -4.846683308606181, 0.0), (-228.964341565243, 11.797591126874245, 0.0), (-227.95938683903609, 28.44186556235467, 0.0), (-226.95443211282918, 45.0861399978351, 0.0), (-225.94947738662228, 61.730414433315524, 0.0), (-224.9445226604154, 78.37468886879594, 0.0), (-223.9395679342085, 95.01896330427638, 0.0), (-222.9346132080016, 111.6632377397568, 0.0), (-221.92965848179472, 128.3075121752372, 0.0), (-220.9247037555878, 144.95178661071765, 0.0), (-219.9197490293809, 161.59606104619806, 0.0), (-218.914794303174, 178.2403354816785, 0.0), (-217.90983957696713, 194.88460991715894, 0.0), (-216.90488485076023, 211.52888435263935, 0.0), (-215.89993012455332, 228.17315878811976, 0.0), (-214.89497539834645, 244.8174332236002, 0.0), (-213.89002067213954, 261.4617076590807, 0.0), (-212.88506594593264, 278.10598209456106, 0.0), (-211.88011121972573, 294.7502565300415, 0.0), (-210.87515649351886, 311.39453096552194, 0.0)], 1602578279.3310695: [(-230.77163382251888, -18.135168559482246, 0.0), (-229.76667909631198, -1.4908941240018194, 0.0), (-228.7617243701051, 15.153380311478607, 0.0), (-227.7567696438982, 31.797654746959033, 0.0), (-226.7518149176913, 48.44192918243946, 0.0), (-225.7468601914844, 65.08620361791989, 0.0), (-224.7419054652775, 81.7304780534003, 0.0), (-223.7369507390706, 98.37475248888074, 0.0), (-222.7319960128637, 115.01902692436116, 0.0), (-221.72704128665683, 131.66330135984157, 0.0), (-220.72208656044992, 148.307575795322, 0.0), (-219.71713183424302, 164.95185023080242, 0.0), (-218.71217710803614, 181.59612466628286, 0.0), (-217.70722238182924, 198.2403991017633, 0.0), (-216.70226765562234, 214.8846735372437, 0.0), (-215.69731292941543, 231.52894797272413, 0.0), (-214.69235820320856, 248.17322240820457, 0.0), (-213.68740347700165, 264.81749684368503, 0.0), (-212.68244875079475, 281.4617712791654, 0.0), (-211.67749402458787, 298.10604571464586, 0.0), (-210.67253929838097, 314.7503201501263, 0.0)], 1602578279.4318256: [(-230.56912276064963, -14.781137176701016, 0.0), (-229.56416803444273, 1.8631372587794104, 0.0), (-228.55921330823585, 18.507411694259837, 0.0), (-227.55425858202895, 35.15168612974026, 0.0), (-226.54930385582205, 51.79596056522069, 0.0), (-225.54434912961514, 68.44023500070111, 0.0), (-224.53939440340827, 85.08450943618155, 0.0), (-223.53443967720136, 101.72878387166196, 0.0), (-222.52948495099446, 118.3730583071424, 0.0), (-221.52453022478758, 135.0173327426228, 0.0), (-220.51957549858068, 151.66160717810325, 0.0), (-219.51462077237377, 168.30588161358367, 0.0), (-218.5096660461669, 184.9501560490641, 0.0), (-217.50471131996, 201.59443048454455, 0.0), (-216.4997565937531, 218.23870492002496, 0.0), (-215.4948018675462, 234.88297935550537, 0.0), (-214.4898471413393, 251.5272537909858, 0.0), (-213.4848924151324, 268.17152822646625, 0.0), (-212.4799376889255, 284.81580266194663, 0.0), (-211.47498296271863, 301.4600770974271, 0.0), (-210.47002823651172, 318.1043515329075, 0.0)], 1602578279.5331707: [(-230.36542854950196, -11.407510223318504, 0.0), (-229.36047382329505, 5.236764212161923, 0.0), (-228.35551909708818, 21.88103864764235, 0.0), (-227.35056437088127, 38.525313083122775, 0.0), (-226.34560964467437, 55.1695875186032, 0.0), (-225.34065491846746, 71.81386195408362, 0.0), (-224.3357001922606, 88.45813638956406, 0.0), (-223.33074546605368, 105.10241082504447, 0.0), (-222.32579073984678, 121.74668526052491, 0.0), (-221.3208360136399, 138.39095969600532, 0.0), (-220.315881287433, 155.03523413148577, 0.0), (-219.3109265612261, 171.67950856696618, 0.0), (-218.3059718350192, 188.32378300244662, 0.0), (-217.30101710881232, 204.96805743792706, 0.0), (-216.2960623826054, 221.61233187340747, 0.0), (-215.2911076563985, 238.25660630888788, 0.0), (-214.28615293019163, 254.90088074436832, 0.0), (-213.28119820398473, 271.54515517984873, 0.0), (-212.27624347777783, 288.1894296153291, 0.0), (-211.27128875157092, 304.83370405080956, 0.0), (-210.26633402536405, 321.47797848629, 0.0)], 1602578282.730479: [(-142.15937474031767, 23.13078478796335, 0.0), (-130.28716771973367, 23.275088402551287, 0.0), (-118.41496069914969, 23.419392017139224, 0.0), (-106.5427536785657, 23.56369563172716, 0.0), (-94.6705466579817, 23.707999246315097, 0.0), (-82.7983396373977, 23.852302860903034, 0.0), (-70.92613261681372, 23.99660647549097, 0.0), (-59.05392559622973, 24.140910090078908, 0.0), (-47.18171857564573, 24.285213704666845, 0.0), (-35.30951155506173, 24.42951731925478, 0.0), (-23.437304534477747, 24.57382093384272, 0.0), (-11.565097513893761, 24.718124548430655, 0.0), (0.30710950669023873, 24.862428163018592, 0.0), (12.179316527274239, 25.006731777606525, 0.0), (24.05152354785821, 25.151035392194462, 0.0), (35.92373056844221, 25.2953390067824, 0.0), (47.79593758902621, 25.439642621370336, 0.0), (59.66814460961021, 25.583946235958273, 0.0), (71.54035163019421, 25.72824985054621, 0.0), (83.41255865077818, 25.872553465134146, 0.0), (95.28476567136218, 26.016857079722083, 0.0)], 1602578282.8313098: [(-138.71200782307233, 21.713794477298674, 0.0), (-124.59109754092935, 18.77052854747553, 0.0), (-110.47018725878638, 15.827262617652384, 0.0), (-96.34927697664341, 12.883996687829239, 0.0), (-82.22836669450045, 9.940730758006096, 0.0), (-68.10745641235748, 6.997464828182951, 0.0), (-53.986546130214506, 4.054198898359804, 0.0), (-39.865635848071534, 1.110932968536659, 0.0), (-25.744725565928576, -1.8323329612864825, 0.0), (-11.62381528378559, -4.775598891109631, 0.0), (2.497094998357369, -7.718864820932772, 0.0), (16.61800528050034, -10.662130750755917, 0.0), (30.738915562643314, -13.605396680579066, 0.0), (44.85982584478626, -16.548662610402207, 0.0), (58.98073612692926, -19.491928540225356, 0.0), (73.1016464090722, -22.435194470048497, 0.0), (87.22255669121517, -25.37846039987164, 0.0), (101.34346697335815, -28.321726329694787, 0.0), (115.46437725550115, -31.264992259517935, 0.0), (129.58528753764404, -34.208258189341066, 0.0), (143.70619781978706, -37.15152411916422, 0.0)], 1602578282.9320924: [(-135.44889370171254, 20.503698574627418, 0.0), (-120.58163299530013, 16.45595882877773, 0.0), (-105.71437228888772, 12.408219082928044, 0.0), (-90.8471115824753, 8.360479337078356, 0.0), (-75.9798508760629, 4.31273959122867, 0.0), (-61.11259016965049, 0.26499984537898413, 0.0), (-46.24532946323808, -3.7827399004707054, 0.0), (-31.37806875682567, -7.830479646320388, 0.0), (-16.51080805041326, -11.878219392170077, 0.0), (-1.6435473440008366, -15.925959138019767, 0.0), (13.223713362411559, -19.97369888386945, 0.0), (28.090974068823982, -24.02143862971914, 0.0), (42.95823477523638, -28.06917837556883, 0.0), (57.8254954816488, -32.11691812141851, 0.0), (72.6927561880612, -36.16465786726819, 0.0), (87.56001689447362, -40.212397613117886, 0.0), (102.42727760088601, -44.26013735896757, 0.0), (117.29453830729847, -48.307877104817265, 0.0), (132.16179901371086, -52.35561685066695, 0.0), (147.02905972012323, -56.40335659651663, 0.0), (161.89632042653565, -60.45109634236631, 0.0)], 1602578283.032885: [(-132.29455348454957, 19.69471864126605, 0.0), (-117.17278173647071, 15.658278133981877, 0.0), (-102.05100998839185, 11.621837626697705, 0.0), (-86.929238240313, 7.58539711941353, 0.0), (-71.80746649223414, 3.548956612129359, 0.0), (-56.68569474415527, -0.48748389515481705, 0.0), (-41.563922996076414, -4.52392440243899, 0.0), (-26.442151247997558, -8.560364909723162, 0.0), (-11.320379499918701, -12.596805417007332, 0.0), (3.8013922481601696, -16.633245924291508, 0.0), (18.923163996239026, -20.669686431575684, 0.0), (34.04493574431788, -24.706126938859853, 0.0), (49.16670749239674, -28.74256744614403, 0.0), (64.2884792404756, -32.7790079534282, 0.0), (79.41025098855445, -36.815448460712375, 0.0), (94.53202273663331, -40.851888967996544, 0.0), (109.65379448471217, -44.88832947528071, 0.0), (124.775566232791, -48.9247699825649, 0.0), (139.8973379808699, -52.961210489849066, 0.0), (155.01910972894876, -56.99765099713325, 0.0), (170.14088147702762, -61.03409150441742, 0.0)], 1602578283.1338692: [(-129.19572816738335, 19.100920235377036, 0.0), (-114.0047198589174, 15.407370314070356, 0.0), (-98.81371155045143, 11.713820392763674, 0.0), (-83.62270324198548, 8.020270471456994, 0.0), (-68.43169493351951, 4.326720550150313, 0.0), (-53.24068662505354, 0.633170628843633, 0.0), (-38.0496783165876, -3.060379292463047, 0.0), (-22.85867000812165, -6.753929213769727, 0.0), (-7.667661699655682, -10.44747913507641, 0.0), (7.5233466088103, -14.141029056383093, 0.0), (22.714354917276268, -17.83457897768977, 0.0), (37.90536322574221, -21.528128898996446, 0.0), (53.096371534208146, -25.22167882030313, 0.0), (68.28737984267411, -28.915228741609813, 0.0), (83.47838815114005, -32.60877866291649, 0.0), (98.66939645960602, -36.302328584223176, 0.0), (113.86040476807199, -39.99587850552986, 0.0), (129.05141307653795, -43.68942842683653, 0.0), (144.24242138500395, -47.382978348143226, 0.0), (159.4334296934699, -51.076528269449895, 0.0), (174.62443800193589, -54.77007819075658, 0.0)], 1602578283.224758: [(-126.43873398769409, 18.68395238368262, 0.0), (-111.2544771452545, 15.381610911847911, 0.0), (-96.0702203028149, 12.079269440013203, 0.0), (-80.88596346037531, 8.776927968178493, 0.0), (-65.70170661793571, 5.474586496343784, 0.0), (-50.517449775496104, 2.172245024509074, 0.0), (-35.33319293305651, -1.1300964473256343, 0.0), (-20.148936090616914, -4.432437919160343, 0.0), (-4.964679248177319, -7.734779390995051, 0.0), (10.21957759426229, -11.03712086282976, 0.0), (25.403834436701885, -14.339462334664471, 0.0), (40.58809127914148, -17.64180380649918, 0.0), (55.772348121581075, -20.944145278333888, 0.0), (70.95660496402067, -24.246486750168597, 0.0), (86.14086180646026, -27.548828222003305, 0.0), (101.32511864889986, -30.851169693838013, 0.0), (116.50937549133945, -34.153511165672725, 0.0), (131.69363233377902, -37.455852637507434, 0.0), (146.87788917621867, -40.75819410934214, 0.0), (162.0621460186582, -44.06053558117685, 0.0), (177.24640286109786, -47.36287705301156, 0.0)], 1602578283.3254902: [(-123.37964084125743, 18.018646845946467, 0.0), (-108.19538399881783, 14.716305374111759, 0.0), (-93.01112715637824, 11.41396390227705, 0.0), (-77.82687031393863, 8.11162243044234, 0.0), (-62.64261347149904, 4.809280958607632, 0.0), (-47.45835662905944, 1.5069394867729216, 0.0), (-32.27409978661984, -1.7954019850617868, 0.0), (-17.089842944180248, -5.097743456896495, 0.0), (-1.9055861017406528, -8.400084928731204, 0.0), (13.278670740698956, -11.702426400565912, 0.0), (28.46292758313855, -15.004767872400624, 0.0), (43.647184425578146, -18.307109344235332, 0.0), (58.83144126801774, -21.60945081607004, 0.0), (74.01569811045734, -24.91179228790475, 0.0), (89.19995495289693, -28.214133759739457, 0.0), (104.38421179533653, -31.516475231574166, 0.0), (119.56846863777612, -34.81881670340887, 0.0), (134.7527254802157, -38.12115817524358, 0.0), (149.93698232265535, -41.42349964707829, 0.0), (165.1212391650949, -44.725841118912996, 0.0), (180.30549600753454, -48.02818259074772, 0.0)], 1602578283.426384: [(-120.31565226004624, 17.35227662671511, 0.0), (-105.13139541760664, 14.049935154880401, 0.0), (-89.94713857516705, 10.747593683045693, 0.0), (-74.76288173272744, 7.445252211210983, 0.0), (-59.57862489028785, 4.1429107393762745, 0.0), (-44.394368047848246, 0.8405692675415644, 0.0), (-29.21011120540865, -2.461772204293144, 0.0), (-14.025854362969056, -5.764113676127852, 0.0), (1.1584024794705385, -9.06645514796256, 0.0), (16.342659321910148, -12.36879661979727, 0.0), (31.526916164349743, -15.671138091631981, 0.0), (46.71117300678934, -18.97347956346669, 0.0), (61.89542984922893, -22.275821035301398, 0.0), (77.07968669166853, -25.578162507136106, 0.0), (92.26394353410812, -28.880503978970815, 0.0), (107.44820037654772, -32.18284545080552, 0.0), (122.63245721898731, -35.48518692264023, 0.0), (137.81671406142686, -38.78752839447494, 0.0), (153.00097090386652, -42.08986986630965, 0.0), (168.18522774630605, -45.39221133814436, 0.0), (183.3694845887457, -48.69455280997907, 0.0)], 1602578283.527277: [(-117.25168162662663, 16.685910310851373, 0.0), (-102.06742478418704, 13.383568839016664, 0.0), (-86.88316794174744, 10.081227367181956, 0.0), (-71.69891109930785, 6.778885895347246, 0.0), (-56.51465425686825, 3.4765444235125376, 0.0), (-41.330397414428646, 0.1742029516778274, 0.0), (-26.14614057198905, -3.128138520156881, 0.0), (-10.961883729549456, -6.430479991991589, 0.0), (4.222373112890139, -9.732821463826298, 0.0), (19.40662995532975, -13.035162935661006, 0.0), (34.59088679776934, -16.337504407495718, 0.0), (49.77514364020894, -19.639845879330426, 0.0), (64.95940048264853, -22.942187351165135, 0.0), (80.14365732508813, -26.244528822999843, 0.0), (95.32791416752772, -29.54687029483455, 0.0), (110.51217100996732, -32.84921176666926, 0.0), (125.69642785240691, -36.151553238503965, 0.0), (140.88068469484648, -39.45389471033867, 0.0), (156.06494153728613, -42.75623618217338, 0.0), (171.24919837972567, -46.05857765400809, 0.0), (186.43345522216532, -49.36091912584281, 0.0)], 1602578283.6282194: [(-118.627530549092, 11.724274061452235, 0.0), (-108.16507393625315, 3.85575304924312, 0.0), (-97.70261732341429, -4.012767962965995, 0.0), (-87.24016071057544, -11.88128897517511, 0.0), (-76.77770409773657, -19.749809987384225, 0.0), (-66.31524748489772, -27.61833099959334, 0.0), (-55.852790872058875, -35.486852011802455, 0.0), (-45.390334259220026, -43.35537302401157, 0.0), (-34.92787764638116, -51.223894036220685, 0.0), (-24.4654210335423, -59.0924150484298, 0.0), (-14.00296442070345, -66.96093606063891, 0.0), (-3.5405078078646, -74.82945707284803, 0.0), (6.9219488049742495, -82.69797808505714, 0.0), (17.384405417813127, -90.56649909726626, 0.0), (27.84686203065195, -98.43502010947537, 0.0), (38.309318643490826, -106.3035411216845, 0.0), (48.771775256329676, -114.1720621338936, 0.0), (59.234231869168525, -122.0405831461027, 0.0), (69.6966884820074, -129.90910415831183, 0.0), (80.15914509484622, -137.77762517052093, 0.0), (90.6216017076851, -145.64614618273006, 0.0)], 1602578283.7290103: [(-117.54074086577296, 10.000126201677626, 0.0), (-108.30320458932391, 1.9662505214411166, 0.0), (-99.06566831287485, -6.067625158795392, 0.0), (-89.8281320364258, -14.101500839031894, 0.0), (-80.59059575997674, -22.135376519268412, 0.0), (-71.35305948352767, -30.169252199504925, 0.0), (-62.11552320707863, -38.203127879741416, 0.0), (-52.877986930629575, -46.23700355997793, 0.0), (-43.64045065418051, -54.27087924021445, 0.0), (-34.40291437773145, -62.304754920450954, 0.0), (-25.165378101282386, -70.33863060068747, 0.0), (-15.927841824833337, -78.37250628092396, 0.0), (-6.690305548384302, -86.40638196116045, 0.0), (2.5472307280647755, -94.44025764139695, 0.0), (11.78476700451381, -102.47413332163347, 0.0), (21.022303280962888, -110.50800900186998, 0.0), (30.259839557411937, -118.54188468210651, 0.0), (39.497375833861014, -126.575760362343, 0.0), (48.73491211031006, -134.60963604257952, 0.0), (57.97244838675911, -142.64351172281604, 0.0), (67.20998466320819, -150.67738740305256, 0.0)], 1602578283.8297467: [(-116.3265306925734, 8.720568772950378, 0.0), (-107.99705301274986, 1.1626184894038891, 0.0), (-99.66757533292633, -6.395331794142599, 0.0), (-91.33809765310279, -13.95328207768909, 0.0), (-83.00861997327927, -21.511232361235578, 0.0), (-74.67914229345573, -29.06918264478206, 0.0), (-66.3496646136322, -36.62713292832856, 0.0), (-58.02018693380866, -44.185083211875046, 0.0), (-49.69070925398513, -51.74303349542153, 0.0), (-41.36123157416159, -59.30098377896801, 0.0), (-33.03175389433807, -66.8589340625145, 0.0), (-24.702276214514526, -74.41688434606101, 0.0), (-16.372798534690986, -81.9748346296075, 0.0), (-8.043320854867446, -89.53278491315399, 0.0), (0.2861568249560804, -97.09073519670048, 0.0), (8.615634504779607, -104.64868548024695, 0.0), (16.945112184603133, -112.20663576379344, 0.0), (25.27458986442666, -119.76458604733995, 0.0), (33.60406754425021, -127.32253633088641, 0.0), (41.93354522407374, -134.8804866144329, 0.0), (50.263022903897266, -142.4384368979794, 0.0)], 1602578283.930575: [(-112.53954502614442, 5.499749709315898, 0.0), (-100.96732207341401, -4.669132249924251, 0.0), (-89.3950991206836, -14.8380142091644, 0.0), (-77.82287616795318, -25.006896168404545, 0.0), (-66.25065321522275, -35.1757781276447, 0.0), (-54.678430262492334, -45.34466008688485, 0.0), (-43.10620730976193, -55.51354204612499, 0.0), (-31.5339843570315, -65.68242400536515, 0.0), (-19.961761404301086, -75.8513059646053, 0.0), (-8.389538451570658, -86.02018792384546, 0.0), (3.1826845011597555, -96.18906988308561, 0.0), (14.75490745389017, -106.35795184232576, 0.0), (26.32713040662057, -116.52683380156589, 0.0), (37.89935335935101, -126.69571576080602, 0.0), (49.471576312081424, -136.8645977200462, 0.0), (61.04379926481184, -147.03347967928633, 0.0), (72.61602221754225, -157.2023616385265, 0.0), (84.18824517027267, -167.37124359776664, 0.0), (95.76046812300311, -177.5401255570068, 0.0), (107.33269107573349, -187.70900751624694, 0.0), (118.90491402846393, -197.8778894754871, 0.0)], 1602578284.0314586: [(-109.07055110670147, 2.716514860393788, 0.0), (-95.69823524502743, -8.613416890153793, 0.0), (-82.32591938335341, -19.943348640701377, 0.0), (-68.95360352167938, -31.273280391248967, 0.0), (-55.581287660005344, -42.60321214179654, 0.0), (-42.208971798331305, -53.93314389234413, 0.0), (-28.83665593665728, -65.26307564289172, 0.0), (-15.464340074983255, -76.5930073934393, 0.0), (-2.092024213309216, -87.92293914398687, 0.0), (11.280291648364809, -99.25287089453445, 0.0), (24.652607510038862, -110.58280264508204, 0.0), (38.02492337171289, -121.91273439562963, 0.0), (51.39723923338691, -133.2426661461772, 0.0), (64.76955509506094, -144.57259789672477, 0.0), (78.14187095673496, -155.90252964727236, 0.0), (91.51418681840902, -167.23246139781997, 0.0), (104.88650268008304, -178.5623931483675, 0.0), (118.25881854175704, -189.8923248989151, 0.0), (131.63113440343108, -201.22225664946268, 0.0), (145.0034502651052, -212.5521884000103, 0.0), (158.37576612677918, -223.88212015055785, 0.0)], 1602578284.1322718: [(-105.97673569665584, -0.07850959526741508, 0.0), (-91.9726158363606, -12.21981823273057, 0.0), (-77.96849597606536, -24.36112687019373, 0.0), (-63.964376115770115, -36.502435507656884, 0.0), (-49.96025625547488, -48.64374414512004, 0.0), (-35.95613639517963, -60.78505278258319, 0.0), (-21.952016534884393, -72.92636142004636, 0.0), (-7.94789667458916, -85.06767005750952, 0.0), (6.056223185706074, -97.20897869497267, 0.0), (20.060343046001307, -109.35028733243581, 0.0), (34.06446290629658, -121.49159596989898, 0.0), (48.0685827665918, -133.63290460736212, 0.0), (62.07270262688705, -145.7742132448253, 0.0), (76.07682248718227, -157.91552188228846, 0.0), (90.08094234747752, -170.0568305197516, 0.0), (104.08506220777274, -182.19813915721477, 0.0), (118.08918206806798, -194.3394477946779, 0.0), (132.0933019283632, -206.48075643214105, 0.0), (146.09742178865844, -218.6220650696042, 0.0), (160.10154164895374, -230.7633737070674, 0.0), (174.105661509249, -242.90468234453053, 0.0)], 1602578284.2331047: [(-103.25712792096272, -2.781877726958202, 0.0), (-89.41792119243972, -15.325232182571675, 0.0), (-75.57871446391673, -27.86858663818515, 0.0), (-61.73950773539372, -40.41194109379862, 0.0), (-47.90030100687072, -52.95529554941209, 0.0), (-34.06109427834771, -65.49865000502557, 0.0), (-20.22188754982473, -78.04200446063903, 0.0), (-6.382680821301719, -90.58535891625252, 0.0), (7.456525907221277, -103.12871337186598, 0.0), (21.295732635744272, -115.67206782747944, 0.0), (35.1349393642673, -128.21542228309295, 0.0), (48.97414609279028, -140.75877673870642, 0.0), (62.81335282131326, -153.30213119431988, 0.0), (76.65255954983627, -165.84548564993335, 0.0), (90.49176627835928, -178.38884010554685, 0.0), (104.33097300688229, -190.93219456116032, 0.0), (118.17017973540527, -203.47554901677378, 0.0), (132.00938646392825, -216.01890347238725, 0.0), (145.84859319245126, -228.5622579280007, 0.0), (159.68779992097427, -241.10561238361421, 0.0), (173.5270066494973, -253.64896683922768, 0.0)], 1602578284.3342814: [(-100.73290536197054, -5.178391201559159, 0.0), (-87.32651309223124, -17.49972397862005, 0.0), (-73.92012082249195, -29.821056755680942, 0.0), (-60.513728552752646, -42.14238953274183, 0.0), (-47.10733628301335, -54.463722309802726, 0.0), (-33.700944013274054, -66.78505508686362, 0.0), (-20.294551743534754, -79.10638786392451, 0.0), (-6.888159473795469, -91.42772064098541, 0.0), (6.518232795943831, -103.7490534180463, 0.0), (19.92462506568313, -116.07038619510719, 0.0), (33.33101733542243, -128.39171897216806, 0.0), (46.737409605161716, -140.71305174922895, 0.0), (60.14380187490103, -153.03438452628984, 0.0), (73.55019414464032, -165.35571730335073, 0.0), (86.9565864143796, -177.67705008041165, 0.0), (100.36297868411894, -189.99838285747254, 0.0), (113.7693709538582, -202.31971563453342, 0.0), (127.17576322359749, -214.64104841159428, 0.0), (140.5821554933368, -226.9623811886552, 0.0), (153.9885477630761, -239.28371396571612, 0.0), (167.39494003281538, -251.60504674277698, 0.0)], 1602578284.4252305: [(-98.5901813901386, -7.127517525327166, 0.0), (-85.6466830600892, -18.991858856364267, 0.0), (-72.70318473003981, -30.856200187401363, 0.0), (-59.759686399990414, -42.72054151843846, 0.0), (-46.81618806994102, -54.58488284947556, 0.0), (-33.87268973989163, -66.44922418051266, 0.0), (-20.929191409842232, -78.31356551154975, 0.0), (-7.9856930797928385, -90.17790684258685, 0.0), (4.9578052502565555, -102.04224817362396, 0.0), (17.90130358030595, -113.90658950466106, 0.0), (30.844801910355343, -125.77093083569815, 0.0), (43.78830024040475, -137.63527216673526, 0.0), (56.73179857045413, -149.49961349777234, 0.0), (69.67529690050354, -161.36395482880945, 0.0), (82.61879523055292, -173.22829615984654, 0.0), (95.56229356060236, -185.09263749088367, 0.0), (108.50579189065171, -196.95697882192076, 0.0), (121.44929022070109, -208.82132015295784, 0.0), (134.39278855075048, -220.68566148399495, 0.0), (147.33628688079995, -232.55000281503206, 0.0), (160.2797852108493, -244.41434414606914, 0.0)], 1602578284.5260084: [(-96.27579819657134, -9.153586619427498, 0.0), (-83.79228159454988, -20.44733733960758, 0.0), (-71.3087649925284, -31.741088059787657, 0.0), (-58.82524839050692, -43.034838779967735, 0.0), (-46.34173178848545, -54.328589500147814, 0.0), (-33.85821518646397, -65.6223402203279, 0.0), (-21.3746985844425, -76.91609094050797, 0.0), (-8.891181982421031, -88.20984166068804, 0.0), (3.59233461960045, -99.50359238086813, 0.0), (16.075851221621917, -110.79734310104821, 0.0), (28.5593678236434, -122.0910938212283, 0.0), (41.04288442566485, -133.38484454140837, 0.0), (53.52640102768635, -144.67859526158844, 0.0), (66.00991762970781, -155.9723459817685, 0.0), (78.49343423172928, -167.26609670194858, 0.0), (90.97695083375075, -178.55984742212868, 0.0), (103.46046743577224, -189.85359814230875, 0.0), (115.94398403779368, -201.14734886248883, 0.0), (128.42750063981518, -212.44109958266893, 0.0), (140.91101724183665, -223.734850302849, 0.0), (153.39453384385814, -235.0286010230291, 0.0)], 1602578284.6267636: [(-95.24531976362442, -11.755155666550609, 0.0), (-85.08070407405184, -23.55756255183203, 0.0), (-74.91608838447925, -35.359969437113456, 0.0), (-64.75147269490667, -47.16237632239488, 0.0), (-54.586857005334096, -58.9647832076763, 0.0), (-44.42224131576151, -70.76719009295773, 0.0), (-34.25762562618892, -82.56959697823915, 0.0), (-24.09300993661634, -94.37200386352056, 0.0), (-13.92839424704377, -106.17441074880199, 0.0), (-3.76377855747117, -117.97681763408342, 0.0), (6.400837132101401, -129.77922451936485, 0.0), (16.565452821674, -141.5816314046463, 0.0), (26.730068511246586, -153.3840382899277, 0.0), (36.89468420081914, -165.18644517520912, 0.0), (47.05929989039174, -176.98885206049053, 0.0), (57.22391557996431, -188.79125894577197, 0.0), (67.38853126953688, -200.59366583105339, 0.0), (77.55314695910948, -212.39607271633483, 0.0), (87.71776264868208, -224.19847960161624, 0.0), (97.88237833825465, -236.00088648689768, 0.0), (108.04699402782722, -247.8032933721791, 0.0)], 1602578284.7274573: [(-94.21088722247708, -14.623908320493177, 0.0), (-85.62730584979924, -27.194351782969406, 0.0), (-77.0437244771214, -39.76479524544563, 0.0), (-68.46014310444356, -52.33523870792187, 0.0), (-59.87656173176572, -64.90568217039808, 0.0), (-51.29298035908788, -77.47612563287431, 0.0), (-42.70939898641003, -90.04656909535055, 0.0), (-34.125817613732195, -102.61701255782677, 0.0), (-25.542236241054354, -115.18745602030299, 0.0), (-16.958654868376513, -127.75789948277922, 0.0), (-8.375073495698672, -140.32834294525546, 0.0), (0.20850787697916928, -152.89878640773168, 0.0), (8.792089249657025, -165.46922987020793, 0.0), (17.375670622334866, -178.03967333268415, 0.0), (25.959251995012693, -190.61011679516037, 0.0), (34.54283336769055, -203.18056025763659, 0.0), (43.126414740368375, -215.7510037201128, 0.0), (51.70999611304623, -228.32144718258905, 0.0), (60.29357748572406, -240.89189064506527, 0.0), (68.87715885840191, -253.46233410754152, 0.0), (77.46074023107974, -266.03277757001774, 0.0)], 1602578284.8282292: [(-92.96262620084066, -17.32286343798573, 0.0), (-85.13119151832645, -30.151666936505677, 0.0), (-77.29975683581223, -42.98047043502562, 0.0), (-69.46832215329802, -55.80927393354557, 0.0), (-61.63688747078381, -68.63807743206551, 0.0), (-53.8054527882696, -81.46688093058545, 0.0), (-45.974018105755384, -94.2956844291054, 0.0), (-38.14258342324117, -107.12448792762535, 0.0), (-30.311148740726964, -119.9532914261453, 0.0), (-22.47971405821275, -132.78209492466527, 0.0), (-14.648279375698536, -145.61089842318518, 0.0), (-6.816844693184322, -158.43970192170514, 0.0), (1.0145899893298918, -171.2685054202251, 0.0), (8.846024671844106, -184.097308918745, 0.0), (16.67745935435832, -196.92611241726496, 0.0), (24.508894036872505, -209.75491591578492, 0.0), (32.34032871938673, -222.58371941430488, 0.0), (40.17176340190095, -235.41252291282484, 0.0), (48.00319808441516, -248.2413264113448, 0.0), (55.834632766929374, -261.0701299098647, 0.0), (63.66606744944359, -273.8989334083846, 0.0)], 1602578284.9290376: [(-91.87172220167986, -20.558839841003863, 0.0), (-84.80236055095655, -34.40177291631667, 0.0), (-77.73299890023324, -48.24470599162949, 0.0), (-70.66363724950995, -62.0876390669423, 0.0), (-63.59427559878664, -75.93057214225512, 0.0), (-56.52491394806333, -89.77350521756793, 0.0), (-49.45555229734002, -103.61643829288074, 0.0), (-42.38619064661672, -117.45937136819356, 0.0), (-35.31682899589341, -131.3023044435064, 0.0), (-28.247467345170108, -145.1452375188192, 0.0), (-21.1781056944468, -158.98817059413201, 0.0), (-14.10874404372349, -172.83110366944484, 0.0), (-7.0393823930001815, -186.67403674475764, 0.0), (0.02997925772312726, -200.51696982007047, 0.0), (7.099340908446422, -214.35990289538327, 0.0), (14.16870255916973, -228.20283597069607, 0.0), (21.23806420989304, -242.0457690460089, 0.0), (28.30742586061635, -255.88870212132173, 0.0), (35.37678751133964, -269.7316351966345, 0.0), (42.446149162062966, -283.5745682719474, 0.0), (49.51551081278626, -297.41750134726016, 0.0)], 1602578285.029768: [(-90.86319109616453, -23.896170783943735, 0.0), (-84.44289495374588, -38.59561841242448, 0.0), (-78.02259881132724, -53.29506604090522, 0.0), (-71.60230266890859, -67.99451366938597, 0.0), (-65.18200652648994, -82.69396129786671, 0.0), (-58.7617103840713, -97.39340892634745, 0.0), (-52.34141424165266, -112.09285655482819, 0.0), (-45.921118099234015, -126.79230418330893, 0.0), (-39.500821956815365, -141.49175181178967, 0.0), (-33.08052581439672, -156.19119944027042, 0.0), (-26.660229671978072, -170.89064706875118, 0.0), (-20.239933529559437, -185.5900946972319, 0.0), (-13.819637387140787, -200.28954232571266, 0.0), (-7.399341244722137, -214.9889899541934, 0.0), (-0.9790451023035018, -229.68843758267414, 0.0), (5.441251040115148, -244.3878852111549, 0.0), (11.861547182533798, -259.0873328396356, 0.0), (18.281843324952433, -273.7867804681164, 0.0), (24.702139467371083, -288.4862280965971, 0.0), (31.122435609789733, -303.18567572507783, 0.0), (37.54273175220838, -317.8851233535586, 0.0)], 1602578285.1306884: [(-90.00329318265439, -26.882390189970575, 0.0), (-84.26376012168704, -41.61193188433217, 0.0), (-78.5242270607197, -56.341473578693765, 0.0), (-72.78469399975235, -71.07101527305537, 0.0), (-67.04516093878499, -85.80055696741697, 0.0), (-61.30562787781765, -100.53009866177857, 0.0), (-55.56609481685031, -115.25964035614015, 0.0), (-49.826561755882956, -129.98918205050174, 0.0), (-44.0870286949156, -144.71872374486335, 0.0), (-38.347495633948256, -159.44826543922494, 0.0), (-32.60796257298091, -174.17780713358655, 0.0), (-26.868429512013556, -188.90734882794814, 0.0), (-21.12889645104623, -203.63689052230973, 0.0), (-15.38936339007887, -218.36643221667134, 0.0), (-9.649830329111523, -233.09597391103293, 0.0), (-3.910297268144163, -247.82551560539451, 0.0), (1.8292357928231837, -262.55505729975613, 0.0), (7.568768853790516, -277.2845989941177, 0.0), (13.308301914757877, -292.0141406884793, 0.0), (19.04783497572521, -306.7436823828409, 0.0), (24.78736803669257, -321.47322407720253, 0.0)], 1602578285.2315192: [(-89.2260696435613, -30.029215012014358, 0.0), (-84.08022654361075, -45.03426565749851, 0.0), (-78.9343834436602, -60.03931630298267, 0.0), (-73.78854034370964, -75.04436694846683, 0.0), (-68.64269724375909, -90.04941759395098, 0.0), (-63.496854143808534, -105.05446823943514, 0.0), (-58.35101104385798, -120.0595188849193, 0.0), (-53.20516794390742, -135.06456953040345, 0.0), (-48.059324843956865, -150.0696201758876, 0.0), (-42.91348174400631, -165.07467082137174, 0.0), (-37.76763864405576, -180.07972146685591, 0.0), (-32.621795544105204, -195.08477211234006, 0.0), (-27.47595244415465, -210.08982275782424, 0.0), (-22.33010934420409, -225.09487340330838, 0.0), (-17.184266244253536, -240.09992404879253, 0.0), (-12.038423144302982, -255.10497469427668, 0.0), (-6.892580044352428, -270.1100253397608, 0.0), (-1.7467369444018885, -285.11507598524497, 0.0), (3.3991061555486795, -300.1201266307291, 0.0), (8.544949255499233, -315.12517727621326, 0.0), (13.690792355449787, -330.13022792169744, 0.0)], 1602578285.3322477: [(-88.25558344948688, -33.032251984708736, 0.0), (-83.21308039368627, -48.00632044605392, 0.0), (-78.17057733788566, -62.9803889073991, 0.0), (-73.12807428208507, -77.95445736874427, 0.0), (-68.08557122628446, -92.92852583008946, 0.0), (-63.04306817048385, -107.90259429143464, 0.0), (-58.00056511468324, -122.87666275277982, 0.0), (-52.95806205888263, -137.850731214125, 0.0), (-47.91555900308203, -152.8247996754702, 0.0), (-42.87305594728142, -167.79886813681537, 0.0), (-37.83055289148082, -182.77293659816053, 0.0), (-32.78804983568021, -197.74700505950574, 0.0), (-27.74554677987961, -212.7210735208509, 0.0), (-22.70304372407901, -227.6951419821961, 0.0), (-17.660540668278387, -242.66921044354126, 0.0), (-12.618037612477792, -257.6432789048865, 0.0), (-7.575534556677184, -272.6173473662316, 0.0), (-2.533031500876575, -287.59141582757684, 0.0), (2.5094715549240334, -302.565484288922, 0.0), (7.551974610724642, -317.5395527502672, 0.0), (12.594477666525236, -332.51362121161236, 0.0)], 1602578285.4330337: [(-87.73896784518374, -36.14969100602705, 0.0), (-83.47689166282461, -51.2784770952291, 0.0), (-79.2148154804655, -66.40726318443114, 0.0), (-74.95273929810638, -81.5360492736332, 0.0), (-70.69066311574726, -96.66483536283525, 0.0), (-66.42858693338815, -111.79362145203729, 0.0), (-62.16651075102902, -126.92240754123935, 0.0), (-57.9044345686699, -142.0511936304414, 0.0), (-53.64235838631078, -157.17997971964346, 0.0), (-49.38028220395167, -172.3087658088455, 0.0), (-45.118206021592556, -187.43755189804753, 0.0), (-40.85612983923343, -202.5663379872496, 0.0), (-36.594053656874316, -217.69512407645163, 0.0), (-32.33197747451519, -232.8239101656537, 0.0), (-28.069901292156068, -247.95269625485574, 0.0), (-23.80782510979695, -263.0814823440578, 0.0), (-19.545748927437828, -278.21026843325984, 0.0), (-15.283672745078718, -293.33905452246194, 0.0), (-11.021596562719608, -308.467840611664, 0.0), (-6.759520380360485, -323.596626700866, 0.0), (-2.497444198001375, -338.72541279006805, 0.0)], 1602578285.5338113: [(-87.04024036827222, -39.167674155685326, 0.0), (-83.02848612021515, -54.24759082390814, 0.0), (-79.01673187215808, -69.32750749213095, 0.0), (-75.004977624101, -84.40742416035377, 0.0), (-70.99322337604393, -99.48734082857658, 0.0), (-66.98146912798686, -114.56725749679939, 0.0), (-62.96971487992978, -129.6471741650222, 0.0), (-58.957960631872716, -144.72709083324503, 0.0), (-54.94620638381564, -159.80700750146784, 0.0), (-50.93445213575857, -174.88692416969062, 0.0), (-46.922697887701496, -189.96684083791342, 0.0), (-42.91094363964442, -205.04675750613623, 0.0), (-38.89918939158735, -220.12667417435907, 0.0), (-34.88743514353028, -235.20659084258185, 0.0), (-30.87568089547321, -250.2865075108047, 0.0), (-26.863926647416136, -265.3664241790275, 0.0), (-22.852172399359063, -280.4463408472503, 0.0), (-18.84041815130199, -295.52625751547316, 0.0), (-14.828663903244916, -310.60617418369594, 0.0), (-10.816909655187843, -325.6860908519187, 0.0), (-6.805155407130769, -340.76600752014156, 0.0)], 1602578285.6245666: [(-86.28248381961886, -41.8198424170633, 0.0), (-82.2244722262489, -56.76684495087417, 0.0), (-78.16646063287894, -71.71384748468505, 0.0), (-74.10844903950897, -86.66085001849592, 0.0), (-70.05043744613901, -101.6078525523068, 0.0), (-65.99242585276906, -116.55485508611767, 0.0), (-61.93441425939909, -131.50185761992856, 0.0), (-57.87640266602913, -146.44886015373942, 0.0), (-53.81839107265917, -161.39586268755028, 0.0), (-49.760379479289206, -176.34286522136114, 0.0), (-45.702367885919244, -191.28986775517205, 0.0), (-41.64435629254929, -206.2368702889829, 0.0), (-37.58634469917932, -221.18387282279377, 0.0), (-33.52833310580936, -236.1308753566047, 0.0), (-29.470321512439398, -251.07787789041555, 0.0), (-25.412309919069443, -266.0248804242264, 0.0), (-21.354298325699475, -280.97188295803727, 0.0), (-17.29628673232952, -295.9188854918482, 0.0), (-13.238275138959551, -310.865888025659, 0.0), (-9.180263545589582, -325.8128905594699, 0.0), (-5.122251952219628, -340.75989309328077, 0.0)], 1602578285.7253075: [(-86.34558930130432, -44.95908758585585, 0.0), (-83.66450295183292, -60.10572822041786, 0.0), (-80.98341660236152, -75.25236885497986, 0.0), (-78.30233025289012, -90.39900948954188, 0.0), (-75.62124390341872, -105.54565012410389, 0.0), (-72.94015755394732, -120.6922907586659, 0.0), (-70.2590712044759, -135.8389313932279, 0.0), (-67.5779848550045, -150.9855720277899, 0.0), (-64.8968985055331, -166.13221266235192, 0.0), (-62.2158121560617, -181.27885329691395, 0.0), (-59.5347258065903, -196.42549393147596, 0.0), (-56.8536394571189, -211.572134566038, 0.0), (-54.1725531076475, -226.7187752006, 0.0), (-51.4914667581761, -241.865415835162, 0.0), (-48.8103804087047, -257.012056469724, 0.0), (-46.1292940592333, -272.158697104286, 0.0), (-43.4482077097619, -287.305337738848, 0.0), (-40.767121360290496, -302.45197837341004, 0.0), (-38.086035010819096, -317.59861900797205, 0.0), (-35.404948661347696, -332.74525964253405, 0.0), (-32.723862311876296, -347.89190027709606, 0.0)], 1602578285.8260305: [(-86.2023645201855, -48.0351862187795, 0.0), (-84.14148620845724, -63.22069385623407, 0.0), (-82.08060789672896, -78.40620149368864, 0.0), (-80.0197295850007, -93.5917091311432, 0.0), (-77.95885127327243, -108.77721676859778, 0.0), (-75.89797296154417, -123.96272440605235, 0.0), (-73.83709464981591, -139.1482320435069, 0.0), (-71.77621633808764, -154.33373968096146, 0.0), (-69.71533802635938, -169.51924731841603, 0.0), (-67.65445971463112, -184.7047549558706, 0.0), (-65.59358140290284, -199.8902625933252, 0.0), (-63.532703091174575, -215.07577023077974, 0.0), (-61.471824779446315, -230.26127786823432, 0.0), (-59.41094646771805, -245.4467855056889, 0.0), (-57.35006815598978, -260.63229314314344, 0.0), (-55.289189844261514, -275.8178007805981, 0.0), (-53.22831153253325, -291.0033084180526, 0.0), (-51.16743322080498, -306.1888160555071, 0.0), (-49.10655490907672, -321.37432369296175, 0.0), (-47.04567659734845, -336.5598313304163, 0.0), (-44.98479828562018, -351.7453389678709, 0.0)], 1602578285.9272761: [(-85.85741201311957, -51.07483930976029, 0.0), (-83.90956034603653, -66.20523519536216, 0.0), (-81.96170867895349, -81.33563108096402, 0.0), (-80.01385701187043, -96.46602696656589, 0.0), (-78.06600534478738, -111.59642285216776, 0.0), (-76.11815367770434, -126.72681873776963, 0.0), (-74.1703020106213, -141.85721462337148, 0.0), (-72.22245034353826, -156.98761050897338, 0.0), (-70.27459867645521, -172.11800639457522, 0.0), (-68.32674700937216, -187.24840228017712, 0.0), (-66.37889534228911, -202.37879816577896, 0.0), (-64.43104367520607, -217.50919405138086, 0.0), (-62.48319200812303, -232.6395899369827, 0.0), (-60.535340341039976, -247.76998582258454, 0.0), (-58.58748867395694, -262.90038170818644, 0.0), (-56.63963700687389, -278.0307775937883, 0.0), (-54.69178533979084, -293.1611734793902, 0.0), (-52.743933672707804, -308.29156936499203, 0.0), (-50.796082005624754, -323.4219652505939, 0.0), (-48.84823033854171, -338.55236113619577, 0.0), (-46.90037867145866, -353.68275702179767, 0.0)], 1602578286.0281482: [(-85.35144108358084, -54.065152272844756, 0.0), (-83.22711436078855, -69.09848841007123, 0.0), (-81.10278763799624, -84.13182454729768, 0.0), (-78.97846091520395, -99.16516068452415, 0.0), (-76.85413419241165, -114.19849682175061, 0.0), (-74.72980746961936, -129.23183295897707, 0.0), (-72.60548074682707, -144.26516909620355, 0.0), (-70.48115402403477, -159.29850523343, 0.0), (-68.35682730124248, -174.3318413706565, 0.0), (-66.23250057845017, -189.36517750788295, 0.0), (-64.10817385565788, -204.3985136451094, 0.0), (-61.98384713286559, -219.43184978233586, 0.0), (-59.85952041007329, -234.46518591956234, 0.0), (-57.735193687281, -249.4985220567888, 0.0), (-55.61086696448869, -264.5318581940153, 0.0), (-53.4865402416964, -279.56519433124174, 0.0), (-51.362213518904106, -294.5985304684682, 0.0), (-49.237886796111816, -309.63186660569465, 0.0), (-47.11356007331951, -324.6652027429211, 0.0), (-44.98923335052722, -339.69853888014757, 0.0), (-42.86490662773493, -354.731875017374, 0.0)], 1602578286.1289403: [(-84.9232091060321, -57.09564433140032, 0.0), (-82.79888238323981, -72.12898046862679, 0.0), (-80.67455566044751, -87.16231660585325, 0.0), (-78.55022893765522, -102.19565274307972, 0.0), (-76.42590221486292, -117.22898888030619, 0.0), (-74.30157549207063, -132.26232501753265, 0.0), (-72.17724876927834, -147.2956611547591, 0.0), (-70.05292204648603, -162.32899729198556, 0.0), (-67.92859532369374, -177.36233342921204, 0.0), (-65.80426860090144, -192.39566956643853, 0.0), (-63.67994187810915, -207.42900570366498, 0.0), (-61.55561515531686, -222.46234184089144, 0.0), (-59.43128843252455, -237.4956779781179, 0.0), (-57.30696170973226, -252.52901411534435, 0.0), (-55.18263498693996, -267.5623502525708, 0.0), (-53.05830826414767, -282.59568638979727, 0.0), (-50.93398154135537, -297.6290225270238, 0.0), (-48.80965481856308, -312.6623586642502, 0.0), (-46.68532809577078, -327.6956948014767, 0.0), (-44.56100137297849, -342.72903093870315, 0.0), (-42.4366746501862, -357.7623670759296, 0.0)], 1602578286.2302284: [(-84.49287159780341, -60.14103671113497, 0.0), (-82.36854487501112, -75.17437284836144, 0.0), (-80.24421815221882, -90.2077089855879, 0.0), (-78.11989142942653, -105.24104512281437, 0.0), (-75.99556470663423, -120.27438126004083, 0.0), (-73.87123798384194, -135.3077173972673, 0.0), (-71.74691126104965, -150.34105353449377, 0.0), (-69.62258453825734, -165.37438967172022, 0.0), (-67.49825781546505, -180.40772580894668, 0.0), (-65.37393109267275, -195.44106194617316, 0.0), (-63.24960436988046, -210.47439808339962, 0.0), (-61.12527764708817, -225.50773422062608, 0.0), (-59.000950924295864, -240.54107035785256, 0.0), (-56.876624201503574, -255.57440649507902, 0.0), (-54.75229747871127, -270.6077426323055, 0.0), (-52.62797075591898, -285.64107876953193, 0.0), (-50.50364403312668, -300.67441490675844, 0.0), (-48.37931731033439, -315.70775104398484, 0.0), (-46.25499058754209, -330.74108718121136, 0.0), (-44.1306638647498, -345.7744233184378, 0.0), (-42.00633714195751, -360.80775945566427, 0.0)], 1602578286.3310118: [(-84.06467801533586, -63.1712570571732, 0.0), (-81.94035129254357, -78.20459319439966, 0.0), (-79.81602456975126, -93.23792933162613, 0.0), (-77.69169784695897, -108.27126546885259, 0.0), (-75.56737112416667, -123.30460160607906, 0.0), (-73.44304440137438, -138.33793774330553, 0.0), (-71.31871767858209, -153.371273880532, 0.0), (-69.19439095578979, -168.40461001775844, 0.0), (-67.0700642329975, -183.43794615498493, 0.0), (-64.94573751020519, -198.47128229221138, 0.0), (-62.8214107874129, -213.50461842943784, 0.0), (-60.69708406462061, -228.5379545666643, 0.0), (-58.57275734182831, -243.57129070389078, 0.0), (-56.44843061903602, -258.60462684111724, 0.0), (-54.32410389624371, -273.6379629783437, 0.0), (-52.19977717345142, -288.67129911557015, 0.0), (-50.075450450659126, -303.70463525279666, 0.0), (-47.951123727866836, -318.73797139002306, 0.0), (-45.82679700507453, -333.7713075272496, 0.0), (-43.70247028228224, -348.80464366447603, 0.0), (-41.57814355948995, -363.8379798017025, 0.0)], 1602578286.4317746: [(-83.63657190414544, -66.20085839056264, 0.0), (-81.51224518135315, -81.23419452778911, 0.0), (-79.38791845856085, -96.26753066501557, 0.0), (-77.26359173576856, -111.30086680224204, 0.0), (-75.13926501297625, -126.3342029394685, 0.0), (-73.01493829018396, -141.36753907669498, 0.0), (-70.89061156739167, -156.40087521392144, 0.0), (-68.76628484459937, -171.4342113511479, 0.0), (-66.64195812180708, -186.46754748837435, 0.0), (-64.51763139901477, -201.50088362560084, 0.0), (-62.393304676222485, -216.5342197628273, 0.0), (-60.268977953430195, -231.56755590005375, 0.0), (-58.14465123063789, -246.60089203728023, 0.0), (-56.0203245078456, -261.6342281745067, 0.0), (-53.8959977850533, -276.66756431173314, 0.0), (-51.77167106226101, -291.7009004489596, 0.0), (-49.64734433946871, -306.73423658618606, 0.0), (-47.52301761667642, -321.7675727234125, 0.0), (-45.398690893884115, -336.800908860639, 0.0), (-43.274364171091825, -351.8342449978655, 0.0), (-41.150037448299535, -366.86758113509194, 0.0)], 1602578286.9260163: [(-94.33765258094124, -77.76674393818202, 0.0), (-99.5398439766393, -93.79731578257113, 0.0), (-104.74203537233738, -109.82788762696023, 0.0), (-109.94422676803546, -125.85845947134933, 0.0), (-115.14641816373353, -141.88903131573846, 0.0), (-120.3486095594316, -157.91960316012756, 0.0), (-125.55080095512967, -173.95017500451667, 0.0), (-130.75299235082775, -189.98074684890577, 0.0), (-135.95518374652582, -206.01131869329487, 0.0), (-141.15737514222388, -222.04189053768397, 0.0), (-146.35956653792198, -238.07246238207313, 0.0), (-151.56175793362002, -254.10303422646217, 0.0), (-156.7639493293181, -270.13360607085133, 0.0), (-161.96614072501617, -286.16417791524043, 0.0), (-167.16833212071424, -302.19474975962953, 0.0), (-172.37052351641233, -318.22532160401863, 0.0), (-177.5727149121104, -334.25589344840773, 0.0), (-182.77490630780846, -350.28646529279683, 0.0), (-187.97709770350656, -366.31703713718593, 0.0), (-193.17928909920462, -382.3476089815751, 0.0), (-198.3814804949027, -398.3781808259642, 0.0)]}}
    # real = {'CAR': {1602578276.8976462: [(-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0), (-228.6798515367136, -72.4534249185623, 0.0)], 1602578276.9984298: [(-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0), (-228.67656963676004, -72.44009387655316, 0.0)], 1602578277.0993078: [(-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0), (-228.66406745532942, -72.40624434879003, 0.0)], 1602578277.2001326: [(-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0), (-228.65546163394708, -72.37725605131601, 0.0)], 1602578277.300926: [(-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0), (-228.64921312537408, -72.35206084690685, 0.0)], 1602578277.4017732: [(-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0), (-228.64424791334093, -72.32146631122751, 0.0)], 1602578277.5026133: [(-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0), (-228.639283053929, -72.29087394832199, 0.0)], 1602578277.6036828: [(-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0), (-228.6343068997569, -72.26021198960835, 0.0)], 1602578277.704598: [(-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0), (-228.62933832758122, -72.22959674947568, 0.0)], 1602578277.7953522: [(-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0), (-228.6248700408823, -72.2020641575293, 0.0)], 1602578278.301383: [(-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0), (-228.65404941842613, -72.56922015592626, 0.0)], 1602578278.402193: [(-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0), (-228.65052732080093, -72.60443107662209, 0.0)], 1602578278.5030248: [(-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0), (-228.65127171493137, -72.64558496721732, 0.0)], 1602578278.6038744: [(-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0), (-228.65380104763761, -72.6872012711976, 0.0)], 1602578278.7046592: [(-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0), (-228.6544815038236, -72.7267655686929, 0.0)], 1602578278.795392: [(-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0), (-228.65509409245823, -72.76238378994077, 0.0)], 1602578278.896217: [(-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0), (-228.6557748184774, -72.80196377655896, 0.0)], 1602578278.9981284: [(-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0), (-228.65646288068356, -72.84197031684901, 0.0)], 1602578279.0988667: [(-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0), (-228.6571430211257, -72.88151625580151, 0.0)], 1602578283.998702: [(-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0), (-228.62847038895768, -72.56912182371045, 0.0)], 1602578284.099579: [(-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0), (-228.6117167735674, -72.58540273491626, 0.0)], 1602578284.200437: [(-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0), (-228.60584977770208, -72.60525771884447, 0.0)], 1602578284.3012002: [(-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0), (-228.6115480445217, -72.55381588387587, 0.0)], 1602578284.4020526: [(-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0), (-228.61549012002183, -72.50269185459888, 0.0)], 1602578284.5027874: [(-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0), (-228.6184101055786, -72.46036027561595, 0.0)], 1602578284.6035872: [(-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0), (-228.61729804383265, -72.43351619986717, 0.0)], 1602578284.7044306: [(-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0), (-228.61618550405439, -72.40666058488856, 0.0)], 1602578284.7951655: [(-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0), (-228.61518448106582, -72.38249687542763, 0.0)], 1602578284.8959172: [(-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0), (-228.61407295240372, -72.35566566779761, 0.0)], 1602578284.9968555: [(-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0), (-228.64152711380046, -72.41559966573132, 0.0)], 1602578285.0978167: [(-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0), (-228.64807377466414, -72.35879641805884, 0.0)], 1602578285.1988516: [(-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0), (-228.59532735248013, -72.56972032539228, 0.0)], 1602578285.2996747: [(-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0), (-228.58484181930723, -72.55584069354873, 0.0)], 1602578285.40048: [(-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0), (-228.57444139490897, -72.521152501939, 0.0)], 1602578285.5011978: [(-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0), (-228.58804322544802, -72.44773346463529, 0.0)], 1602578285.601981: [(-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0), (-228.6008968415244, -72.37063028857104, 0.0)], 1602578285.7028177: [(-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0), (-228.6118643737542, -72.29547314566457, 0.0)], 1602578285.8036344: [(-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0), (-228.6331464840892, -72.3352854866752, 0.0)], 1602578285.9044755: [(-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0), (-228.65033324324565, -72.3710569142957, 0.0)], 1602578285.9951594: [(-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0), (-228.66000371071954, -72.39855054602205, 0.0)], 1602578286.0959911: [(-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0), (-228.6718557574654, -72.40475483247755, 0.0)], 1602578286.1967912: [(-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0), (-228.68370405929798, -72.4109571585531, 0.0)], 1602578286.2979631: [(-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0), (-228.69559609609925, -72.41718237892528, 0.0)], 1602578286.3987622: [(-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0), (-228.7074443201185, -72.42338466426726, 0.0)]}}
    #
    # print(compare_prediction_paths(exp, real, './ll.png', 1000))

    # compare_line(exp, real,  './tt.png', 900)
