# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 14:20:56 2023

@author: DAELN
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter
import pds

L = 10
w = np.linspace(-np.pi,np.pi,1024)
X1 = np.exp(-1j*w*(L-1)/2)
X2 = np.sin(w*L/2)/np.sin(w/2)
X = X1*X2


plt.figure(1)
plt.plot(w,np.abs(X))
plt.grid()
plt.figure(2)
plt.plot(w,np.angle(X))
plt.grid()

n = np.arange(L)
x = np.ones(L)

Xnum = pds.dtft(x,n,w)

plt.figure(3)
plt.plot(w,np.abs(Xnum))
plt.grid()
plt.figure(4)
plt.plot(w,np.angle(Xnum))
plt.grid()
plt.show()
print(pds.mse(X, Xnum))
#wc = np.pi/4
#n = np.arange(-20,21)
#x = pds.sinc2(wc,n)
#plt.figure(3)
#plt.stem(n, x)
#plt.grid()