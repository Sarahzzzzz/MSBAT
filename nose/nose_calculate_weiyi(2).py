import pandas as pd
import os

# 设置表格文件夹路径
folder_path = r"C:\Users\HP\Desktop\Ctrl，KD_有CD1_正_处理表格\俯视位移计算（nose）\原始处理excel（1）"
output_file = r"C:\Users\HP\Desktop\Ctrl，KD_有CD1_正_处理表格\俯视位移计算（nose）\位移总和（2）"


# 获取文件夹下所有表格文件名
files = os.listdir(folder_path)

# 遍历每个表格文件
for file in files:
    if file.endswith('.csv'):  # 假设表格是CSV格式的，如果不是，可以修改文件格式
        file_path = os.path.join(folder_path, file)

        # 读取表格文件
        df = pd.read_csv(file_path)

        # 计算每两行之间的位移并添加为新的一列
        displacements = []
        for i in range(1, len(df)):
            x1, y1 = df.iloc[i-1]['nose_x'], df.iloc[i-1]['nose_y']
            x2, y2 = df.iloc[i]['nose_x'], df.iloc[i]['nose_y']
            displacement = ((x2 - x1)**2 + (y2 - y1)**2)**0.5  # 计算欧氏距离作为位移
            displacements.append(displacement)
        df['displacement'] = [None] + displacements  # 在第一行的位移值为None
        # 计算 displacement 列的数值总和
        displacement_sum = df['displacement'].sum()
        # 将数值总和添加为新的一列
        df['displacement_sum'] = displacement_sum        # 计算总的位移并保存

        # 保存处理后的表格到新的文件夹
        output_file_path = os.path.join(output_file, file)
        df.to_csv(output_file_path, index=False)

