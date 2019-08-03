#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 案例.py
# Author: MuNian
# Date  : 2019/7/10
'''
买个房子: 总面积 户型 贴地板
        总面积 - 地板的面积 = 剩余面积

贴地板: 名字  占地面积

被使用的类先开发

项目里面: 每一功能 都封成一个对象  方便很多
Python :
    web开发 爬虫  自动化 数据分析 AI 算法 游戏开发  脚本 GUI APP软件 ....

封装 继承 多态  节省开发效率
就业趋势最好的:  快速就业
    web开发  爬虫  自动化

未来发展好的方向: 5 -10
    AI  算法 数据分析(金融数据分析 量化)...

线上直播 + 课后录播 + 随堂笔记
4. 5 个月 快速就业
课程方向: web开发 自动化 爬虫逆向
1 3 5 正课  2 4 6解答课
20:30 - 22:30
就特晚上 新班开班  明天可以直接直接进班学习
自动化
项目经验
简历 项目过程  网上
1. 课后一对一解答 课后作业  课中测试   每天都可以跟上课程的进度
2. 阶段考核 学会才毕业  项目实战检验 独立开发项目的能力
3. 就业...

就业指导
7880  = 全栈班级 + 数据分析班级
1980 基础阶段

程序员客栈 ...
活动 1个   成本   6 9 12 花呗 借呗 信用卡 京东白条....  500多块
爬虫 Python + 物联网
Python 趋势  自己打算?   开发效率最高的  flask  django
对于学费?  一个月500多块钱   4个月  8K  10K
AI 首选 Python 就业趋势 薪资 Python课程  微软
物联网  5G  AI 的顺风车



'''

class House:
    ''' 房子类 '''
    def __init__(self, gross_area, house_type):
        '''
        :param gross_area: 总面积
        :param house_type: 户型
        '''
        self.gross_area = gross_area
        self.house_type = house_type
        # 剩余面积
        self.free_area = gross_area
        # 地板列表
        self.item_list = []

    def __str__(self):
        return '房子总面积:{}, 户型是:{}, 剩余面积:{}, 地板:{}'.format(self.gross_area, self.house_type, self.free_area, self.item_list)

    def add_item(self, item):
        print('现在添加的是:{}'.format(item.name))

        self.item_list.append(item.name)
        self.free_area -= item.area


class Floor:
    ''' 地板类 '''
    def __init__(self, name, area):
        '''
        :param name: 地板的名称
        :param area: 地板占地面积
        '''
        self.name = name
        self.area = area

    def __str__(self):
        return '{}地板占地面积是:{}'.format(self.name, self.area)


floor = Floor('青花瓷', 5)
floor2 = Floor('黑瓷', 7)
floor3 = Floor('花瓷', 4)
floor4 = Floor('青瓷', 3)
floor5 = Floor('红瓷', 2)
floor6 = Floor('黄瓷', 6)
home = House(150, '北京市大祥区****')
home.add_item(floor)
home.add_item(floor2)
home.add_item(floor3)
home.add_item(floor4)
home.add_item(floor5)
home.add_item(floor6)

print(home)

