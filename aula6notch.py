# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:59:18 2023

@author: DAELN
"""
import pds
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

def find_c(f,r):
    c = (1 - (1 + r**2)*np.cos(2*np.pi*f2) + r**2)/(2 - 2*np.cos(2*np.pi*f2)) 
    return c
    
y = np.load('123test_noisy.npy')

Fs = 8192

#sd.play(y, Fs, blocking=True)

r = .99

f1 = 500

f2 = 3000

#c1 = find_c(f1,r)
#b1 = [(1 - (1 + r**2)*np.cos(2*np.pi*f1) + r**2)*1,(1 - (1 + r**2)*np.cos(2*np.pi*f1) + r**2)*-2*np.cos(2*np.pi*f1),(1 - (1 + r**2)*np.cos(2*np.pi*f1) + r**2)*1]
#a1 = [(2 - 2*np.cos(2*np.pi*f1))*1,(2 - 2*np.cos(2*np.pi*f1))*-1*np.cos(2*np.pi*f1)*(1+r**2),(2 - 2*np.cos(2*np.pi*f1))*r**2]
w1 = (2*np.pi*f1)/Fs
b1 = [1,-2*np.cos(w1),1]
a1 = [1,-1*(1+r**2)*np.cos(w1),r**2]
w, H = pds.freqz(b1,a1)
plt.plot(w,np.abs(H))
x1 = pds.lfilter(b1, a1, y)

#c2 = find_c(f2,r)
#b2 = [(1 - (1 + r**2)*np.cos(2*np.pi*f2) + r**2)*1,(1 - (1 + r**2)*np.cos(2*np.pi*f2) + r**2)*-2*np.cos(2*np.pi*f2),(1 - (1 + r**2)*np.cos(2*np.pi*f2) + r**2)*1]
#a2 = [(2 - 2*np.cos(2*np.pi*f2))*1,(2 - 2*np.cos(2*np.pi*f2))*-1*np.cos(2*np.pi*f2)*(1+r**2),(2 - 2*np.cos(2*np.pi*f2))*r**2]
w2 = (2*np.pi*f2)/Fs
b2 = [1,-2*np.cos(w2),1]
a2 = [1,-1*(1+r**2)*np.cos(w2),r**2]
x2 = pds.lfilter(b2, a2, x1)

sd.play(x2, Fs, blocking=True)