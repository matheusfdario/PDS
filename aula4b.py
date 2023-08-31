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

p = [np.exp(1j*np.pi/10),np.exp(-1j*np.pi/10).[0.5,-0.2, 0, 0]
a = np.poly(p)
b = [1]
n = np.arange(-3,100)
h_a = 2*pds.u(n) + 3*2.**n*pds.delta(n)

h_n = pds.lfilter(b,a,pds.delta(n))

plt.stem(n,h_n)
plt.show()
