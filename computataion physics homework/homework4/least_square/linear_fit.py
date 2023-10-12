#python 3.13.3
# -*- coding: utf-8 -*-
'''
@File    :   linear_interpolation.py
@Time    :   2023/10/12 10:38:22
@Author  :   Zhongyi Yang 
@Version :   1.0
@Desc    :   None
'''

import numpy as np
import math

def linear():
    A = np.ones((9,2))
    xlist = [1,2,3,4,5,6,7,8,9]
    Tlist = [14.6,18.5,36.6,30.8,59.2,60.1,62.2,79.4,99.9]
    x_out = np.ones((9,1))
    #将矩阵第二列变成xi
    for i in range (9):
        A[i][1] = xlist[i]

    #SVD分解
    U, SL, VT = np.linalg.svd(A)
    S = np.diag(SL)
    UT = np.transpose(U)
    V = np.transpose(VT)
    S_inv = np.linalg.inv(S)
    #对S_inv进行维度扩充
    S_inv = np.pad(S_inv, ((0, 0), (0, 7)), mode='constant')
    x_out = V @ S_inv @ UT @ Tlist
    return x_out

print('a=%.4f'%linear()[0],'b=%.4f'%linear()[1])
print('The linear fitting line is:T=%.4f+%.4f*x'%(linear()[0],linear()[1]))