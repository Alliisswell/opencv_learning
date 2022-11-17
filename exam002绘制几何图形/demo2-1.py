# -*- coding: utf-8 -*-
# By:Eastmount CSDN
import cv2
import numpy as np

# 创建黑色背景图
img = np.zeros((1024, 2048, 3), np.uint8)
print(type(img))

img_1 = cv2.imread("E:\\PycharmProjects\\opencv_learning\\exam001显示图像\\2.jpg")
print(type(img_1))
img_2 = img_1
img[:200, :300, :] = img_1
img[:200, 300:600, :] = img_2

# (1)绘制直线：图像、起点坐标、终点坐标、颜色、粗细
cv2.line(img, (0, 0), (512, 512), (255, 0, 255), 5)  # 将直线绘制在img图片上

# (2)绘制矩形：图像、左上角坐标、右下角坐标、颜色、粗细
cv2.rectangle(img, (20, 300), (350, 450), (255, 0, 0), 2)

# (3)绘制圆形：图像、圆心坐标、半径、颜色、粗细\填充
cv2.circle(img, (400, 400), 50, (255, 255, 0), -1)

# (4)绘制椭圆：图像、圆心坐标、长轴和短轴、偏转角度20
# 圆弧起始角的角度、圆弧终结角的角度、颜色、线条粗细
cv2.ellipse(img, (320, 100), (100, 50), 20, 0, 360, (255, 0, 255), 2)

# (5)绘制四边形：图像、多边形曲线阵列、是否闭合、颜色、粗细
pts = np.array([[10, 80], [120, 80], [120, 200], [30, 250]])
cv2.polylines(img, [pts], True, (255, 255, 255), 5)

# (6)绘制六边形
pts = np.array([[50, 190], [380, 420], [255, 50], [120, 420], [450, 190], [0, 0]])
cv2.polylines(img, [pts], True, (0, 255, 255), 1)

# (7)绘制文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'I love Python!!! By:Eatmount CSDN',
            (0, 512), font, 0.6, (255, 255, 0), 2)

height, width = img.shape[:2]
img = cv2.resize(img, (width//2, height//2), interpolation=cv2.INTER_AREA)
print(img.shape)
print(type(img))

# height, width = img.shape[:2]
# img = np.resize(img, (height//2, width//2, 3))
print(img.shape)
print(type(img))


# 显示图像
cv2.imshow("img", img)  # "img"为标题

# 等待显示
cv2.waitKey(30000)
cv2.destroyAllWindows()

