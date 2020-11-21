# -*- coding:utf8 -*-
import rosbag
import hashlib
import math
import os
import numpy as np
import shutil
import rospy
# from tf.transformations import euler_from_quaternion
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from utils.generate_graph import generate_bar, generate_bar_rows, generate_trace_rows, generate_line_rows
from utils.calculate import cal_std, cal_euc_distance
from collections import Counter
import logging
logger = logging.getLogger()


"""
1. 障碍物UUID数量uuid_count，检出率: uuid_count/t，给出每秒检出UUID的数量，并画出折线图
2. 障碍物正确的semantic，出现的semantic类型和分别对应的数量，正确语义所占的百分比，语义饼状图，语义每秒的折线图，不同的语义不同的折线图
3. 障碍物的position，取x,y的值，按照时间顺序组成二维list，并画出折线图
4. 障碍物的orientation，计算偏航角，按照时间顺序组成list，并画出折线图
5. 障碍物的线速度line，只取x和y的值，X轴数据按照时间顺序组成list，并画出折线图, Y轴数据按照时间顺序组成list，并画出折线图，并给出X和Y的平均速度
6. 障碍物的预测数据，取出每个点预测信息的第二个值，第二个值预测的是当前障碍物在0.5s后，所在的位置和方向。像第2和3一样获取list，然后画出和3,4相比较的折线图，预测数据的折线图，X轴的起点较3和4的要晚0.5s。
    后期可将预测的数据和3和4的数据分别做欧氏距离和余弦相似性处理，并计算标准方差，以做数据参考
7. 障碍物的shape, 出现的shape类型和对应的数量，正确类型所占的百分比，shape饼状图。按照时间顺序分别组成X和Y的list，并画出折线图。分别计算X和Y的标准方差
"""
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
    def __init__(self, bag_path):
        self.bag_path = bag_path
        self._sect_len = 0
        self.bag = rosbag.Bag(self.bag_path)
        self.msg_count = self.bag.get_message_count()
        start_time = self.bag.get_start_time()
        end_time = self.bag.get_end_time()
        # self.time_list = np.linspace(start_time, end_time, num=1).data
        self.time_list = []
        self.time_split(start_time, end_time)  # 对时间进行切片
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

    def uuid_md5(self, uuid):
        """对uuid进行md5加密"""
        print(dir(uuid))
        print(type(uuid))
        print(uuid)
        src = str(uuid, encoding='utf-8')
        print(src)
        m2 = hashlib.md5()
        m2.update(src)
        return m2.hexdigest()

    def time_split(self, start, end):
        """
        开始和结束时间分割，间隔为1s
        """
        num = end-start
        self._sect_len = math.ceil(num)
        for i in range(self._sect_len):
            self.time_list.append(end - i)

    def time_section(self, t):
        """
        判断当前时间处在哪一段位
        按秒分割的时间，段位从0开始
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
            # UUID 已经存在的情况处理
            data_struct = self.data_dict[uuid]

            # semantic 处理 'semantic': {'type_1': [1, 2, 3, 1], 'type_2': [1, 2, 3, 1] },  # uuid对应的语义，以及每秒出现的次数
            semantic = SEMANTIC[obj.semantic.type]
            semantic_dict = data_struct['semantic']
            if semantic not in semantic_dict:
                semantic_dict[semantic] = [0] * self._sect_len

            # shape 处理
            shape = SHAPE[obj.shape.type]
            shape_dict = data_struct['shape']
            if shape not in shape_dict:
                shape_dict[shape] = {'sect': [0] * self._sect_len, 't_size': {}}

        # 公共处理方式
        # uuid 处理
        data_struct['uuid_sec'][sect] += 1

        # semantic 处理
        semantic_dict[semantic][sect] += 1
        data_struct['semantic'] = semantic_dict

        # position 处理
        data_struct['position'][mt] = (obj.state.pose_covariance.pose.position.x, obj.state.pose_covariance.pose.position.y)
        # data_struct['position'].append((obj.state.pose_covariance.pose.position.x, obj.state.pose_covariance.pose.position.y))

        # orientation 处理, 此处需要计算偏向角
        data_struct['orientation'][mt] = self.to_euler_angles(obj.state.pose_covariance.pose.orientation)

        # line 处理
        data_struct['line'][mt] = (obj.state.twist_covariance.twist.linear.x, obj.state.twist_covariance.twist.linear.y)
        # data_struct['line']['x'].append(obj.state.twist_covariance.twist.linear.x)
        # data_struct['line']['y'].append(obj.state.twist_covariance.twist.linear.y)

        # prediction_paths 处理 'prediction_paths': [{'pose_x': [], 'pose_y': [], 'orientation': []}] * 21,
        data_struct['prediction_paths'][mt] = []
        for i, path in enumerate(obj.state.predicted_paths[0].path):
            path_obj = path.pose
            data_struct['prediction_paths'][mt].append((path_obj.pose.position.x, path_obj.pose.position.y, self.to_euler_angles(path_obj.pose.orientation)))
            # data_struct['prediction_paths'][i]['pose_x'].append(path_obj.pose.position.x)
            # data_struct['prediction_paths'][i]['pose_y'].append(path_obj.pose.position.y)
            # data_struct['prediction_paths'][i]['orientation'].append(self.to_euler_angles(path_obj.pose.orientation))
        # print(shape_dict[shape]['sect'])
        shape_dict[shape]['sect'][sect] += 1
        shape_dict[shape]['t_size'][mt] = (obj.shape.dimensions.x, obj.shape.dimensions.y)
        # shape_dict[shape]['x'].append(obj.shape.dimensions.x)
        # shape_dict[shape]['y'].append(obj.shape.dimensions.y)
        data_struct['shape'] = shape_dict

        self.data_dict[uuid] = data_struct

    def p_cal(self, orientation):
        """计算偏向角"""
        # return euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])
        return 0

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
        目前仅支持按照语义分类
        将分析的数据汇总
        1. uuid 汇总为每秒检出的所有uuid的数量，不区分障碍物
        2. semantic 汇总为每秒每种semantic的数量
        3. position 根据轨迹图得出的障碍物位置数组，此处需要手动操作，将障碍物分类物体分类，可分局shape和位置分类，具体值需要传入进来cat_type=1，shape，2，位置，目前仅支持1
        4. orientation 暂不分解
        5. line 根据分类情况（同3），将速度分成数组
        6. shape 汇总每秒每种语义对应的shape类型和size
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
            'uuid': np.array([0]*self._sect_len),  汇总为每秒检出的所有uuid的数量，不区分障碍物
            'semantic': {},  汇总为每秒每种semantic的数量
            'position': {'CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}},
            'orientation': {t1: yaw1, t2: yaw2} # t: yaw
            'line':{CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}},  根据分类情况（同3），将速度分成数组
            'shape': {CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}}  汇总每种类型下shape的大小
        }
        """
        if cat_type == 1:
            ret_dict = {'uuid': np.array([0]*self._sect_len), 'semantic': {}, 'position': {}, 'line':{}, 'shape': {}}
        else:
            ret_dict = {}
        # 循环数据
        for uuid, data in self.data_dict.items():
            # uuid 汇总为每秒检出的所有uuid的数量，不区分障碍物
            ret_dict['uuid'] += np.array(data['uuid_sec'])
            # 语义,位置，线速度，shape 汇总
            # print(data['semantic'])
            # sum data by semantic
            for sem, sec_data in data['semantic'].items():
                if sem in ret_dict['semantic']:
                    ret_dict['semantic'][sem] += np.array(sec_data)
                    # print(data['shape'])
                    # print(Counter(ret_dict['position'][sem])+Counter(data['position']))
                    # ret_dict['position'][sem] = dict(ret_dict['position'][sem], **data['position'])
                    ret_dict['position'][sem].update(data['position'])
                    ret_dict['position'][sem].update(data['orientation'])
                    ret_dict['line'][sem].update(data['line'])
                    ret_dict['prediction_paths'][sem].update(data['prediction_paths'])
                    for shape, shape_data in data['shape'].items():  # 忽略掉形状
                        ret_dict['shape'][sem].update(data['shape'][shape]['t_size'])
                    # ret_dict['shape'][sem] = ret_dict['shape'][sem].update(data['shape']['t_size'])

                else:
                    ret_dict['semantic'] = {sem: np.array(sec_data)}
                    # print(data_dict['position'][sem])
                    # print(sec_data)
                    ret_dict['position'] = {sem: data['position']}
                    ret_dict['orientation'] = {sem: data['orientation']}
                    ret_dict['line'] = {sem: data['line']}
                    ret_dict['prediction_paths'] = {sem: data['prediction_paths']}

                    # print(ret_dict['position'])
                    ret_dict['shape'] = {sem: {}}
                    for shape, shape_data in data['shape'].items():  # 忽略掉形状
                        ret_dict['shape'][sem].update(data['shape'][shape]['t_size'])

        return ret_dict

    def show_graph(self):
        """
        将数据画图，并将图片保存到bag所在路径
        1. 障碍物UUID数量uuid_count，检出率: uuid_count/t，给出每秒检出UUID的数量，并画出折线图
        2. 障碍物正确的semantic，出现的semantic类型和分别对应的数量，正确语义所占的百分比，语义饼状图，语义每秒的折线图，不同的语义不同的折线图
        3. 障碍物的position，取x,y的值，按照时间顺序组成二维list，并画出折线图
        4. 障碍物的orientation，计算偏航角，按照时间顺序组成list，并画出折线图
        5. 障碍物的线速度line，只取x和y的值，X轴数据按照时间顺序组成list，并画出折线图, Y轴数据按照时间顺序组成list，并画出折线图，并给出X和Y的平均速度
        6. 障碍物的预测数据，取出每个点预测信息的第二个值，第二个值预测的是当前障碍物在0.5s后，所在的位置和方向。像第2和3一样获取list，然后画出和3,4相比较的折线图，预测数据的折线图，X轴的起点较3和4的要晚0.5s。
            后期可将预测的数据和3和4的数据分别做欧氏距离和余弦相似性处理，并计算标准方差，以做数据参考
        7. 障碍物的shape, 出现的shape类型和对应的数量，正确类型所占的百分比，shape饼状图。按照时间顺序分别组成X和Y的list，并画出折线图。分别计算X和Y的标准方差
        """
        graph_path_dir = self.bag_path.split('.bag')[0]
        os.makedirs(graph_path_dir, exist_ok=True)

        # 分析数据画图
        t_x = range(1, self._sect_len + 1)
        fig_line, ax_line = plt.subplots(figsize=(10, 5))  # uuid 折线图
        uuid_line_path = '{}/uuid.png'.format(graph_path_dir)

        fig_se, (ax0_se, ax1_se) = plt.subplots(2, 1, figsize=(10, 16))  # 语义
        semantic_count_dict = {}   # semantic 数据统计
        semantic_path = '{}/semantic.png'.format(graph_path_dir)  # 图片位置

        # position 轨迹图
        fig_position, ax_position = plt.subplots(figsize=(10, 5))  # 位置 轨迹图
        position_path = '{}/position.png'.format(graph_path_dir)  # 图片位置

        # twist line 折线图
        fig_t, (axx_t, axy_t) = plt.subplots(2, 1, figsize=(10, 16))  # 速度
        twist_path = '{}/twist.png'.format(graph_path_dir)  # 图片位置

        # shape 饼状图，X折线图，Y折线图
        fig_shape, (ax_sec, ax_x, ax_y) = plt.subplots(3, 1, figsize=(10, 24))  # 速度
        shape_path = '{}/shape.png'.format(graph_path_dir)  # 图片位置
        # 循环数据
        for uuid, data in self.data_dict.items():
            label_semantic_list = []  # semantic 列表组
            # semantic 折线图
            for s_type, sec_data in data['semantic'].items():
                ax0_se.plot(range(1, self._sect_len + 1), sec_data, label=s_type)
                if s_type in semantic_count_dict:
                    semantic_count_dict[s_type] += sum(data['semantic'][s_type])
                else:
                    semantic_count_dict[s_type] = sum(data['semantic'][s_type])
                if s_type not in label_semantic_list:
                    label_semantic_list.append(s_type)

            # label, 每个uuid 对应的语义拼接
            label_semantic = '_'.join(label_semantic_list)

            uuid_sec_list = data['uuid_sec']
            # uuid 折线图
            ax_line.plot(t_x, uuid_sec_list, label='{}_{}'.format(uuid, label_semantic))

            # position 轨迹图
            Path = mpath.Path
            path_data = []
            c_f = 0
            # 生成path
            for t in sorted(data['position'].keys()):
                x = data['position'][t][0]
                y = data['position'][t][1]
                # print((x, y))
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
            ax_position.plot(x, y, marker=mpath.Path(verts, codes), label=label_semantic)  # 画轨迹
            ax_position.text(x[-1], y[-1], label_semantic)  # 最后一个点显示文字

            # 偏航角
            # print(data['orientation'])

            # 速度图
            # print(sorted(data['line'].keys()))
            twist_x = [data['line'][item][0] for item in sorted(data['line'].keys())]
            twist_y = [data['line'][item][1] for item in sorted(data['line'].keys())]
            # twist_y = data['line']['y']
            line_x = [i for i in range(0, len(twist_x))]
            axx_t.plot(line_x, twist_x, label=label_semantic)
            axy_t.plot(line_x, twist_y, label=label_semantic)
            axx_t.text(line_x[-1], twist_x[-1], label_semantic)
            axy_t.text(line_x[-1], twist_y[-1], label_semantic)

            # 预测路径图
            # print(data['prediction_paths'])

            # 形状图
            # ax_sec, ax_x, ax_y
            for shape, dt in data['shape'].items():
                ax_sec.plot(t_x, dt['sect'], label='{}_{}'.format(shape, label_semantic))
                x_size = [size[0] for t, size in dt['t_size'].items()]
                y_size = [size[1] for t, size in dt['t_size'].items()]
                x_v = len(x_size)
                ax_x.plot([i for i in range(x_v)], x_size, label='{}_{}'.format(shape, label_semantic))
                ax_y.plot([i for i in range(x_v)], y_size, label='{}_{}'.format(shape, label_semantic))

        # 折线图
        ax_line.set_title('uuid sec graph')
        ax_line.legend()
        fig_line.savefig(uuid_line_path, dpi=600)

        # semantic 饼状图
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

        # 保存位置轨迹图
        ax_position.grid()
        ax_position.axis('equal')
        ax_position.set_title('position line graph')
        ax_position.legend()
        fig_position.savefig(position_path, dpi=600)

        # 保存速度折线图
        axx_t.set_title('twist line x graph')
        axx_t.legend()
        axy_t.set_title('twist line y graph')
        axy_t.legend()
        fig_t.savefig(twist_path, dpi=600)

        # 保存形状图
        ax_sec.set_title('shape second count graph')
        ax_x.set_title('shape size x')
        ax_y.set_title('shape size y')
        ax_sec.legend()
        ax_x.legend()
        ax_y.legend()

        fig_shape.savefig(shape_path, dpi=600)


