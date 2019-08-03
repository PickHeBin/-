#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 腾讯招聘抓取.py
# Author: MuNian
# Date  : 2019/7/23
''''
爬虫的采集数据的流程:
    1. 获取网页的请求地址
    2. 获取相对应的请求参数  请求头部信息
    3. 对web后台服务器发送请求
    4. json数据提取  {键(唯一的):值}

1 2334354
破解 渗透 解析  .... 爬虫逆向
Python:
    1 - 5趋势 15K: 自动化测试 自动化运维 后端开发 GUI桌面程序 爬虫 逆向 网络编程 网络通信 游戏开发 APP软件开发
    未来5 -10 趋势 50K:数据分析 数据可视化 数据挖掘 机器学习 深度学习 AI 无人技术(无人机 无人驾驶 无人酒店 无一餐厅)  机器视觉 图像处理

整个IT市场  就业趋势 就业薪资Python
全栈开发 自动化测试 爬虫 后端开发
4.5 一期 线上直播  课后录播 随堂笔记
1 3 5正课  2 4 6解答课  20:30 -22:30  13:00 - 23:00 一对一的解答 辅导
学会才毕业
1. 架构师一对一的学习计划制定
2. 课中测试 课后作业 课后补课 课后解答
3. 学习任务的跟踪
4. 重修(免费) 项目实战检验  具备独立开发项目的能力
5. 兼职认证  就业指导 就业跟踪 模拟BAT面试笔试
6. 职业规划...

基础语法学 ---> 网络编程 ---> 对接框架(web) ---> 自动化
全栈开发25K: 前端 + 后端 + 自动化测试 + 自动化运维 + 爬虫
后端开发(django flask ) 对于整个市场 项目开发经验 3左右项目经验的



'''
import requests
import time
import json

# 请求地址
url = 'https://careers.tencent.com/tencentcareer/api/post/Query?'

page = input('输入想要抓取的页数:')

for n in range(1, int(page) + 1):
    # 请求参数
    params = {
        'timestamp': str(time.time()),
        'keyword': 'Python',
        'pageIndex': str(n),
        'pageSize': '10',
        'language': 'zh-cn',
        'area': 'cn'
    }

    # 请求web后台服务器
    json_data = requests.get(url, params=params).json()
    res = json_data['Data']['Posts']

    # 文件的读写方式
    with open('腾讯招聘.json', 'a', encoding='utf-8') as f:

        # 循环遍历数据
        for i in res:
            temp = {}
            temp['岗位名称'] = i['RecruitPostName']
            temp['岗位详情'] = ''.join(i['Responsibility'].split())
            temp['地址'] = i['LocationName']
            temp['岗位链接'] = i['PostURL']
            # print(temp)
            f.write(json.dumps(temp, ensure_ascii=False) + ',\n')


