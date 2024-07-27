# #每个excel的  时间段-频率-所占百分比-累计百分比
# import os
# import pandas as pd
# # 输入文件夹和输出文件夹路径
# input_folder = r"J:\年后更新20240226\第二轮\全部原始数据\头上戴帽第二批\背部抖动频率分析\抖动频率+平均抖动频率（5）"
# output_folder = r"J:\年后更新20240226\第二轮\全部原始数据\头上戴帽第二批\背部抖动频率分析\抖动频率百分比原始数据（6）"
#
#
# # 确保输出文件夹存在
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#
# # 获取所有excel文件
# excel_files = os.listdir(input_folder)
#
# # 循环处理每个excel文件
# for file_name in excel_files:
#     # 构造输入文件路径
#     input_file = os.path.join(input_folder, file_name)
#
#     # 读取excel文件
#     df = pd.read_csv(input_file)
#
#     # 提取前20行的shaking_frequency_average列数据
#     shaking_frequency_average = df['shaking_frequency_average'].head(20)
#
#     # 计算frequency_sum
#     frequency_sum = shaking_frequency_average.sum()
#
#     # 计算percent
#     percent = (shaking_frequency_average / frequency_sum) * 100
#
#     # 计算accumulate
#     accumulate = percent.cumsum()
#
#     # 创建新的DataFrame
#     time_intervals = [f'{i}-{i + 30}' for i in range(0, 600, 30)]
#     new_df = pd.DataFrame({
#         'time': time_intervals[:20],  # 只选择前20个时间间隔
#         'shaking_frequency_average': shaking_frequency_average,
#         'frequency_sum': [frequency_sum] * 20,  # 重复20次以匹配DataFrame的长度
#         'percent': percent,
#         'accumulate_percent': accumulate
#     })
#
#     # 构造输出文件路径
#     output_file = os.path.join(output_folder, file_name)
#
#     # 保存新的excel文件
#     new_df.to_csv(output_file, index=False)

#------------------------------------------------------------------------------------------------------------
#总结excel  时间段-ctrl1-ctrl8
import os
import pandas as pd

# 新文件夹路径和总结 Excel 文件路径
new_folder_path = r"J:\年后更新20240226\第二轮\全部原始数据\头上戴帽第二批\背部抖动频率分析\抖动频率百分比原始数据（6）\无CD1" #全部数据
summary_excel_path = r"J:\年后更新20240226\第二轮\全部原始数据\头上戴帽第二批\背部抖动频率分析\抖动频率百分比总结表格（7）\无CD1.xlsx"

# 获取新文件夹中所有的 Excel 文件
excel_files = sorted(os.listdir(new_folder_path))

# 时间间隔列表
time_intervals = [f'{i}-{i + 30}' for i in range(0, 600, 30)]

# 创建一个空的 DataFrame 用于存储总结数据
summary_df = pd.DataFrame({'time': time_intervals})

# 遍历新文件夹中的每个 Excel 文件
for file_name in excel_files:
    # 构造文件路径
    file_path = os.path.join(new_folder_path, file_name)
    # 去掉文件名的后缀部分
    file_name_without_extension = os.path.splitext(file_name)[0]
    # 读取 Excel 文件
    df = pd.read_csv(file_path)

    # 获取 accumulate_percent 列的值
    accumulate_percent = df['accumulate_percent'].tolist()

    # 将 accumulate_percent 列的值添加到总结 DataFrame 中
    summary_df[file_name_without_extension] = accumulate_percent

# 保存总结 Excel 文件
summary_df.to_excel(summary_excel_path, index=False)