#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 线程.py
# Author: MuNian
# Date  : 2019/7/16

import threading
import time

def saySorry():
    time.sleep(2)
    print('对不起,我错了, 再也不去外面....')


def sing():
    for i in range(3):
        print('正在唱歌..{}'.format(i))
        time.sleep(2)


for i in range(0, 5):
    print(time.ctime())
    # 创建一个线程
    t  = threading.Thread(target=saySorry)
    t2 = threading.Thread(target=sing)
    t.start()
    t2.start()
    print('结束:{}'.format(time.ctime()))

    while True:
        length = len(threading.enumerate())
        print('当前运行的线程数为:{}'.format(length))
        if length <= 1:
            break
