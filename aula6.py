# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np
import matplotlib.pyplot as plt
import pds

beta = 0.2
alpha = 0.8

# Analítico
def H(w, beta, alpha):
    return beta/(1-alpha*np.exp(-1j*w))

W = 1024 
w = np.linspace(-np.pi, np.pi, 1024)
Ha = H(w,beta,alpha)
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(w,np.abs(Ha),'tab:blue')
ax2.plot(w,np.angle(Ha),'black')
ax1.grid(True, axis='both')

# Analítico 2
a = [1,-alpha]
b = [beta]

def H(w, beta, alpha):
    return beta/(1-alpha*np.exp(-1j*w))

W = 1024 
w , Ha2 = pds.freqz(b,a,W,whole=True)
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(w,np.abs(Ha2),'tab:blue')
ax2.plot(w,np.angle(Ha2),'black')
ax1.grid(True, axis='both')


# Numérico
n = np.arange(100)
w0 = 0.1*np.pi
x = np.cos(w0*n)
y = pds.lfilter(b,a,x)
plt.figure()
plt.plot(n,x,'.-b',n, y,'.-k')