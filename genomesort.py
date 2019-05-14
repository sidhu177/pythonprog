# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 23:48:22 2019

gnomesort example from Python Algorithms by Magnus Lie Hetland
"""

def gnomesort(seq):
    i =0 
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1
