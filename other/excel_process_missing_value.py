#寻找表格中的缺失值
# import pandas as pd
#
# # 读取数据集
# df = pd.read_csv("J:\年后更新20240226\全部原始数据\dorsum轨迹绘制原始数据\无cd1\无CD1_2INT_all0.95_2056.csv")
#
# # 创建布尔值的 DataFrame，标识缺失值位置
# missing_values = df.isnull()
#
# # 打印包含缺失值的行和列索引
# missing_indexes = missing_values[missing_values.any(axis=1)].index
# print("Rows with missing values:")
# print(missing_indexes)
#
# missing_columns = missing_values.columns[missing_values.any()]
# print("Columns with missing values:")
# print(missing_columns)

#寻找表格中的非法字符
import pandas as pd

# 读取数据集
df = pd.read_csv("J:\年后更新20240226\全部原始数据\dorsum轨迹绘制原始数据\无cd1\无CD1_3INT_all0.8_2056.csv")

# 检查 'bodyparts' 列是否只包含数字
for index, value in enumerate(df['bodyparts']):
    if not str(value).isdigit():  # 检查是否只包含数字
        print(f"Non-numeric value found at index {index}: {value}")
