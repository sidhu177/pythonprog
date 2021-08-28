# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 23:45:22 2019

Color Plot example taken from Designing Machine Learning Systems with Python by David Julian, Pakt publishing
"""

import numpy as np
import matplotlib.pyplot as plt

N = 10000
x = np.random.rand(N)
y = np.random.rand(N)
colors = ('r','b','g')
area = np.pi*(10*np.random.rand(N))**2
plt.scatter(x,y,s=area,c=colors,alpha=0.5)
plt.show()