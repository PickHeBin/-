#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 图片人脸处理.py
# Author: MuNian
# Date  : 2019/7/30

'''
人脸识别技术:
    1. 基于几何/基于模板/基于外貌
    SVM(支持向量机)   PCA(主成分分析)  LDA(线性判断分析) 核方法 跟踪变换

识别技术: .....

零基础 - Python基础语法 --> web开发(15K)(自动化(10K))爬虫(13K) --> 机器学习 --> 深度学习 机器视觉 --> 无人技术 --> AI

8K - 30K
爬虫  自动化 web开发  AI
投资学习 ---> 长期的发展
线上直播 + 课后录播 + 随堂笔记
1 3 5正课 2 4 6解答课  20:30 -22:30
学会才毕业 毕业后具备独立开发项目的能力
课后补课 一对一的课后辅导

兼职 7K左右  8天左右 专门的老师带着各位同学做兼职
全职 就业指导 技术专项指导 模拟BAT笔试面试
毕业后 --就业规划 规划职业 长远发展

2年左右的项目经验 --> 项目主导人才
兼职
8K - 30K

学会才毕业 阶段考核(重读(免费))
flask  django  Python APP软件 web网页 主流框架
架构师 --> 初级架构师(20K平均值)
7880 -- 1000 = 6880 - 500(预订) = 6380

'''

import cv2

# 加载训练集
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

# 读取图片
frame = cv2.imread('timg.jpg')

# 灰度处理
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# 画出人脸
for (x, y, w, h) in faces:
    # print('x', x)
    # print('y', y)
    # print('w', w)
    # print('h', h)
    frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)

# 显示图片
cv2.imshow('python', frame)
# 等待 延迟
cv2.waitKey(0)

# 销毁窗口
cv2.destroyAllWindows()


