#python 3.13.3
# -*- coding: utf-8 -*-
'''
@File    :   searching_minimum
@Time    :   2023/09/15 14:09:43
@Author  :   Zhongyi Yang 
@Version :   1.0
@Desc    :   None
'''


import math
print('Input your starting point to find the minimum:')
x0 = float(input('x='))
y0 = float(input('y='))
c = 1e-10       #precision
a = 0.01    #步长
istrue = True

def f(x,y):
    z= math.sin(x + y) + math.cos(x + 2 * y)
    return z

def f1(x,y):        # x方向上的偏导数
    z = math.cos(x + y) - math.sin(x + 2 * y)
    return z

def f2(x,y):        # y方向上的偏导数
    z = math.cos(x + y) - 2*math.sin(x + 2 * y)
    return z 

while istrue:
    x = x0 - a * f1(x0,y0)
    y = y0 - a * f2(x0,y0)
    dx = abs(x - x0)
    dy = abs(y - y0)
    if dx < c and dy < c:
        istrue = False
    else:
        x0 = x
        y0 = y

print('Minimum of the funciton f(x,y) is %.1f'%f(x,y))

