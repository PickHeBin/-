#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 图像处理.py
# Author: MuNian
# Date  : 2019/7/2

import cv2

# 读取图片  返回一个矩形数组
img = cv2.imread('27a02.jpg', 0)
# 显示窗口 1. 窗口的名称
cv2.imshow('python', img)
cv2.waitKey(0)


# 定义窗口来显示图片
cv2.namedWindow('Python2', cv2.WINDOW_NORMAL)
cv2.imshow('Python2', img)

# 等待用户输入
# 作用: 用来延迟
cv2.waitKey(0)