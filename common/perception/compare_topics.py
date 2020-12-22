# -*- coding:utf8 -*-
"""
1. Number of obstacles UUID_ The detection rate was UUID_ Count / T, give the number of UUIDs detected per second,
and draw a line graph
2. The correct semantic, the type and number of semantics, the percentage of correct semantics, the semantic pie chart,
the line chart of semantics per second, and the broken line chart with different semantics
3. Position of obstacles, take x, Y values, form a two-dimensional list in chronological order,
and draw a broken line diagram
List and draw the angle of the obstacle according to the time order
5. The linear velocity line of obstacles, only the values of X and y are taken. The x-axis data forms a list
according to the time sequence and draws a broken line graph. The y-axis data forms a list according to the time order,
and draws the broken line diagram, and gives the average speed of X and Y
6. The second value of prediction information of each point is taken out from the prediction data of obstacles.
The second value predicts the position and direction of the current obstacle after 0.5s.
Get the list like the second and third, and then draw a line chart comparing with 3 and 4.
The starting point of X axis is 0.5s later than that of 3 and 4.
In the later stage, Euclidean distance and cosine similarity processing can be done for the predicted data and
the data of 3 and 4, and the standard deviation can be calculated for data reference
7. The shape of the obstacle, the shape type and corresponding number, the percentage of the correct type,
and the shape pie chart. The list of X and Y is formed in chronological order, and a broken line chart is drawn.
Calculate the standard deviation of X and Y respectively
"""
import logging
import numpy as np
from common.utils.generate_graph import generate_bar, generate_bar_rows, generate_trace_rows, generate_line_rows, \
    generate_pre_path_row, generate_scatter_rows
from common.utils.calculate import cal_std, cal_euc_distance

logger = logging.getLogger()


def compare_uuid(uuid_exp, uuid_rel, save_path, step=2):
    """
    Compare the UUID of two bags and generate pictures
    uuid_ Exp: [2,4], expected UUIDs per second
    uuid_ Rel: [3, 5], the actual number of UUIDs per second
    generate uuid compare graph
    Return bool, standard deviation, description information
    """
    # cal std
    r_bool, std_uuid, diff_list, msg = cal_std(uuid_exp, uuid_rel, step)
    if not r_bool:
        return False, 0, msg
    logger.info('expect and real uuid diff: {diff}, std: {std}'.format(diff=diff_list, std=std_uuid))

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
    for sem, value in sem_dict_exp.items():
        r_bool, std, diff_list, msg = cal_std(value, sem_dict_rel[sem], 1)
        logger.info('semantic: {sem}, expect and real uuid diff: {diff}, std: {std}'.format(sem=sem,
                                                                                            diff=diff_list, std=std))
        if not r_bool:
            return False, msg
        sem_std_dict[sem] = std
        sem_list.append({'data': {'expect semantic': value, 'real semantic': sem_dict_rel[sem]}, 'x_label': 'Second',
                         'y_label': 'Count per second', 'title': 'Semantic: {} expect and real, '
                                                                 'std: {:<8.2f}'.format(sem, std)})

    # Draw a bar chart
    r_bool, msg = generate_bar_rows(sem_list, save_path)
    if not r_bool:
        logger.error(msg)
        return False, msg
    return True, sem_std_dict


