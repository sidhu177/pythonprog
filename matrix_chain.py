# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 22:31:07 2018

Taken from Data Structures and Algorithms using Python
"""

def matrix_chain(d):
    n = len(d) - 1
    N =[[0]*n for i in range(n)]
    for b in range(1,n):
        for i in range(n-b):
            j = i+b
            N[i][j] = min(N[i][j]+N[k+1][j]+d[i]*d[k+1]*d[j+1] for k in range(i,j))
    return N
