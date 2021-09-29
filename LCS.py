# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 23:12:03 2018

Taken from Data Structures and Algorithms using Python
"""

def LCS(X,Y):
    n,m = len(X), len(Y)
    L = [[0]*(m+1) for k in range(n+1)]
    for j in range(n):
        for k in range(m):
            if X[j] == Y[k]:
                L[j+1][k+1] = L[j][k] + 1
            else:
                L[j+1][k+1] = max(L[j][k+1],L[j+1][k])
    return L