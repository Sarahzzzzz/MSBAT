#  # --------------------------在原excel中计算平均v和w--------------------------
import pandas as pd
import os
# 定义文件夹路径
folder_path = r"J:\年后更新20240226\第二轮\全部原始数据\头上戴帽第二批\v-w\原始表格\有CD1"

# 获取文件夹中所有Excel文件的路径
excel_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.csv')]

# 循环处理每个Excel文件
for file_path in excel_files:
    # 读取Excel文件
    df = pd.read_csv(file_path)

    # 计算Speed列和Angle Change列的平均值
    speed_mean = df['Speed'].mean()
    angle_change_mean = df['angle'].mean()

    # 将平均值添加到DataFrame中的新列
    df['Speed Mean'] = speed_mean
    df['Angle  Mean'] = angle_change_mean

    # 将修改后的DataFrame保存回原Excel文件
    df.to_csv(file_path, index=False)
#
# # # # --------------------------在原excel中计算平均v和w--------------------------
#

#提取所有excel--总和所有小鼠的平均速度和平均角度
import pandas as pd
import os
# 提取所有文件夹里的某一个单元格的值，并且生成在新的文件夹里的新的excel里，
# 新的文件夹里excel的文件名和旧的文件夹里的excel名相同，新的excel的构成是，
# 第一列是各个excel的名字，第二列是旧excel提取出来的对应的单元格的值

# 定义旧文件夹和新文件夹的路径

old_folder = r"J:\年后更新20240226\第二轮\全部原始数据\头上戴帽第二批\v-w\原始表格\有CD1"# 旧文件夹路径
new_folder = r"J:\年后更新20240226\第二轮\全部原始数据\头上戴帽第二批\v-w\meanv_w 单独\有CD1" # 新文件夹路径


# 遍历旧子文件夹中的所有 Excel 文件_提取数据
for root, dirs, files in os.walk(old_folder):
    for file in files:
        if file.endswith('.csv'):  # 假设文件都是 Excel 文件
            file_path = os.path.join(root, file)
            file_name = os.path.splitext(file)[0]  # 获取 Excel 文件名，去除扩展名

            # 读取 Excel 文件中的指定单元格值
            df = pd.read_csv(file_path)  # 指定引擎为 openpyxl
            mean_v = df.iloc[2, 13]
            mean_w = df.iloc[2, 14]


            # 创建新的 DataFrame，包含文件名和单元格值
            new_df = pd.DataFrame({'file Name': [file_name], 'mean_v': [mean_v],'mean_w':[mean_w]})

            # 保存新的 DataFrame 到新文件夹中的 Excel 文件中
            new_excel_path = os.path.join(new_folder, f"{file_name}.xlsx")
            new_df.to_excel(new_excel_path, index=False)

            print(f"Excel '{file_name}' 的单元格值已提取并保存到新的 Excel 文件中：{new_excel_path}")


# 生成的excel文件合成一个excel


# 定义新文件夹的路径

# 初始化一个空的 DataFrame 用于存储所有数据
combined_df = pd.DataFrame()

# 遍历新文件夹中的所有 Excel 文件
for root, dirs, files in os.walk(new_folder):
    for file in files:
        if file.endswith('.xlsx'):  # 假设文件都是 CSV 文件
            file_path = os.path.join(root, file)

            # print("File path:", file_path)  # 打印文件路径用于调试

            # 读取 CSV 文件
            df = pd.read_excel(file_path)

            # 将数据添加到组合 DataFrame 中
            combined_df = pd.concat([combined_df, df], ignore_index=True)

# 保存合并后的 DataFrame 到一个新的 Excel 文件中
combined_excel_path = r"J:\年后更新20240226\第二轮\全部原始数据\头上戴帽第二批\v-w\meanv_w总结\有CD1.xlsx"  # 新 Excel 文件路径
combined_df.to_excel(combined_excel_path, index=False)

print(f"所有 Excel 文件已合并到 '{combined_excel_path}'")
