# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:47:45 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

def merge(S1,S2,S):
    while not S1.is_empty() and not S2.is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(s2.dequeue())
    while not S1.is_empty():
        S.enqueue(S1.dequeue())
    while not S2.is_empty():
        S.enqueue(S2.dequeue())
        
def merge_sort(S):
    n = len(S)
    if n<2:
        return
    S1 = LinkedQueue()
    S2 = LinkedQueue()
    while len(S1)<n//2:
        S1.enqueue(S.dequeue())
    while not S.is_empty():
        S2.enqueue(S.dequeue())
    
    merge_sort(S1)
    merge_sort(S2)
    merge_sort(S1,S2,S)
    