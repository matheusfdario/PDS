# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal.windows as wndws
import pds

wc = np.pi/2
M = 40
m = np.arange(M+1)
hrec = pds.sinc2(m-M/2, wc)
Hrec, w = pds.dtft(hrec,m,np.linspace(0,np.pi,1024))

hHan = wndws.hann(M+1)*pds.sinc2(m-M/2,wc)
HHan, w = pds.dtft(hHan,m,np.linspace(0,np.pi,1024))

fig, ax1  = plt.subplots()
ax1.grid()
ax1.plot(w, np.abs(Hrec),w, np.abs(HHan))