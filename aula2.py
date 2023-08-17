# -*- coding: utf-8 -*-
"""
Spyder Editor

Autor: Matheus Fortunato Dário.
Criação: 17/08/2023.
1. Implementar a eq. a diferenças.
2. Calcular numericamente respostas ao impolso.
"""

import numpy as np
import matplotlib.pyplot as plt
import pds

# Média Móvel
M = 5
n = np.arange(-3,10)
x = pds.delta(n)
b = np.ones(M+1)/(M+1)
a = np.ones(1)
h_ref = pds.lfilter(b, a, x)
h = pds.eqdif(b, a, x)
plt.figure(1)
plt.stem(n,h_ref)
plt.figure(2)
plt.stem(n,h)

print("RES1:",pds.mse(h_ref, h))

#Sistema IIR
b = np.ones(1)
a = np.array([1,.5])
h_ref = pds.lfilter(b, a, x)
h = pds.eqdif(b, a, x)
plt.figure(3)
plt.stem(n,h_ref)
plt.figure(4)
plt.stem(n,h)
print("RES2:",pds.mse(h_ref, h))