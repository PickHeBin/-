#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : cred.py
# Author: MuNian
# Date  : 2019/7/11
'''
1. 主菜单
2. 新建名片 --- 名片信息保存字典
3. 查询名片

'''

# 名片列表
card_list = []

def show_meun():
    '''
    显示菜单
    :return:
    '''
    print('*' * 50)
    print('[名片管理系统]')
    print('')
    print('1. 新建名片')
    print('2. 查询名片')
    print('')
    print('0. 退出系统')
    print('*' * 50)


def new_card():
    '''
    新建名片
    1. 提示用户输入名片信息
    2. 名片信息保存到一个字典
    3. 将字典添加到名片列表
    :return:
    '''
    print('_' * 50)
    print('功能:新建名片')

    # 从键盘获取数据
    name = input('请输入姓名:')
    phone = input('请输入电话号码:')
    qq = input('请输入你的qq号码:')
    # 2. 名片信息保存到一个字典
    card__dict = {
        'name':name,
        'phone':phone,
        'qq':qq
    }
    # 将字典添加到名片列表
    card_list.append(card__dict)

    print(card_list)
    print('成功添加了{}的名片'.format(card__dict['name']))


def search_card():
    '''
    搜索名片
    1. 从键盘获取你要搜索的名片
    2. 遍历字典
    :return:
    '''
    print('_' * 50)
    print('功能:搜索名片')

    find_name = input('请输入你要搜索的名片:')

    for card_dict in card_list:
        # 判断字典里面的name是否和输入的是一样的
        if card_dict['name'] == find_name:
            print("姓名\t\t\t电话\t\t\tQQ")
            print('_' * 50)

            print('{}\t\t\t{}\t\t\t{}'.format(
                card_dict['name'],
                card_dict['phone'],
                card_dict['qq']
            ))
            print('_' * 50)
            break

    else:
        print('抱歉!{}名片不存在'.format(find_name))

