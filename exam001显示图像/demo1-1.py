# -*- coding: utf-8 -*-
# By:Eastmount CSDN
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 读取图像
img1 = cv2.imread('1.jpg')
"""
cv2.imread()接口读图像，读进来直接是BGR格式，数据格式在0~255。需要特别注意的是图片读出来的格式是BGR，不是我们最常见的RGB格式，颜色肯定有区别。
"""
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
# np.resize(img1, (200, 300, -1))
print(img1.shape)
"""
cv2.cvtColor(p1,p2) 是颜色空间转换函数，p1是需要转换的图片，p2是转换成何种格式。
cv2.COLOR_BGR2RGB 将BGR格式转换成RGB格式
cv2.COLOR_BGR2GRAY 将BGR格式转换成灰度图片
"""

img2 = cv2.imread('2.jpg')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
print(img2.shape)

img3 = cv2.imread('3.jpg')
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
print(img3.shape)

img4 = cv2.imread('4.jpg')
img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
print(img4.shape)


# 显示四张图像
titles = ['1', '2', '3', '4']
images = [img1, img2, img3, img4]
for i in range(4):
    plt.subplot(2, 2, i + 1)  # 两行两列，从左到右，从上到下
    plt.imshow(images[i], 'gray')  # 将灰度图像按照灰度值的高低映射成彩色图像
    plt.title(titles[i])  # 设置图像标题
# plt.xticks([]), plt.yticks([])  # 设置x,y轴刻度，不设置则自动设置
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
