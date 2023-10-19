# -*- coding: utf-8 -*-
"""
Laboratório 8

Reproduzir figuras dos slides 19, 20 e 28 da aula DFT 
"""


import pds
import numpy as np
import matplotlib.pyplot as plt
w1 = (2*np.pi/9)
w2 = (2*np.pi/6)

#cos
N = 40

n = np.arange(-N/2,N/2)
k = np.arange(-N/2,N/2)


x = np.cos(w2*n)

plt.figure(1)
plt.stem(k,x)


k2 = np.linspace(-3,3,num=N)
w =np.linspace(-np.pi,np.pi,N)
X = pds.dtft(x,n,w)
plt.figure(2)
plt.plot(k2, np.abs(X)/N)


#janela
k = np.arange(19)
janela = np.zeros(19)
indice_central = 19//2
janela[indice_central - 9:indice_central + 10] = 1
#plt.figure(3)
#plt.plot(k,janela)
"""
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
#x2 = 

x = np.cos(w1*n) + (3/4)*np.cos(w2*n)
X = pds.dft(x)
plt.figure(3)
plt.stem(k, np.abs(X)/N)
"""