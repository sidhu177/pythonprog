# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:52:58 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

def compute_kmp_fail(P):
    m = len(P)
    fail = [0]*m
    j = 1
    k = 0
    while j<m:
        if P[j] == P[k]:
            fail[j] = k+1
            j += 1
            k += 1
        elif k>0:
            k = fail[k-1]
        else:
            j += 1
    return fail