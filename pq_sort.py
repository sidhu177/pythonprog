# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 22:44:13 2018

Taken from Data Structure and Algorithms using Python 

Following program is a sorting method for a collection of elements stored in a list

@author: SIDHARTH
"""
def pq_sort(C):
    n = len(C)
    P = PriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        P.add(element,element)
    for j in range(n):
        (k,v) = P.remove_min()
        C.add_last(v)
        
        
       