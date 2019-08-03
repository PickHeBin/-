#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : __init__的使用.py
# Author: MuNian
# Date  : 2019/7/20


class Cat():

    # name = '老王'

    def __init__(self, name, age):
        '''
        1. 自动调用
        2. 类自带的魔法方法
        3. 作用: 3.1 初始化: 一个类创建多个对象的时候  提高运行效率
                    3.2 在使用的时候 必要要进行self声明 把他变成类的全局变量
        '''
        self.name = name
        print(id(self.name))
        print(id(name))
        self.age = age


    def eat(self):
        print("%s 爱吃鱼" % self.name)



tom = Cat('张三', 18)
# 创建出来的对象来调用类方法
tom.eat()
# print(Cat.eat)

