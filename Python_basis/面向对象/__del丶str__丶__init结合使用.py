#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : __del丶str__丶__init结合使用.py
# Author: MuNian
# Date  : 2019/7/20

'''
建一个房子  户型  面积  添加家具
买家具: 家具名称  家具的占地面积

两个类一般先写被使用的类
__str__: 返回对象的描述信息  返回的类型为字符串 自动调用

'''

class Furniture:
    ''' 家具类 '''
    def __init__(self, furniture_name, area):
        '''
        :param furniture_name: 家具名称
        :param area: 家具的占地面积
        '''
        self.furniture_name = furniture_name
        self.area = area

    def __str__(self):
        return '家具名称:{}, 占地面积为:{}'.format(self.furniture_name, self.area)

    # def __del__(self):
    #     ''' 在程序被销毁(程序结束完)前会自动执行del方法
    #         永远是在最后执行的
    #     '''
    #     print('{}占地:{}'.format(self.furniture_name, self.area))


class Home:
    ''' 房子类 '''
    def __init__(self, house_type, area):
        '''
        :param house_type: 户型
        :param area: 总面积
        '''
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.item = []

    def __str__(self):
        return '房子的户型:{}\n房子的面积:{}\n房子剩余面积:{}\n家具列表:{}'.format(
            self.house_type, self.area, self.free_area, self.item
        )

    def add_item(self, item):
        print('现在添加的是{}'.format(item.furniture_name))
        if self.free_area > item.area:
            # 剩余面积 = 总面积 - 家具的面积
            self.free_area = self.free_area - item.area
            self.item.append(item.furniture_name)

        else:
            print('家具{}太大了 放不下了'.format(item.furniture_name))


XiMengSi = Furniture('席梦思', 15)
Zhuozi = Furniture('桌子1', 10)
Zhuozi2 = Furniture('桌子2', 20)
Zhuozi3 = Furniture('桌子3', 5)
Zhuozi4 = Furniture('桌子4', 12)
home = Home('北京一环大别墅', 150)
home.add_item(XiMengSi)
home.add_item(Zhuozi)
home.add_item(Zhuozi2)
home.add_item(Zhuozi3)
home.add_item(Zhuozi4)
print(home)