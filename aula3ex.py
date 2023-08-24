# -*- coding: utf-8 -*-
"""
Spyder Editor

Autor: Matheus Fortunato Dário.
Criação: 24/08/2023.

"""

import numpy as np
import matplotlib.pyplot as plt
import pds

n = np.arange(-10,31)
w1 = np.pi/10   #freq [amostra]
p = 100
w1 = round(w1*p)/p
x1 = np.cos(w1*n)

w2 = w1 + 2*np.pi*7
x2 = np.cos(w2*n)

plt.figure(1)
plt.stem(n,x1)

plt.figure(2)
plt.stem(n,x2)

print(pds.mse(x1,x2))
