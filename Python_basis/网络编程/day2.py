#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : day2.py
# Author: MuNian
# Date  : 2019/7/12

from socket import *

# 1. 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 2. 接收方的地址
# 第一个参数为IP  port端口
dest_addr = ('192.168.0.191', 8080)

# 3. 从键盘获取要发送的数据
send_data = input('请输入你要发送的数据:')

# 4. 发送数据到指定电脑的指定程序当中
udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

# 等待对方发送数据 显示数据
recv_data = udp_socket.recvfrom(1024) # 设置本次接受最大字节

# recv_data[0]对方发送过来的数据
# [1] 对方的IP和port
print(recv_data[0].decode('gbk'))
print(recv_data[1])

udp_socket.close()
