# -*- coding:utf8 -*-
"""生成图片"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import traceback


def generate_bar(data_list, save_path, x_value=[], x_label='', y_label='', title=''):
    """
    generate bar
    data_list = [{‘data’: [1, 2, 3], 'label': 'expect uuid count/second'}, {‘data’: [1, 2, 3], 'label': 'expect uuid count/second'},]
    """
    if not data_list:
        return False, 'data_list can not be empty'

    fig, ax = plt.subplots(figsize=(10, 8))
    # x axis value
    if x_value:
        x = x_value
    else:
        x = np.arange(1, len(data_list[0]['data'])+1)  # the label locations
    width = 0.2  # the width of the bars

    for i, data in enumerate(data_list):
        if i % 2 == 0:
            rects = ax.bar(x - width / 2, data['data'], width, label=data['label'])
        else:
            rects = ax.bar(x + width / 2, data['data'], width, label=data['label'])
        auto_label(ax, rects)

    if x_label:
        ax.set_xlabel(x_label)
    if y_label:
        ax.set_ylabel(y_label)
    if title:
        ax.set_title(title)
    ax.legend()
    fig.tight_layout()
    # plt.show()
    fig.savefig(save_path, dpi=600)
    return True, ''


def generate_bar_rows(data_list, save_path):
    """
    generate bar rows
    data_list = [
        { data: {label1: [1, 2, 3], label2: [1, 2, 3]}, 'x_label': x, 'x_value':[], 'x_label':'', y_label:'', title:''},
        { data: {label1: [1, 2, 3], label2: [1, 2, 3]}, 'x_label': x, 'x_value':[], 'x_label':'', y_label:'', title:''},
        { data: {label1: [1, 2, 3], label2: [1, 2, 3]}, 'x_label': x, 'x_value':[], 'x_label':'', y_label:'', title:''},
    ]
    几个list几个横向图
    """
    if not data_list:
        return False, 'data_list can not be empty'
    # row number
    row = len(data_list)
    fig, ax_list = plt.subplots(row, 1, figsize=(10, 5*row))

    for i, item in enumerate(data_list):
        if isinstance(ax_list, list):
            ax = ax_list[i]
        else:
            ax = ax_list
        d_dict = item['data']
        # x axis value
        if 'x_value' in item and item['x_value']:
            x = item['x_value']
        else:
            x = np.arange(1, len(list(d_dict.values())[0])+1)  # the label locations
        width = 0.2  # the width of the bars

        j = 0
        for label, data in d_dict.items():

            if j % 2 == 0:
                rects = ax.bar(x - width / 2, data, width, label=label)
            else:
                rects = ax.bar(x + width / 2, data, width, label=label)
            auto_label(ax, rects)
            j += 1

        if 'x_label' in item and item['x_label']:
            ax.set_xlabel(item['x_label'])
        if 'v' in item and item['y_label']:
            ax.set_ylabel(item['y_label'])
        if 'title' in item and item['title']:
            ax.set_title(item['title'])
        ax.legend()
    fig.tight_layout()
    # plt.show()
    fig.savefig(save_path, dpi=600)
    return True, ''


def auto_label(ax, rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


def generate_trace_rows(data_list, save_path):
    """画出多行轨迹图
    data_list: [
        {
            'trace_title': 'BUS trace',
            'trace_dict': {'BUS_exp': [(x1, y1), (x2, y2)], 'BUS_real': [(x1, y1), (x2, y2)]}
        },
        {
            'trace_title': 'CAR trace',
            'trace_dict': {'CAR_exp': [(x1, y1), (x2, y2)], 'CAR_real': [(x1, y1), (x2, y2)]}
        },
    ]
    """
    try:
        # position 轨迹图
        row = len(data_list)
        fig, ax_list = plt.subplots(row, 1, figsize=(10, 5*row))  # 位置 轨迹图

        # position 轨迹图
        Path = mpath.Path
        # 循环轨迹
        for i, d_dict in enumerate(data_list):  # 循环每一行的轨迹，得到某行的轨迹数据
            # {
            #             'trace_title': 'BUS trace',
            #             'trace_dict': {'BUS_exp': [(x1, y1), (x2, y2)], 'BUS_real': [(x1, y1), (x2, y2)]}
            #         }
            title = d_dict['trace_title']  # 轨迹图的title
            trace_dict = d_dict['trace_dict']  #　轨迹数据，包含有多个轨迹数据

            if isinstance(ax_list, list):
                ax = ax_list[i]
            else:
                ax = ax_list

            # 循环某轨迹的单个元素，组成path
            for label, trace_list in trace_dict.items():
                # label: 'BUS_exp'
                # trace_list: [(x1, y1), (x2, y2)]
                path_data = []
                c_f = 0
                for x, y in trace_list:  # 循环具体的轨迹
                    # print((x, y))
                    if c_f == 0:
                        path_data.append((Path.MOVETO, (x, y)))
                    elif c_f == len(trace_list):
                        path_data.append((Path.CLOSEPOLY, (x, y)))
                    # elif c_f == 2:
                    #     path_data.append((Path.LINETO, (x, y)))
                    else:
                        path_data.append((Path.CURVE4, (x, y)))
                    c_f += 1

                # print(path_data)
                # 画图
                codes, verts = zip(*path_data)
                path = mpath.Path(verts, codes)
                # patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
                # ax_position.add_patch(patch)
                x, y = zip(*path.vertices)
                ax.plot(x, y, marker=mpath.Path(verts, codes), label=label)  # 画轨迹
                ax.text(x[-1], y[-1], label)  # 最后一个点显示文字

            # 保存位置轨迹图
            ax.grid()
            ax.axis('equal')
            ax.set_title(title)
            ax.legend()
        # plt.show()
        fig.savefig(save_path, dpi=600)
    except:
        # traceback.print_exc()
        return False, '%s' % traceback.format_exc()
    return True, ''


def generate_line_rows(data_list, save_path):
    """
    画多行两列的折线图
    行数由data_dict1的元素个数确性
    data_dict1和data_dict2的元素个数是相等的
    data_list = [
        (
            {title: CAR_Shape_X, data: {'shape_exp_x': [2, 3, 4, 2], 'shape_real_x': [2, 3, 4, 2], 'shape_diff_x': [2, 3, 4, 2]}},
            {title: CAR_Shape_Y, data: {'shape_exp_y': [2, 3, 4, 2], 'shape_real_y': [2, 3, 4, 2], 'shape_diff_y': [2, 3, 4, 2]
        ),
        (
            {title: BUS_Shape_X, data: {'shape_exp_x': [2, 3, 4, 2], 'shape_real_x': [2, 3, 4, 2], 'shape_diff_x': [2, 3, 4, 2]}},
            {title: BUS_Shape_Y, data: {'shape_exp_y': [2, 3, 4, 2], 'shape_real_y': [2, 3, 4, 2], 'shape_diff_y': [2, 3, 4, 2]
        )
        ]
    """
    row = len(data_list)
    col = len(data_list[0])
    fig, ax_list = plt.subplots(row, col, figsize=(10, 5 * row))  # 位置 轨迹图
    # print(ax1_list)
    # print(ax2_list)
    # 开始话折线图
    for i, data_tuple in enumerate(data_list):
        # print(data_tuple)
        if isinstance(ax_list, list):
            ax = ax_list[i]
        else:
            ax = ax_list
        for j, data_dict in enumerate(data_tuple):
            # print(data_dict)
            # 先画 CAR_Shape_X
            title = data_dict['title']
            data = data_dict['data']
            for label, l in data.items():
                ax[j].plot(range(1, len(l)+1), l, label=label)
            ax[j].grid()
            ax[j].axis('equal')
            ax[j].set_title(title)
            ax[j].legend()
    # plt.show()
    fig.savefig(save_path, dpi=600)
    return True, ''


if __name__ == '__main__':
    # generate_bar([{'data': [1, 2, 3, 4], 'label': 'test1 '}, {'data': [1, 2, 13, 4], 'label': 'test2'}], '')
    # data_list = [
    #     {'data': {'label1': [1, 2, 13], 'label2': [1, 2, 3]}, 'title': 'title1'},
    #     {'data': {'label1': [1, 2, 3], 'label2': [1, 2, 3]}, 'title': 'title1'},
    #     {'data': {'label1': [1, 2, 3], 'label2': [1, 2, 3]}, 'title': 'title1'},
    # ]
    # generate_bar_rows(data_list, './semantic.png')
    # data_list = [
    #     {
    #         'trace_title': 'BUS trace',
    #         'trace_dict': {'BUS_exp': [(2,3), (5,7)], 'BUS_real': [(2,3), (5,7)]}
    #     },
    #     {
    #         'trace_title': 'CAR trace',
    #         'trace_dict': {'CAR_exp': [(2,3), (5,7)], 'CAR_real': [(-2,-3), (-5,-7)]}
    #     },
    # ]
    # generate_trace_row(data_list, './position.png')
    data_list = [
        (
            {"title": "CAR_Shape_X", "data": {'shape_exp_x': [2, 3, 4, 2], 'shape_real_x': [2, 3, 4, 2], 'shape_diff_x': [2, 3, 4, 2]}},
            {"title": "CAR_Shape_Y", "data": {'shape_exp_y': [2, 3, 4, 2], 'shape_real_y': [2, 3, 4, 2], 'shape_diff_y': [2, 3, 4, 2]}}
        ),
        (
            {'title': "BUS_Shape_X", 'data': {'shape_exp_x': [2, 3, 4, 2], 'shape_real_x': [2, 3, 4, 2], 'shape_diff_x': [2, 3, 4, 2]}},
            {'title': 'BUS_Shape_Y', 'data': {'shape_exp_y': [2, 3, 4, 2], 'shape_real_y': [2, 3, 4, 2], 'shape_diff_y': [2, 3, 4, 2]}}
        )
        ]
    generate_line_rows(data_list, '')