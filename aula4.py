# -*- coding: utf-8 -*-
"""
Spyder Editor

Autor: Matheus Fortunato Dário.
Criação: 10/08/2023.
"""
from scipy.signal import residuez 
import numpy as np
import matplotlib.pyplot as plt
import pds

b = (0, -10, 2)
a = (1, -3, 2)

r, p , k = residuez(b,a)

n = np.arange(-3,10)
h_a = 2*pds.u(n) + 3*2.**n*pds.delta(n)

h_n = pds.lfilter(b,a,pds.delta(n))

plt.stem(n,h_a)
plt.show()

print(pds.mse(h_a,h_n))