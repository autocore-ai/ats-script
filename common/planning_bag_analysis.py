"""
1.pose x , y 分别取值
2. 偏航角差值计算

1.bag， groundtruth bag, 进行点数对比分析判断
2.position 比较两组数据的均值、方差，必要的话用f检验看看其是否有显著性差异
取出bag 文件,
"""
import numpy as np
import pandas as pd
import os
import mpl_toolkits.axisartist.axislines as axislines
import re

# csv to df
def csv_to_df(csv1,csv2):
    a = pd.read_csv(csv1)
    b = pd.read_csv(csv2)
    return a,b

#a,b计算点数计算
def point_count(a,b):
    a_col = a.columns
    a_last_num = a_col[-1]
    a_last_num = int(re.sub("\D", "", a_last_num))
    b_col = b.columns
    b_last_num = b_col[-1]
    b_last_num = int(re.sub("\D", "", b_last_num))
    return a_last_num, b_last_num

#每个点欧式距离计算
def eur_calculate(a,b,point_num):
    ac,bc=point_count(a,b)
    if ac == bc :
        a_col = a.columns
        b_col = b.columns
        keyword = str("points" + str(point_num) + ".pose.position.x" )
        keyword1 = str("points" + str(point_num) + ".pose.position.y")
        for i in a_col:
            if keyword in str(i):
                dfx_a = a[i]
                dfx_b = b[i]
            if keyword1 in str(i):
                dfy_a = a[i]
                dfy_b = b[i]

        df_all= np.sqrt((dfx_a-dfx_b)**2+(dfy_a-dfy_b)**2)
        key = "eu_distance of "+str(point_num)
    return key, df_all

#全部点的欧式距离，然后重新组合成Dataframe
def eu_dataFrame(a,b):
    a_num,b_num=point_count(a,b)
    print("there are "+ str(a_num) + " points")
    df_eu = pd.DataFrame()
    for i in range(0, a_num + 1):
        key, df = eur_calculate(a, b, i)
        df_eu[key] = df
    print(df_eu.head(20))
    return df_eu

# 偏航角计算
import math
def to_euler_angles(w, x, y, z):
    """w、x、y、z to euler angles"""
    angles = {'pitch': 0.0, 'roll': 0.0, 'yaw': 0.0}
    r = math.atan2(2*(w*x+y*z),1-2*(x*x+y*y))
    # p = math.asin(2*(w*y-z*z))
    y = math.atan2(2*(w*z+x*y),1-2*(z*z+y*y))

    angles['roll'] = r*180/math.pi
    # angles['pitch'] = p*180/math.pi
    angles['yaw'] = y*180/math.pi
    return angles['yaw']

def ori_angel(a_angle):
    a_w=[]
    a_x=[]
    a_y=[]
    a_z=[]
    a_w = a_angle[0]
    a_x =a_angle[1]
    a_y = a_angle[2]
    a_z = a_angle[3]
    return a_w, a_x, a_y, a_z

#每个点的偏航角
def orientation_one_point(a,b,point_num,four_angles):
        a_col = a.columns
        b_col = b.columns
        a_angle=[]
        b_angle=[]
        for angle in four_angles:
            keyword = str("points" + str(point_num) + ".pose.orientation."+angle)
            # 找dataframe中存在的column
            for i in a_col:
                if keyword in str(i):
                    a_result = a[i].tolist()
            for i in b_col:
                if keyword in str(i):
                    b_result = b[i].tolist()
            a_angle.append(a_result)
            b_angle.append(b_result)
        a_w, a_x, a_y, a_z = ori_angel(a_angle)
        b_w, b_x, b_y, b_z = ori_angel(b_angle)
        a_yaw_list=[]
        b_yaw_list = []
        c_yaw_list=[]
        mean_c_yaw_list=[]
        for i in range(len(a_w)):
            a_yaw= to_euler_angles(a_w[i],a_x[i],a_y[i],a_z[i])
            b_yaw= to_euler_angles(b_w[i], b_x[i], b_y[i], b_z[i])
            c_yaw= abs(a_yaw) - abs(b_yaw)#偏航角之差
            a_yaw_list.append(a_yaw)
            b_yaw_list.append(b_yaw)
            c_yaw_list.append(c_yaw)
        return c_yaw_list

