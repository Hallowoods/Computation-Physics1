#python 3.13.3
# -*- coding: utf-8 -*-
'''
@File    :   cubic_interpolation.py
@Time    :   2023/10/11 20:28:41
@Author  :   Zhongyi Yang 
@Version :   1.0
@Desc    :   None
'''

#python 3.13.3
# -*- coding: utf-8 -*-
'''
@File    :   cubic_interpolation.py
@Time    :   2023/10/11 21:36:47
@Author  :   Zhongyi Yang 
@Version :   1.0
@Desc    :   None
'''

import numpy as np

#需要计算不同插值位置处函数的二阶导数f''(xi),此函数的输出是一个由二阶导数构成的向量
def cubicSpline(points_x, points_y):    
    n = len(points_x)
    A = np.zeros((n,n))
    B = np.zeros((n,1))
    #写出A的具体形式，考虑到边界条件为左右两个端点的二阶导数值为0
    A[0][0] = 1
    A[-1][-1] = 1
    B[0][0] = 0
    B[-1][0] = 0


    for i in range(1,n-1):
        A[i][i-1] = points_x[i] - points_x[i-1]
        A[i][i] = 2 * (points_x[i+1] -points_x[i-1])
        A[i][i+1] = points_x[i+1] - points_x[i]
        B[i][0] = 6*(points_y[i+1]-points_y[i])/(points_x[i+1]-points_x[i])+6*(points_y[i-1]-points_y[i])/(points_x[i]-points_x[i-1])

    #矩阵求逆
    A_inv = np.linalg.inv(A)
    x_out = A_inv @ B
    return x_out