# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 22:22:21 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

def find_brute(T,P):
    n, m =len(T), len(P)
    for i in range(n-m+1):
        k = 0
        while k<m and T[i+k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1