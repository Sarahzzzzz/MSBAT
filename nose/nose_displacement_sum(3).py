import pandas as pd
import os
#
# #分离出每个excel文件的位移值
# # 提取所有文件夹里的某一个单元格的值，并且生成在新的文件夹里的新的excel里，
# # 新的文件夹里excel的文件名和旧的文件夹里的excel名相同，新的excel的构成是，
# # 第一列是各个excel的名字，第二列是旧excel提取出来的对应的单元格的值
#
# # 定义旧文件夹和新文件夹的路径
old_folder = r"C:\Users\HP\Desktop\kc_detect_20240424\round2_CD1_four_20240424\coordinate_20240425(1)"# 旧文件夹路径
new_folder = r"C:\Users\HP\Desktop\kc_detect_20240424\round2_CD1_four_20240424\coordinate_20240425(2)" # 新文件夹路径
#
# 遍历旧子文件夹中的所有 Excel 文件_提取数据
for root, dirs, files in os.walk(old_folder):
    for file in files:
        if file.endswith('.csv'):  # 假设文件都是 Excel 文件
            file_path = os.path.join(root, file)
            file_name = os.path.splitext(file)[0]  # 获取 Excel 文件名，去除扩展名

            # 读取 Excel 文件中的指定单元格值
            df = pd.read_csv(file_path)  # 指定引擎为 openpyxl
            displacement = df.iloc[0, 4]  # 假设要提取的单元格位于第一行第一列

            # 创建新的 DataFrame，包
            # 含文件名和单元格值
            new_df = pd.DataFrame({'file Name': [file_name], 'displacement': [displacement]})

            # 保存新的 DataFrame 到新文件夹中的 Excel 文件中
            new_excel_path = os.path.join(new_folder, f"{file_name}.xlsx")
            new_df.to_excel(new_excel_path, index=False)

            print(f"Excel '{file_name}' 的单元格值已提取并保存到新的 Excel 文件中：{new_excel_path}")


# 将生成的excel文件（单个的file_name）合成一个excel

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
combined_excel_path =r"C:\Users\HP\Desktop\kc_detect_20240424\round2_CD1_four_20240424\displacement.xlsx"
# 保存合并的Excel文件
combined_df.to_excel(combined_excel_path, index=False)
print(f"所有 Excel 文件已合并到 '{combined_excel_path}'")

