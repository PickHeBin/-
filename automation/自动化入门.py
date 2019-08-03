#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 自动化入门.py
# Author: MuNian
# Date  : 2019/7/19
'''
自动化: 人为驱动变成机器执行  UI自动化 web自动化 软件自动化 ....

selenium
元素定位:
    1. class_name 类选择器  id  id选择器
    2. css  样式
    3. xpath  元素路径定位
    3. tag_name 元素标签定位

输入: send_keys
点击:click()
测试 运维 ---> 自动化
AI  大数据  逆向 爬虫  自动化 首选语言Python
就业趋势比较好的:
    非计算机专业的:
    爬虫(数据采集 数据挖掘 逆向) 8K - 18K 自动化6K - 15K web开发(全栈开发 后端开发) 10K - 25K
    50K
    全栈开发  后端开发 自动化测试 爬虫开发
    框架项目教学

4.5个月想 为一期
线上直播 + 课后录播 +随堂笔记
1 3 5正课 2 4 6解答课  20:30 -22:30 其他时间解答时间13:00 - 23:00
1. 进班之后 架构师一对一的学习计划制定
2. 课中测试 课后作业 课后学习进度跟踪 每日学习反馈  一对一解答 辅导 补课
3. 阶段考核(重修 免费  学会才毕业) 项目实战检验(具备独立开发项目的能力)
4. 兼职专门带着做一段时间兼职  就业指导 就业跟踪 模拟BAT面试笔试(应对各种面试难关) 职业规划

局限于一个
GUI
原价7880  1000学费优惠 6880  分期 6 9 12

6880 =  AI研发班  + BAT全栈 + 面试特训班









'''

from selenium import webdriver
import time

# # 创建一个浏览器驱动
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# # id属性来进行元素定位
# driver.find_element_by_id('kw').send_keys('京东')
# time.sleep(1)
# # xpath定位元素
# driver.find_element_by_xpath('//*[@id="su"]').click()
# driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
# time.sleep(10)
# # 1. 选中搜索框元素
# # query = driver.find_element_by_name('query').clear()
# # print(query)
# # driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div/dl[1]/dd/a[1]').click()
# driver.find_element_by_xpath('//*[@id="key"]').send_keys('笔记本电脑')

# driver = webdriver.Chrome()
# driver.get('https://www.jd.com/')
# driver.find_element_by_xpath('//*[@id="key"]').send_keys('笔记本电脑')

driver = webdriver.Chrome()
driver.get('https://www.wjx.cn/jq/37766520.aspx')
elements = driver.find_elements_by_xpath('//*[@class="ulradiocheck"]')[3:]
for element in elements:
    el = element.find_element_by_xpath('./li[4]/a')
    el.click()