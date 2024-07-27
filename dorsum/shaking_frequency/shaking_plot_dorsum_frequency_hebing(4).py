import os
import pandas as pd
import matplotlib.pyplot as plt

# 设置全局字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用中文字体SimHei

# 两个文件夹路径
folder_path_with_cd1 = r"J:\年后更新20240226\全部原始数据\第一轮\背部抖动频率计算\每五秒统计一次的抖动次数（背部位移在阈值内）（3）\有CD1_精度后(只用于合并)"  # 含有CD1的文件夹
folder_path_without_cd1 = r"J:\年后更新20240226\全部原始数据\第一轮\背部抖动频率计算\每五秒统计一次的抖动次数（背部位移在阈值内）（3）\无CD1_精度后(只用于合并)"  # 不含有CD1的文件夹

# 新建一个文件夹用于保存图形
output_folder = r"J:\年后更新20240226\全部原始数据\第一轮\背部抖动频率计算\dorsum_frequency_plot_将（3）除以5得出频率（4）\5s统计一次抖动次数\有CD1和无CD1合并\精度筛选后的数据"

# 遍历含有CD1的文件夹中的所有 Excel 文件
for file_name in os.listdir(folder_path_with_cd1):
    if file_name.endswith('.xlsx') or file_name.endswith('.csv'):  # 确保文件是 Excel 文件
        # 获取当前文件名
        base_name = os.path.splitext(file_name)[0]

        # 构建相应的文件路径
        file_path_with_cd1 = os.path.join(folder_path_with_cd1, file_name)
        file_path_without_cd1 = os.path.join(folder_path_without_cd1, file_name)

        # 读取两个文件夹中对应的 Excel 文件
        df_with_cd1 = pd.read_csv(file_path_with_cd1)
        df_without_cd1 = pd.read_csv(file_path_without_cd1)

        # 提取 count 列数据
        frequency_with_cd1 = df_with_cd1['count']/5
        frequency_without_cd1 = df_without_cd1['count']/5

        # 合并两个文件夹中相同文件名的 Excel 文件的 count 数据
        combined_count = pd.concat([frequency_with_cd1, frequency_without_cd1], axis=1)
        combined_count.columns = ['frequency_with_cd1', 'frequency_without_cd1']

        # 绘制折线图
        plt.plot(combined_count.index*50, combined_count['frequency_with_cd1'], label="有CD1", color='blue')
        plt.plot(combined_count.index*50, combined_count['frequency_without_cd1'], label="无CD1", color='red')
        plt.legend()

        # 设置图形标题和坐标轴标签
        plt.title(base_name)
        plt.xlabel('Time')
        plt.ylabel('抖动频率变化')
        plt.ylim(0,8)

        # 图形保存路径
        output_path = os.path.join(output_folder, base_name + '.png')

        # 保存图形
        plt.savefig(output_path)  # 保存为 png 格式图片
        plt.close()  # 关闭当前图形，以便绘制下一个图形
