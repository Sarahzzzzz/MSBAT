import os
import pandas as pd
import matplotlib.pyplot as plt

# 设置全局字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用中文字体SimHei

# 文件夹路径
folder_path = r"C:\Users\HP\Desktop\Ctrl，KD_有CD1_正_处理表格\背部坐标轨迹图（nose）\v-w原始数据" # 替换为您的文件夹路径
output_folder = r"C:\Users\HP\Desktop\Ctrl，KD_有CD1_正_处理表格\背部坐标轨迹图（nose）\背部坐标轨迹图" # 新建一个文件夹用于保存图形

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 用于保存所有图形的纵坐标最大值
max_y_values = []

# 遍历文件夹中的所有 Excel 文件
for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx') or file_name.endswith('.csv'):  # 确保文件是 Excel 文件
        file_path = os.path.join(folder_path, file_name)

        # 读取 Excel 文件
        df = pd.read_csv(file_path)

        # 提取坐标点数据
        time = df["bodyparts"]
        x_values = df['doursm_x']
        y_values = df['doursm_y']
        # likelihood = df['doursm']
        # 每隔五行读取一次坐标点
        x_values = x_values[::30]
        y_values = y_values[::30]
        time = time[::30]/30
        # 绘制曲线图
        plt.plot(time, x_values, color="red",label="x")
        plt.plot(time, y_values, color="blue",label="y")
        plt.legend()
        plt.ylim(0,2500)

        # 用 os.path.splitext() 函数来删除文件扩展名
        plt.title(os.path.splitext(file_name)[0])  # 使用文件名作为图形标题
        plt.xlabel('time')
        plt.ylabel('x和y随时间的变化')

        # 获取当前图形纵坐标的最大值，并保存到列表中
        max_y_values.append(max(max(x_values), max(y_values)))

        plt.grid(True)

        # 图形保存路径
        output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.png')

        # 保存图形
        plt.savefig(output_path)  # 保存为 png 格式图片
        plt.close()  # 关闭当前图形，以便绘制下一个图形

# 设置所有图形的纵坐标范围为最大值中的最大值
plt.ylim(0, max(max_y_values))

# 显示所有图形
# plt.show()


        #-------------------------------------------------------------------------
#散点图-----颜色深浅表示时间
# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.colors import Normalize
#
# # 文件夹路径
# folder_path = "J:\年后更新20240226\全部原始数据\dorsum轨迹绘制原始数据\无cd1"  # 替换为您的文件夹路径
# output_folder = "J:\年后更新20240226\全部原始数据\dorsum轨迹绘制\无CD1"  # 新文件夹名称
#
# # 创建新的文件夹用于保存图形
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#
# # 遍历文件夹中的所有文件
# for file_name in os.listdir(folder_path):
#     if file_name.endswith('.xlsx') or file_name.endswith('.csv'):  # 确保文件是 Excel 文件
#         file_path = os.path.join(folder_path, file_name)
#
#         # 读取 Excel 文件
#         df = pd.read_csv(file_path)
#
#         # 将时间列转换为日期时间格式
#         time = df['bodyparts']
#
#         # 创建归一化器，用于将时间映射到颜色映射范围内
#         norm = Normalize(vmin=time.min(), vmax=time.max())
#
#         # 绘制散点图，并使用红色 colormap 表示时间的变化
#         plt.figure(figsize=(10, 6))
#         plt.scatter(df['doursm_x'], df['doursm_y'], c=time, cmap='Reds', norm=norm, s=5)
#         plt.colorbar(label='Time')  # 添加颜色条，用于表示时间
#         plt.title(f'XY Coordinates Over Time - {os.path.splitext(file_name)[0]}')
#         plt.xlabel('X Coordinate')
#         plt.ylabel('Y Coordinate')
#         plt.grid(True)
#
#         # 图形保存路径
#         output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.png')
#
#         # 保存图形
#         plt.savefig(output_path)  # 保存为 png 格式图片
#         plt.close()  # 关闭当前图形，以便绘制下一个图形


# -------------------------------------------------------------------------
#三维空间
# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用中文字体SimHei
# # 文件夹路径
# folder_path = "J:\年后更新20240226\全部原始数据\dorsum轨迹绘制原始数据\无cd1"  # 替换为您的文件夹路径
# output_folder = "J:\年后更新20240226\全部原始数据\dorsum轨迹绘制\无CD1"  # 新文件夹名称
#
# # 创建新的文件夹用于保存图形
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#
# # 遍历文件夹中的所有文件
# for file_name in os.listdir(folder_path):
#     if file_name.endswith('.xlsx') or file_name.endswith('.csv'):  # 确保文件是 Excel 文件
#         file_path = os.path.join(folder_path, file_name)
#
#
#         df = pd.read_csv(file_path)
#
#
#         time = df['bodyparts']
#
#         fig = plt.figure(figsize=(10, 6))
#         ax = fig.add_subplot(111, projection='3d')
#         ax.plot_trisurf(df['doursm_x'], df['doursm_y'], time, cmap='viridis')
#
#         ax.set_title(f'3D - {os.path.splitext(file_name)[0]}')
#         ax.set_xlabel('X Coordinate')
#         ax.set_ylabel('Y Coordinate')
#         ax.set_zlabel('Time')
#         ax.grid(True)
#
#         output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '_3d.png')
#
#         # 保存图形
#         plt.savefig(output_path)  # 保存为 png 格式图片
#         plt.close()  # 关闭当前图形，以便绘制下一个图形



