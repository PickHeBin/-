#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 基本的数据类型.py
# Author: MuNian
# Date  : 2019/7/25
'''
字符串 ---> "字符串类型"   '字符串类型'  str
整数 ----> 123   int
浮点数 ----> 1.2 1.4 小数  float
布尔值 ----> 真 假   1  0   True  False   bool

姓名-- '小明'

type: 查看数据类型
变量地址id号:  id()

'''

name1 = input('请输入你想输入的名称:')

name = name1
age = 18
sex = True
height = 1.75
weight = 70.0
last_name = '哈哈哈哈'

print(name)
print(type(name))
print(id(name))

print(name * age)
# print(height * name)
print(name + last_name)