import cv2
import numpy as np


video_path = r"C:\Users\HP\Desktop\11111\INT1.mp4" # 原视频
trj_path = r"C:\Users\HP\Desktop\11111\video\trj.mp4"  # 轨迹视频
processed_video_path = r"C:\Users\HP\Desktop\11111\video\processed.mp4"  #处理后检索视频
output_image_path = r"C:\Users\HP\Desktop\11111\video\trj.png"  # 轨迹图

def process_frame(frame):
    # 将BGR图像转换为HSV图像
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 定义黑色的HSV范围
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])

    # 创建黑色区域的掩模
    mask = cv2.inRange(hsv_image, lower_black, upper_black)

    # 寻找掩模中的轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return frame, (0, 0)

    # 找到最大的轮廓
    largest_contour = max(contours, key=cv2.contourArea)

    # 计算最大轮廓的中心位置
    M = cv2.moments(largest_contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        # return (cX, cY)   # 返回中心位置
    else:
        cX, cY = 0, 0
        #除了找到并标记黑色区域的轮廓外，还在轮廓的中心绘制一个红色圆点，并以绿色线条突出显示最大轮廓。
    cv2.circle(frame, (cX, cY), 5, (255, 0, 0), -1)  # 在中心位置绘制红色圆点
    cv2.drawContours(frame, [largest_contour], -1, (0, 255, 0), 2)  # 绘制绿色轮廓
    return frame, (cX, cY)



#保存两个视频文件：一个是带有中心点轨迹的视频，另一个是将每帧处理后的视频。它还显示处理过的帧，并允许用户通过按q键来提前退出。
def process_video(video_path, trajectory_path, processed_video_path, final_frame_path):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # 获取视频帧率和尺寸
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 创建视频写入对象
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 注意编解码器与文件格式的匹配
    trj_video = cv2.VideoWriter(trajectory_path, fourcc, fps, (width, height))
    processed_video = cv2.VideoWriter(processed_video_path, fourcc, fps, (width, height))

    # 创建用于绘制轨迹的黑色背景
    background = np.zeros((height, width, 3), dtype=np.uint8)

    # 用于存储中心点，以便连续绘制线段
    points = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame, center = process_frame(frame)
        if center:
            points.append(center)  # 添加新的中心点到列表中

        # 在黑色背景上绘制所有点连成的线
        for i in range(1, len(points)):
            if points[i - 1] is None or points[i] is None:
                continue
            cv2.line(background, points[i - 1], points[i], (0, 0, 255), 2)

        # 将带有轨迹的背景写入新视频

        trj_video.write(background)
        processed_video.write(processed_frame)
        cv2.imshow("Processed Frame", processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if background is not None:
        cv2.imwrite(final_frame_path, background)

    cap.release()
    trj_video.release()
    processed_video.release()
    cv2.destroyAllWindows()


# 示例调用
process_video(video_path, trj_path, processed_video_path, output_image_path)