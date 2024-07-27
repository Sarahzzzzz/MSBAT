#计算V-W
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from scipy.interpolate import make_interp_spline

input_folder = r"C:\Users\HP\Desktop\JY_Data_20240520\round2\Z\v-w\原始数据"
output_folder = r"C:\Users\HP\Desktop\JY_Data_20240520\round2\Z\v-w\v-w结果图"
#
# # 获取所有excel文件
excel_names = os.listdir(input_folder)

## 计算欧几里得距离

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)


# 循环处理每个excel文件
for i, excel_name in enumerate(excel_names):
    excel_path = os.path.join(input_folder, excel_name)

    df = pd.read_csv(excel_path)
    print("shape:", df.shape)

    # 提取坐标数据
    nose_coordinates = df[['nose_x', 'nose_y']].values
    back_coordinates = df[['doursm_x', 'doursm_y']].values
    tail_coordinates = df[['tailbase_x', 'tailbase_y']].values
    # print(nose_coordinates)
    # print("背部坐标\n",back_coordinates)
    # print("鼻子坐标\n",nose_cordinates)
    # print("尾巴坐标\n",tail_coordinates)

    # #
    # # 计算速度
    # delta_coordinates = np.diff(back_coordinates, axis=0)
    # frame_rate = 30.0  # 假设视频的帧率是30帧/秒
    # velocity = delta_coordinates * frame_rate
    # speed = np.linalg.norm(velocity, axis=1)
    # # 计算速度_改后----------------------------------------
    # 计算位移和速度
    frame_rate = 30.0  # 假设视频的帧率是30帧/秒
    displacements = []  # 存储每对相邻帧之间的位移
    for i in range(len(back_coordinates) - 1):
        displacement = euclidean_distance(back_coordinates[i], back_coordinates[i + 1])
        displacements.append(displacement)

    displacements = np.array(displacements)
    speed = displacements * frame_rate  # 速度 = 位移 / 时间间隔
 # # 计算速度_改后----------------------------------------

    # 计算向量
    vector_nose_to_back = nose_coordinates - back_coordinates
    vector_tail_to_back = tail_coordinates - back_coordinates

    # 计算向量的模
    magnitude_nose_to_back = np.linalg.norm(vector_nose_to_back, axis=1)
    magnitude_tail_to_back = np.linalg.norm(vector_tail_to_back, axis=1)

    # # 计算点积
    dot_product = np.sum(vector_nose_to_back * vector_tail_to_back, axis=1)

    #  计算夹角（弧度）
    # 计算了鼻子到背部和背部到尾巴两个向量之间的夹角。如果余弦相似度为1，夹角为0度；如果余弦相似度为-1，夹角为180度。
    # 夹角的计算结果是以弧度为单位的，你可以将其转换为度数，得到更直观的角度
    # 余弦相似性通过测量两个向量的夹角的余弦值来度量它们之间的相似性。0度角的余弦值是1，而其他任何角度的余弦值都不大于1；并且其最小值是-1。
    # 从而两个向量之间的角度的余弦值确定两个向量是否大致指向相同的方向。两个向量有相同的指向时，余弦相似度的值为1；
    # 两个向量夹角为90°时，余弦相似度的值为0；两个向量指向完全相反的方向时，余弦相似度的值为-1。
    # 这结果是与向量的长度无关的，仅仅与向量的指向方向相关。余弦相似度通常用于正空间，因此给出的值为-1到1之间。
    cosine_similarity = dot_product / (magnitude_nose_to_back * magnitude_tail_to_back)

    # clip这个函数将将数组中的元素限制在a_min, a_max之间，大于a_max的就使得它等于 a_max，小于a_min,的就使得它等于a_min。
    angle_radians = np.arccos(np.clip(cosine_similarity, -1.0, 1.0))
    # print("最大值：",max(angle_radians))
    # print("最小值：",min(angle_radians))

    # # 将弧度转换为度
    angle_degrees = np.degrees(angle_radians)
    # angle_degrees = np.clip(angle_degrees, 0, 180)  # 将角度限制在 [0, 180] 范围内


    # 计算夹角变化
    angle_change = np.diff(angle_degrees)

    # 将速度和角度数据添加到DataFrame中
    df['Speed'] = np.append(speed, np.nan)  # 在速度数据中添加一个NaN值以匹配数据长度
    df['angle'] = angle_degrees  # 在速度数据中添加一个NaN值以匹配数据长度
    df['Angle Change'] = np.append(angle_change, np.nan)  # 在角度变化数据中添加一个NaN值以匹配数据长度

    # 保存更新后的DataFrame到原始Excel文件中
    df.to_csv(excel_path, index=False)
    print("已保存速度和角度数据到文件:", excel_path)
#-------------------------------------------------------------------------------------
    # 可视化速度和夹角变化
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Time(s)', fontsize=19)
    ax1.set_ylabel('Speed(pixels per second)', color='#4F94CD', fontsize=19)
    ax1.plot(speed, color='#4F94CD')
    ax1.tick_params(axis='y', labelcolor='#4F94CD', labelsize=14)
    ax1.set_ylim(ymax=35000)

    ax2 = ax1.twinx()
    ax2.set_ylabel('Angle Change (degrees)', color='#CD0000', fontsize=19)
    ax2.plot(angle_change, color='#CD0000')
    ax2.tick_params(axis='y', labelcolor='#CD0000', labelsize=14)
    ax2.set_ylim(ymin=-200, ymax=200)
#--------------------------------v-w-----------------------------------
    # 设置横坐标刻度字体大小
    ax1.tick_params(axis='x', labelsize=15)  # 设置横坐标刻度字体大小为14

    # 设置横坐标刻度字体
    prop = FontProperties(family='Arial', size=15)  # 设置字体族和大小
    for label in ax1.get_xticklabels():
        label.set_fontproperties(prop)
    for label in ax1.get_yticklabels():
        label.set_fontproperties(prop)
    for label in ax2.get_yticklabels():
        label.set_fontproperties(prop)
    # # 设置刻度标签字体加粗
    # prop = FontProperties(size=14)  # 设置字体加粗
    # for label in ax1.get_yticklabels():
    #     label.set_fontproperties(prop)
    # for label in ax2.get_yticklabels():
    #     label.set_fontproperties(prop)
    # 设置外边框粗细
   # --------------------------------v - w - ----------------------------------

    output_path = os.path.join(output_folder, os.path.splitext(excel_name)[0] + '.png')
    plt.savefig(output_path)
    plt.close()

    for spine in ax1.spines.values():
        spine.set_linewidth(3)  # 设置粗细为2

    fig.tight_layout()
    # plt.title('Speed and Angle Change over Time', fontsize=17)
    plt.show()







