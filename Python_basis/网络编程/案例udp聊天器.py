#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 案例udp聊天器.py
# Author: MuNian
# Date  : 2019/7/12

import socket


def send_msg(udp_socket):
    ''' 发送数据 '''
    # 1. 从键盘获取要发送的数据
    msg = input('\n请输入你要发送的数据:')
    # dest_ip = input('\n请输入对方的IP:')
    dest_ip = '192.168.0.191'
    # dest_port = int(input('请输入对方的端口:'))
    dest_port = 8080
    udp_socket.sendto(msg.encode('utf-8'), (dest_ip, dest_port))


def recv_msg(udp_socket):
    ''' 接受数据 '''
    # 1. 接收的最大字节
    recv_msg = udp_socket.recvfrom(1024)
    # 2. 解码对方发送的数据
    # [1] 对方的IP和端口
    recv_ip = recv_msg[1]
    recv_msg = recv_msg[0].decode('gbk')
    print(">>>>>{}:{}".format(recv_ip, recv_msg))


def main():
    ''' 主程序 '''
    # 1. 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 绑定本地信息
    udp_socket.bind(('', 9090)) # 本地默认是使用127.0.0.1
    while True:
        # 3. 选择功能
        print("=" * 50)
        print("1:发送信息")
        print("2:接受信息")
        print("=" * 50)
        user_input = input('请输入你想要操作的功能:')

        #  根据用户输入选择对应的函数功能
        if user_input == "1":
            send_msg(udp_socket)

        elif user_input == "2":
            recv_msg(udp_socket)

        else:
            print('输入有误,重新输入')


if __name__ == '__main__':
    main()