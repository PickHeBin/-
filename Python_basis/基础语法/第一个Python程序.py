#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 第一个Python程序.py
# Author: MuNian
# Date  : 2019/7/25
'''
执行Python程序三种方式:
    1. 解释器 --- Python/ Python3
    2. 交互模式 --- ipython/ bpython
    3. 集成开发环境 --- pycharm

Python的源程序特殊格式文本文件 .py结尾  执行程序之后 .pyc文件

Python2 Python3
3.3  3.4  3.5  3.6
64位  32位

企业当中注意的点:
    每一个功能 就写一个功能注释

Python的代码规划:PEP
Python执行的过程:
    1. CPU:中央处理器 负责处理数据 计算数据
    2. 内存: 临时存储数据(断电之后就会消失)
    3. 硬盘: 固态(文件读写非常快 ) 机器 ()  永久存储数据

'''

# 单行注释:  打印hello wolrd程序
# print('hello wolrd')

# 1. 变量的基本使用
'''
每一个值都是需要赋值  等号(=)  想等 ==  
= 左边是变量名 
= 右边 存储在变量当中的值
变量名 = 值
'''

# qq_number = '123456'
#
# print(qq_number)

# 有几个变量?
# 苹果价格的变量
price = 8.5
# 购买数量
weigth = 7.5

money = price * weigth

# 买了苹果就返回5块钱
# money = money - 5
money -= 5

print(money)