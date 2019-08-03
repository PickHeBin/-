#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 刷访问.py
# Author: MuNian
# Date  : 2019/7/31

import requests
from lxml import etree

url = 'http://www.meizitu.com/tag/banluo_5_1.html'

# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'Host': 'www.meizitu.com',
#     'If-Modified-Since': 'Wed, 15 May 2019 00:41:48 GMT',
#     'Proxy-Connection': 'keep-alive',
#     'Referer': 'https://www.google.com/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
#     'Cookie':'__cfduid=d757e9d925115ae4fea7393908e03822b1564550042',
# }

# proxies={
#     # 'http':"104.27.146.156:8080"
#     "http": "http://www.free99999.com:dongtaiwang.com@104.27.146.156:8080/",
# }

# proxies = {
#   "http": "http://104.27.146.156:8080",
#   "https": "http://104.27.146.156:8080",
# }


headers = {
    # 'Cookie': '__cfduid=d757e9d925115ae4fea7393908e03822b1564550042; UM_distinctid=16c46912271466-021c8c58e72372-c343162-1fa400-16c46912272c06; CNZZDATA30056528=cnzz_eid%3D549226793-1564552011-http%253A%252F%252Fwww.meizitu.com%252F%26ntime%3D1564552011',
    # 'Host': 'www.meizitu.com',
    # 'Pragma': 'no-cache',
    # 'Proxy-Connection': 'keep-alive',
    # 'Referer': 'http://www.meizitu.com/',
    # 'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

}

response_data = requests.get(url, headers=headers, timeout=3).text
print(response_data)