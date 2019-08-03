#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 备课_day1.py
# Author: MuNian
# Date  : 2019/7/3

import requests
from pyquery import PyQuery as pq


url = 'http://www.dianping.com/changsha/ch10/r303'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Host': 'www.dianping.com',
    'Referer': 'http://www.dianping.com/changsha/food',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36'
}

response_data = requests.get(url, headers=headers).text
doc = pq(response_data)
tit = doc('.txt').items()
for i in tit:
    title = i.find('.tit h4').text()
    comment = i.find('.comment span').attr('title')
    recommend = i.find('.recommend').text()

    data = {
        '商铺名' : title,
        '店铺星级' : comment,
        '店铺特色' : recommend
    }

    print(data)

