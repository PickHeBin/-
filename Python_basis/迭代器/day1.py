#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 刷访问.py
# Author: MuNian
# Date  : 2019/7/26
'''
迭代器是一种设计模式 通用性可以遍历基本类型

无限迭代器
count(start=0, step=1) 从0开始
cycle: 对可迭代对象的元素反复执行循环
repeat(object, times): 反复生成对象至无限


有限迭代器
 chain() --->  chain('ABC', 'DEF') --> ABCDEF
 compress() ---> compress('ABCDEF', [1, 0, 1, 0, 1, 1]) ---> ACEF
 groupby() --->
 print(itertools.tee('abc', 3))

组合迭代器:
    product(): 可以求解多个迭代器对象的笛卡尔积       'ABC', [1, 2] ----> ('A', 1) ('A', 2)
    permutations(): 求解可迭代对象的元素的排序         'ABC', 2  --->  AB AC BA  BC...
    combinations(): 迭代对象元素的组合                  'ABC', 2 ---> AB, AC, BC

内置方法:
    zip(): 同时迭代多个序列

微软  阿里 百度  腾讯 .....
Python从事方向:
    1. 爬虫  数据分析 人工智能  自动化(自动化运维 自动化测试)  web开发 app软件开发  大数据   机器学习 深度学习 机器视觉... 游戏开发  GUI桌面程序开发

    就业趋势比较适合零基础的:
        1.爬虫
        2.自动化
        3 web全栈开发  web后端开发
    豆瓣  知乎  YouTube
自动化测试 web全栈开发 后端开发 爬虫
独立开发一个类似于天猫...  百度新闻  新闻资讯
4.5 为一期
上课模式: 线上直播 + 课后录播 + 随堂笔记
1 3 5 正课  2 4 6 解答课 20:30 -22:30  13:00 - 23:00 解答 补课 辅导
就业指导 模拟面试笔试 企业一线的技术专项指导  毕业后 职业规划
30   5个老师
学会才毕业的  具备独立开发项目的能力

迷茫: 对于这个行业不了解
基础 ---> web 爬虫 自动化 ---> AI  大数据 算法
学完毕业后 兼职
测试 --> 自动化 --> 开发
java 市场饱和 --> 开发 跨平台 性能稳定
Python大数据  数据分析 首选Python
项目经验? -->
实习?
实干?

'''

import itertools

# for i in itertools.product('ABC', [1, 2]):
#     print(i)

# for i in itertools.permutations([1, 2, 3], 3):
#     print(i)

# for i in itertools.combinations('ABCD', 3):
#     print(i)

a = [1, 2, 3, 4]
b = ['w', 'e', 'r', 't']
for i in zip(a, b):
    print(i)


# for i, x in itertools.groupby('aaabbbaaccdhhkkklllsjhfdasfas'):
#     print(i, ':', list(x))
#
# print(itertools.tee('abc', 3))

# for i in itertools.compress('ABCDEF', [1, 0, 1, 0, 0, 1]):
#     print(i, end='')

# for i in itertools.chain('DEF', 'GHJ'):
#     print(i, end='')


# co = itertools.count()
# cy = itertools.cycle('ABC')
# re = itertools.repeat('A', 10)
#
# for x in re:
#     print(x)

# for n in cy:
#     print(n)

# for i in co:
#     print(i)