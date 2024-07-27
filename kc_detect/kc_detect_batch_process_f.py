import cv2
import numpy as np
import os
import time
import csv
import pandas as pd
#俯视————生成轨迹图--生成坐标的文件夹（含displacement）---生成总结的displacement
video_folder = r"C:\Users\HP\Desktop\JY_Data_20240520\round2\F\video"
output_folder = r"C:\Users\HP\Desktop\JY_Data_20240520\round2\F\tra"  # 轨迹文件夹
csv_folder = r"C:\Users\HP\Desktop\JY_Data_20240520\round2\F\coordinate\coordinate(1)" # CSV 存放文件夹

#处理帧
def process_frame(frame):
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])
    mask = cv2.inRange(hsv_image, lower_black, upper_black)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return frame, (0, 0)
    largest_contour = max(contours, key=cv2.contourArea)
    M = cv2.moments(largest_contour)
    cX = int(M["m10"] / M["m00"]) if M["m00"] != 0 else 0
    cY = int(M["m01"] / M["m00"]) if M["m00"] != 0 else 0
    cv2.circle(frame, (cX, cY), 5, (255, 0, 0), -1)
    cv2.drawContours(frame, [largest_contour], -1, (0, 255, 0), 2)
    return frame, (cX, cY)

def process_video(video_path, output_image_path, output_csv_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    background = np.zeros((height, width, 3), dtype=np.uint8)
    points = []

    with open(output_csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Frame", "X", "Y"])

        frame_index = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            _, center = process_frame(frame)
            if center:
                points.append(center)
                writer.writerow([frame_index] + list(center))
            for i in range(1, len(points)):
                if points[i - 1] is None or points[i] is None:
                    continue
                cv2.line(background, points[i - 1], points[i], (0, 0, 255), 2)
            frame_index += 1

    if background is not None:
        cv2.imwrite(output_image_path, background)
        print(f"Background image saved to {output_image_path}")
    else:
        print(f"Background image not saved for {video_path}")
    cap.release()
    cv2.destroyAllWindows()


def displacement(csv_path):
    df = pd.read_csv(csv_path)
    displacements = []
    for i in range(1, len(df)):
        x1, y1 = df.iloc[i - 1]['X'], df.iloc[i - 1]['Y']
        x2, y2 = df.iloc[i]['X'], df.iloc[i]['Y']
        displacement = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        displacements.append(displacement)
    df['displacement'] = [None] + displacements
    # 计算总位移
    displacement_sum = sum(displacement for displacement in displacements if displacement is not None)
    # 初始化 displacement_sum 列
    df['displacement_sum'] = None
    if len(df) > 0:
        df.at[0, 'displacement_sum'] = displacement_sum

    df.to_csv(csv_path, index=False)


if not os.path.exists(output_folder):
    os.makedirs(output_folder)
if not os.path.exists(csv_folder):
    os.makedirs(csv_folder)

for video_filename in os.listdir(video_folder):
    video_path = os.path.join(video_folder, video_filename)
    if video_path.lower().endswith(('.mp4', '.avi', '.mov')):
        output_image_path = os.path.join(output_folder, video_filename.split('.')[0] + '.png')
        csv_file_path = os.path.join(csv_folder, video_filename.split('.')[0] + '.csv')
        time_start = time.time()
        process_video(video_path, output_image_path, csv_file_path)
        displacement(csv_file_path)
        time_end = time.time()
        mytime = time_end - time_start
        print("Time cost for processing {}: {:.2f} seconds".format(video_filename, mytime))

#
#
#     #---------------------------------------------分离出每个表格的displacement-----------------------------------------------------

# #分离出每个excel文件的位移值
# # 提取所有文件夹里的某一个单元格的值，并且生成在新的文件夹里的新的excel里，
# # 新的文件夹里excel的文件名和旧的文件夹里的excel名相同，新的excel的构成是，
# # 第一列是各个excel的名字，第二列是旧excel提取出来的对应的单元格的值
#
# # 定义旧文件夹和新文件夹的路径
old_folder = csv_folder# 旧文件夹路径
new_folder = r"C:\Users\HP\Desktop\JY_Data_20240520\round2\F\coordinate\coordinate(2)" # 新文件夹路径

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


#---------------------------------------------- 合并成displacement --------------------------------------------------
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
combined_excel_path =r"C:\Users\HP\Desktop\JY_Data_20240520\round2\F\displacement.xlsx"
# 保存合并的Excel文件
combined_df.to_excel(combined_excel_path, index=False)
print(f"所有 Excel 文件已合并到 '{combined_excel_path}'")


#
#
# #------------------------------------------计算俯视速度------------------------------------------------
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

input_folder = r"C:\Users\HP\Desktop\JY_Data_20240520\round2\F\coordinate\coordinate(1)"
speed_folder = r"C:\Users\HP\Desktop\JY_Data_20240520\round2\F\speed_excel"
plot_folder = r"C:\Users\HP\Desktop\JY_Data_20240520\round2\F\speed_plot"

# 获取所有excel文件
excel_names = os.listdir(input_folder)


# 计算欧几里得距离
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)


# 循环处理每个excel文件
for excel_name in excel_names:
    excel_path = os.path.join(input_folder, excel_name)
    df = pd.read_csv(excel_path)

    # 提取坐标数据
    centroid_coordinates = df[['X', 'Y']].values
    speeds = []
    displacements = []
    t = 1  # 每0.5秒计算一次位移
    for i in range(0, len(centroid_coordinates) - 60, 60):  # 每隔30帧（0.5秒）计算一次位移
        displacement = euclidean_distance(centroid_coordinates[i], centroid_coordinates[i + 30])
        displacements.append(displacement)
        speeds.append(displacement / t)

    df_speed = pd.DataFrame(speeds, columns=['Speed'])  # 创建包含速度数据的新DataFrame
    speed_file_path = os.path.join(speed_folder, excel_name.replace('.csv', '_speed.csv'))
    df_speed.to_csv(speed_file_path, index=False)
    print("已保存速度到文件:", speed_file_path)

    # 绘图保存
    time = np.arange(0, len(speeds) , 1)
    plt.plot(time, speeds, color="red", label="Speed")
    plt.xlabel('Time (s)', fontsize=18)
    plt.ylabel('Speed (units/s)', fontsize=18)
    plt.ylim(0, 1500)
    prop = FontProperties(family='Arial', size=14)
    plt.xticks(fontproperties=prop)
    plt.yticks(fontproperties=prop)
    plt.legend()

    plot_path = os.path.join(plot_folder, os.path.splitext(excel_name)[0] + '.png')
    plt.savefig(plot_path)
    plt.close()