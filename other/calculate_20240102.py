import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# 替换为你的 Excel 文件路径
excel_path = r"J:\第二批老鼠数据\二次补\无CD1  INT\正\1INT.csv"
df = pd.read_csv(excel_path)
print("shape:",df.shape)
# 提取坐标数据

nose_coordinates = df[['nose_x', 'nose_y']].values
back_coordinates = df[['doursm_x', 'doursm_y']].values
tail_coordinates = df[['tailbase_x', 'tailbase_y']].values

# print("背部坐标\n",back_coordinates)
# print("鼻子坐标\n",nose_cordinates)
# print("尾巴坐标\n",tail_coordinates)

#
# # 计算速度
delta_coordinates = np.diff(back_coordinates, axis=0)
frame_rate = 30.0  # 假设视频的帧率是30帧/秒
velocity = delta_coordinates * frame_rate
speed = np.linalg.norm(velocity, axis=1)
#
# 计算向量
vector_nose_to_back = nose_coordinates - back_coordinates
vector_tail_to_back = tail_coordinates - back_coordinates

# 计算向量的模
magnitude_nose_to_back = np.linalg.norm(vector_nose_to_back, axis=1)
magnitude_tail_to_back = np.linalg.norm(vector_tail_to_back, axis=1)

# # 计算点积
dot_product = np.sum(vector_nose_to_back * vector_tail_to_back, axis=1)
#
# # 计算夹角（弧度）
# 计算了鼻子到背部和背部到尾巴两个向量之间的夹角。如果余弦相似度为1，夹角为0度；如果余弦相似度为-1，夹角为180度。
# 夹角的计算结果是以弧度为单位的，你可以将其转换为度数，得到更直观的角度
cosine_similarity = dot_product / (magnitude_nose_to_back * magnitude_tail_to_back)
angle_radians = np.arccos(np.clip(cosine_similarity, -1.0, 1.0))
#
# # 将弧度转换为度
angle_degrees = np.degrees(angle_radians)
#
# 计算夹角变化
angle_change = np.diff(angle_degrees)

# 可视化速度和夹角变化
fig, ax1 = plt.subplots()

ax1.set_xlabel('Time',fontsize=15)
ax1.set_ylabel('Speed', color='blue',fontsize=15)
ax1.plot(speed, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_ylim(ymax = 35000)



ax2 = ax1.twinx()
ax2.set_ylabel('Angle Change (degrees)', color='darkred',fontsize=15)
ax2.plot(angle_change, color='red')
ax2.tick_params(axis='y', labelcolor='darkred')
ax2.set_ylim(ymin = -200,ymax = 200)


# fig.tight_layout()
plt.title('Speed and Angle Change over Time',fontsize=15)
plt.show()

