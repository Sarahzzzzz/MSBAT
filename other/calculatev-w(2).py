#计算V-W

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

excel_paths=[
#无cd1
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\2INT.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\3INT.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\4INT.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\5INT.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\ctrl1.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\ctrl2.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\ctrl3.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\ctrl4.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\ctrl5.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\ctrl6.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\ctrl7.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\ctrl8.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\KD1.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\KD2.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\KD3.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\KD4.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\KD5.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\KD6.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\KD7.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\KD8.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\KDG1.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\KDG2.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\NC2.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\NC3.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\NC5.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\NC6.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\NCG1.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_1INT_all0.92_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_2INT_all0.95_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_3INT_all0.8_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_4INT_all0.78_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_5INT_all0.85_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_Ctrl1_0.68_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_Ctrl2_0.73_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_Ctrl3_0.72_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_Ctrl4_0.8_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_Ctrl5_0.61_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_Ctrl6_0.75_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_Ctrl7_0.72_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_Ctrl8_0.72_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_KD1_0.7_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_KD2_0.75_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_KD3_0.7_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_KD4_0.75_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_KD5_0.75_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_KD6_0.8_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_KD7_0.8_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_KD8_0.75_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_KDG1_0.8_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_KDG2_0.7_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_NC2_0.6_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_NC3_0.5_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_NC5_0.5_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_NC6_0.6__2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\无CD1_NCG1_0.6__2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\无cd1\1INT.csv",
#
# #有cd1
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\3INT.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\4INT.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\5INT.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\ctrl1.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\ctrl2.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\ctrl3.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\ctrl4.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\ctrl5.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\ctrl6.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\ctrl7.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\ctrl8.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\KD1.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\KD2.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\KD3.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\KD4.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\KD5.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\KD6.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\KD7.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\KD8.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\KDG1.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\KDG2.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\NC1.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\NC2.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\NC3.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\NC5.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\NC6.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\NCG1.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\NCG2.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_1INT_0.5_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_2INT_0.9_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_3INT_0.85_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_4INT_0.3_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_5INT_0.9_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_ctrl1_0.68_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_ctrl2_0.7_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_ctrl3_0.72_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_ctrl4_0.8_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_ctrl5_0.65_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_ctrl6_0.75_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_ctrl7_0.75_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_ctrl8_0.75_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_KD1_0.75_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_KD2_0.7_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_KD3_0.75_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_KD4_0.65_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_KD5_0.8_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_KD6_0.75_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_KD7_0.78_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_KD8_0.75_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_KDG1_0.75_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_KDG2_0.75_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_NC1_0.5_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_NC2_0.4_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_NC3_0.65_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_NC5_0.35_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_NC6_0.45_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_NCG1_0.9_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\有CD1_NCG2_0.4_2056.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\1INT.csv",
# r"J:\年后更新20240226\全部原始数据\含mean_v-w的原始数据\有cd1\2INT.csv",


#for抖动阳性指标
# r"C:\Users\HP\Desktop\检测抖动阳性指标\excel处理后\1_1DLC_resnet50_mouse_c20231230Dec30shuffle1_550000.csv",
# r"C:\Users\HP\Desktop\检测抖动阳性指标\excel处理后\1_2DLC_resnet50_mouse_c20231230Dec30shuffle1_550000.csv",
# r"C:\Users\HP\Desktop\检测抖动阳性指标\excel处理后\1_3DLC_resnet50_mouse_c20231230Dec30shuffle1_550000.csv",

r"J:\年后更新20240226\全部原始数据\第一轮\第一轮原始视频+原始表格\Ctrl\无CD1\改字体\1.csv",
r"J:\年后更新20240226\全部原始数据\第一轮\第一轮原始视频+原始表格\Ctrl\无CD1\改字体\2.csv",
r"J:\年后更新20240226\全部原始数据\第一轮\第一轮原始视频+原始表格\Ctrl\无CD1\改字体\3.csv",
r"J:\年后更新20240226\全部原始数据\第一轮\第一轮原始视频+原始表格\Ctrl\无CD1\改字体\4.csv",
r"J:\年后更新20240226\全部原始数据\第一轮\第一轮原始视频+原始表格\Ctrl\无CD1\改字体\5.csv",
r"J:\年后更新20240226\全部原始数据\第一轮\第一轮原始视频+原始表格\Ctrl\无CD1\改字体\6.csv",


]


