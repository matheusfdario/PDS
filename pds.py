# -*- coding: utf-8 -*-
"""
Spyder Editor

Autor: Matheus Fortunato Dário.
Criação: 10/08/2023.
"""

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