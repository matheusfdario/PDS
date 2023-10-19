# -*- coding: utf-8 -*-

import pds
import numpy as np
import matplotlib.pyplot as plt
w1 = (2*np.pi/9)
w2 = (4*np.pi/7)

#com vazamento
N = 32
n = np.arange(N)
k = np.arange(N)


x = np.cos(w1*n) + (3/4)*np.cos(w2*n)
X = pds.dft(x)

plt.stem(k, np.abs(X)/N)

#com muito vazamento
N = 32
n = np.arange(N)
k = np.arange(N)


x = np.cos(w1*n) + (3/4)*np.cos(w2*n)
X = pds.dft(x)
plt.figure(1)
plt.stem(k, np.abs(X)/N)


#solução 1: mais amostras, menos vazamento

N = 100
n = np.arange(N)
k = np.arange(N)


x = np.cos(w1*n) + (3/4)*np.cos(w2*n)
X = pds.dft(x)
plt.figure(2)
plt.stem(k, np.abs(X)/N)
#Solução 2: zero padding

N = 32
K = 100
n = np.arange(N)
k = np.arange(K)
x2 = 

x = np.cos(w1*n) + (3/4)*np.cos(w2*n)
X = pds.dft(x)
plt.figure(3)
plt.stem(k, np.abs(X)/N)