#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : day2.py
# Author: MuNian
# Date  : 2019/7/3
'''
1. 爬虫工作流程
    使用代码模拟客户端请求浏览器

2. 分析大众点评的网页结构信息
    1.得到网页的url 域名
    2. 构造客户端请求头
    3. 使用客户端(伪造的)请求服务器 并且服务器响应数据给客户端
    4. 服务器响应的数据进行转换成可视界面
        4.1  text  字符对象
        4.2  content 字节对象    1G = 1024mb =  1024 * 1024kb
        4.3  json() 返回  键值对组成
    5. 数据提取
        5.1 pyquery提取方式: 前端 标签  类选择器(.txt) ID选择器(#id选择器) css 布局  属性
3. 使用代码氢气后台服务器得到数据
4. 显示采集到的数据

python 趋势  微软  Python 趋势  46  500W年薪
AI  效率
web方向: 代码优美  开发效率很高  分布式集成
豆瓣  YouTube  知乎....

4个月快速就业的

1.  掌握企业技能的基本框架
2. 对公司的业务流程基本开发对应的数据库  前后台网页

项目主导:
    8k - 27K
    就业趋势最好 :web开发  自动化   1. 招聘需求量大
    web开发
    自动化
    爬虫(web开发)(1. 网页结构 反爬) - 薪资10K  - 18K   - 数据采集 - 基于大数据
    2. 红帽子编程 - 逆向工程

单独学习爬虫班?
基础 - 跳阶段    爬虫 -> 1. 考核
                            2. 保障学员
企业开发中 实际应用    课后辅导  一对一的解答

就业趋势好的: web  爬虫  自动化
高数 + Python运算能力
从事什么职业?  转行   市场 技术吃香的
web发展 架构师才都是有的

1 3 5正课  2 4 6解答课
晚上 20:30 - 22:30
线上直播 + 课后录播 + 随堂笔记  学会才毕业的 重修(免费的)
学员保障:
    1. 就业指导 就业跟踪
    2. 课后一对一辅导 补课 解答
    3. 架构师学习计划   就业后规划

原价 7880 价格  预订500 得到 1000 优惠 = 6880
分期的 6 9 12期  一个月才500多块钱  花呗 借呗 京东白条 信用卡

技能
1. 64岁  8岁
2. 12K    15K平均

线上直播
1. 学不会

'''

import requests
from pyquery import PyQuery as pq


def DaZhong(page):
    # http://www.dianping.com/changsha/ch10/r7956p3
    # http://www.dianping.com/changsha/ch10/r7956p2
    url = 'http://www.dianping.com/changsha/ch10/r7956p{}'.format(page)
    # http: // www.dianping.com / changsha / ch10 / r303
    # 构造请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Host': 'www.dianping.com',
        'Referer': 'http://www.dianping.com/changsha/food',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36'
    }

    response_data = requests.get(url, headers=headers, timeout=3).text
    # print(response_data)
    # 初始化
    doc = pq(response_data)
    # 通过类选择器来获取数据
    txt = doc('.txt').items()
    for i in txt:
        # print(i)
        # 通过类选择器和h4标签来获取数据
        title = i.find('.tit h4').text()
        comment = i.find('.comment span').attr('title')
        data = {
            title : comment
        }
        print(data)


DaZhong(5)
# if __name__ == '__main__':
#     page = int(input('请输入你想要抓取的页数:'))
#     for i in range(1, page):
#         DaZhong(i)

