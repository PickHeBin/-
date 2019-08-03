#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : manage.py
# Author: MuNian
# Date  : 2019/6/30

from discern.图像识别.aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '16679398'
API_KEY = 'aWWeoKGruBzeG8g4ouT2WqOp'
SECRET_KEY = 'vOSRKMaXilivG88DGQ3jhSmnFa6WCIGg'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('23.jpg')

""" 调用通用物体识别 """
img = client.advancedGeneral(image)
result = img['result']
print(result)
for i in result:
    data = i['root']
    keyword = i['keyword']

    cdata = {
        data : keyword
    }
    print(cdata)


