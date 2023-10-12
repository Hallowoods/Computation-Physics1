#python 3.13.3
# -*- coding: utf-8 -*-
'''
@File    :   potential_v2_para_s.py
@Time    :   2023/09/28 13:49:30
@Author  :   Zhongyi Yang 
@Version :   1.0
@Desc    :   None
'''

# 使用变分法求解一维薛定谔方程，势场为 V(x)=x^4-x^2,固定以固定宽度的高斯波包（不同中心）为一组基展开
import math
from sympy import *
import numpy as np
from scipy.linalg import sqrtm
import matplotlib.pyplot as plt

#规定相关物理参数取值
h_bar = 1
m = 0.5         #质量
v = 2 * math.pi     #势能宽度
dim = 50       #变分的维数（展开的基的数量）
s_list = np.linspace(-5,+5,dim)     #展开的基的s的取值列表
x_list = np.linspace(-7,+7,1000)
def potential(x):
    return x**4-x**2

#创建一个 S 矩阵和 H 矩阵
S_matrix = np.zeros((dim,dim))
H_matrix = np.zeros((dim,dim))

def Phi_Phi(si,sj):       #两个基的内积
    return math.sqrt(v) * math.exp(-v * (si - sj) ** 2 / 2) / math.sqrt(2 * math.pi)

def Phi_H_Phi(si,sj):     #哈密顿量的矩阵元
    return (math.exp(-v * (si - sj)**2 / 2) * (8 * h_bar**2 * v**3 * (1 - v * (si - sj)**2)+ m * (v * ((si + sj)**2 * (v * (si + sj - 2) * (si + sj + 2) + 6)- 4) + 3))) / (16 * math.sqrt(2 * math.pi) * m * v**(3 / 2))

#计算 S,H
for i in range(dim):
    for j in range(dim):
        S_matrix[i][j] = Phi_Phi(s_list[i],s_list[j])
        H_matrix[i][j] = Phi_H_Phi(s_list[i],s_list[j])

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


print('The three lowest eigenenergy with potention V(x) = x^4_x^2 are:')
for i in eigen_states_lowest:
    print('%.4f' %i)

def wave_function(index, s, eigenvectors, x):  
    sum = 0
    for j in range(dim):
        sum += eigenvectors[j][index] * math.sqrt(v / math.pi) * math.exp(-v * (x - s[j])**2)
    return sum

fig, ax = plt.subplots()
for i in range(3):
    Wavefunction = [wave_function(indexes[i],s_list,eigenvectors,xi) for xi in x_list]
    ax.plot(x_list, Wavefunction, label=f"$\phi_{i}$")
ax.plot(x_list, potential(x_list), "k--", label="$V(x) = x^4-x^2$")
ax.legend(loc="upper right")
ax.set_ylim(-1, 1)
plt.show()