def compare_uuid(uuid_exp, uuid_rel, save_path):
    """
    两个bag的uuid比较，并生成图片
    uuid_exp: [2, 4], 期望每秒UUID数量
    uuid_rel: [3, 5], 实际每秒UUID数量
    generate uuid compare graph
    return bool, 标准差，描述信息
    """
    # 计算标准差
    r_bool, std_uuid, diff_list, msg = cal_std(uuid_exp, uuid_rel, 1)
    if not r_bool:
        return False, 0, msg
    logger.info('expect and real uuid diff: {}'.format(std_uuid))

    # 画出每秒
    data_list = [{'data': uuid_exp, 'label': 'expect uuid'}, {'data': uuid_rel, 'label': 'real uuid'}]
    r_bool, msg = generate_bar(data_list, save_path, y_label='Count', title='Expect and real uuid count per second')
    if not r_bool:
        logger.error(msg)
        return False, 0, msg
    return True, std_uuid, ''


def compare_semantic(sem_dict_exp, sem_dict_rel, save_path):
    """
    两个bag的semantic比较，并生成图片
    汇总为每秒每种semantic的数量
    sem_dict_exp: {type_1: [1,1,1], type_1: [2,2,2]}, 期望每种semantic每秒数量
    sem_dict_rel: {type_1: [1,1,1], type_1: [2,2,2]}, 实际每种semantic每秒数量
    return bool, 标准差，描述信息
    """
    # 比较 semantic 种类
    exp_category = sem_dict_exp.keys()
    real_category = sem_dict_rel.keys()
    if not sorted(exp_category) == sorted(real_category):
        return False, 'semantic category is not equal, expect val: {}, real val: {}'.format(exp_category, real_category)

    # 初始化返回semantic标准差结果
    sem_std_dict = {key: 0 for key in exp_category}
    # 循环计算每个种类的标准差,并画出每种semantic条状图
    sem_list = []  # 存放每种语义对应的画图信息
    for key, value in sem_dict_exp.items():
        # 计算标准差
        r_bool, std, diff_list, msg = cal_std(value, sem_dict_rel[key], 1)
        if not r_bool:
            return False, msg
        sem_std_dict[key] = std
        sem_list.append({'data': {'expect semantic': value, 'real semantic': sem_dict_rel[key]}, 'x_label': 'Second',
                         'y_label': 'Count per second', 'title': 'Semantic: {} expect and real'.format(key)})

    # 画柱状图
    r_bool, msg = generate_bar_rows(sem_list, save_path)
    if not r_bool:
        logger.error(msg)
        return False, msg
    return True, sem_std_dict


