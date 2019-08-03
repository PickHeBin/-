#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 刷访问.py
# Author: MuNian
# Date  : 2019/7/18
'''
AI  大数据 时代
购买第三方数据
免费的网站下载数据
爬虫采集
人工收集

百度新闻 = 后端 + 爬虫搜索引擎
12306抢票

requests.请求方式(请求网页的url, 请求头部信息, 参数).text
text:返回数据为字符格式
content: 字节
爬虫: 数据采集  渗透 破解 模拟 ...
web 全栈开发 后端开发 爬虫开发  自动化

1. 基于零基础
2. 项目驱动教学(三个企业项目)
3. flask --> 新浪  django --  天猫  爬虫 - 百度新闻

8K - 27K
系统性学习
1. 及时解答
2. 规划性

web阶段 ---> 爬虫阶段 ---> 数据分析

基础语法 --> 基础思维 --> 基础的业务 --> 进阶 --> web前端 --> web后端 --> 爬虫 --> 自动化 --> 数据分析 算法 ---> AI

上课: 线上直播 + 课后录播 + 随堂笔记
1 3 5正课 2 46 解答课 晚上:20:30 - 22:30
4.5个月
学会才毕业的
1. 课中测试 课后作业 课后一对一辅导解答 补课
2. 学习进度
3. 阶段考核 重读(免费的) 学会才毕业
4. 项目检验: 毕业后具备独立开发项目的能力
6. 就业指导 就业跟踪 工作职业规划

爬虫 全栈开发 后端开发 自动化测试(web测试 软件测试 UI测试)

7880 - 1000优惠 = 6880

学会才毕业的

基础思维和业务逻辑  ---> 框架(web  全栈) ---> 爬虫 ---> 机器学习 图像处理 深度学习


'''
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3708.400 QQBrowser/10.4.3661.400'
}

url = 'https://www.baidu.com/s?wd=Python'

response_data = requests.get(url, headers=headers).text
print(response_data)