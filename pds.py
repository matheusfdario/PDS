# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
Autor: Matheus Fortunato Dário.
Criação: 10/08/2023.
"""

import numpy as np
import matplotlib.pyplot as plt

def delta(n):           #função do impulso unitário
    return 1.*(n==0)
def u(n):               #função do impulso unitário
    return 1.*(n>=0)