def compare_position(position_dict_exp, position_dict_real, save_path, max_step=5):
    """
    两个bag的位置比较，并生成轨迹图
    两者的key一定是相等的
    position_dict_exp: {'CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}},   # x和y方向的位置值
    position_dict_real: {'CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}},   # x和y方向的位置值
    max_step: 两组数据最多相差的元素数量
    0. 判断两个位置数据的个数，不能相差太大
    1. 计算对应时间点位置的欧氏距离，并返回list
    2. 计算上边list的标准差
    3. 画出两个的轨迹图
    return bool, 位置距离差list，标准差，描述信息
    """
    exp_semantic_list = position_dict_exp.keys()
    real_semantic_list = position_dict_real.keys()
    if sorted(exp_semantic_list) != sorted(real_semantic_list):
        return False, 'expect position\'s semantic is not equal real\'s semantic: expect semantic {}, real semantic {}'.format(exp_semantic_list, real_semantic_list)

    ret_dict = {semantic: {} for semantic in exp_semantic_list}
    data_list = []  # 存放要画每种shape的轨迹数据
    for semantic, exp_position_dict in position_dict_exp.items():
        real_position_dict = position_dict_real[semantic]

        # 0. 判断两个位置数据的个数，不能相差太大
        exp_len = len(exp_position_dict.keys())
        real_len = len(real_position_dict.keys())
        max_len = exp_len + max_step
        min_len = exp_len - max_step
        if real_len not in range(min_len, max_len+1):
            return False, 'shape: {}\nposition elements count is not in normal range\nexpect len: {} - {}, real len: {}'.format(semantic, min_len, max_len, real_len)

        # 1. 计算对应时间点位置的欧氏距离，并返回list
        exp_data_list = [exp_position_dict[t] for t in sorted(exp_position_dict.keys())]
        real_data_list = [real_position_dict[t] for t in sorted(real_position_dict.keys())]
        if exp_len > real_len:
            exp_data_list = exp_data_list[:real_len+1]
        elif exp_len < real_len:
            real_data_list = real_data_list[:exp_len+1]
        r_bool, ret_list = cal_euc_distance(exp_data_list, real_data_list)
        if not r_bool:
            return False, ret_list

        ret_dict[semantic]['distance'] = ret_list  # 相同shape下的距离

        # 2. 计算上边list的标准差
        std = np.std(ret_list)
        logger.info(ret_list)
        logger.info(std)

        ret_dict[semantic]['std'] = std

        # 轨迹图数据拼接
        data_list.append({'trace_title': '{} Trace'.format(semantic),
                          'trace_dict': {'{}_exp'.format(semantic): exp_data_list, '{}_real'.format(semantic): real_data_list},
                          })
    # 3. 画出两个的轨迹图
    r_bool, msg = generate_trace_rows(data_list, save_path)

    if not r_bool:
        logger.error(msg)
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
            return False, 'semantic: {}\norientation elements count is not in normal range\n' \
                          'expect len: {} - {}, real len: {}'.format(semantic, min_len, max_len, real_len)

        # 1. Calculate expect orientation the difference with real orientation
        exp_data_list = [exp_ori_dict[t] for t in sorted(exp_ori_dict.keys())]
        real_data_list = [real_ori_dict[t] for t in sorted(real_ori_dict.keys())]
        if exp_len > real_len:
            exp_data_list = exp_data_list[:real_len + 1]
        elif exp_len < real_len:
            real_data_list = real_data_list[:exp_len + 1]
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
                    'title': '{}_Orientation'.format(semantic),
                    'data': {'ori_exp': exp_data_list, 'ori_real_x': real_data_list, 'ori_diff_x': ret_list}
                }
            )
        )

        # 画出每种语义的下shape x和y以及差值的三条折线图
        r_bool, msg = generate_line_rows(data_list, save_path)

        if not r_bool:
            logger.error(msg)
            return False, msg

    return True, ret_dict


