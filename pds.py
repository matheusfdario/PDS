# -*- coding: utf-8 -*-
"""
Spyder Editor

Autor: Matheus Fortunato Dário.
Criação: 10/08/2023.
"""
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter,freqz

def mse(x, y):          # diferença média quadrática
    return np.mean(np.abs(x-y)**2)    

def delta(n):           #função do impulso discreto
    return 1.*(n==0)
def u(n):               #função do degrau unitário
    return 1.*(n>=0)
def eqdif(b, a, x):
    y = np.zeros_like(x)    #cria variável para saída
    M = len(b)
    N = len(a)
    for n in range(len(y)):
        for kb in range(M):    
            if((n-kb)>=0):
                y[n] += b[kb]*x[n-kb]
        for ka in range(1,N):
            if((n-kb)>=0):
                y[n] += -1*(a[ka]*y[n-ka]) 
    return y

def dtft(x, n, w=np.linspace(-np.pi,np.pi,1024)):
    X=np.zeros(len(w),dtype=complex)
    for k in range(len(w)):
        for i in range(len(n)):
            X[k] += x[i]*np.exp(-1j*w[k]*n[i])
            
    return x

def dftmtx(N):
    n = np.arange(N).reshape(N,1)
    return np.exp(-1j*2*np.pi/N)**(n@n.T)

def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    W = np.exp(-1j*2*np.pi/N)
    for k in range(N):
        for i in range(N):
            #X[k] += x[i]*W[i]**
            X[k] += x[i]*W**(k*i)
    return X 

def fft(x):
    N = len(x)
    
    if N > 1:
        X = np.zeros(N, dtype=complex)
        W = np.exp(-1j*2*np.pi/N)
        xe = x[:-1:2]
        xo = x[1::2]
        Xe = fft(xe)
        Xo = fft(xo)
        k = np.arange(N/2, dtype=int)
        X[k] = Xe[k]+(W**k)*Xo[k]
        X[k+ round(N/2)] = Xe[k]-(W**k)*Xo[k]
        return X
    else:
        return x
    