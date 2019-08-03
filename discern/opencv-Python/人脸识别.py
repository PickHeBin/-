#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 人脸识别.py
# Author: MuNian
# Date  : 2019/7/24
'''
1. 基于几何/基于模板
    人脸识别算法  SVM()支持向量机  PCA(主成分分析)多个维度提取主要成分  LDA(线性判别分析)  核方法

神经网络: 模式识别 分类识别 Kohonen  特征提取  动态人脸识别

亚马逊: 深度神经网络
谷歌: 卷积神经网络
IBM: 深度学习算法
微软: 人脸算法

阿里 腾讯 百度 ...  AI平台
微软 Python的平台
AI 数据分析 爬虫 web开发 自动化 游戏开发  脚本  GUI桌面程序  算法 ...

就业趋势: 要求不高 项目经验
    自动化(10K)  web全栈开发(25K) 后端开发(15K) 爬虫(12K)
    15K平均值
    兼职: Python开发  爬虫

自动化 web开发  爬虫  ---> 全栈开发
就业指导 就业跟踪 BAT模拟面试笔试
线上直播 + 课后录播 + 随堂笔记
1 3 5正课  2 4 6解答课  20:30 -22:30
课后一对一解答 辅导 补课
学习任务  课中测试 课后作业   阶段考核(重修(免费的))
项目实战检验  独立开发项目的能力
制定学习计划  毕业后 职业规划
2 -3  项目经验
新闻资讯  天猫商城  百度新闻

AI发展  兼职:  积累AI经验  25K  专门的老师带着你做一段时间
分期  花呗 借呗 信用卡 京东白条 分期 分期 6 9 12  一个月才500多快钱
为什么现在会觉得有压力?

学会才毕业的    30个人   老师监督 每天跟踪你的学习任务 64岁  8岁
全栈开发(自动化运维 自动化测试) 前后端开发

后端开发(flask  django  数据库  网络编程  异步 多任务 )
实习 跟你专业不对口

基础(语法 基本数据类型 ...) ---> 框架  数据库 --- 爬虫  -- 自动化 --- 数据分析 算法  AI  机器视觉

不超过8K
专门的,老师对你进行学习计划的制定
疑问呢?
分期  学费1000优惠  AI 班级赠送学习


'''

# pip install opencv-python
import cv2

# 1. 创建一个摄像头调用采集数据 0默认摄像头   1外置摄像头
cap = cv2.VideoCapture(0)
# 定义一个窗口来显示相对应的人脸
cv2.namedWindow('V')

# 2. 载入人脸识别训练数据
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

# 3. 打开摄像头
while True:
    # 4. 采集到的视频进行帧数处理
    ret, frame = cap.read()
    if not ret:
        # 等待用户输入
        cv2.waitKey(30)

    # 5. 图像灰度转换 opencv默认 BGR  HSV RGB
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 6. 视频采集的窗口 检测目标物体 并且标出对应的人脸
    # 1. 灰度图  2. 缩放比列 3. 窗口子大小
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # 标识人脸
    for (x, y, w, h) in faces:
        # 制定画笔的位置 和 颜色 大小
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    # 显示图片
    cv2.imshow('V', frame)
    # 等待检测人脸
    keyvalue = cv2.waitKey(20)
    # 点击键盘q退出  0xff --->ESC
    if keyvalue & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



