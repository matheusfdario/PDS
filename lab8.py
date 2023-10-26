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

X = pds.dft(x)


#k = np.arange(-3,4)
#k2 = np.linspace(-3,3,num=N)
#w = np.linspace(-np.pi,np.pi,N)

plt.figure(2)
plt.stem(k, np.abs(X)/N)


N = 40
#criando  o sinal janela
# Crie um vetor preenchido com zeros
janela = np.zeros(N, dtype=int)
k = np.arange(-N/2,N/2)
# Preencha a parte central do vetor com 1s
inicio_1s = (N - 19) // 2
fim_1s = inicio_1s + 20

janela[inicio_1s:fim_1s] = 1
#plotando a janela
plt.figure(3)
plt.stem(k,janela)
#plotando a dft da janela -> deveria ter uma sinc
X = pds.dft(janela)
plt.figure(4)
plt.plot(k, np.abs(X)/N)


#janelando o sinal
W = janela*x
X = pds.dft(W)
#plotando o sinal janelado
plt.figure(5)
plt.stem(k, W)

#plotando a dft do sinal janelado
plt.figure(6)
plt.plot(k, np.abs(X)/N)
count = 0
for i in X:
    if i != 0:
        count+=1
Y = []#np.zeros(count)

for i in range(len(X)):
    if X[i] != 0:
        Y.append(X[i])
N = 20
k = np.arange(-N/2,N/2)
X = pds.dft(Y)
plt.figure(7)
plt.plot(k, Y)

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