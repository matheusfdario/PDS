# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:35:03 2023

@author: DAELN
"""
import pds
import numpy as np
x = np.array([7,5,9,3])

xe = x[:-1:2]
xo = x[1::2]

xee = xe[:-1:2]
xeo = xe[1::2]

xoe = xo[:-1:2]
xoo = xo[1::2]

#
#Xe[0] = Xee + Xeo

# Como conferência da FFT
Xe_c = pds.dft(xe)
Xo_c = pds.dft(xo)
X_c = pds.dft(x)


