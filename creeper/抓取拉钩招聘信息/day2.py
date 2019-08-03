#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : day2.py
# Author: MuNian
# Date  : 2019/7/18

# 1. json的数据请求
# 2. 用户session反爬机制(cookies)(保存的用户账户信息)
# 3. content使用

import requests

# 页面的url
url1 = 'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput='

# json数据的url
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

# 请求头部信息
headers = {
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3708.400 QQBrowser/10.4.3661.400'
}

data = {
    'first': 'true',
    'pn': '1',
    'kd': 'Python'
}

# 建立session
s = requests.Session()
s.get(url=url1, headers=headers, timeout=3)
cookie = s.cookies

response_data = requests.post(url, headers=headers, data=data, cookies=cookie).json()
print(response_data['content']['positionResult']['result'])

