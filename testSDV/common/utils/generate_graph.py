# -*- coding:utf8 -*-
"""generate picture"""

import logging
import traceback

import numpy as np
import gc
import matplotlib.path as mpath
import matplotlib.pyplot as plt
logger = logging.getLogger()


def generate_bar(data_list, save_path, x_value=None, x_label='', y_label='', title=''):
    """
    generate bar
    data_list = [{‘data’: [1, 2, 3], 'label': 'expect uuid count/second'},
    {‘data’: [1, 2, 3], 'label': 'expect uuid count/second'},]
    """
    if not data_list:
        return False, 'data_list can not be empty'

    fig, ax = plt.subplots(figsize=(10, 8))
    # x axis value
    if x_value:
        x_list = x_value
    else:
        x_list = np.arange(1, len(data_list[0]['data'])+1)  # the label locations
    width = 0.2  # the width of the bars

    for i, data in enumerate(data_list):
        if i % 2 == 0:
            rects = ax.bar(x_list - width / 2, data['data'], width, label=data['label'])
        else:
            rects = ax.bar(x_list + width / 2, data['data'], width, label=data['label'])
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
    plt.close('all')
    gc.collect()
    return True, ''


def generate_bar_rows(data_list, save_path):
    """
    generate bar rows
    data_list = [
        { data: {label1: [1, 2, 3], label2: [1, 2, 3]}, 'x_label': x, 'x_value':[], 'x_label':'', y_label:'', title:''},
        { data: {label1: [1, 2, 3], label2: [1, 2, 3]}, 'x_label': x, 'x_value':[], 'x_label':'', y_label:'', title:''},
        { data: {label1: [1, 2, 3], label2: [1, 2, 3]}, 'x_label': x, 'x_value':[], 'x_label':'', y_label:'', title:''},
    ]
    """
    if not data_list:
        return False, 'data_list can not be empty'
    # row number
    row = len(data_list)
    fig, ax_list = plt.subplots(row, 1, figsize=(10, 5*row))
    for i, item in enumerate(data_list):
        if row == 1:
            ax = ax_list
        else:
            ax = ax_list[i]
        d_dict = item['data']
        # x axis value
        if 'x_value' in item and item['x_value']:
            x_list = item['x_value']
        else:
            x_list = np.arange(1, len(list(d_dict.values())[0])+1)  # the label locations
        width = 0.2  # the width of the bars

        j = 0
        for label, data in d_dict.items():

            if j % 2 == 0:
                rects = ax.bar(x_list - width / 2, data, width, label=label)
            else:
                rects = ax.bar(x_list + width / 2, data, width, label=label)
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
    plt.close('all')
    gc.collect()
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
    """Draw a multi line trajectory
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
        row = len(data_list)
        fig, ax_list = plt.subplots(row, 1, figsize=(10, 5*row))

        # position trace
        Path = mpath.Path
        # Loop the trajectory of each row to get the trajectory data of a row
        for i, d_dict in enumerate(data_list):
            # {
            #             'trace_title': 'BUS trace',
            #             'trace_dict': {'BUS_exp': [(x1, y1), (x2, y2)], 'BUS_real': [(x1, y1), (x2, y2)]}
            #         }
            title = d_dict['trace_title']
            trace_dict = d_dict['trace_dict']  # Track data, including multiple track data

            if row == 1:
                ax = ax_list
            else:
                ax = ax_list[i]

            # Loop the individual elements of a track to form a path
            for label, trace_list in trace_dict.items():
                # label: 'BUS_exp'
                # trace_list: [(x1, y1), (x2, y2)]
                path_data = []
                c_f = 0
                for x, y in trace_list:
                    # print((x, y))
                    if c_f == 0:
                        path_data.append((Path.MOVETO, (x, y)))
                    else:
                        path_data.append((Path.LINETO, (x, y)))
                    c_f += 1

                # print(path_data)
                # make pic
                codes, verts = zip(*path_data)
                path = mpath.Path(verts, codes)
                # patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
                # ax_position.add_patch(patch)
                x, y = zip(*path.vertices)
                ax.plot(x, y, marker=mpath.Path(verts, codes), label=label)  # trace
                ax.text(x[-1], y[-1], label)  # The last point displays the text

            # Save position trajectory
            ax.grid()
            # ax.axis('equal')
            ax.set_title(title)
            ax.legend()
        # plt.show()
        fig.savefig(save_path, dpi=600)
        plt.close('all')
        gc.collect()
    except Exception as e:
        logger.exception(e)
        return False, '%s' % traceback.format_exc()
    return True, ''


def generate_line_rows(data_list, save_path):
    """
    Draw a line chart with multiple rows and two columns
    The number of rows is determined by data_ The number of elements of dict1
    data_ Dict1 and data_ The number of elements in dict2 is equal
    data_list = [
        (
            {title: CAR_Shape_X, data: {'shape_exp_x': [2, 3, 4, 2], 'shape_real_x': [2, 3, 4, 2],
            'shape_diff_x': [2, 3, 4, 2]}},
            {title: CAR_Shape_Y, data: {'shape_exp_y': [2, 3, 4, 2], 'shape_real_y': [2, 3, 4, 2],
            'shape_diff_y': [2, 3, 4, 2]
        ),
        (
            {title: BUS_Shape_X, data: {'shape_exp_x': [2, 3, 4, 2], 'shape_real_x': [2, 3, 4, 2],
            'shape_diff_x': [2, 3, 4, 2]}},
            {title: BUS_Shape_Y, data: {'shape_exp_y': [2, 3, 4, 2], 'shape_real_y': [2, 3, 4, 2],
            'shape_diff_y': [2, 3, 4, 2]
        )
        ]
    """
    row = len(data_list)
    if isinstance(data_list[0], dict):
        col = 1
    else:
        col = len(data_list[0])

    fig, ax_list = plt.subplots(row, col, figsize=(10, 5 * row))
    if isinstance(ax_list, np.ndarray):
        ax_list = ax_list.tolist()

    # begin to make line graph
    for i, data_tuple in enumerate(data_list):
        if row == 1:
            ax = ax_list
        else:
            ax = ax_list[i]

        if isinstance(data_tuple, tuple):
            for j, data_dict in enumerate(data_tuple):
                # CAR_Shape_X
                axe = ax
                if col != 1:
                    axe = ax[j]
                title = data_dict['title']
                data = data_dict['data']
                for label, d_list in data.items():
                    data_len = len(d_list) + 1
                    axe.plot(range(1, data_len), d_list, label=label)
                axe.grid()
                # axe.axis('equal')
                axe.set_title(title)
                axe.legend()
        else:
            title = data_tuple['title']
            data = data_tuple['data']
            for label, d_list in data.items():
                data_len = len(d_list) + 1
                ax.plot(range(1, data_len), d_list, label=label)
            ax.grid()
            # ax.axis('equal')
            ax.set_title(title)
            ax.legend()
    # plt.show()
    fig.savefig(save_path, dpi=600)
    plt.close('all')
    gc.collect()
    return True, ''


def generate_pre_path_row(data_dict, save_path):
    """
    for pre path
    data_dict:
    { 'CAR':
        [
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
                        'title': 'The 2nd xy eul of {}\'s, std: {}'.format(semantic, paths_std_2th_xy),
                        'line_data': {'{}_xy_eul'.format(semantic): paths_diff_2th_xy}
                    },
                    # ori line (exp, real, diff)
                    {
                        'title': 'The 2nd orientation of {}\'s, std: {}'.format(semantic, paths_std_2th_ori),
                        'line_data': {'{}_ori_exp'.format(semantic): exp_2th_ori,
                                      '{}_ori_real'.format(semantic): real_2th_ori,
                                      '{}_ori_diff'.format(semantic): paths_diff_2th_ori}
                    }
                ),
                # the 3rd pre path
                (
                    # xy trace
                    {
                        'title': 'The 3nd xy trace of {}\'s Prediction Path'.format(semantic),
                        'trace_dict': {'{}_xy_exp'.format(semantic): exp_3th_xy,
                                       '{}_xy_real'.format(semantic): real_3th_xy
                                       }
                    },
                    # xy eul line graph
                    {
                        'title': 'The 3nd xy eul of {}\'s, std: {}'.format(semantic, paths_std_3th_xy),
                        'line_data': {'{}_xy_eul'.format(semantic): paths_diff_3th_xy}
                    },
                    # ori line (exp, real, diff)
                    {
                        'title': 'The 3nd orientation of {}\'s, std: {}'.format(semantic, paths_std_3th_ori),
                        'line_data': {'{}_ori_exp'.format(semantic): exp_3th_ori,
                                      '{}_ori_real'.format(semantic): real_3th_ori,
                                      '{}_ori_diff'.format(semantic): paths_diff_3th_ori}
                    }
                ),
            ]
    }
    """
    sem_count = len(data_dict.keys())
    row = sem_count * 2  # 2nd and 3rd
    col = len(list(data_dict.values())[0])
    fig, ax_list = plt.subplots(row, col, figsize=(15, 5 * row))  # 位置 轨迹图
    # begin to make graph
    Path = mpath.Path
    i = 0
    for sem, data_list in data_dict.items():
        ax_tuple = ax_list[i:i+2]
        i += 2
        for j, data_tuple in enumerate(data_list):
            # xy trace
            # xy eul line
            # orientation line
            ax_trace = ax_tuple[j][0]
            ax_eul_line = ax_tuple[j][1]
            if col > 2:
                ax_ori_line = ax_tuple[j][2]

            # trace
            trace_title = data_tuple[0]['title']
            trace_dict = data_tuple[0]['trace_dict']
            for label, d in trace_dict.items():
                path_data = []
                c_f = 0
                for x, y in d:
                    if c_f == 0:
                        path_data.append((Path.MOVETO, (x, y)))
                    elif c_f == len(d):
                        path_data.append((Path.CLOSEPOLY, (x, y)))
                    else:
                        path_data.append((Path.CURVE4, (x, y)))
                    c_f += 1
                codes, verts = zip(*path_data)
                path = mpath.Path(verts, codes)
                x, y = zip(*path.vertices)
                ax_trace.plot(x, y, marker=mpath.Path(verts, codes), label=label)  # 画轨迹
                ax_trace.text(x[-1], y[-1], label)
            ax_trace.set_title(trace_title)
            ax_trace.grid()
            ax_trace.legend()

            # ax_eul_line
            eul_title = data_tuple[1]['title']
            eul_line_dict = data_tuple[1]['line_data']
            for label, d_list in eul_line_dict.items():
                data_len = len(d_list) + 1
                ax_eul_line.plot(range(1, data_len), d_list, label=label)
            ax_eul_line.set_title(eul_title)
            ax_eul_line.grid()
            ax_eul_line.legend()

            if col > 2:
                # ax_ori_line
                ori_title = data_tuple[2]['title']
                ori_line_dict = data_tuple[2]['line_data']
                for label, d in ori_line_dict.items():
                    data_len = len(d) + 1
                    ax_ori_line.plot(range(1, data_len), d, label=label)
                ax_ori_line.set_title(ori_title)
                ax_ori_line.grid()
                ax_ori_line.legend()
    # plt.show()
    fig.savefig(save_path)
    plt.close('all')
    gc.collect()
    return True, ''


def generate_scatter_rows(scatter_list, save_path):
    """Draw a multi line scatter
    scatter_list: [
        {
            'scatter_title': 'BUS scatter',
            'scatter_dict': {'BUS_exp': [(x1, y1), (x2, y2)], 'BUS_real': [(x1, y1), (x2, y2)]}
        },
        {
            'scatter_title': 'CAR scatter',
            'scatter_dict': {'CAR_exp': [(x1, y1), (x2, y2)], 'CAR_real': [(x1, y1), (x2, y2)]}
        },
    ]
    """
    try:
        row = len(scatter_list)
        fig, ax_list = plt.subplots(row, 1, figsize=(10, 5*row))

        for i, scatter in enumerate(scatter_list):
            if row == 1:
                ax = ax_list
            else:
                ax = ax_list[i]
            scatter_title = scatter['scatter_title']
            for key, sca in scatter['scatter_dict'].items():
                scatter_x = [d[0] for d in sca]
                scatter_y = [d[1] for d in sca]
                ax.scatter(scatter_x, scatter_y, label=key,
                           alpha=0.3, edgecolors='none')
            ax.grid()
            ax.set_title(scatter_title)
            ax.legend()
        fig.savefig(save_path, dpi=600)
        plt.close('all')
        gc.collect()

    except Exception as e:
        # traceback.print_exc()
        logger.exception(e)
        return False, '%s' % traceback.format_exc()
    return True, ''
