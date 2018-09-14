# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 22:24:17 2018

Recursive Binary search taken from Data Structures and Algorithms in Python 

@author: SIDHARTH
"""

def binary_search(data, target, low, high):
    if low>high:
        return False
    else:
        mid = (low+high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)
