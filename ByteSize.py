# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 21:21:10 2018

@author: SIDHARTH
"""

import sys
data = []
n = int(input('Input Data range\n'))
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
    data.append(None)
    
    