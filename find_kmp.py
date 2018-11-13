# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:26:48 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

def find_kmp(T,P):
    n,m = len(T), len(P)
    if m==0:
        return 0
    fail = compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        if T[j] == P[k]:
            if k == m-1:
                return j-m+1
            j += 1
            k += 1
        elif k> 0:
            k = fail[k-1]
        else:
            j += 1
    return -1