#集合所有点的偏航角之差
def yaw_df(a,b):
    a_num,b_num= point_count(a,b)
    c_all_dict={}
    for i in range(0,a_num+1):

        c_dict= orientation_one_point(a,b,i,["w","x","y","z"])
        c_all_dict["delta yaw "+str(i)]=c_dict
    yaw_df = pd.DataFrame(c_all_dict)
    return yaw_df

#选取异样值
def extract(df1,df2):
    for i in df1.columns:
        df1_reuslt = df1.loc[df1[i] > 1]

    return df1_reuslt

import matplotlib.pyplot as plt
# plot欧式距离差
def plot_eur(a,b):
    df1= eu_dataFrame(a,b)
    df_ex=df1["eu_distance of 0"]
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.plot([i for i in range(1, len(df_ex)+1)], list(np.array(df_ex)))
    # print(list(np.array(df_ex)))
    # plt.show()

#plot两个速度
def plot_twist(a,b):
    df1_1 = a["field.twist.linear.x"]
    df2_1 = b["field.twist.linear.x"]
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.plot([i for i in range(1, len(df1_1) + 1)], list(np.array(df1_1)*3.6),label="1")
    ax.plot([i for i in range(1, len(df2_1) + 1)], list(np.array(df2_1)*3.6),label="2")
    ax.set_title('tests')
    ax.legend()
    plt.savefig('./twist.png')
    # plt.show()

def plot_pose(a,b):
    fig = plt.figure(1, figsize=(10, 6))
    fig.subplots_adjust(bottom=0.2)
    ax = axislines.Subplot(fig, 131)

    ax.plot( list(a["field.pose.position.x"]), label="1")
    ax.plot( list(b["field.pose.position.x"]), label="2")
    ax.set_title('field.pose.position.x')
    ax.legend()

    ax2 = axislines.Subplot(fig, 132, sharex=ax)
    ax2.plot(list(a["field.pose.position.y"]), label="1")
    ax2.plot(list(b["field.pose.position.y"]), label="2")
    ax2.set_title('field.pose.position.y')
    ax2.legend()

    ax3 = axislines.Subplot(fig, 133,sharex=ax)
    ax3.plot(list(a["field.pose.position.z"]), label="1")
    ax3.plot(list(b["field.pose.position.z"]), label="2")
    ax3.set_title('field.pose.position.z')
    ax3.legend()

    fig.add_subplot(ax)
    fig.add_subplot(ax2)
    fig.add_subplot(ax3)
    upper_loc = os.path.abspath(os.path.dirname(os.getcwd()))
    upper_loc = upper_loc+"/bags/"
    pic_loc = upper_loc + 'pose.png'
    plt.savefig(pic_loc)

    return pic_loc

def compare_analysis(csv1,csv2):
    "欧式距离之差"
    a,b = csv_to_df(csv1,csv2)
    eu_dataFrame(a,b)
    "偏航角之差"
    print(yaw_df(a,b))
    plot_eur(a, b)
    return eu_dataFrame(a,b), yaw_df(a,b)

def velocity_not_zero(df):
    df_1 = df["field.twist.linear.x"]
    if df_1.sum() !=0:
        return True
    else:
        return False

def current_pose_change(df):
    df_list = df["field.pose.position.x"].tolist()
    if len(set(df_list)) != 1:
        return True
    else:
        return False

def current_pose_analysis_eur(rangenum, df1 , df2 ):
        df_all= pd.DataFrame()
        ac = df1.shape[0]
        bc = df2.shape[0]
        print(ac,bc)
        if ac == bc:
            a_col = df1.columns
            b_col = df2.columns
            keyword = str("pose.position.x")
            keyword1 = str("pose.position.y")
            for i in a_col:
                if keyword in str(i):
                    dfx_a = df1[i]
                    dfx_b = df2[i]
                if keyword1 in str(i):
                    dfy_a = df1[i]
                    dfy_b = df2[i]

            df_all = np.sqrt((dfx_a - dfx_b) ** 2 + (dfy_a - dfy_b) ** 2)
            for i in df_all.tolist():
                if abs(i) > rangenum :
                    result = False
                else :
                    result =True
            key_name = "eu_distance of current pose"
        else:
            result = False
            print("current pose shape is not the same")
            kkey_name = None
        df_all = pd.DataFrame(df_all,columns=[key_name])
        print(df_all)
        print(key_name)
        return result, key_name, df_all

