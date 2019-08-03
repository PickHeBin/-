#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 图像几何处理.py
# Author: MuNian
# Date  : 2019/7/6
'''
电脑识别的图片  16进制图片 ---> 矩形数组
[[
    1, 2, 3, 4
    4, 6, 6, 7
]]
自动化  ---> AI 底层
web - > 开发

爬虫 - > 大数据

扫地机器人 识别技术  自动躲避障碍 ---> 卷积神经网络 + TF
就业趋势最好的:
    web开发
    自动化
    爬虫

发展最好的:
    数据分析
    人工智能
    云计算

4.5个月  1 2 3 正课  2 4 6 解答课
每天晚上20:30 - 22:30  直播上课 + 课后录播 + 随堂笔记
学会才毕业的水平 毕业后 具备独立开发项目的能力

8K - 27K

1. 掌握市场上面的主流框架  ....
2.  应对公司的技能需求 .....
.....
零基础学习Python优势:
    1. 比其他语言入门快
    2. 简单 易懂  第三方库非常多
    3. 快速的到达企业技能需求
    4. Python在未来的方向比其他语言就业范围广
    ....
转行
高薪 web  爬虫 自动化

转行 :   1. 学不学的会  课后辅导 课后解答 一对一的  学员学习跟踪  学员反馈 学习计划制定...
        2 . 就业方向

1. 框架  数据库  架构 模型 ...  APP软件开发
java 100行实现     独立的功能
Python 30 实现


'''

import numpy as np
import cv2

# 图片读取  行列 通道
img = cv2.imread('27a02.jpg')

#  按照指定的宽度 高度 缩放
res = cv2.resize(img, (132, 150))

# 按照比例缩放   x, y 放大一倍    None 在后面设置缩放因子
# 插值法  INTER_LINEAR   缩放 INTER_AREA
res2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Python', res)
cv2.imshow('Pythoon2', res2)
cv2.waitKey(0)

# 图片的翻转
# 参数 2 = 0; 垂直翻转 x轴  2 > 0 水平翻转  y轴  2< 0 水平垂直翻转
dst = cv2.flip(img, -1)
#  横向并排  对比显示
cv2.imshow('hahaha', np.hstack((img, dst)))
cv2.waitKey()

# 平移
rows, cols = img.shape[:2]
# 平移矩阵  numpy  float32 类型
#  x 100   y 50
M = np.float32([[1, 0 ,500], [0 , 1, 200]])
# 第三个参数 图像的尺寸中心
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('daaadda', dst)
cv2.waitKey()

# 45°顺时针 旋转图片 缩小一半
# 第一个参数 旋转中心  第二个 旋转角度  第三个缩放因子
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -45, 0.5)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('aaa', dst)
cv2.waitKey()







