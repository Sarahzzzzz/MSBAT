
import pandas as pd
import os

# 设置表格文件夹路径
folder_path = r"C:\Users\HP\Desktop\videotest-20240619\3\video\test_20240703\process data"

# 获取文件夹下所有表格文件名
files = os.listdir(folder_path)

# 遍历每个表格文件
for file in files:
    if file.endswith('.csv'):  # 假设表格是CSV格式的，如果不是，可以修改文件格式
        file_path = os.path.join(folder_path, file)

        # 读取表格文件
        df = pd.read_csv(file_path,low_memory=False,header=None)

        #删除前三行
        # df = df.drop(range(3)).reset_index(drop=True)

        #正视修改表格
        # df = pd.read_csv(file_path, low_memory=False, header=None, names=['bodyparts', 'nose_x', 'nose_y', 'nose', 'doursm_x', 'doursm_y', 'doursm', 'tailbase_x', 'tailbase_y',
        #     'tailbase', 'Speed', 'angle','Angle Change','Speed Mean','Angle  Mean'])

        df = pd.read_csv(file_path, low_memory=False, header=None, names=['bodyparts', 'nose_x', 'nose_y', 'nose', 'dorsum_x', 'dorsum_y', 'dorsum', 'tailbase_x', 'tailbase_y',
            'tailbase'] )
        # df.to_csv(file_path,header=None, index=None)
        df.to_csv(file_path, index=None)

        print(df.head())