def compare_position(position_dict_exp, position_dict_real, exp_pos_all_dict, real_pos_all_dict, save_path,
                     scatter_save_path, max_step=5):
    """
    The position of the two bags is compared and the trajectory is generated
    The keys of the two must be equal
    position_ dict_ Exp: {car ': {T1: (x, y), T2: (x, y)},
    'bus': {T1: (x, y), T2: (x, y)}, # position values in X and Y directions
    position_ dict_ Real: {car ': {T1: (x, y), T2: (x, y)},
    'bus': {T1: (x, y), T2: (x, y)}, # position values in X and Y directions
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
        return False, 'expect position\'s semantic is not equal real\'s semantic: expect semantic {}, ' \
                      'real semantic {}'.format(exp_semantic_list, real_semantic_list)

    ret_dict = {semantic: {} for semantic in exp_semantic_list}
    data_list, scatter_list = [], []
    for semantic, exp_position_dict in position_dict_exp.items():
        real_position_dict = position_dict_real[semantic]

        # 0. Judge the number of two location data, can not be too big difference
        exp_len = len(exp_position_dict.keys())
        real_len = len(real_position_dict.keys())
        max_len = exp_len + max_step
        min_len = exp_len - max_step
        if real_len not in range(min_len, max_len+1):
            logger.info('shape: {}\nposition elements count is not in normal range\nexpect len: {} - {}, '
                        'real len: {}'.format(semantic, min_len, max_len, real_len))
            return False, 'shape: {},position elements count is not in normal range, expect len: {} - {}, ' \
                          'real len: {}'.format(semantic, min_len, max_len, real_len)

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
                          'trace_dict': {'{}_exp'.format(semantic): exp_data_list,
                                         '{}_real'.format(semantic): real_data_list},
                          })
        scatter_list.append({
            'scatter_title': '{sem} Scatter'.format(sem=semantic),
            'scatter_dict': {'{sem}_exp'.format(sem=semantic): exp_pos_all_dict[semantic],
                             '{sem}_real'.format(sem=semantic): real_pos_all_dict[semantic]}
        })
    # 3. draw two trace
    r_bool, msg = generate_trace_rows(data_list, save_path)

    if not r_bool:
        logger.error('generate trace rows failed: {}'.format(msg))
        return False, msg

    # 4. draw scatter picture
    r_bool, msg = generate_scatter_rows(scatter_list, scatter_save_path)
    if not r_bool:
        logger.error('generate scatter rows failed: {}'.format(msg))
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
        return False, 'expect orientation\'s semantic is not equal real\'s semantic: ' \
                      'expect semantic {}, real semantic {}'.format(exp_ori_list, real_ori_list)

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
            return False, 'semantic: {} orientation elements count is not in normal range expect ' \
                          'len: {} - {}, real len: {}'.format(semantic, min_len, max_len, real_len)

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
    'line': {car ': {T1: (x, y), T2: (x, y)},'bus': {T1: (x, y), T2: (x, y)}. According to the classification
    (same as 3), the speed is divided into arrays
    The keys of the two must be equal
    line_dict_exp: {car ': {T1: (x, y), T2: (x, y)},'bus': {T1: (x, y), T2: (x, y)}, # position values in X and Y
    directions
    line_dict_real: {car ': {T1: (x, y), T2: (x, y)},'bus': {T1: (x, y), T2: (x, y)}, # position values in X and Y
    directions
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
        return False, 'expect line\'s semantic is not equal real\'s semantic: ' \
                      'expect semantic {}, real semantic {}'.format(exp_semantic_list, real_semantic_list)

    ret_dict = {semantic: {} for semantic in exp_semantic_list}
    data_list = []
    for semantic, exp_line_dict in line_dict_exp.items():
        real_line_dict = line_dict_real[semantic]

        exp_len = len(exp_line_dict.keys())
        real_len = len(real_line_dict.keys())
        max_len = exp_len + max_step
        min_len = exp_len - max_step
        if real_len not in range(min_len, max_len + 1):
            return False, 'shape: {}\nline elements count is not in normal range\n' \
                          'expect len: {} - {}, real len: {}'.format(semantic, min_len, max_len, real_len)

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
        return False, 'expect prediction_paths\'s semantic is not equal real\'s semantic: ' \
                      'expect prediction_paths semantic {},' \
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
                          'expect len: {} - {}, real len: {}'.format(semantic, min_len, max_len, real_len)

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
        _, paths_diff_2th_xy = cal_euc_distance(exp_2th_xy, real_2th_xy)  # line
        _, paths_diff_3th_xy = cal_euc_distance(exp_3th_xy, real_3th_xy)  # line
        _, paths_diff_2th_ori = cal_euc_distance(exp_2th_ori, real_2th_ori)
        _, paths_diff_3th_ori = cal_euc_distance(exp_3th_ori, real_3th_ori)

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
    'shape ': {car': {T1: (x, y), T2: (x, y)},'bus': {T1: (x, y), T2: (x, y)}}. According to the
    classification (same as 3), shape is divided into arrays
    The keys of the two must be equal
    shape_dict_exp: {car ': {T1: (x, y), T2: (x, y)},'bus': {T1: (x, y), T2: (x, y)}, # position values in X
    and Y directions
    shape_dict_real: {car ': {T1: (x, y), T2: (x, y)},'bus': {T1: (x, y), T2: (x, y)}, # position values in X
    and Y directions
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
        return False, 'expect shape\'s semantic is not equal real\'s semantic: expect semantic {}, ' \
                      'real semantic {}'.format(exp_semantic_list, real_semantic_list)

    ret_dict = {semantic: {'shape_diff_x': [], 'shape_diff_y': [], 'std_x': 0, 'std_y': 0} for
                semantic in exp_semantic_list}

    data_list = []
    for semantic, exp_shape_dict in shape_dict_exp.items():
        real_shape_dict = shape_dict_real[semantic]

        # 0. The number of two shape data should not be too different
        exp_len = len(exp_shape_dict.keys())
        real_len = len(real_shape_dict.keys())
        max_len = exp_len + max_step
        min_len = exp_len - max_step
        if real_len not in range(min_len, max_len + 1):
            return False, 'semantic: {}\nshape elements count is not in normal range\n' \
                          'expect len: {} - {}, real len: {}'.format(semantic, min_len, max_len, real_len)

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