def compare_line(line_dict_exp, line_dict_real, save_path, max_step=5):
    """
    比较线速度
    'line':{CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}},  根据分类情况（同3），将速度分成数组
    两者的key一定是相等的
    line_dict_exp: {'CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}},   # x和y方向的位置值
    line_dict_real: {'CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}},   # x和y方向的位置值
    max_step: 两组数据最多相差的元素数量
    0. 判断两个线速度数据的个数，不能相差太大
    1. 计算对应时间点线速度的欧氏距离，并返回list
    2. 计算上边list的标准差
    3. 画出两个的轨迹图
    return bool, 线速度距离差list，标准差，描述信息
    """
    exp_semantic_list = line_dict_exp.keys()
    real_semantic_list = line_dict_real.keys()
    if sorted(exp_semantic_list) != sorted(real_semantic_list):
        return False, 'expect line\'s semantic is not equal real\'s semantic: expect semantic {}, real semantic {}'.format(
            exp_semantic_list, real_semantic_list)

    ret_dict = {semantic: {} for semantic in exp_semantic_list}
    data_list = []  # 存放要画每种shape的轨迹数据
    for semantic, exp_line_dict in line_dict_exp.items():
        real_line_dict = line_dict_real[semantic]

        # 0. 判断两个位置数据的个数，不能相差太大
        exp_len = len(exp_line_dict.keys())
        real_len = len(real_line_dict.keys())
        max_len = exp_len + max_step
        min_len = exp_len - max_step
        if real_len not in range(min_len, max_len + 1):
            return False, 'shape: {}\nline elements count is not in normal range\nexpect len: {} - {}, real len: {}'.format(
                semantic, min_len, max_len, real_len)

        # 1. 计算对应时间点位置的欧氏距离，并返回list
        exp_data_list = [exp_line_dict[t] for t in sorted(exp_line_dict.keys())]
        real_data_list = [real_line_dict[t] for t in sorted(real_line_dict.keys())]
        if exp_len > real_len:
            exp_data_list = exp_data_list[:real_len + 1]
        elif exp_len < real_len:
            real_data_list = real_data_list[:exp_len + 1]
        r_bool, ret_list = cal_euc_distance(exp_data_list, real_data_list)
        if not r_bool:
            return False, ret_list

        ret_dict[semantic]['distance'] = ret_list  # 相同shape下的距离

        # 2. 计算上边list的标准差
        std = np.std(ret_list)
        ret_dict[semantic]['std'] = std

        # 轨迹图数据拼接
        data_list.append({'trace_title': '{} Trace'.format(semantic),
                          'trace_dict': {'{}_exp'.format(semantic): exp_data_list,
                                         '{}_real'.format(semantic): real_data_list},
                          })
    # 3. 画出两个的轨迹图
    r_bool, msg = generate_trace_rows(data_list, save_path)

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
    graph_list = []  # for graph data
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
            exp_data_list = exp_data_list[:real_len + 1]
        elif exp_len < real_len:
            real_data_list = real_data_list[:exp_len + 1]

        # 1. get 2th and 3th element
        paths_exp_2th = []
        paths_exp_3th = []
        paths_real_2th = []
        paths_real_3th = []
        for i, paths_list in enumerate(exp_data_list):
            paths_exp_2th.append(paths_list[1])
            paths_exp_3th.append(paths_list[2])
            paths_real_2th.append(real_data_list[i][1])
            paths_real_3th.append(real_data_list[i][2])

        # 2. make diff
        paths_diff_2th = np.array(paths_exp_2th) - np.array(paths_real_2th)
        paths_diff_3th = np.array(paths_exp_3th) - np.array(paths_real_3th)

        # 3. cal std
        paths_std_2th = np.std(paths_diff_2th)
        paths_std_3th = np.std(paths_diff_3th)
        ret_dict[semantic] = {'paths_diff_2th': paths_diff_2th, 'paths_diff_3th': paths_diff_3th,
                              'paths_std_2th': paths_std_2th, 'paths_std_3th': paths_std_3th}
        graph_list.append(
            (
                {
                    'title': '{}_Prediction_2Th'.format(semantic),
                    'data': {'Prediction_exp_2th': paths_exp_2th, 'Prediction_real_2th': paths_real_2th,
                             'Prediction_diff_2th': list(paths_diff_2th)}
                },
                {
                    'title': '{}_Prediction_3Th'.format(semantic),
                    'data': {'Prediction_exp_3th': paths_exp_2th, 'Prediction_real_3th': paths_real_2th,
                             'Prediction_diff_3th': list(paths_diff_2th)}
                },
            )
        )
    # make graph
    r_bool, msg = generate_line_rows(graph_list, save_path)

    if not r_bool:
        logger.error(msg)
        return False, msg
    return True, ret_dict





