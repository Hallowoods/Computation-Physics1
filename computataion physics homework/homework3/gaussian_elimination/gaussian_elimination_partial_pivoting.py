#python 3.13.3
# -*- coding: utf-8 -*-
'''
@File    :   gaussian_elimination_partial_pivoting.py
@Time    :   2023/10/08 14:04:01
@Author  :   Zhongyi Yang 
@Version :   1.0
@Desc    :   None
'''


import numpy as np
D = np.array([[2.,3.,5.],[3.,4.,8.],[1.,3.,3.]])
d = np.array([[5.],[6.],[5.]])
E = np.hstack((D,d))        #增广矩阵

#定义一个交换两行的函数
def swap_rows(A,i,j):
    tem = np.copy(A[j])
    A[j] = A[i]
    A[i] = tem
    return A


for row in range(2):        #再遍历第row行时，做一个partial pivoting使得此时该行的主元最大
    max = E[row][row]
    for row2 in range(row+1,3):
        if np.fabs(E[row2][row])>np.fabs(max):
            max = E[row2][row]
            E = swap_rows(E,row,row2)
           
    #然后将其下方的每一行的主元对应位置消去
    for row3 in range(row+1,3):
        a = E[row3][row]/E[row][row]
        cancellation = np.array(np.zeros((3,4)))
        cancellation[row3] = a * E[row]
        E -= cancellation
        

# 回溯求解
x = np.zeros(3)
#第一个解可以直接得到
x[2] = E[2][3]/E[2][2]
#其余解需要用到递推
for i in range(1,-1,-1):
    for j in range(i+1,3):
        E[i][3] -= E[i][j] * x[j] 
    x[i] = E[i][3]/E[i][i]

print('The solution to the given function is:')
for i in range(3):
    print('x'+str(i)+'=','%.4f'%x[i])
    
    
    


