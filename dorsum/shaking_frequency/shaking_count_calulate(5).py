import os
import glob
import pandas as pd
import math
#计算抖动频率和平均抖动频率
# 输入文件夹和输出文件夹路径
input_folder = r"J:\年后更新20240226\第二轮\全部原始数据\头上戴帽第二批\背部抖动频率分析\每五秒统计一次的抖动次数（背部位移在阈值内）（3）"
output_folder = r"J:\年后更新20240226\第二轮\全部原始数据\头上戴帽第二批\背部抖动频率分析\抖动频率+平均抖动频率（5）"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取所有csv文件
csv_files = glob.glob(os.path.join(input_folder, "*.csv"))

# 循环处理每个csv文件
for file in csv_files:
    # 读取csv文件
    df = pd.read_csv(file)
    # 获取“count”列的值
    counts = df['count'].tolist()
    # 计算平均值并向上取整
    shaking_frequency= [round(x/ 5) for x in counts]
    shaking_frequency_average = [round(sum(counts[i:i+6]) / 6 /5) for i in range(0, len(counts), 6)]
    # 在原始DataFrame中添加新列
    df["shaking_frequency"] = pd.Series(shaking_frequency)
    df['shaking_frequency_average'] = pd.Series(shaking_frequency_average)

    # 构造输出文件路径
    output_file = os.path.join(output_folder, os.path.basename(file))
    # 保存新的csv文件
    df.to_csv(output_file, index=False)
