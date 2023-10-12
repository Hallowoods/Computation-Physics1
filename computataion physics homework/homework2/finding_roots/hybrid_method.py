#python 3.13.3
# -*- coding: utf-8 -*-
'''
@File    :   hybrid_method.py
@Time    :   2023/09/15 11:25:01
@Author  :   Zhongyi Yang 
@Version :   1.0
@Desc    :   None
'''
def f(x):
    y = x**3-5*x+3
    return y

def f_1(x):
    y = 3*x**2-5
    return y


def bisection(a,b,c):
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
a0 = 0
a1 = 1
a2 = 2
c = 1e-14   #precision
def hybrid(a,b):
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
                x = bisection(a,b,c)
        else:
            x = bisection(a,b,c)
    return x

print('Using hybrid method , we find two roots > 0 for f(x)=x**3-5*x+3:')
print('root1 = %.14f'%hybrid(a0,a1) )
print('root2 = %.14f'%hybrid(a1,a2) )