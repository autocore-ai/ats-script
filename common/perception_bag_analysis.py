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
        self.data_dict = {}

    def analysis(self):
        """
        return dict:
        {
            'uuid_0': {
                        'uuid_sec': [2, 3, 4, 5],  # uuid 每秒出现的次数
                        'semantic': {'type_1': [1, 2, 3, 1], 'type_2': [1, 2, 3, 1] },  # uuid对应的语义，以及每秒出现的次数
                        'position': {'x': [], 'y': []},   # x和y方向的位置值
                        'orientation': [偏向角, 偏向角, 偏向角],   # 偏向角
                        'line': {'x': [], 'y': []},   # x和y方向的线速度
                        'peri_path': [{pose_x: [1, 2, 3], pose_y: [1, 2, 0, 0], orientation: []}, ],   # 预测的位置和方向
                        'shape': {type_0: [1, 2, 3], type_1: [1, 2, 0, 0]},  # 对应的形状和每秒出现的次数
                        },
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
        消息处理
        'uuid_0': {
                        'uuid_sec': [2, 3, 4, 5],  # uuid 每秒出现的次数
                        'semantic': {'type_1': [1, 2, 3, 1], 'type_2': [1, 2, 3, 1] },  # uuid对应的语义，以及每秒出现的次数
                        'position': {'t1': (x, y), 't2': (x, y)},   # x和y方向的位置值
                        # 'position': [],   # x和y方向的位置值
                        'orientation': [偏向角, 偏向角, 偏向角],   # 偏向角
                        'line': {'t1: (x, y), 't2': (x, y)},   # x和y方向的线速度
                        'prediction_paths': [{pose_x: [1, 2, 3], pose_y: [1, 2, 0, 0], orientation: []}, ],   # 预测的位置和方向
                        'shape': {type_0: {sect: [1, 2, 3], t_size: {t: (x, y)}}, type_1: {sect: [1, 2, 3], t_size: {t: (x, y)}}},  # 对应的形状和每秒出现的次数
                        },
        """
        uuid = obj.id.uuid
        if uuid not in self.data_dict:  # 初始化数据类型
            data_struct = {'uuid_sec': [0] * self._sect_len, 'semantic': {}, 'position': {},
                           'orientation': [], 'line': {},
                           'prediction_paths': [{'pose_x': [], 'pose_y': [], 'orientation': []}] * 21,
                           'shape': {}
                           }

            # semantic 处理
            semantic = SEMANTIC[obj.semantic.type]
            semantic_dict = {semantic: [0] * self._sect_len}

            # shape 处理
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
        data_struct['orientation'].append(self.to_euler_angles(obj.state.pose_covariance.pose.orientation))

        # line 处理
        data_struct['line'][mt] = (obj.state.twist_covariance.twist.linear.x, obj.state.twist_covariance.twist.linear.y)
        # data_struct['line']['x'].append(obj.state.twist_covariance.twist.linear.x)
        # data_struct['line']['y'].append(obj.state.twist_covariance.twist.linear.y)

        # prediction_paths 处理 'prediction_paths': [{'pose_x': [], 'pose_y': [], 'orientation': []}] * 21,
        for i, path in enumerate(obj.state.predicted_paths[0].path):
            path_obj = path.pose
            data_struct['prediction_paths'][i]['pose_x'].append(path_obj.pose.position.x)
            data_struct['prediction_paths'][i]['pose_y'].append(path_obj.pose.position.y)
            data_struct['prediction_paths'][i]['orientation'].append(self.to_euler_angles(path_obj.pose.orientation))
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
                        'uuid_sec': [2, 3, 4, 5],  # uuid 每秒出现的次数
                        'semantic': {'type_1': [1, 2, 3, 1], 'type_2': [1, 2, 3, 1] },  # uuid对应的语义，以及每秒出现的次数
                        'position': {'t1': (x, y), 't2': (x, y)},   # x和y方向的位置值
                        # 'position': [],   # x和y方向的位置值
                        'orientation': [偏向角, 偏向角, 偏向角],   # 偏向角
                        'line': {'t1: (x, y), 't2': (x, y)},   # x和y方向的线速度
                        'prediction_paths': [{pose_x: [1, 2, 3], pose_y: [1, 2, 0, 0], orientation: []}, ],   # 预测的位置和方向
                        'shape': {type_0: {sect: [1, 2, 3], t_size: {t: (x, y)}}, type_1: {sect: [1, 2, 3], t_size: {t: (x, y)}}},  # 对应的形状和每秒出现的次数
                        },
        return data_struct
        {
            'uuid': np.array([0]*self._sect_len),  汇总为每秒检出的所有uuid的数量，不区分障碍物
            'semantic': {},  汇总为每秒每种semantic的数量
            'position': {},
            'line':{},  根据分类情况（同3），将速度分成数组
            'shape': {sect: [], t_size: {t: (x, y)}}  汇总每秒每种语义对应的shape类型
        }
        """
        if cat_type == 1:
            data_dict = {'uuid': np.array([0]*self._sect_len), 'semantic': {}, 'position': {}, 'line':{}, 'shape': {}}
        else:
            data_dict = {}
        # 循环数据
        for uuid, data in self.data_dict.items():
            # uuid 汇总为每秒检出的所有uuid的数量，不区分障碍物
            data_dict['uuid'] += np.array(data['uuid_sec'])

            # 语义,位置，线速度，shape 汇总
            for sem, sec_data in data['semantic'].items():
                if sem in data_dict['semantic']:
                    data_dict['semantic'][sem] += np.array(sec_data)
                    data_dict['position'][sem] = data_dict['position'][sem].copy(sec_data['position'])
                    data_dict['line'][sem] = data_dict['line'][sem].copy(sec_data['line'])
                    data_dict['shape'][sem] += np.array(sec_data['shape']['sect'])
                    data_dict['shape'][sem]['t_size'] = data_dict['shape'][sem]['t_size'].copy(sec_data['shape']['t_size'])
                else:
                    data_dict['semantic'][sem] = np.array([0]*self._sect_len)
                    data_dict['position'][sem] = sec_data['position']
                    data_dict['line'][sem] = sec_data['line']
                    data_dict['shape'][sem]['sect'] = np.array(sec_data['shape']['sect'])
                    data_dict['shape'][sem]['t_size'] = sec_data['shape']['t_size']

        return data_dict

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
            ax_position.plot(x, y, marker=mpath.Path(verts, codes), label=label_semantic)
            ax_position.text(x[-1], y[-1], label_semantic)

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


def compare_uuid(data1_struct, data2_struct):
    """
    两个bag的uuid比较
    uuid1:
    """
    pass


if __name__ == '__main__':
    bag_path = '/home/duan/PycharmProjects/auto_test/bag/object_2020-11-04-13-44-28.bag'
    ans = Analysis(bag_path)
    ans.analysis()
    # print(ans.data_dict)
    # for key, data in ans.data_dict.items():
    #     print(key)
    #     print(data)
    ans.show_graph()
