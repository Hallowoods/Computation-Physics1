#python 3.13.3
# -*- coding: utf-8 -*-
'''
@File    :   parbolic_fit.py
@Time    :   2023/10/12 11:08:10
@Author  :   Zhongyi Yang 
@Version :   1.0
@Desc    :   None
'''

import numpy as np
import math
import matplotlib.pyplot as plt
from linear_fit import linear

A = np.ones((9,3))
xlist = [1,2,3,4,5,6,7,8,9]
xsquare_list = [i**2 for i in xlist]
Tlist = [14.6,18.5,36.6,30.8,59.2,60.1,62.2,79.4,99.9]
x_out = np.ones((9,1))

#将矩阵第二列变成xi,第三列变成xi**2
for i in range (9):
    A[i][1] = xlist[i]
    A[i][2] = xsquare_list[i]

#SVD分解
U, SL, VT = np.linalg.svd(A)
S = np.diag(SL)
UT = np.transpose(U)
V = np.transpose(VT)
S_inv = np.linalg.inv(S)
#对S_inv进行维度扩充
S_inv = np.pad(S_inv, ((0, 0), (0, 6)), mode='constant')

x_out = V @ S_inv @ UT @ Tlist
print('a=%.4f'%x_out[0],'b1=%.4f'%x_out[1],'b2=%.4f'%x_out[2])
print('The Parbolic fitting line is:T=%.4f+%.4f*x+%.4f*x**2'%(x_out[0],x_out[1],x_out[2]))

#将两个拟合结果放在一张图上
x = np.linspace(1,9,100)
y2 = x_out[0]+x_out[1]*x+x_out[2]*x**2
y1 = linear()[0] + linear()[1]*x

plt.scatter(xlist,Tlist,color='r',alpha =0.7,label='Data points')
plt.plot(x,y1,color='b',alpha =0.7,label='Linear fit')
plt.plot(x,y2,color='g',alpha =0.7,label='Parbolic fit')
plt.legend(loc='best')
plt.show()
