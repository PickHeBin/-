#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 刷访问.py
# Author: MuNian
# Date  : 2019/7/12
'''
IP :  局域网使用的 私网IP
127.0.0.1 - 127.255.255.255 回路测试
1024 -65535 动态端口

socket套接字

encode ---> 编码 字符串 --> 字节
decode ---> 解码 字节 --> 字符串

微软 首席技术专家 阿里首席技术专家
Python趋势:
    首选Python有: 人工智能  数据分析  算法 机器学习 深度学习
    就业趋势最好的:  web 后端开发  爬虫 自动化

计算机科学专业 : 数据分析 AI 算法发展
非计算机专业: web  爬虫 自动化

VIP服务:
    1. 4.5个月 为一期   1 3 5 正课  2 4 6 解答课  线上直播 + 课后录播 + 随堂笔记 晚上 20:30 - 22:30
    2. 课中测试 课后作业 课后反馈 课后一对一解答 辅导 补课
    3. 腾讯架构师一对一的学习计划制定
    4. 就业指导 规划学习 模拟BAT面试笔试
    学会才毕业  就业指导老师 就业跟踪  带你做兼职

无人驾驶  无人机  识别技术  语音技术 .... 大几什么专业
全栈

'''

# 创建一个socket
import socket

# socket.socket(Internet进程通信, 用于TCP协议 UDP协议)
# 创建一个udp套接字
socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. 接收方的地址
# 第一个参数为IP  port端口
dest_addr = ('192.168.0.191', 8080)

# 3. 从键盘获取要发送的数据
send_data = input('请输入你要发送的数据:')

# 4. 发送数据到指定电脑的指定程序当中
socket_udp.sendto(send_data.encode('utf-8'), dest_addr)

# 5. 关闭套接字
socket_udp.close()


