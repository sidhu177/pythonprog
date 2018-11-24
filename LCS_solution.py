# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 09:32:27 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

def LCS_solution(X,Y,L):
    solution = []
    j,k = len(X),len(Y)
    while L[j][k] > 0:
        if X[j-1]==Y[k-1]:
            solution.append(X[j-1])
            j -= 1
            k -= 1
        elif L[j-1][k] >= L[j][k-1]:
            j -= 1
        else:
            k -= 1
    return ''.join(reversed(solution))
    