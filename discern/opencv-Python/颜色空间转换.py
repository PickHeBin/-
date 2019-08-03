#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 颜色空间转换.py
# Author: MuNian
# Date  : 2019/7/2
'''
1. BGR   HSV - numpy 数组
opencv:
     人机交互
     物体识别
     ...

Python的趋势:
    就业方向好的: 4 -5 个月快速就业   基于零基础开发的
        1. web开发   15K
        2. 爬虫开发  15K
        3. 自动化   10K
4个月 快速就业  项目主导
学习你能够达到什么样的企业需求:
    1. 掌握Python主流 web框架 爬虫框架 自动化框架
    2. 根据web框架设计 开发对应的数据库 并且进行数据采集 存储
    3. 根据业务流程  需求分析逻辑 开发对应的 爬虫搜索引擎  web前后台业务  自动化使用
    4. 2 -3  年项目经验的  企业当中遇到问题 根据实践情况解决  设计对应流程 架构
    ....

腾讯AI研发班(5080)教研成本 服务成本  名额限制 2个名额 + 报一期送一期 + BAT全栈进阶班级
VIP: 课后录播 + 随堂笔记 + 源码 + 线上直播
    学会才毕业  1 3 5 正课  2 4 6解答 20:30 - 22:30

学习Python优势:
    1. 简单 易懂 可读性高 开源 免费 ...
    2. 非常适合零基础的入门编程行业
    3. 第三方库多
    4. 在未来Python就业趋势和发展比其他语言范围广
    ...


'''

import cv2

# 读取图片
img = cv2.imread('27a02.jpg')
#  转换成灰度图
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 1. 窗口标题  彩色图像
cv2.imshow('img', img)
# 灰度图像
cv2.imshow('gray', img_gray)
cv2.waitKey()

# 获取所有的转换模式: 把图像的所有色素全部转换
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

# 蓝色HSV值
import numpy as np
# numpy 数组转换 [[[255, 0, 0]]]  RGB颜色对应表 [[[120 255 255]]]
blue = np.uint8([[[255, 0, 0]]])
# cv2.COLOR_BGR2HSV
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
print(hsv_blue)

# 追踪蓝色物体
# 视频采集  默认摄像设备
capture = cv2.VideoCapture(0)

# 蓝色的范围 不同的光照条件是不一样的
lower_blue = np.array([100, 110, 110])
upper_blue = np.array([130, 255, 255])

# 死循环
while True:
    # 捕获视频中的一帧
    ret, frame = capture.read()
    # 从BGR转换到 HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # inRange()介于 lower/upper 之间为白色 其余为黑色
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # 保留原图中的蓝色部分
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # 显示图片
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) == ord('q'):
        break
