import pandas as pd
import os
import matplotlib as  plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用中文字体SimHei
#--------------------------------------------------计算小鼠平均身长的1/50---------------------------------------------------
# 读取表格数据

folder_path=r"J:\年后更新20240226\第二轮\全部原始数据\头上戴帽第二批\背部抖动频率分析\背部位移原始数据（含阈值-身长的1-50）（1）"
files = os.listdir(folder_path)
# 遍历每个表格文件
for file in files:
    # if file.endswith('.csv'):  # 假设处理的文件是Excel文件
    file_path = os.path.join(folder_path, file)

    # 读取Excel文件
    df = pd.read_csv(file_path)

    # 计算新列的值
    new_column = abs(df['tailbase_x'] - df['nose_x'])
    # print(new_column.isnull().sum())    # 将新列添加到DataFrame中
    df['length_mouse'] = new_column
    # 计算新列的总和和平均值
    total = df['length_mouse'].sum()
    average = df['length_mouse'].mean()
    thr_average=average/50
    # 将总和和平均值写入另外一列的第一行
    df.loc[0, 'length'] = total
    df.loc[0, 'length_mouse_mean'] = average
    df.loc[0, 'thr_average_1-50'] = thr_average

    # 保存修改后的表格
    df.to_csv(file_path, index=False, encoding='utf-8')
#--------------------------------------------------计算小鼠平均身长的1/50---------------------------------------------------



#
#-----------------------------------------------------计算抖动频率-----------------------------------------------------
import pandas as pd
import os

folder_path = r"J:\年后更新20240226\第二轮\全部原始数据\头上戴帽第二批\背部抖动频率分析\背部位移原始数据（含阈值-身长的1-50）（1）"
displacement_path = r"J:\年后更新20240226\第二轮\全部原始数据\头上戴帽第二批\背部抖动频率分析\只有背部位移（每5帧算一次）（2）"
#                                     ----------计算每五帧的背部位移-------------
#获取文件名
files1 = os.listdir(folder_path)    # 背部位移原始数据——用于计算displacement

for file in files1:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    threshold = df.iloc[0, 18]

    print(threshold)
    # 初始化位移列和 count 列
    dorsum_displacement = []

    # 每五帧计算一次位移
    for i in range(0, len(df), 5):  # 从索引0开始每隔五帧
        if i + 4 < len(df):  # 确保计算位移的帧在 DataFrame 的范围内
            x_diff = df.iloc[i + 4]['tailbase_x'] - df.iloc[i]['tailbase_x']  # 计算x坐标的变化量
            y_diff = df.iloc[i + 4]['tailbase_y'] - df.iloc[i]['tailbase_y']  # 计算y坐标的变化量
            displacement = (x_diff ** 2 + y_diff ** 2) ** 0.5  # 计算位移
            dorsum_displacement.append(displacement)
        else:
            dorsum_displacement.append(None)  # 添加缺失值

    # 将位移列添加到 DataFrame 中
    new_df = pd.DataFrame()
    new_df['dorsum_displacement'] = dorsum_displacement

    # 保存结果到每个文件的输出文件中
    new_file_path = os.path.join(displacement_path, file)
    new_df.to_csv(new_file_path, index=False)

#                                 # ----------计算每五帧的背部位移 - ------------
#                                   #----------统计5s内的抖动次数----------------

files2 = os.listdir(displacement_path)    # 只有displacement的文件
count_path_5s_50=r"J:\年后更新20240226\第二轮\全部原始数据\头上戴帽第二批\背部抖动频率分析\每五秒统计一次的抖动次数（背部位移在阈值内）（3）"


for file_displacement in files2:
    file_path1 = os.path.join(displacement_path, file_displacement)
    new_df1 = pd.read_csv(file_path1)

    # 获取当前文件对应的阈值文件
    # 因为files2和file1里面其实是一样的名字，所以找阈值的时候可以直接用file2代替file1
    threshold_file = os.path.join(folder_path, file_displacement)
    threshold_df = pd.read_csv(threshold_file)
    threshold = threshold_df.iloc[0, 18]  # 获取阈值
    # print(threshold)
    # 初始化计数列表
    countper150 = []

    # 遍历当前文件的每个位移值，并计数
    count = 0
    for i, displacement in enumerate(new_df1['dorsum_displacement'], 1):
        if displacement is not None and displacement > 0 and displacement < threshold:
            count += 1
        if i % 30 == 0:  # 每30个位移（1个位移六分之一s）（共5s）（共150帧）计算一次 count
            countper150.append(count)
            count = 0  # 重置 count

    # 将统计结果添加到新的DataFrame中
    new_df2 = pd.DataFrame()
    new_df2['count'] = countper150

    # 保存结果到每个文件的输出文件中
    new_file_path = os.path.join(count_path_5s_50, file_displacement)
    new_df2.to_csv(new_file_path, index=False)
#                                   #-------------统计5S内的抖动次数----------------

