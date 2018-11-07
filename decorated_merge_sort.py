# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 21:08:30 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

def decorated_merge_sort(data, key=None):
    if key is not None:
        for j in range(len(data)):
            data[j] = _Item(key(data[j]),data[j])
    merge_sort(data)
    if key is not None:
        for j in range(len(data)):
            data[j] = data[j]._value
    