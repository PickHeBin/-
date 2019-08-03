#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : day.py
# Author: MuNian
# Date  : 2019/7/27
'''
请求一个网页:
    1. 地址 url  域名
提取数据
爬虫:数据采集 数据抓取 逆向(黑客) 数据挖掘 物理地址
Python能从事哪些方向:
    web  爬虫  AI  数据分析 量化  算法 自动化...
谷歌 微软 甲骨文  全球前五企业 ----> Python平台
选择一门编程语言  未来发展(背后的支撑着)

全职10K - 35K   兼职 6K - 15K
4.5 为一期
线上直播授课 + 课后录播 + 随堂笔记
1 3 5 正课  2 4 6 解答课
20:30 -22:30  13:00 - 23:00 一对一解答  补课 辅导 学会才毕业
自动化  爬虫  web
兼职  能力  自考   兼职一段时间(一年左右时间) ---> 社会IT阅历 ---> 全职 (对于学历要求就不是很高)
兼职: 老师带着做一段时间
全职: 就业指导 BAT面试笔试模拟
一个月几百块钱支出  毕业后的长期发展

web开发  app软件开发   爬虫 人工智能(无人机  无人酒店 无人餐厅 感知器 ... 自动驾驶...)
新手 迷茫对于这个行业的不了解
办理入学之后: 一对一完整学习计划制定
职业规划 --> 快速升职加薪

数据分析  算法  AI 机器视觉  50K
软件专业: 5K 实习 专业都不一样 经验

'''

import requests
from lxml import etree

count = 1

def Bqb_data(page):

    global count

    # 网页的地址
    url = 'https://fabiaoqing.com/biaoqing/lists/page/{}.html'.format(page)

    # 请求网页后台服务器 并且得到服务器响应的数据
    response_data = requests.get(url).text

    html = etree.HTML(response_data)
    # xpath 元素获取数据
    # //*[@id="bqb"]/div[1]/div[2]/a/img
    # //*[@id="bqb"]/div[1]/div[3]/a/img
    # page = int(input('请输入你要抓取的个数:'))
    # for word in range(1, page):
    #     bqb = html.xpath('//*[@id="bqb"]/div[1]/div[{}]/a/img/@data-original'.format(word))
    #     print(bqb)

    # 通过类选择器来定位数据
    bqb = html.xpath('//*[@id="bqb"]/div[1]/div[@class="tagbqppdiv"]/a/img/@data-original')
    for i in bqb:
        # 发送二次请求 请求图片的地址
        url_image = requests.get(i)
        # a 追加  b 进制文件读写方式
        with open('热门表情包/{}.gif'.format(count), 'ab') as f:
            f.write(url_image.content)
        count += 1


page = int(input('请输入你要抓取的个数:'))
for word in range(1, page):
    Bqb_data(word)