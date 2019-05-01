# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 21:46:48 2018

Taken from Data Structures and Algorithms using Python
"""

def merge(S1, S2, S):
    i=j=0
    while i+j<len(S):
        if j==len(S2)or(i<len(S1)and S1[i]<S2[j]):
            S[i+j]=S1[i]
            i +=1
        else:
            S[i+j]=S2[j]
            j += 1
            
            
