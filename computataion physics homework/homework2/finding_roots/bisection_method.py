#python 3.13.3
# -*- coding: utf-8 -*-
'''
@File    :   finding_roots.py
@Time    :   2023/09/15 10:30:38
@Author  :   Zhongyi Yang 
@Version :   1.0
@Desc    :   None
'''
#定义函数
def f(x):
    y=x**3-5*x+3
    return y

# 定义二分法寻根函数，输入a,b(范围),c(精度)，输出满足要求的根x
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

#我们发现 f(0)>0,f(1)<0,f(2)>0.
a0=0
a1=1
a2=2
c=1e-5

print('Using bisecection method , we find 2 roots >0 for f(x)=x**3-5*x+3 :')
print('root1 = %.4f' %bisection(a0,a1,c))
print('root1 = %.4f' %bisection(a1,a2,c))
