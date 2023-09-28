# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np
import pds
np.set_printoptions(precision=3, suppress=True)

N = 4
n = np.arange(N)
x = n

X = pds.dft(x)
print(X,"\n")

#xinv = (1/N)*np.conj(W)@X
#print(xinv)

N = 8
n = np.arange(N)
x = 5 + 2*np.cos(np.pi/2*n)
X = pds.dft(x)
print(X,"\n")


N = 12
n = np.arange(N)
x = 1 + 3*np.cos(np.pi/3*n) + np.sin(5*np.pi/6*n)
X = pds.dft(x)
print(X,"\n")

