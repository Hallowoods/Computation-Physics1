#python 3.13.3
# -*- coding: utf-8 -*-
'''
@File    :   (1+25x^2).py
@Time    :   2023/10/12 10:23:54
@Author  :   Zhongyi Yang 
@Version :   1.0
@Desc    :   None
'''


import numpy as np
import math
import Newton_interpolation
import Cubic_interpolation
import matplotlib.pyplot as plt
#计算插值点函数值
points_x = np.linspace(-1 ,1 , 10)
points_y = 1/(1+25*points_x**2)

#先计算newton interpolation
xlist = np.linspace(-1 , 1 , 2000)
ylist = Newton_interpolation.newton_interpolation(points_x,points_y,xlist)
plt.plot(xlist, ylist, 'r', alpha = 0.7, label='Newton Interpolation')
plt.legend(loc='best')


#再计算cubic interpolation
dev = Cubic_interpolation.cubicSpline(points_x,points_y)
for i in range(len(points_x)-1):
    x_i = np.linspace(points_x[i],points_x[i+1],100)
    y_i = -dev[i][0]*(x_i-points_x[i+1])**3/(6*(points_x[i+1]-points_x[i])) + dev[i+1][0]*(x_i-points_x[i])**3/(6*(points_x[i+1]-points_x[i])) + (points_x[i+1]-x_i)*(points_y[i]/(points_x[i+1]-points_x[i])-dev[i][0]*(points_x[i+1]-points_x[i])/6) + (x_i-points_x[i])*(points_y[i+1]/(points_x[i+1]-points_x[i])-dev[i+1][0]*(points_x[i+1]-points_x[i])/6)
    if i == 0:
        plt.plot(x_i, y_i, 'b', alpha = 0.7, label = "Cubic Spline")
    else:
        plt.plot(x_i, y_i, 'b', alpha = 0.7)


#三个图进行比较，补充一个标准的函数
plt.plot(xlist, 1/(1+25*xlist**2), 'g', alpha = 0.7, label='Original Function')
plt.scatter(points_x, points_y, label='Data Points')
plt.legend(loc='best')

plt.show()


#计算误差
#牛顿法
plt.plot(xlist, ylist - 1/(1+25*xlist**2), 'r', alpha = 0.7, label='Newton Interpolation Error')

#cubic spline
for i in range(len(points_x)-1):
    x_i = np.linspace(points_x[i],points_x[i+1],100)
    y_i = -dev[i][0]*(x_i-points_x[i+1])**3/(6*(points_x[i+1]-points_x[i])) + dev[i+1][0]*(x_i-points_x[i])**3/(6*(points_x[i+1]-points_x[i])) + (points_x[i+1]-x_i)*(points_y[i]/(points_x[i+1]-points_x[i])-dev[i][0]*(points_x[i+1]-points_x[i])/6) + (x_i-points_x[i])*(points_y[i+1]/(points_x[i+1]-points_x[i])-dev[i+1][0]*(points_x[i+1]-points_x[i])/6)
    if i == 0:
        plt.plot(x_i , y_i-1/(1+25*x_i**2), 'b', alpha = 0.7, label = "Cubic Spline Error")
    else:
        plt.plot(x_i , y_i-1/(1+25*x_i**2), 'b', alpha = 0.7)
plt.legend()
plt.show()