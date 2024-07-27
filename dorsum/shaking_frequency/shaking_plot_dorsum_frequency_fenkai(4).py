import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# 设置全局字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用中文字体SimHei

# 文件夹路径
folder_path = r"J:\年后更新20240226\第二轮\全部原始数据\头上戴帽第二批\背部抖动频率分析\每五秒统计一次的抖动次数（背部位移在阈值内）（3）" #抖动次数原始数据
output_folder = r"J:\年后更新20240226\第二轮\全部原始数据\头上戴帽第二批\背部抖动频率分析\dorsum_frequency_plot_将（3）除以5得出频率（4）"  # 新建一个文件夹用于保存图形

# 遍历文件夹中的所有 Excel 文件
for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx') or file_name.endswith('.csv'):  # 确保文件是 Excel 文件
        file_path = os.path.join(folder_path, file_name)

        # 读取 Excel 文件
        df = pd.read_csv(file_path)

        # 提取坐标点数据
        y_values = df['count']/5
        x_values = range(len(y_values))  # x轴为数据点的索引
        # 将 x_values 中的每个值都乘以 5
        x_values = [x * 5 for x in x_values]

        # 绘制散点图
        plt.scatter(x_values, y_values, color="red", label="frequency_length1/40")
        plt.legend()

        # 设置图形标题和坐标轴标签
        plt.title(os.path.splitext(file_name)[0])  # 使用文件名作为图形标题
        plt.xlabel('Time')
        plt.ylabel('抖动频率变化')
        plt.ylim(0, 20)



        # 绘制柱状图
        plt.bar(x_values, y_values, color="red", label="frequency_1/40")
        plt.legend()

        # 设置图形标题和坐标轴标签
        plt.title(os.path.splitext(file_name)[0])  # 使用文件名作为图形标题
        plt.xlabel('Time')
        plt.ylabel('抖动频率变化')
        plt.ylim(0, 30)

        # 绘制折线图
        plt.plot(x_values, y_values, color="red", label="shaking frequency")
        # plt.legend()

        # 设置图形标题和坐标轴标签
        # plt.title(os.path.splitext(file_name)[0])  # 使用文件名作为图形标题
        plt.xlabel('Time（s）',fontsize=18)
        plt.ylabel('shaking frequency change(times/s)',fontsize=18)
        plt.ylim(0, 8)
        # 设置横纵坐标刻度字体为 Arial
        prop = FontProperties(family='Arial', size=14)
        plt.xticks(fontproperties=prop)
        plt.yticks(fontproperties=prop)

        # 图形保存路径
        output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.png')

        # 保存图形
        plt.savefig(output_path)  # 保存为 png 格式图片
        plt.close()  # 关闭当前图形，以便绘制下一个图形
