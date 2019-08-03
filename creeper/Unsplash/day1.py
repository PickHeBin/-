#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 刷访问.py
# Author: MuNian
# Date  : 2019/7/29

import requests
from pyquery import PyQuery as pq

conut = 1

def Img_url_Dowloads(page):
    global conut
    url = 'http://gratisography.com/page/{}/'.format(page)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }

    response_data = requests.get(url, headers=headers).text
    doc = pq(response_data)
    single = doc('.single-photo-thumb a img').items()
    for i in single:
        dowloads_url = i.attr('src')
        img_data = requests.get(dowloads_url, headers=headers)
        with open('高清图片/{}.jpg'.format(conut), 'ab') as f:
            f.write(img_data.content)
        conut += 1


page = int(input('输入你要抓取的页数:'))
for i in range(1, page):
    Img_url_Dowloads(i)