# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:09:15 2023

Repetir Exemplo 3 dos slides 12-fir_win.pdf
alternado-se o ganho da primeira faixa de
0.02 para 0.005

"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal.windows as wndws
import pds

wp = 0.78*np.pi
ws = 0.7*np.pi
wc = (wp+ws)/2
Dw = wp - ws

Ap = 0
As = 0.005
d = Ap - As

dp = (10**(As/20)-1)/(10**(As/20)+1)
ds = 10**(-As/20)

a = -20*np.log10(d)

M, beta = pds.kaiserord(a,Dw)

m = np.arange(M+1)
h = (np.sin(0.74*(m-M/2)))/(np.pi*(m-M/2)) - (np.sin(0.25*(m-M/2)))/(np.pi*(m-M/2))
Hkaiser, w = pds.dtft(h,m,np.linspace(0,np.pi,2048))


A = [0,1,0]

#w = np.arange(1,3)*np.pi/5

h = pds.multifaixa(A,w,M)
H, w = pds.dtft(h,m,np.linspace(0, np.pi, 2048))

fig, ax1  = plt.subplots()
ax1.grid()
ax1.plot(w, np.abs(Hkaiser))

ax1.plot([wp,wp],[0,1-dp])
ax1.plot([0,wp],[1+dp,1+dp])
ax1.plot([0,wp],[1-dp,1-dp])

ax1.plot([ws,ws],[ds,1])
ax1.plot([ws,np.pi],[ds,ds])
