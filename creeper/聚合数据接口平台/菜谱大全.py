#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 菜谱大全.py
# Author: MuNian
# Date  : 2019/7/8
import requests, json

url = 'http://apis.juhe.cn/cook/query.php'

menu = input('请输入你要获取的菜谱名:')
key = 'e6610bd552c36ba29346b1d0e28fed56'
parmas = {
    'menu':menu,
    'key':key,
    'dtype':'',
    'rn':'30'
}

response_data = requests.get(url, params=parmas).json()
result = response_data['result']['data']
for  i in result:
    data = {}
    # 菜名
    data['菜名'] = i['title']
    # 类型
    data['类型'] = i['tags']
    # 配料
    data['配料'] = i['burden']
    data['制作方式'] = i['steps']
    print(data)