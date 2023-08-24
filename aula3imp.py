# -*- coding: utf-8 -*-
"""
Spyder Editor

Autor: Matheus Fortunato Dário.
Criação: 24/08/2023.

Reverberação

pip install sounddevice


alpha= 0.7

tau = 50, 100 e 500 ms

usar lfilter

"""

import numpy as np
import matplotlib.pyplot as plt
import pds
import sounddevice as sd
import scipy.signal as sci

x = np.load('123test.npy')
Fs = 8192                       # frequência de amostragem 
tau = 500e-3                    # tempo de atraso em segundos
D = round(tau*Fs)               # número de amostras (obs: s*1/s => adimensional)
alpha = 0.7                     #
sd.play(x,Fs,blocking=True)     # original
b = np.ones(1)                  # bk
a = np.zeros(D)
a[0] = 1
a[-1] = alpha
y = sci.lfilter(b,a,x)          # filtragem
sd.play(y,Fs,blocking=True)     # com ecos