#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 第一个class程序.py
# Author: MuNian
# Date  : 2019/7/20
'''
车(类):
    包装  颜色 车名  ----> 特征是属性
    车在跑 ---- 行为是方法

扫把在扫地
在类里面
    类全局变量: 添加属性作为参数在魔法方法里面__init__
    局部变量: 不在类的魔法方法__init__ 里面 的属性是局部的 如要访问需要 加上self

1. self: 那个对象在调用这个类 那么这个self就是指向谁

1. 面向对象中的引用
    1.1  使用print可以输出对象在内存地址中开辟的空间
    2.1   在创建对象的时候不加入括号 类

'''

class Ponsor:
    ''' 人类 '''
    # 属性
    name = '张三'
    age = 18

    def eat(self):
        print('{}在吃东西'.format(self.name))
        self.name = '李四'

    # def __del__(self):
    #     Ponsor.name = '小明'


# 创建一个对象
xiaoming = Ponsor()
print(xiaoming)

print(id(xiaoming.name))

# 在类的外部来修改类属性  类属性是从新在内存当中开辟了空间  但是不推荐使用，作为了解
xiaoming.name = 'laowang'

print(xiaoming.name)
print(id(xiaoming.name))

xiaomei = Ponsor()
xiaoming.eat()
print(xiaomei)
print(id(xiaoming.name))
print(xiaoming.name)





