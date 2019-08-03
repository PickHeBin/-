#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 备课_day1.py
# Author: MuNian
# Date  : 2019/7/5

import requests


keyapp = '525e96cab2031edc8e743965c68de9a3'

url = 'http://v.juhe.cn/toutiao/index?type=junshi&key=' + keyapp

response_data = requests.get(url).json()
data = response_data['result']['data']
for i in data:
    result = {}
    result['标题'] = i['title']
    result['时间'] = i['date']
    result['类型'] = i['category']
    result['来源'] = i['author_name']
    result['地址'] = i['url']

    print(result)