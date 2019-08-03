#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 刷访问.py
# Author: MuNian
# Date  : 2019/7/10
'''
面向对象:
    类方法
    类属性
人:
    面貌 特征  --   属性
    泡妹子 行为 ----  方法

类与对象
 1. 类是对象的创建者
 2. 在一个类里面 需要在类方法里面调用类属性 使用self来进行声明
 3. 一个类可以创建多个对象
 4. 属性进行初始化后 属性冲突

__init__ 初始化

'''

class Proson:
    ''' 人类 '''
    # name = '小明'
    # age = 18
    # heigth = 1.75
    def __init__(self, name, age, heigth):
        # 初始化
        self.name = name
        self.age = age
        self.heigth = heigth

    def __str__(self):
        ''' 返回类的描述信息 '''
        return '大家好我是:{}, 年龄:{}, 身高:{}'.format(self.name, self.age, self.heigth)

    def run(self):
        ''' 跑 --> 方法 '''
        print('{}在跑步'.format(self.name))


# 通过类名来创建对象
proson = Proson('小美', 19, 1.67)
# 通过类名来调用属性
# print(Proson.name)
# 通过对象来调用方法
proson.run()
# 对象来调用属性
print(proson.name)

xiaoming = Proson('小明', 18, 1.75)
print(xiaoming.name)
print(xiaoming)


