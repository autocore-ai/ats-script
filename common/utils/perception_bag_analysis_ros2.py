#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@Project ：auto_test 
@File    ：perception_bag_analysis.py
@Date    ：2020/12/18 上午11:11 
"""
import math
import os
import sys
import logging
import numpy as np
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import rosbag
sys.path.append('./../../')
from common.utils.generate_graph import generate_bar, generate_bar_rows, generate_trace_rows, generate_line_rows, \
    generate_pre_path_row, generate_scatter_rows
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
                        'semantic': {'CAR': [1, 2, 3, 1], 'BUS': [1, 2, 3, 1] },  # semantic dict, key: semantic,
                        value: count per second
                        'position': {'t1': (x, y), 't2': (x, y)},   # t: x and y's position
                        'orientation': {t1: yaw1, t2: yaw2} # t: yaw
                        'line': {'t1: (x, y), 't2': (x, y)},   # t: x and y's line speed
                        'prediction_paths': {t1: [(x11, y11, yaw11), (x12, y12, yaw12)],
                        t2: [(x21, y21, yaw21), (x22, y22, yaw22)]},   # position and orientation of prediction
                        'shape': {type_0: {sect: [1, 2, 3], t_size: {t: (x, y)}}, type_1: {sect: [1, 2, 3],
                        t_size: {t: (x, y)}}},  # shape's type and count per second
                        },
        'uuid_1': {......},
        ......
        }

        """
        ans_list = []
        for _, (_, msg, mt) in enumerate(self.bag.read_messages()):
            if not msg.objects:
                continue
            sect = self.time_section(mt.to_sec())  # time segment of the current time
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
        len_time = len(self.time_list) - 1
        sect = 0
        for i, val in enumerate(self.time_list):
            if t > val:
                sect = len_time - i
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
                    'semantic': {'CAR': [1, 2, 3, 1], 'BUS': [1, 2, 3, 1] },  # semantic dict, key: semantic,
                    value: count per second
                    'position': {'t1': (x, y), 't2': (x, y)},   # t: x and y's position
                    'orientation': {t1: yaw1, t2: yaw2} # t: yaw
                    'line': {'t1: (x, y), 't2': (x, y)},   # t: x and y's line speed
                    'prediction_paths': {t1: [(x11, y11, yaw11), (x12, y12, yaw12)],
                    t2: [(x21, y21, yaw21), (x22, y22, yaw22)]},   # position and orientation of prediction
                    'shape': {type_0: {sect: [1, 2, 3], t_size: {t: (x, y)}}, type_1: {sect: [1, 2, 3],
                    t_size: {t: (x, y)}}},  # shape's type and count per second
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

            # semantic 'semantic': {'type_1': [1, 2, 3, 1], 'type_2': [1, 2, 3, 1] },
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
        data_struct['position'][mt] = (obj.state.pose_covariance.pose.position.x,
                                       obj.state.pose_covariance.pose.position.y)

        # orientation
        data_struct['orientation'][mt] = self.to_euler_angles(obj.state.pose_covariance.pose.orientation)

        # line
        data_struct['line'][mt] = (obj.state.twist_covariance.twist.linear.x, obj.state.twist_covariance.twist.linear.y)

        data_struct['prediction_paths'][mt] = []
        for _, path in enumerate(obj.state.predicted_paths[0].path):
            path_obj = path.pose
            data_struct['prediction_paths'][mt].append(
                (path_obj.pose.position.x, path_obj.pose.position.y, self.to_euler_angles(path_obj.pose.orientation))
            )

        shape_dict[shape]['sect'][sect] += 1
        shape_dict[shape]['t_size'][mt] = (obj.shape.dimensions.x, obj.shape.dimensions.y)
        data_struct['shape'] = shape_dict
        self.data_dict[uuid] = data_struct

    def to_euler_angles(self, orientation):
        """w、x、y、z to euler angles"""
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
        3. Position the obstacle position array obtained according to the trajectory diagram.
        Manual operation is required here to classify the obstacles, objects, shapes and positions.
        The specific values need to be passed into cat_ Type = 1, shape, 2, position, currently only 1 is supported
        4. Orientation will not be decomposed for the time being
        5. Line divide the speed into arrays according to the classification (the same as 3)
        6. Shape summarizes the shape type and size corresponding to each semantics per second
        'uuid_0': {
                        'uuid_sec': [2, 3, 4, 5],  # uuid count per second for checking out object percent
                        'semantic': {'CAR': [1, 2, 3, 1], 'BUS': [1, 2, 3, 1] },  # semantic dict, key: semantic,
                        value: count per second
                        'position': {'t1': (x, y), 't2': (x, y)},   # t: x and y's position
                        'orientation': {t1: yaw1, t2: yaw2} # t: yaw
                        'line': {'t1: (x, y), 't2': (x, y)},   # t: x and y's line speed
                        'prediction_paths': {t1: [(x11, y11, yaw11), (x12, y12, yaw12)], t2: [(x21, y21, yaw21),
                        (x22, y22, yaw22)]},   # position and orientation of prediction
                        'shape': {type_0: {sect: [1, 2, 3], t_size: {t: (x, y)}}, type_1: {sect: [1, 2, 3],
                        t_size: {t: (x, y)}}},  # shape's type and count per second
                        },
        return data_struct
        {
            'uuid': np.array([0]*self._sect_len),  Sum up the number of all UUIDs detected per second,
            regardless of obstacles
            'semantic': {},  Sum up to the number of each semantic per second
            'position': {'CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}},
            'orientation': {t1: yaw1, t2: yaw2} # t: yaw
            'line':{CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}},
            'shape': {CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}}
        }
        """
        if cat_type == 1:  # according to semantic
            ret_dict = {'uuid': np.array([0]*self._sect_len), 'semantic': {}, 'position': {}, 'position_all': {},
                        'line': {}, 'shape': {}, 'orientation': {}, 'prediction_paths': {}}
        else:
            ret_dict = {}

        for _, data in self.data_dict.items():
            ret_dict['uuid'] += np.array(data['uuid_sec'])
            # sum data by semantic
            for sem, sec_data in data['semantic'].items():
                if sem in ret_dict['semantic']:
                    ret_dict['semantic'][sem] += np.array(sec_data)
                    ret_dict['position'][sem].update(data['position'])
                    ret_dict['position_all'][sem].extend(list(data['position'].values()))
                    ret_dict['orientation'][sem].update(data['orientation'])
                    ret_dict['line'][sem].update(data['line'])
                    ret_dict['prediction_paths'][sem].update(data['prediction_paths'])
                    for _, shape_data in data['shape'].items():
                        ret_dict['shape'][sem].update(shape_data['t_size'])

                else:
                    ret_dict['semantic'][sem] = np.array(sec_data)
                    # print(data_dict['position'][sem])
                    ret_dict['position'][sem] = data['position']
                    ret_dict['position_all'][sem] = list(data['position'].values())
                    ret_dict['orientation'][sem] = data['orientation']
                    ret_dict['line'][sem] = data['line']
                    ret_dict['prediction_paths'][sem] = data['prediction_paths']

                    ret_dict['shape'][sem] = {}
                    for _, shape_data in data['shape'].items():
                        ret_dict['shape'][sem].update(shape_data['t_size'])

        return ret_dict

    def show_graph_after_sum(self):
        """
        After sum rosbag data, draw picture
        1. uuid count per second
        2. semantic count per second
        3. position, trace by semantic
        4. position_all, scatter plot
        5. line, x and y line graph
        6. orientation, line graph
        7. prediction_paths, trace
        8. shape, x and y line
        :return:
        """
        sum_data_dict = self.sum_data(1)
        graph_path_dir = self.bag_path.split('.bag')[0]
        os.makedirs(graph_path_dir, exist_ok=True)

        # uuid count per second
        uuid_bar_data = [{'data': sum_data_dict['uuid'], 'label': 'uuid count'}]
        uuid_bar_path = '{}/uuid_sum.png'.format(graph_path_dir)
        r_bool, msg = generate_bar(uuid_bar_data, uuid_bar_path, y_label='Count',
                                   title='uuid count per second, sum: {}'.format(sum(sum_data_dict['uuid'])))
        if not r_bool:
            print(msg)
            return
        print('generate uuid sum graph successfully')

        # semantic count per second
        semantic_bar_path = '{}/semantic_sum.png'.format(graph_path_dir)
        semantic_bar_data = []
        for sem, count_list in sum_data_dict['semantic'].items():
            semantic_bar_data.append({'data': {'{} count'.format(sem): count_list},
                                      'x_label': 'Second',
                                      'y_label': '{} count'.format(sem)})
        r_bool, msg = generate_bar_rows(semantic_bar_data, semantic_bar_path)
        if not r_bool:
            print(msg)
            return
        print('generate semantic sum graph successfully')

        # line speed
        line_speed_path = '{}/line_sum.png'.format(graph_path_dir)
        line_speed_data = []
        for sem, speed_dict in sum_data_dict['line'].items():
            speed_order_dict = [speed_dict[t] for t in sorted(speed_dict.keys())]
            x_speed = [s[0] for s in speed_order_dict]
            y_speed = [s[1] for s in speed_order_dict]
            line_speed_data.append((
                {'title': '{}_X Line Speed, avg: {:<8.2f}'.format(sem, np.mean(x_speed)),
                 'data': {'{}_x'.format(sem): x_speed}
                 },
                {'title': '{}_Y Line Speed, avg: {:<8.2f}'.format(sem, np.mean(y_speed)),
                 'data': {'{}_y'.format(sem): y_speed}
                 },
            ))

        r_bool, msg = generate_line_rows(line_speed_data, line_speed_path)
        if not r_bool:
            print(msg)
            return
        print('generate line speed sum graph successfully')

        # position
        position_path = '{}/position_trace_sum.png'.format(graph_path_dir)
        position_scatter_path = '{}/position_scatter_sum.png'.format(graph_path_dir)
        position_trace_data = []
        position_scatter_data = []
        for sem, position_dict in sum_data_dict['position'].items():
            # trace data
            position_trace_data.append({'trace_title': '{} Trace'.format(sem),
                                        'trace_dict':
                                        {'{}'.format(sem): [position_dict[t] for t in sorted(position_dict.keys())]},
                              })
            position_scatter_data.append({
                'scatter_title': '{sem} Scatter'.format(sem=sem),
                'scatter_dict': {'{sem}'.format(sem=sem): sum_data_dict['position_all'][sem]}
            })

        # draw two trace
        r_bool, msg = generate_trace_rows(position_trace_data, position_path)
        if not r_bool:
            print(msg)
            return
        r_bool, msg = generate_scatter_rows(position_scatter_data, position_scatter_path)
        if not r_bool:
            print(msg)
            return
        print('generate position trace and scatter graph successfully')

        # orientation
        ori_path = '{}/orientation_sum.png'.format(graph_path_dir)
        ori_data_list = []
        for sem, ori_dict in sum_data_dict['orientation'].items():
            ori_data_list.append({
                'title': '{}_Orientation'.format(sem),
                'data': {'ori': [ori_dict[t] for t in sorted(ori_dict.keys())]}
            })

        r_bool, msg = generate_line_rows(ori_data_list, ori_path)
        if not r_bool:
            print(msg)
            return
        print('generate orientation sum graph successfully')

        # prediction_paths
        pre_path = '{}/pre_path_sum.png'.format(graph_path_dir)
        pre_data_dict = {}
        for sem, pre_dict in sum_data_dict['prediction_paths'].items():
            pre_list = [pre_dict[t] for t in sorted(pre_dict.keys())]
            paths_2th = [path[1] for path in pre_list if len(path) > 1]
            paths_3th = [path[2] for path in pre_list if len(path) > 2]
            path_2xy = [(p[0], p[1]) for p in paths_2th]
            path_2ori = [p[2] for p in paths_2th]
            path_3xy = [(p[0], p[1]) for p in paths_3th]
            path_3ori = [p[2] for p in paths_3th]
            graph_data_s = [
                # the 2nd pre path
                (
                    # xy trace
                    {
                        'title': 'The 2nd xy trace of {}\'s Prediction Path'.format(sem),
                        'trace_dict': {'{}_xy'.format(sem): path_2xy}
                    },
                    # ori line (exp, real, diff)
                    {
                        'title': 'The 2nd orientation of {}\'s'.format(sem),
                        'line_data': {'{}_ori'.format(sem): path_2ori},
                    }
                ),
                # the 3rd pre path
                (
                    # xy trace
                    {
                        'title': 'The 3nd xy trace of {}\'s Prediction Path'.format(sem),
                        'trace_dict': {'{}_xy'.format(sem): path_3xy}
                    },
                    # ori line (exp, real, diff)
                    {
                        'title': 'The 3nd orientation of {}\'s'.format(sem),
                        'line_data': {'{}_ori'.format(sem): path_3ori},
                    }
                )
            ]
            pre_data_dict[sem] = graph_data_s
        # make graph
        r_bool, msg = generate_pre_path_row(pre_data_dict, pre_path)
        if not r_bool:
            print(msg)
            return
        print('generate prediction path sum graph successfully')

        # shape
        shape_path = '{}/shape_sum.png'.format(graph_path_dir)
        shape_data_list = []
        for sem, shape_dict in sum_data_dict['shape'].items():
            shape_order = [shape_dict[t] for t in sorted(shape_dict.keys())]
            shape_x = [shape[0] for shape in shape_order]
            shape_y = [shape[1] for shape in shape_order]
            shape_data_list.append(
                (
                    {
                        'title': '{}_Shape_X, avg: {:<6.2f}, '
                                 'std: {:<6.2f}'.format(sem, np.mean(shape_x), np.std(shape_x)),
                        'data': {'shape_x': shape_x}
                    },
                    {
                        'title': '{}_Shape_Y, avg: {:<6.2f}, '
                                 'std: {:<6.2f}'.format(sem, np.mean(shape_y), np.std(shape_y)),
                        'data': {'shape_y': shape_y}
                    },
                )
            )

        # Draw the bottom shape X and Y and the three line graph of the difference
        r_bool, msg = generate_line_rows(shape_data_list, shape_path)
        if not r_bool:
            print(msg)
            return
        print('generate shape sum graph successfully')
        print('generate all graph successfully')

    def show_graph(self):
        """
        1. Number of obstacles UUID_ The detection rate was UUID_ Count / T, give the number of UUIDs detected
        per second, and draw a line graph
        2. The correct semantic, the type and number of semantics, the percentage of correct semantics,
        the semantic pie chart, the line chart of semantics per second, and the broken line chart
        with different semantics
        3. Position of obstacles, take x, Y values, form a two-dimensional list in chronological order,
        and draw a broken line diagram
        List and draw the angle of the obstacle according to the time order
        5. The linear velocity line of obstacles, only the values of X and y are taken. The x-axis data forms a list
        according to the time sequence and draws a broken line graph. The y-axis data forms a list
        according to the time order, and draws the broken line diagram, and gives the average speed of X and Y
        6. The second value of prediction information of each point is taken out from the prediction data of obstacles.
        The second value predicts the position and direction of the current obstacle after 0.5s. Get the list like the
        second and third, and then draw a line chart comparing with 3 and 4. The starting point of X axis is 0.5s later
        than that of 3 and 4.
            In the later stage, Euclidean distance and cosine similarity processing can be done for the predicted data
            and the data of 3 and 4, and the standard deviation can be calculated for data reference
        7. The shape of the obstacle, the shape type and corresponding number, the percentage of the correct type, and
        the shape pie chart. The list of X and Y is formed in chronological order, and a broken line chart is drawn.
        Calculate the standard deviation of X and Y respectively
        """
        graph_path_dir = self.bag_path.split('.bag')[0]
        os.makedirs(graph_path_dir, exist_ok=True)

        # analysis data and make pic
        t_x = range(1, self._sect_len + 1)
        fig_line, ax_line = plt.subplots(figsize=(10, 5))
        uuid_line_path = '{}/uuid.png'.format(graph_path_dir)
        print(uuid_line_path)

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


if __name__ == '__main__':
    argv_list = sys.argv
    if len(argv_list) < 2:
        print('please input bag path')
    else:
        bag_path = argv_list[1]
        ans = Analysis(bag_path)
        ans.analysis()
        ans.show_graph_after_sum()
