#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : python识别和生成二维码.py
# Author: NanFeng
# Date  : 2019/6/27

from pyzbar import pyzbar
from PIL import Image
from MyQR import myqr


def get_ewm(img_adds):
    """ 读取二维码的内容： img_adds：二维码地址（可以是网址也可是本地地址 """
    img = Image.open(img_adds)

    txt_list = pyzbar.decode(img)
    barcodeData = txt_list[0].data.decode("utf-8")

    return barcodeData


def get_qr(qr_img, picture, save_name):
    words = get_ewm(qr_img)
    myqr.run(words, version=1, level='H', picture=picture, colorized=True, brightness=1.0, save_name=save_name, contrast=1.2)


if __name__ == '__main__':
    qr_img = '丸子老师.jpg'  # 你要改变的二维码
    save_name = 'qr_wzls.gif'  # 保存的名字
    picture = 'wzls.jpg'  # 需要结合的图片
    # 解析本地二维码
    get_qr(qr_img=qr_img, save_name=save_name, picture=picture)

