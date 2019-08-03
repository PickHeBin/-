#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : manage.py
# Author: MuNian
# Date  : 2019/6/30
'''
web方向:
    豆瓣 知乎...

自动化:
    自动化测试 自动化运维

爬虫:
    数据采集
    安全网络

游戏开发
GUI程序开发
大数据
算法
AI
4个月的快速就业
线上直播 + 课后录播 + 随堂笔记
1 3 5正课  2 4 6解答
20:30 - 22:30
课后辅导
企业标准:
    web:
        1. 掌握Python市场技能需求的主流框架
        2. Web框架设计 开发对应的数据库
        3. 企业当中的开发流程 开发架构
        4. 独立开发一个项目的能力 基本的业务逻辑

8k - 27K

市场就业方向 : web开发
                自动化
                爬虫

'''

from aip import AipImageCensor

""" 你的 APPID AK SK """
APP_ID = '16680076'
API_KEY = 'ku8T6z4BpQAYFllLRxHzRS1Z'
SECRET_KEY = 'xhH8Yf1yHR8xl6skig8sXmxmvMTndrS8'

client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
# def get_file_content(file):
#     '''
#     :param file:  图片的路径
#     :return:  读取图片成功的进制文件
#     '''
#     with open(file, 'rb') as f:
#         return f.read()
#
# images = get_file_content('23b01.jpg')

# with open('25c01.jpg', 'rb') as f:
#     img = f.read()

imgs = client.imageCensorUserDefined('https://i.meizitu.net/2019/05/17f03.jpg')
data = imgs['data']
for i in data:
    msg = i['msg']
    conclusion = i['conclusion']

    data2 = {
        msg : conclusion
    }

    print(data2)