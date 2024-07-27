
import pandas as pd
import os

# 设置表格文件夹路径
folder_path = r"C:\Users\HP\Desktop\俯视表格处理"

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

        #俯视修改表格
        df = pd.read_csv(file_path, low_memory=False, header=None, names=[
            'bodyparts', 'nose_x', 'nose_y', 'nose', 'doursm_x', 'doursm_y', 'doursm', 'tailbase_x', 'tailbase_y',
            'tailbase', 'hip_L_x', 'hip_L_y','hip_L','hip_R_x','hip_R_y','hip_R'])
        # 删除列
        # df = df.drop(df.columns[11], axis=1,)
        # 删除行
        # df.drop(df.index[0], inplace=True)

        # df.to_csv(file_path,header=None, index=None)
        df.to_csv(file_path, index=None)

        print(df.head())