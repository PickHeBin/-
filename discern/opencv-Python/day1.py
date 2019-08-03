#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 刷访问.py
# Author: MuNian
# Date  : 2019/7/30

import cv2

# 创建一个视频窗口 0 默认的摄像头 外置摄像头 1,
# 视频捕获
cap = cv2.VideoCapture(0)
cv2.namedWindow('Python')
# waitKey 等待用户输入
# cv2.waitKey(0)
# 读取人脸识别的训练集 人脸特征提取
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

# 打开摄像头 视频采集到的数据处理
# 1. while True  2. isOpened
while True:
    # 读取帧 ---> (矩形数组)
    ret, frame = cap.read()
    if not ret:
        cv2.waitKey(30)
    # 灰度转换: gray 作用: 图片的计算强度得以降低
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # 显示图片
    cv2.imshow('python', frame)
    # 等待检测人脸
    keyvalue = cv2.waitKey(20)
    # 点击键盘q键 退出
    if keyvalue & 0xff == ord('q'):
        break


# 窗口的释放
cap.release()
cv2.destroyAllWindows()