def compare_shape(shape_dict_exp, shape_dict_real, save_path, max_step=5):
    """
    比较shape大小
    'shape': {CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}},  根据分类情况（同3），将shape分成数组
    两者的key一定是相等的
    shape_dict_exp: {'CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}},   # x和y方向的位置值
    shape_dict_real: {'CAR': {t1: (x,y), t2: (x, y)}, 'BUS': {t1: (x,y), t2: (x, y)}},   # x和y方向的位置值
    max_step: 两组数据最多相差的元素数量
    0. 判断两个shape数据的个数，不能相差太大,左右相差不能超过max_step
    1. 计算对应时间点 不同semantic shape x的差值，并返回list
    2. 计算对应时间点 不同semantic shape y的差值，并返回list
    3. 计算上边list的标准差
    4. 画出每种语义的x和y分别的折线图
    return bool, 线速度距离差list，标准差，描述信息
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

        # 0. 判断两个 shape 数据的个数，不能相差太大
        exp_len = len(exp_shape_dict.keys())
        real_len = len(real_shape_dict.keys())
        max_len = exp_len + max_step
        min_len = exp_len - max_step
        if real_len not in range(min_len, max_len + 1):
            return False, 'semantic: {}\nshape elements count is not in normal range\nexpect len: {} - {}, real len: {}'.format(
                semantic, min_len, max_len, real_len)

        # 1. 计算对应时间点 不同semantic shape x的差值，并返回list
        shape_exp_x = [exp_shape_dict[t][0] for t in sorted(exp_shape_dict.keys())]
        shape_real_x = [exp_shape_dict[t][0] for t in sorted(real_shape_dict.keys())]
        # 计算标准差
        r_bool, std, diff_list, msg = cal_std(shape_exp_x, shape_real_x)
        if not r_bool:
            return False, msg
        ret_dict[semantic]['shape_diff_x'] = diff_list
        ret_dict[semantic]['std_x'] = std

        shape_exp_y = [exp_shape_dict[t][1] for t in sorted(exp_shape_dict.keys())]
        shape_real_y = [exp_shape_dict[t][1] for t in sorted(real_shape_dict.keys())]
        r_bool_y, std_y, diff_list_y, msg_y = cal_std(shape_exp_y, shape_real_y)
        if not r_bool_y:
            return False, msg_y
        ret_dict[semantic]['shape_diff_y'] = diff_list_y
        ret_dict[semantic]['std_y'] = std_y
        data_list.append(
            (
                {
                    'title': '{}_Shape_X'.format(semantic),
                    'data': {'shape_exp_x': shape_exp_x, 'shape_real_x': shape_real_x, 'shape_diff_x': diff_list}
                },
                {
                    'title': '{}_Shape_Y'.format(semantic),
                    'data': {'shape_exp_y': shape_exp_y, 'shape_real_y': shape_real_y, 'shape_diff_y': diff_list_y}
                },
            )
        )

    # 画出每种语义的下shape x和y以及差值的三条折线图
    r_bool, msg = generate_line_rows(data_list, save_path)

    if not r_bool:
        logger.error(msg)
        return False, msg
    return True, ret_dict


if __name__ == '__main__':
    bag_path = '/media/duan/OS/bag/moving_p_inner_front_2020-10-13-16-37-15/expect.bag'
    ans = Analysis(bag_path)
    print(ans.msg_count)
    ans.analysis()
    # print(ans.data_dict)
    print(ans.sum_data())
    # for key, data in ans.data_dict.items():
    #     print(key)
    #     print(data)
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