#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : run.py
# Author: MuNian
# Date  : 2019/6/30
'''
微软  + 谷歌
AI技术:
    1. 智能芯片  人脸解锁
    2. 无人酒店 无人餐厅 无人超市  智能家居
    3. 无人驾驶  安全驾驶 小爱 天猫精灵
'''

from discern.图像识别.aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '16679398'
API_KEY = 'aWWeoKGruBzeG8g4ouT2WqOp'
SECRET_KEY = 'vOSRKMaXilivG88DGQ3jhSmnFa6WCIGg'
# 创建一个客户端
client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

# r 文件读取模式  b 进制文件的读写方式
with open('25c01.jpg', 'rb') as f:
    img = f.read()

imgs = client.advancedGeneral(img)
result = imgs['result']
for i in result:
    data = i['root']
    keyword = i['keyword']

    cdata = {
        data : keyword
    }
    print(cdata)
