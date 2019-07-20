# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 22:10:35 2018

Taken from Data Structures and Algorithms using Python
"""

def merge_sort(S):
    n = len(S)
    if n<2:
        return 
    mid = n//2
    S1 = S[0:mid]
    S2 = S[mid:n]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1,S2,S)