# 计算欧几里得距离
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)



for i,excel_path in  enumerate(excel_paths):
    df = pd.read_csv(excel_path)
    print("shape:",df.shape)
# 提取坐标数据
    nose_coordinates = df[['nose_x', 'nose_y']].values
    back_coordinates = df[['doursm_x', 'doursm_y']].values
    tail_coordinates = df[['tailbase_x', 'tailbase_y']].values
    print(nose_coordinates)
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


    #
    # 计算向量
    vector_nose_to_back = nose_coordinates - back_coordinates
    vector_tail_to_back = tail_coordinates - back_coordinates

    # 计算向量的模
    magnitude_nose_to_back = np.linalg.norm(vector_nose_to_back, axis=1)
    magnitude_tail_to_back = np.linalg.norm(vector_tail_to_back, axis=1)

    # # 计算点积
    dot_product = np.sum(vector_nose_to_back * vector_tail_to_back, axis=1)
    #
    # # 计算夹角（弧度）
    # 计算了鼻子到背部和背部到尾巴两个向量之间的夹角。如果余弦相似度为1，夹角为0度；如果余弦相似度为-1，夹角为180度。
    # 夹角的计算结果是以弧度为单位的，你可以将其转换为度数，得到更直观的角度
    #余弦相似性通过测量两个向量的夹角的余弦值来度量它们之间的相似性。0度角的余弦值是1，而其他任何角度的余弦值都不大于1；并且其最小值是-1。
    # 从而两个向量之间的角度的余弦值确定两个向量是否大致指向相同的方向。两个向量有相同的指向时，余弦相似度的值为1；
    # 两个向量夹角为90°时，余弦相似度的值为0；两个向量指向完全相反的方向时，余弦相似度的值为-1。
    # 这结果是与向量的长度无关的，仅仅与向量的指向方向相关。余弦相似度通常用于正空间，因此给出的值为-1到1之间。
    cosine_similarity = dot_product / (magnitude_nose_to_back * magnitude_tail_to_back)

    #clip这个函数将将数组中的元素限制在a_min, a_max之间，大于a_max的就使得它等于 a_max，小于a_min,的就使得它等于a_min。
    angle_radians = np.arccos(np.clip(cosine_similarity, -1.0, 1.0))
    # print("最大值：",max(angle_radians))
    # print("最小值：",min(angle_radians))

    # # 将弧度转换为度
    angle_degrees = np.degrees(angle_radians)
    # angle_degrees = np.clip(angle_degrees, 0, 180)  # 将角度限制在 [0, 180] 范围内

    #
    # 计算夹角变化
    angle_change = np.diff(angle_degrees)

    # 将速度和角度数据添加到DataFrame中
    df['Speed'] = np.append(speed, np.nan)  # 在速度数据中添加一个NaN值以匹配数据长度
    df['angle'] = angle_degrees # 在速度数据中添加一个NaN值以匹配数据长度
    df['Angle Change'] = np.append(angle_change, np.nan)  # 在角度变化数据中添加一个NaN值以匹配数据长度

    # 保存更新后的DataFrame到原始Excel文件中
    df.to_csv(excel_path, index=False)
    print("已保存速度和角度数据到文件:", excel_path)




    # 可视化速度和夹角变化
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Time', fontsize=17)
    ax1.set_ylabel('Speed', color='blue', fontsize=17)
    ax1.plot(speed, color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_ylim(ymax=35000)

    ax2 = ax1.twinx()
    ax2.set_ylabel('Angle Change (degrees)', color='darkred', fontsize=17)
    ax2.plot(angle_change, color='red')
    ax2.tick_params(axis='y', labelcolor='darkred')
    ax2.set_ylim(ymin=-200, ymax=200)

    # fig.tight_layout()
    plt.title('Speed and Angle Change over Time', fontsize=17)
    plt.show()


