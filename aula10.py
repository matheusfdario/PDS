# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pds

wc = np.pi/2
M = 10
m = np.arange(M+1)
h10 = pds.sinc2(m-M/2, wc)
#plt.stem(m, h10)

H10, w = pds.dtft(h10, m)

fig, ax1  = plt.subplots()
ax1.grid()
ax1.plot(w, np.abs(H10))
ax1.set_ylabel('[H(e)]))',color="C0")
ax2 = ax1.twinx()
ax2.plot(w,np.unwrap(np.angle(H10)),"C1")
ax2.set_ylabel('[angle]',color='C1')
plt.show()