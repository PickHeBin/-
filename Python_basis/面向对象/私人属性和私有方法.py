#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 私人属性和私有方法.py
# Author: MuNian
# Date  : 2019/7/20
'''
私有方法和私有属性: __私有属性 __私有方法
    1. 只能在类的内部使用 比如:通过类创建出来的对象来调用私有的 是不行的
    2. 如果想要调用私有属性 可以通过公共方法来调用私有属性
    3. 应用场景: 在开发当中不希望别人可以在类的外部调用你的属性或者方法
    4. 通过公共方法或者属性可以调用到私有方法或属性  在公共方法当中调用的私有方法 所指向的内存是一样的

'''

class Festival():
    ''' 节日类 '''
    def __init__(self, happy_name, happy_time):
        '''
        :param happy_name:  节日的名称
        :param happy_time: 节日的时间
        '''
        self.happy_name = happy_name
        # 私有属性
        self.__happy_time = happy_time

        # __Qingrenjie1()
        # happy_time = None

    # 私有方法
    def __Qingrenjie1(self):
        print('{}快乐....时间:{}'.format(self.happy_name, self.__happy_time))

    def Shengri(self):
        self.__Qingrenjie1()


Qingrenjie = Festival('情人节', '15:00')
# print(_Qingrenjie._Qingrenjie1.happy_time)
Qingrenjie.Shengri()



