#python 3.13.3
# -*- coding: utf-8 -*-
'''
@File    :   newton_interpolation.py
@Time    :   2023/10/11 20:35:31
@Author  :   Zhongyi Yang 
@Version :   1.0
@Desc    :   None
'''

import numpy as np

#根据输入的点坐标(xi,yi)计算出各阶差分：f[x_j, x_j-1, ... , x_i] = (f[x_j, x_j-1, ... , x_i+1] - f[x_j-1, x_j-2, ... , x_i]) / (x_j - x_i)，存放在矩阵中，第i列储存相应的i阶差分。
def calculate_derivative(points_x,points_y):
    length = len(points_x)
    A = np.zeros((length,length))       #初始化矩阵
    #把第一列的值设置为纵坐标的值
    for i in range(length):
        A[i][0] = points_y[i]
    
    #然后计算更高阶的项
    for colum in range(1,length):
        for row in range(length-colum):
            A[row][colum] = (A[row][colum-1]-A[row+1][colum-1])/(points_x[row]-points_x[row+colum])

    return A

def newton_interpolation(points_x,points_y,xlist):
    dev_matrix = calculate_derivative(points_x,points_y)
    # Print the normal function of newton interpolation.
    print("The newton Interpolation function is")
    for i in range(len(points_x)):
        print("%.6f" % dev_matrix[0][i], end='')
        if i !=0:       #第一个数值是常数后面不需要跟(x-xi)的项
            for j in range(i):
                print('*(x-(%.4f))'%points_x[j],end='')
            
        if i != len(points_x)-1:
            print('\n +',end='')
    
    #根据给出的xlist计算相应的y值
    ylist = np.zeros(xlist.shape)
    for i in range(len(points_x)):
        dev = dev_matrix[0][i]
        func = np.ones(xlist.shape)
        for j in range(i):     #生成一个(x-x1)(x-x2)……(x-xn)的表达式
            func = func * (xlist-points_x[j])
        ylist += dev*func    
    return ylist
    
