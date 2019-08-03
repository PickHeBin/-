#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : day.py
# Author: MuNian
# Date  : 2019/7/16

import numpy
import pandas
import matplotlib.pyplot as plt
# 散点矩形
from pandas.plotting import scatter_matrix
# 特征缩放
from sklearn.preprocessing import StandardScaler
# 交叉验证法
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
# 逻辑回归
from sklearn.linear_model import LogisticRegression

myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = ['a', 'b']
colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)

# 导入csv
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
print(data.shape)

data = pandas.read_csv(url, names=names)
description = data.describe()
print(description)

data = pandas.read_csv(url, names=names)
scatter_matrix(data)
plt.show()

dataframe = pandas.read_csv(url, names=names)
array = dataframe.values
# 数组分成输入和输出组件
X = array[:,0:8]
Y = array[:,8]
scaler = StandardScaler().fit(X)
# 通过定心和定标来实现标准化
rescaledX = scaler.transform(X)
# 汇总转换后的数据
# 设置打印选项
numpy.set_printoptions(precision=3)
print(rescaledX[0:5,:])

