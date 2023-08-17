# -*- coding: utf-8 -*-
"""
Spyder Editor

Autor: Matheus Fortunato Dário.
Criação: 17/08/2023.
"""

import numpy as np
import matplotlib.pyplot as plt
import pds

n = np.arange(0,31)     #Gera um vetor de numpy com 31 posições, de 0 até 30.
w0 = (np.pi)/10     
x = np.cos(w0*n)
plt.figure()
plt.stem(n, x)
plt.figure()
plt.stem(n,pds.delta(n))
plt.figure()
plt.stem(n,pds.u(n))
