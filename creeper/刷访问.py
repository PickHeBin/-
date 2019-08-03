#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 刷访问.py
# Author: MuNian
# Date  : 2019/7/22

'''
调用接口的流程:
    1. 接口的地址
    2. AppKey 指向对应的接口
爬虫的请求:
    可以截取到任何在互联网上面传输的数据

云平台  非法软件
就业趋势比较好的方向:
    1. 数据分析
    2. web开发  flask  django
    3. 自动化  自动化测试 自动化运维
    4. 爬虫

爬虫  自动化测试 web全栈开发 web后端开发
线上直播 + 课后录播 + 随堂笔记
1 3 5正课 2 4 6解答课
20:30 - 22:30
保证学员能够学会才毕业  具备独立开发项目的能力的
考核(重修 免费的 )

12期分期  一个月才500多块钱
全栈开发
Python基础 --> web开发 --> 爬虫 自动化 --> 数据分析 算法 AI 机器视觉
从事Python想往哪方面发展?
框架 AI  主讲老师
开发网页(flask  django 数据 后端)
基于零基础
4.5月

网页独立开发  网页结构 DRF  CSRF.. 机器学习
自动化脚本
Python ---> 微软 谷歌
百度AI 腾讯AI 阿里AI

申请免费名额
'''

# 该程序实现刷CSDN网页访问量，当访问被拒绝或者遇到其他异常时会自动重启，无限刷
# 经过测试发现大概间隔70秒访问一下，访问量才会增加1
# 只需要修改或者添加url的链接就可以了
# about:version

import requests
import time

url = ['https://blog.csdn.net/qq_42370150/article/details/93734159',
       'https://blog.csdn.net/qq_42370150/article/details/96190033']

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

count = 0
countUrl = len(url)

# 访问次数设置
while count < 100000:
    try:  # 正常运行
        for i in range(countUrl):
            response = requests.get(url[i], headers=headers)
            if response.status_code == 200:
                count = count + 1
                print('Success ' + str(count), 'times')
        time.sleep(50)

    except Exception:  # 异常
        print('Failed and Retry')
        time.sleep(60)







