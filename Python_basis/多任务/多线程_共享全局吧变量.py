#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 多线程_共享全局吧变量.py
# Author: MuNian
# Date  : 2019/7/16
'''
互斥锁:
同步: 协同步调

避免死锁:
    1. 添加超时时间
    2. 银行家算法

分布式:
    多任务主要区分为同步和异步

Python:
    web开发  爬虫开发 自动化  AI  大数据 算法 游戏开发  ....

就业趋势:
    web 15K 自动化(10K)  爬虫(13K)  适合零基础快速就业  就业岗位比较多的

Python 入门比其他语言快 简单
4万  --- 3年 架构师 --> 全栈开发 逆向  自动化 爬虫 ...
简历
4.5个月快速就业  线上直播 + 课后录播 + 随堂笔记
1 3 5 正课  2 4 6解答  20:30 - 22:30
学会才毕业的
网络编程?  Python web(网页安全 网页攻击) + 爬虫(解析 渗透 破解...逆向)  --->  数据挖掘 ....  微软安全工程师认证 Python + C
AI  硬件   物联网 + Python + C
分期  6 9 12  通过花呗 借呗 京东白条 ... 一个月才500多块钱
1000学费优惠  7880 - 1000 = 6880  / 12 = ...

VIP服务:
    1. 课中测试 课后作业 每日反馈 课后一对一解答 辅导 补课
    2. 阶段考核(重修 免费) 学会才毕业
    3. 项目实战检验  学完后具备独立开发项目的能力
    4. 制定学习  毕业后  就业跟踪 学习路线规划
    5. 就业服务: 模拟BAT面试不是 就业指导 就业跟踪

'''


from threading import Thread
import threading


g_num = 100


def work1():
    global g_num
    for i in range(100000):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release()  # 解锁


print(g_num)


def work2():
    global g_num
    for i in range(100000):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release() # 解锁

    print(g_num)


if __name__ == '__main__':
    # 创建一个互斥锁
    mutex = threading.Lock()
    t1 = Thread(target=work1)
    t2 = Thread(target=work2)

    t1.start()
    t2.start()
