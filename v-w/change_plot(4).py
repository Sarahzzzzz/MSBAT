#1.双y轴
# #------------------------------------------------------------------------------------
# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties
# import numpy as np
#
#
# input_folder = r"C:\Users\HP\Desktop\v-w改图\表格4.23"
# excel_names = os.listdir(input_folder)
#
# for i, excel_name in enumerate(excel_names):
#     excel_path = os.path.join(input_folder, excel_name)
#     df = pd.read_csv(excel_path)  # 确保这里的读取方式和你的数据格式匹配，如果是Excel应该用read_excel
#
#     fig, ax1 = plt.subplots()
#
#     color1 = '#4F94CD'
#     color2 = '#A00000'
#
#     # 第一组数据绘制在ax1
#     ax1.set_xlabel('Time (s)', fontsize=19)
#     ax1.set_ylabel('Angle Change (ctrl3)', color=color1, fontsize=19)
#     ax1.plot(df["Angle Change_ctrl3"], color=color1, linewidth=2)
#     ax1.tick_params(axis='y', labelcolor=color1, labelsize=15)
#     ax1.set_yticks(np.linspace(-200, 200, 5))  # 设置y轴刻度范围和刻度数
#
#     # 创建并设置第二个y轴
#     ax2 = ax1.twinx()
#     ax2.set_ylabel('Angle Change (int5)', color=color2, fontsize=19)
#     ax2.plot(df["Angle Change_int5"], color=color2, linewidth=2)
#     ax2.tick_params(axis='y', labelcolor=color2, labelsize=15)
#     ax2.set_yticks(np.linspace(-200, 200, 5))  # 设置y轴刻度范围和刻度数
#
#     ax1.set_xticks(np.arange(0, 2500, 500))  # 设置x轴刻度
#     prop = FontProperties(family='Arial', size=20)
#     ax1.tick_params(axis='x', labelsize=20)
#
#     # 设置边框的线宽
#     for spine in ax1.spines.values():
#         spine.set_linewidth(2)
#     for spine in ax2.spines.values():
#         spine.set_linewidth(2)
#
#     # 调整布局以防止标签超出边界
#     fig.tight_layout()
#
#     plt.show()
#------------------------------------------------------------------------------------

#在Matplotlib中，set_yticks() 和 set_yticklabels() 两个方法分别负责不同的功能：

#set_yticks() - 这个方法用来指定y轴上的刻度线应该出现的具体位置。你通过传入一个数字列表来定义这些位置，这些数字代表y轴上哪些点应该有刻度线。
#set_yticklabels() - 这个方法用来定义在由 set_yticks() 指定的每个刻度位置上显示的文本标签。
# 这意味着你可以为每个刻度自定义文本，比如将数值转换成更有意义的描述，或者在你的例子中，调整标签以反映原始的、未经偏移的数据值。
#这两个方法结合使用，允许你完全控制图表的y轴刻度的位置和显示的内容，确保图表既美观又实用。
# 正因为此，使用这些方法时需要保证刻度位置和标签之间的一一对应关系，以避免创建出令人困惑的图表。如果标签和位置不匹配，图表的读者可能会误解数据的真实含义。
# #
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

input_folder = r"C:\Users\HP\Desktop\v-w改图\表格0509"
excel_names = os.listdir(input_folder)

for i, excel_name in enumerate(excel_names):
    excel_path = os.path.join(input_folder, excel_name)
    df = pd.read_csv(excel_path)  # 确保这里的读取方式和你的数据格式匹配

    fig, ax1 = plt.subplots(figsize=(9,5))

    color1 = "#0000C0"  #蓝色
    color2 = "#A00000"  #红色

    #戴帽
    # # 有CD1_给药前
    # ax1.plot(df["Angle Change_yBM1"], color=color3, linewidth=1)
    # #有CD1_给药后，将其向下偏移400
    # ax1.plot(df["Angle Change_yLM1"] - 250, color=color4, linewidth=1)

    # # 无CD1_给药前
    ax1.plot(df["Angle Change_yCtrl3"], color=color1, linewidth=1)
    #无CD1 给药后，将其向下偏移400
    ax1.plot(df["Angle Change_yINT5"] - 250, color=color2, linewidth=1)




    # ax1.set_xlabel('Time (s)', fontsize=19)
    # ax1.set_ylabel('Angle Change', fontsize=19)

    # 设置正确的y轴刻度和标签，反映实际数据范围
    #用于设置y轴上的刻度位置,这些数值会成为y轴的刻度点,图表的y轴将在这些具体的数值位置显示刻度线。
    # actual_ticks = np.linspace(-600, 200, 9)  # 从-600到200，适应数据偏移

    #ax1.set_yticklabels() 方法用于设置与通过 set_yticks() 方法指定的刻度位置相对应的标签。
    # corrected_labels = [str(int(tick)) if tick >= -200 else str(int(tick + 400)) for tick in actual_ticks]
    # ax1.set_yticks(actual_ticks)
    # ax1.set_yticklabels(corrected_labels, fontsize=15)

    # ax1.set_xticks(np.arange(0, 2500, 500))
    # ax1.tick_params(axis='x', labelsize=20)
    ax1.set_yticks([])
    ax1.set_xticks([])

    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['left'].set_visible(False)

    # 设置边框的线宽
    # for spine in ax1.spines.values():
    #     spine.set_linewidth(2)

    # 调整布局以防止标签超出边界
    fig.tight_layout()

    plt.show()