def current_pose_analysis_yaw(range_scale, df1 , df2 ):
    ac = df1.shape[0]
    bc = df2.shape[0]
    a_col = df1.columns
    b_col = df2.columns
    four_angles=["w","x","y","z"]
    if ac == bc:
        a_angle = []
        b_angle = []
        for angle in four_angles:
          keyword = str("pose.orientation." + angle)
          # 找dataframe中存在的column
          for i in a_col:
              if keyword in str(i):
                  a_result = df1[i].tolist()
          for i in b_col:
              if keyword in str(i):
                  b_result = df2[i].tolist()
          a_angle.append(a_result)
          b_angle.append(b_result)
        a_w, a_x, a_y, a_z = ori_angel(a_angle)
        b_w, b_x, b_y, b_z = ori_angel(b_angle)
        a_yaw_list = []
        b_yaw_list = []
        c_yaw_list = []
        # mean_c_yaw_list = []
        ss= len(a_w)
        print(ss)
        for ii in range(0, ss):
          a_yaw = to_euler_angles(a_w[ii], a_x[ii], a_y[ii], a_z[ii])
          b_yaw = to_euler_angles(b_w[ii], b_x[ii], b_y[ii], b_z[ii])
          c_yaw = abs(a_yaw) - abs(b_yaw)  # 偏航角之差
          a_yaw_list.append(a_yaw)
          b_yaw_list.append(b_yaw)
          c_yaw_list.append(c_yaw)
        for i in set(c_yaw_list) :
          if abs(i) > range_scale:
              result = False
          else:
              result = True
    else:
        result = False
        print("current pose shape is not the same")
        c_yaw_list = None
    return result, c_yaw_list



def data_analysis():
    """
    调用函数
    一。
    1. 如果输出文档速度一直为 0   -> not pass
    2. current_pose 值一直没有变 -> not pass
    3. current pose: 两值比较： 1.欧式距离之差 -》 超过一个range， 不pass
                              2.偏航角之差  -》  超过一个range, 不pass
    4. current twist 两值比较： ×3.6 画图
    5. trajectory：  比较各个points
    6. /planning/mission_planning/route   不为空
    7. /planning/mission_planning/route   信息匹配
    8. plot pose
    """
    #1.

    local = "/home/minwei/autotest/common"
    dfa, dfb = csv_to_df(local + "/record_current_pose.csv", local + "/record_current_pose1.csv")
    dfb.drop(dfb.tail(3).index, inplace=True)
    df_ta,df_tb=csv_to_df(local+"/record_vehiclewist.csv",local+"/record_vehiclewist1.csv")
    print(dfa.shape, dfb.shape)
    result, ll = current_pose_analysis_yaw(10,dfa,dfb)

    print(result,ll)
    # plot_twist(df_ta, df_tb)
    # plot_pose(dfa,dfb)


    pass
if __name__ == '__main__':


    # df1,df2 = compare_analysis(local + "/record_result1.csv", local + "/record_result.csv")
    # # compare_position(local + "/record_trajectory1.csv", local + "/record_trajectory.csv")
    # print("==================================================")
    # dd =extract(df1, df2)
    # print(dd)
    local = "/home/minwei/autotest/common"
    # df1 , df2 = csv_to_df(local + "/record_vehiclewist.csv", local + "/record_vehiclewist1.csv")
    # # plot_twist(df1,df2)
    dfa, dfb = csv_to_df(local + "/record_current_pose.csv", local + "/record_current_pose1.csv")
    dfb.drop(dfb.tail(3).index, inplace=True)
    result, key, df_all = current_pose_analysis_eur(10, dfa,dfb)
    df_all.to_csv("./tzzs_data.csv")
    plot_pose(dfa,dfb)

    # plot_pose(dfa,dfb)
    # # p = extract(df1,df2).plot.bar()
    # # plot.show()

    # for ii in range(0, 4485):
    #     print(ii)




