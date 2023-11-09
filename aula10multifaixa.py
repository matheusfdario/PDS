# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:58:29 2023

@author: DAELN
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pds

M = 60
m = np.arange(M+1)
w = np.arange(1,6)*np.pi/5
A = [1,3,5,4,2] 

h = pds.multifaixa(A,w,M)
H, w = pds.dtft(h,m,np.linspace(0, np.pi, 1024))



#w5 = np.pi
#w4 = 4*np.pi/5
#h = pds.sinc2(m-M/2, w4)#- pds.sinc2(m-M/2, w5)
#H, w = pds.dtft(h,m,np.linspace(0, np.pi, 1024))

fig, ax1  = plt.subplots()
ax1.grid()
ax1.plot(w, np.abs(H))
