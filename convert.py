#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# learning time: 2022/11/11 15:51
__author__ = '李晓宁'

import numpy as np
import cv2
from matplotlib import pyplot as plt

cv2.namedWindow('SHOW', cv2.WINDOW_NORMAL)  # 窗口大小保持比例，可以改变大小
# cv2.namedWindow("SHOW",cv2.WINDOW_AUTOSIZE)  # 窗口大小不可以改变
# cv2.namedWindow('SHOW', cv2.WINDOW_FREERATIO)  # 窗口大小自适应比例（图片变形），可以改变大小
# cv2.namedWindow('SHOW', cv2.WINDOW_KEEPRATIO)  # 窗口大小保持比例，可以改变大小

img_bgr = cv2.imread("E:\\PycharmProjects\\opencv_learning\\exam001显示图像\\1.jpg")
print(img_bgr.shape)
height, width = img_bgr.shape[:2]
img_bgr = cv2.resize(img_bgr, (width//4, height//4), interpolation=cv2.INTER_AREA)

cv2.imshow("BGR", img_bgr)
# cv2.waitKey(0)

# B、G、R分量的提取
(B, G, R) = cv2.split(img_bgr)
# cv2.imshow("Blue", B)
# cv2.imshow("Green", G)
# cv2.imshow("Red", R)

img_merged = cv2.merge([B,G,R])
# cv2.imshow("Merged",img_merged)
# cv2.waitKey(0)

img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
cv2.imshow("RGB",img_rgb)
# cv2.waitKey(0)

img_gray = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY",img_gray)
# cv2.waitKey(0)

img_hsv = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",img_hsv)
# cv2.waitKey(0)

img_lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", img_lab)
# cv2.waitKey(0)

titles = ['BGR', 'Blue', 'Green', 'Red', 'RGB', 'GRAY', 'HSV', 'LAB']
images = [img_rgb, B, G, R, img_bgr, img_gray, img_hsv, img_lab]  # 'BGR'对应img_rgb，'RGB'对应img_bgr，原因：plt和cv2的区别所致
for i in range(8):
    plt.subplot(2, 4, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])  # 设置图像标题
# plt.xticks([]), plt.yticks([])  # 设置x,y轴刻度，不设置则自动设置
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

