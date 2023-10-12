#python 3.13.3
# -*- coding: utf-8 -*-
'''
@File    :   finite_square_well_potential.py
@Time    :   2023/09/15 14:09:28
@Author  :   Zhongyi Yang 
@Version :   1.0
@Desc    :   None
'''

from math import sin,cos,sqrt,tan,pi
V0 = 10     
a = 0.2
m = float(input('m='))     #自己定义对应的质量
hbar = 1        #规定普朗克常数为 1
c = 1e-5    #precision
x0 = sqrt(2*m*V0) * a / hbar

def sec(x):
    z = 1/cos(x)
    return z

def cot (x):
    z = 1/tan(x)
    return z

def csc(x):
    z = 1/sin(x)
    return z

def f(x):      #若波函数为偶函数
    z = x*sin(x)-sqrt(x0**2-x**2)*cos(x)
    return z

def f_1(x): #一阶导数
    z = x*cos(x) + x*cos(x)/sqrt(x0**2-x**2) + sin(x) + sin(x)*sqrt(x0**2-x**2)
    return z

def g(x):       #若波函数为奇函数
    z = x*cos(x) + sqrt(x0**2-x**2)*sin(x)
    return z

def g_1(x):     #一阶导数
    z = cos(x) + sqrt(x0**2 - x**2)*cos(x) - x*sin(x) - x*sin(x)/sqrt(x0**2 - x**2)
    return z

def bisection_even(a,b,c):
    if f(a)*f(b)>0:
        print('wrong choice for a and b')
    else:    
        while b-a >= c:
            x = (a+b)/2
            if f(a)*f(x)<0:
                b=x
            elif f(b)*f(x)<0:
                a=x
            else:
                break
        return x
    
def hybrid_even(a,b):
    x = (a+b)/2
    while b-a > c:
        if f_1(x) != 0:
            temx = x-f(x)/f_1(x)
            if abs(temx - x) < c:
                return temx
            
            if temx >a and temx < b :
                if f(temx) * f(a) < 0:
                    b = temx
                elif f(temx) * f(b) < 0:
                    a = temx
                x = temx
            else:
                x = bisection_even(a,b,c)
        else:
            x = bisection_even(a,b,c)
    return x

def bisection_odd(a,b,c):
    if g(a)*g(b)>0:
        print('wrong choice for a and b')
    else:    
        while b-a >= c:
            x = (a+b)/2
            if g(a)*g(x)<0:
                b=x
            elif g(b)*g(x)<0:
                a=x
            else:
                break
        return x

def hybrid_odd(a,b):
    x = (a+b)/2
    while b-a > c:
        if g_1(x) != 0:
            temx = x-g(x)/g_1(x)
            if abs(temx - x) < c:
                return temx
            if temx >a and temx < b :
                if g(temx) * g(a) < 0:
                    b = temx
                elif g(temx) * g(b) < 0:
                    a = temx
                x = temx
            else:
                x = bisection_odd(a,b,c)
        else:
            x = bisection_odd(a,b,c)
    return x




functiontype = input('想知道偶函数的能量还是奇函数的能量（输入“偶”或者“奇”）：')

# 针对偶函数的情况
if functiontype == '偶':
    num_of_solution_even = int(x0/pi)+1      #偶函数能量解的个数
    k = int(input('共有%d个能级,想知道第几能级(eg.输入:"2"):'%num_of_solution_even))
    if k <= num_of_solution_even:
        a0 = (k-1)*pi if k!=1 else (k-1)*pi + 1e-10 
        b0 = (k-1/2)*pi if k!=num_of_solution_even else num_of_solution_even-1e-10
        x = hybrid_even(a0,b0)
        E_even = (x*hbar**2)/2*m*a**2
        print('第%d个能级的能量是:%.2f'%(k,E_even))
        
    else :
        print('想要的能级不在合理范围内！')

# 针对奇函数的情况
if functiontype == '奇':
    if x0 < pi/2:
        print('能量太低不足以形成定态！')
    else:
        num_of_solution_odd = int(x0/pi)+1          #奇函数能量解的个数
        k = int(input('共有%d个能级,想知道第几能级(eg.输入:"2"):'%num_of_solution_odd))
        if k <= num_of_solution_odd:
            a0 = (k-1/2)*pi 
            b0 = k*pi if k!=num_of_solution_odd else num_of_solution_odd-1e-10
            x = hybrid_odd(a0,b0)
            E_odd = (x*hbar**2)/2*m*a**2
            print('第%d个能级的能量是:%.2f'%(k,E_odd))
        else : 
            print('想要的能级不在合理范围内！')


    




