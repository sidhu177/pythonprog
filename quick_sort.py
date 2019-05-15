# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 22:21:17 2018

Taken from Data Structures and Algorithms using Python
"""

def quick_sort(S):
    n = len(S)
    if n<2:
        return
    P = S.first()
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    while not S.is_empty():
        if S.first() < P:
            L.enqueue(S.dequeue())
        elif P<S.first():
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())
    quick_sort(L)
    quick_sort(G)
    while not L.is_empty():
        S.enqueue(l.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())
        
