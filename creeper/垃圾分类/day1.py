# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 刷访问.py
# Author: MuNian
# Date  : 2019/7/15

'''
sql注入: CSRF  token  ddos   爬虫 渗透

json : 所有编程语言通用的数据格式   取数据的方式:

{'1'(键 唯一的) : 2(值)}
[1,1,1,1, ]

第三方平台
AI  数据分析 算法 自动化 全部都是在使用Python
全能型的语言

吃鸡 透视外挂
Python未来发展  17年

高级架构  ---> 数据分析 ---> 人工智能工程师
全栈开发  后端开发  爬虫  自动化
1. web 爬虫 自动化 市场主流框架  mysql redis .....
2. ...   三个项目  flask   django   搜索引擎

完善的VIP服务:
    1. 4.5个月 快速就业  线上直播 + 课后录播 + 随堂笔记  1 3 5 正课  2 4 6解答课  20:30 - 22:30
    2. 课中测试 课后作业 每天班主任老师 跟踪学员的学习内容  课后一对一的解答 辅导 补课   学会才毕业
    3. 阶段考核 升班考试(重修(免费的))  项目实践检验  具备独立开发项目的能力
    4. 就业服务: 就业指导  就业跟踪 就业内推(名额限制) BTA面试笔试  升职加薪
    5. 学习计划制定   职业规划

6 9 12  花呗 借呗 信用卡 京东白条

70% Python

专业
读大学: 1. 最成熟第三方包  高级语言
        2. 非常适合零基础学员入门
        3. 未来的发展 就业趋势 范围都是非常广的
        ....学科

1. 转行 ----> 实习 --->  富士康 兼职积累经验
本事


'''

import requests


word = input('请输入你想要查询的垃圾:')

url = 'http://apis.juhe.cn/rubbish/search'

params = {
    'key':'464ae332ad03cdddf7ef955747751dc0',
    'q':word,
    'type':2
}

request_data = requests.get(url, params=params).json()


result = request_data['result']
for i in result:
    data = {}
    data['垃圾名称'] = i['itemName']
    data['垃圾分类'] = i['itemCategory']
    print(data)

# result = request_data['result']
# for i in result:
#     data = {
#     }
#     # 垃圾的命名
#     data['垃圾的命名'] = i['name']
#     # 分类的说明
#     data['分类的说明'] = i['explain']
#     # 投放指导
#     data['投放的指导'] = i['require']
#     # 常见的垃圾
#     data['常见的垃圾'] = i['common']
#     print(data)
