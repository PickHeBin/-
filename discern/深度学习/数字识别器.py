#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 数字识别器.py
# Author: MuNian
# Date  : 2019/7/19

import numpy as np

# numpy array
array = [[1,2,3],[4,5,6]]
first_array = np.array(array) # 2x3 array
print("Array Type: {}".format(type(first_array))) # type
print("Array Shape: {}".format(np.shape(first_array))) # shape
print(first_array)

# import torch
#
# # pytorch array
# tensor = torch.Tensor(array)
# print("Array Type: {}".format(tensor.type)) # type
# print("Array Shape: {}".format(tensor.shape)) # shape
# print(tensor)

# numpy ones
print("Numpy {}\n".format(np.ones((2,3))))

# # pytorch ones
# print(torch.ones((2,3)))