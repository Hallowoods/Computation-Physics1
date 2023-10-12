#python 3.13.3
# -*- coding: utf-8 -*-
'''
@File    :   potential_v2_para_v.py
@Time    :   2023/09/28 14:05:33
@Author  :   Zhongyi Yang 
@Version :   1.0
@Desc    :   None
'''

# 使用变分法求解一维薛定谔方程，势场为 V(x)=x^4-x^2,以中心的高斯波包（不同宽度）为一组基展开
import math
from sympy import *
import numpy as np
from scipy.linalg import sqrtm
import matplotlib.pyplot as plt

#规定相关物理参数取值
h_bar = 1
m = 1        #质量
s = 0       #势能位置
dim = 10       #变分的维数（展开的基的数量）
v_list = np.linspace(1,11,dim)     #展开的基的s的取值列表
x_list = np.linspace(-4,+4,1000)
def potential(x):
    return x**4-x**2

#创建一个 S 矩阵和 H 矩阵
S_matrix = np.zeros((dim,dim))
H_matrix = np.zeros((dim,dim))

def Phi_Phi(vi,vj):       #两个基的内积
    return math.sqrt(vi * vj) / math.sqrt(math.pi * (vi + vj))

def Phi_H_Phi(vi, vj):        #哈密顿量的矩阵元
    return math.sqrt(vi * vj) * (4 * h_bar**2 * vi * vj * (vi + vj)+ m * (4 * (s**2 - 1) * s**2 * vi**2 + 2 * vi * (2 * s**2 * (2 * (s**2 - 1)* vj + 3) - 1) + 4 * s**2 * vj * ((s**2 - 1) * vj + 3) - 2 * vj + 3))/ (4 * m * (vi + vj)**(5 / 2) * math.sqrt(math.pi))

#计算 S,H
for i in range(dim):
    for j in range(dim):
        S_matrix[i][j] = Phi_Phi(v_list[i],v_list[j])
        H_matrix[i][j] = Phi_H_Phi(v_list[i],v_list[j])

S_matrix_sqrt = sqrtm(S_matrix)     #sqrt(S)
H_matrix_prime = np.linalg.inv(S_matrix_sqrt) @ H_matrix @ np.linalg.inv(S_matrix_sqrt)        #H'

eigen_states, eigenvectors_prime = np.linalg.eig(H_matrix_prime)        #H'的本征值和本征向量
eigenvectors = np.linalg.inv(S_matrix_sqrt) @ eigenvectors_prime        #真实的本征态矩阵

eigen_states_lowest = sorted(eigen_states)[:3]      #对本征值排序并且截取前三个

#还想知道排序之后的最低三个能级对应的原来的本征态下标
indexes=[]        #indexes的三个元素分别代表从低到高，最低三个能级的下标
for i in range(3):
    index = np.argwhere(eigen_states == eigen_states_lowest[i])
    indexes.append(int(index))

print('The three lowest eigenenergy with potention V(x) = x^2-x^4 are:')
for i in eigen_states_lowest:
    print('%.4f' %i)

#作图
def wave_function(index, v, eigenvectors, x): 
    # wave_function = \sum{j from 1 to n}{eigenvalue_j * phi_j} 
    sum = 0
    for j in range(dim):
        sum += eigenvectors[j][index] * math.sqrt(v[j] / math.pi) * math.exp(-v[j] * (x - s)**2)
    return sum

fig, ax = plt.subplots()
x = np.linspace(-4, 4, 1000)
for i in range(3):
    waveFunction = [wave_function(indexes[i], v_list, eigenvectors, xi) for xi in x]
    ax.plot(x, waveFunction, label=f"$\phi_{i}$")
ax.plot(x, potential(x), "k--", label="$V(x) = x^4 - x^2$")
ax.legend(loc="upper right")
ax.set_ylim(-1, 1)
plt.show()