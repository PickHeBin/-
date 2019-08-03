#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 函数入门.py
# Author: MuNian
# Date  : 2019/7/11
'''
封装
1. 定义一个函数
    def 函数名(字母 下划线 数字 不可以数字开头 不能与关键字重用):
        函数内部的内容
2. 函数的调用
 登录功能
 1......
 2.....
 不需要去重复的写相同的代码
 形参 : 作为变量使用的
 实参 : 调用函数是传递的值

'''

def _hello(num, num2):
    ''' 函数的文档说明 实现两个数的相加 '''
    # num = 1
    # num2 = 2
    print(num + num2)
    print('hello wolrd')


_hello(10, 20)