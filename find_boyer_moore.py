# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 22:12:30 2018

Taken from Data Structures and Algorithms using Python
"""

def find_boyer_moore(T,P):
    n, m = len(T), len(P)
    if m ==0:
        return 0
    last = {}
    for k in range(m):
        last[P[k]] = k
    i = m-1
    k = m-1
    while i<n:
        if T[i]==P[k]:
            if k==0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j=last.get(T[i],-1)
            i += m-min(k,j+1)
            k = m-1
    return -1
            
