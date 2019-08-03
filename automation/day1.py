#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 刷访问.py
# Author: MuNian
# Date  : 2019/7/9

'''
Python开发程序员  自动化部署  自动化运维 自动化测试
                web开发
                爬虫
                自动化
学习知识点
线上直播 + 课后录播 + 随堂笔记
1 3 5 正课  2 4 6解答  20:30 - 22:30
课后一对一解答 辅导 学会才毕业  英语单词
VIP服务:
    1. 课后辅导 补课 课后作业 课后测试 每日反馈....
    2. 架构师 一对一的 学习计划制定
    3. 项目实战检验  毕业后独立开发项目
    4. 阶段考核(重修免费) 学会才毕业
    5. 就业指导 就业跟踪  职业规划 BAT面试笔试

课程主导: 针对零基础学员学习的  项目主导 由浅入深
中级工程师的级别:
    web全栈开发
    web后端开发
    爬虫开发
    自动化
打造全栈工程师
全栈20K = 前端 + 后端(Python)
Python 代码 优美 hello wolrd Python 1行代码

web测试
AI  大数据  算法   首选 Python  70% 框架 基于Python开发
无人驾驶  无人机 无人酒店 .....
技术 成熟  5G = 实现AI 云存储

1 -5 全栈 Python 底层
5 -10 AI  算法

能力  技术
2
1
毕业 失业 转行
AI班级免费学习 1个
转行?
不需要转行 基础 -> 框架底层知识 基础 ->框架实现
浪费时间
6880 分期  12 期  一个月 才500多块钱  花呗 借呗 京东白条 信用卡   7880
预订 ---> 就剩下一个名额(1000学费优惠的  终身答疑)
夜宵 烤鱼
1. 为什么是月光族  以前没有提升  现在还不去提升 ---> 月光族
不去做 肯定不会改变  去做了 有可能会改变
项目经验  工作经验  毕业 ----> 拼搏到自己无能为力
韩语
'''
# A|t + enter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 1. 创建一个浏览器设置对象
chrome_options = Options()
# 2. 浏览器添加设置
# chrome_options.add_argument('--headless')

# 3. 创建浏览器对象
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver.exe')
# 4. 使用创建的浏览器对象请求网页
driver.get('https://www.wjx.cn/jq/37766520.aspx')
# 保存浏览器的当前截图
# driver.save_screenshot('123.png')
# 通过xpath元素定位来自动化点击
driver.find_element_by_xpath('//*[@id="divquestion1"]/ul/li[2]').click()
driver.find_element_by_xpath('//*[@id="divquestion2"]/ul/li[3]/label').click()
driver.find_element_by_xpath('//*[@id="divquestion3"]/ul/li[3]/label').click()
# 带上s 多个
elements = driver.find_elements_by_xpath('//*[@class="ulradiocheck"]')[3:]
for element in elements:
    el = element.find_element_by_xpath('./li[4]/a')
    print(el.get_attribute('title'))
    el.click()

el = driver.find_element_by_id('submit_button')
print(el.get_attribute('value'))
el.click()
# 当前url
print(driver.current_url)
# 当前网页的标题
print(driver.title)
# 当前网页cookie -> 网页用户保存的信息
print(driver.get_cookies())
print(driver.page_source)

time.sleep(5)
# 关闭浏览器
driver.close()


