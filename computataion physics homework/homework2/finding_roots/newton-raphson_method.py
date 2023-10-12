#python 3.13.3
# -*- coding: utf-8 -*-
'''
@File    :   newton-raphson_method.py
@Time    :   2023/09/15 11:03:32
@Author  :   Zhongyi Yang 
@Version :   1.0
@Desc    :   None
'''

def f(x):
    y = x**3-5*x+3
    return y

# 从 f(x)形式推出它的一阶导数 f_1(x)
def f_1(x):
    y = 3*x**2-5
    return y

def newrap(a,c):    #输入初始值 a 和精度 c
    b = a+2*c   # 初始化一个与 a 有较大间隔的数字开始循环，之后的 b 用于储存上一次的计算结果用于比较
    while abs(b-a) >=c:
        b = a
        a = a - f(a)/f_1(a)
    return a

x1 = 0.6566
x2 = 1.8342
c = 1e-15

print('Using Newton-Raphson method , we polish our results to 14 decimal spaces:')
print('root1 = %.14f'%newrap(x1,c))
print('root2 = %.14f'%newrap(x2,c))