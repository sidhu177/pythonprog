# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 22:46:32 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

def inplace_quick_sort(S,a,b):
    if a>=b:
        return
    pivot = S[b]
    left = a
    right = b-1
    while left<=right:
        while left<=right and S[left] < pivot:
            left +=1
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left],S[right] = S[right], S[left]
            left, right = left+1, right-1
            
    S[left],S[b] = S[b], S[left]
    inplace_quick_sort(S, a, left-1)
    inplace_quick_sort(S, left+1,b)