#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 刷访问.py
# Author: MuNian
# Date  : 2019/7/2

'''
爬虫的流程:
    1. url - 域名: 由DNS来解析域名并且返回地址
    2. 请求: 浏览器带着由DNS解析处理的地址来访问web后台服务器
    3. 响应: 由web后台服务器来渲染浏览器界面
    4. 数据提取: 精准的数据获取
线上直播 + 课后录播 +随堂笔记
1 3 5 正课   2 4 6 解答课
20:30 - 22:30   课后一对一的解答 补课 辅导
每个阶段 考核 学会才毕业的标准

4个月快速就业
1. 基于零基础到项目实战的
学习编程 - 学习英语的   提升

市场就业情况比较好的:
    1. web开发   平均市场薪资 15K

学完后可以达到企业的什么标准:
    1. 掌握Python的web  爬虫 自动化 主流框架
    2. 根据公司业务需求 开发对应的数据库 进行数据采集 并且进行存储
    3. 根据业务流程 开发对应的后端功能 并且进行自动化 运维 + 自动化测试  对应的数据都由自己采集
    4. 市场对应的需求设计对应的功能模块(脚本  web后端  爬虫采集 爬虫搜索引擎)
    5. web自动化   app软件自动化  UI自动化 安全性能自动化
    6. 分布式爬虫(百度新闻)  搜索引擎爬虫(百度 谷歌 )  爬虫框架
    7. 基本需求分析 架构搭建 .....

新领域  学习   了解 不去学习   学会了 自然就了解了   眼前的状态是不满足的


'''
import requests
# A|t + enter(回车)
from pyquery import PyQuery as pq
from lxml import etree


# 这是url地址
url = 'https://cs.anjuke.com/sale/'
# 构造请求头部信息
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'eferer': 'https://www.anjuke.com/captcha-verify/?callback=shield&from=antispam&serialID=2646e06585e6255a35d1838ada41ab3e_5d61c0c78dd24e54b2ae94fc6810502a&history=aHR0cHM6Ly9jcy5hbmp1a2UuY29tL3NhbGUv',
    'upgrade-insecure-requests':'1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3708.400 QQBrowser/10.4.3661.400'
}

# 对web后台发送请求 并且响应数据
response_data = requests.get(url, headers=headers).text
# 初始化前端界面
doc = pq(response_data)
# 通过前端的类选择器来获取数据
house_details = doc('.house-details').items()
# 房子的价格
# 页面化
html = etree.HTML(response_data)
price = html.xpath('//div[@class="pro-price"]/span/strong/text()')

for i, n in zip(house_details, price):
    # 房子的标题
    houseListTitle = i.find('.houseListTitle').text()
    # 获取房源信息
    item = i.find('.details-item').text()

    data = {
        '房子的标题' : houseListTitle,
        '房源信息' : item,
        '价格' : n + '万'
    }
    print(data)





