# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 20:53:44 2018

@author: SIDHARTH
"""

import matplotlib.pyplot as plt
from numpy import linspace, array
import scipy.integrate
def derv(x,time):
    a = -2.0
    b = -0.1
    return array([x[1],a*x[0]+b*x[1]])
    
time = linspace(1.0,15.0,1000)
xinitialize = array([1.05,10.2])
x = odeint(derv,xinitialize,time)
plt.figure()
plt.plot(time,x[:,0])
plt.xlabel('t')
plt.ylabel('x')
plt.show()