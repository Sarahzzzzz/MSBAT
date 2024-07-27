import os
import pandas as pd
import glob
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 使用中文字体SimHei
plt.rcParams['font.sans-serif'] = ['SimHei']

# 处理小鼠身长数据
def process_length(folder_path):
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        df['length_mouse'] = abs(df['tailbase_x'] - df['nose_x'])
        df.loc[0, 'length'] = df['length_mouse'].sum()
        df.loc[0, 'length_mouse_mean'] = df['length_mouse'].mean()
        df.loc[0, 'thr_average_1-50'] = df['length_mouse'].mean() / 50
        df.to_csv(file_path, index=False, encoding='utf-8')

# 计算每五帧的背部位移
def calculate_displacement(folder_path, displacement_path):
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        threshold = df.iloc[0, 18]
        dorsum_displacement = [
            ((df.iloc[i + 4]['tailbase_x'] - df.iloc[i]['tailbase_x'])**2 +
             (df.iloc[i + 4]['tailbase_y'] - df.iloc[i]['tailbase_y'])**2)**0.5
            if i + 4 < len(df) else None
            for i in range(0, len(df), 5)
        ]
        new_df = pd.DataFrame({'dorsum_displacement': dorsum_displacement})
        new_file_path = os.path.join(displacement_path, file)
        new_df.to_csv(new_file_path, index=False)

# 统计每五秒内的抖动次数
def count_shakes(displacement_path, folder_path, count_path_5s_50):
    files = os.listdir(displacement_path)
    for file in files:
        file_path = os.path.join(displacement_path, file)
        new_df = pd.read_csv(file_path)
        threshold = pd.read_csv(os.path.join(folder_path, file)).iloc[0, 18]
        countper150 = [
            sum(1 for displacement in new_df['dorsum_displacement'][i:i+30]
                if displacement is not None and displacement > 0 and displacement < threshold)
            for i in range(0, len(new_df), 30)
        ]
        new_df2 = pd.DataFrame({'count': countper150})
        new_file_path = os.path.join(count_path_5s_50, file)
        new_df2.to_csv(new_file_path, index=False)

# 绘制抖动频率图
def plot_frequency(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xlsx') or file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            df = pd.read_csv(file_path)
            y_values = df['count'] / 5
            x_values = range(len(y_values))
            x_values = [x * 5 for x in x_values]
            plt.figure()
            plt.plot(x_values, y_values, color="red", label="shaking frequency")
            plt.xlabel('Time（s）', fontsize=18)
            plt.ylabel('shaking frequency change(times/s)', fontsize=18)
            plt.ylim(0, 8)
            prop = FontProperties(family='Arial', size=14)
            plt.xticks(fontproperties=prop)
            plt.yticks(fontproperties=prop)
            output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.png')
            plt.savefig(output_path)
            plt.close()

# 计算抖动频率和平均抖动频率
def calculate_shaking_frequency(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for file in glob.glob(os.path.join(input_folder, "*.csv")):
        df = pd.read_csv(file)
        counts = df['count'].tolist()
        shaking_frequency = [round(x / 5) for x in counts]
        shaking_frequency_average = [
            round(sum(counts[i:i + 6]) / 30) for i in range(0, len(counts), 6)
        ]
        df["shaking_frequency"] = pd.Series(shaking_frequency)
        df['shaking_frequency_average'] = pd.Series(shaking_frequency_average)
        df.to_csv(os.path.join(output_folder, os.path.basename(file)), index=False)

# 计算抖动频率百分比
def calculate_shaking_percentage(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for file in glob.glob(os.path.join(input_folder, "*.csv")):
        df = pd.read_csv(file)
        shaking_frequency_average = df['shaking_frequency_average'].head(20)
        frequency_sum = shaking_frequency_average.sum()
        percent = (shaking_frequency_average / frequency_sum) * 100
        accumulate = percent.cumsum()
        time_intervals = [f'{i}-{i + 30}' for i in range(0, 600, 30)]
        new_df = pd.DataFrame({
            'time': time_intervals[:20],
            'shaking_frequency_average': shaking_frequency_average,
            'frequency_sum': [frequency_sum] * 20,
            'percent': percent,
            'accumulate_percent': accumulate
        })
        output_path = os.path.join(output_folder, os.path.basename(file))
        new_df.to_csv(output_path, index=False)

# 总结抖动频率百分比数据
def summarize_shaking(input_folder, summary_excel_path):
    time_intervals = [f'{i}-{i + 30}' for i in range(0, 600, 30)]
    summary_df = pd.DataFrame({'time': time_intervals})
    for file_name in sorted(os.listdir(input_folder)):
        file_path = os.path.join(input_folder, file_name)
        file_name_without_extension = os.path.splitext(file_name)[0]
        df = pd.read_csv(file_path)
        accumulate_percent = df['accumulate_percent'].tolist()
        summary_df[file_name_without_extension] = accumulate_percent
    summary_df.to_excel(summary_excel_path, index=False)

# 路径设置
folder_path = r"C:\Users\HP\Desktop\JY_Data_20240520\round2\Z\shaking_frequency\原始数据（1）"    #原始表格
displacement_path = r"C:\Users\HP\Desktop\JY_Data_20240520\round2\Z\shaking_frequency\分离出的背部位移（2）" #分离出的背部位移
count_path_5s_50 = r"C:\Users\HP\Desktop\JY_Data_20240520\round2\Z\shaking_frequency\每五秒统计一次的抖动次数（3）" #每五秒统计一次的抖动次数（背部位移在阈值内）
output_folder_plots = r"C:\Users\HP\Desktop\JY_Data_20240520\round2\Z\shaking_frequency\抖动频率图（4）"  #抖动频率图
output_folder_shaking = r"C:\Users\HP\Desktop\JY_Data_20240520\round2\Z\shaking_frequency\抖动频率+平均抖动频率（5）"  #抖动频率+平均抖动频率
percentage_folder = r"C:\Users\HP\Desktop\JY_Data_20240520\round2\Z\shaking_frequency\抖动频率百分比原始数据（6）"  #抖动频率百分比原始数据
summary_excel_path = r"C:\Users\HP\Desktop\JY_Data_20240520\round2\Z\shaking_frequency\抖动频率百分比总结表格（7）\1.xlsx"    #抖动频率百分比总结表格

# 执行函数
process_length(folder_path)
calculate_displacement(folder_path, displacement_path)
count_shakes(displacement_path, folder_path, count_path_5s_50)
plot_frequency(count_path_5s_50, output_folder_plots)
calculate_shaking_frequency(count_path_5s_50, output_folder_shaking)
calculate_shaking_percentage(output_folder_shaking, percentage_folder)
summarize_shaking(percentage_folder, summary_excel_path)
