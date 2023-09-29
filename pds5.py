import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

def mse(x, y):          # diferença média quadrática
    return np.mean(np.abs(x-y)**2) 
def u(n):
    return 1.*(n >= 0)

def sinc2(wc, n):
    x = np.zeros(len(n))
    x[n != 0] = np.sin(wc*n[n != 0])/(np.pi*n[n != 0])
    x[n == 0] = wc/np.pi
    return x

def dtft(x,n,w = np.linspace(-np.pi,np.pi,1024)):
    X = np.zeros(len(w),dtype=complex)
    for k in range(len(w)):
        for i in range(len(n)):
            X[k]+=x[i]*np.exp(-1j*w[k]*n[i])
    return X

