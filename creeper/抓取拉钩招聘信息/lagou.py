#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : lagou.py
# Author: MuNian
# Date  : 2019/7/9
'''
用户验证: cookie 验证 请求方式
post请求 三要素:
    1. url 地址
    2. 参数
    3. 请求头部信息


用户数据
登录了才可以访问  session验证: 会话保持 (用户登录状态) session 返回cookie (客户端里面保存的用户信息)  痕迹
爬虫工程师 - 开发网页 搭建网页
回过头 很简单  过程
编程行业: Python 薪资 发展是最好的
就业趋势: web  自动化 爬虫
架构开始
零基础 到项目实战 (4.5个月)
线上直播授课 + 课后录播 + 随堂笔记
1 3 5正课  2 4 6 解答课 20:30 -22:30
VIP服务:
    1. 课堂测试 课后一对一辅导 解答
    2. 制定学习计划
    3. 阶段考试(重修) 学会才毕业
    4. 项目经验 3年水平  三个企业项目
    5. 就业指导 就业跟踪 就业后职业规划

1. 手把手 搭环境  跟踪学员学习情况 课后补课 下午补课  完全掌握
2. 从零基础开始的 过程
转行  提升   Python  VIP 英文 补习
网上授课
线下 80个人 补习

下午 14: -17 补课 有时候
1 3 5正课  2 4 6解答  20:30 - 22:30 课后学完补习
笔记   Python 选公司  能力
开发效率高 首选Python 成本低  Python开发工程师  自动化 爬虫 前后端
代码优美  就业趋势 未来发展 就业薪资   Python最高的  高级语言
政府 人工智能发展规划  130亿元 ...  普及  无人餐厅  .... AI
能力

8K - 27K
全栈开发
后端开发
爬虫开发
自动化

'''
import requests
import json

url1 = 'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput='

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

data = {
    'first': 'true',
    'pn': '1',
    'kd': 'Python'
}

headers = {
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3708.400 QQBrowser/10.4.3661.400'
}
# 建立一个session 用户验证
s = requests.Session()
s.get(url=url1, headers=headers, timeout=3)
cookie = s.cookies

# text 字符串  json js数据
response = requests.post(url, headers=headers, data=data, cookies=cookie, timeout=3).json()
json_data = response['content']['positionResult']['result']

for i in json_data:
    # ret = {}
    #
    # ret['岗位名称'] = i['positionName']
    # ret['薪资'] = i['salary']
    # ret['福利待遇'] = i['positionAdvantage']
    # ret['公司名称'] = i['companyFullName']
    # print(ret)

    ret1 = i['positionName']
    ret2 = i['salary']
    ret3 = i['positionAdvantage']
    ret4 = i['companyFullName']

    with open('拉钩招聘.json', 'a') as f:
        f.write('{},{},{},{}\n'.format(ret1, ret2, ret3, ret4))
