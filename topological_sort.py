# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:08:34 2018

Taken from Data Structures and Algorithms using Python text book...

@author: sidharth
"""

def topological_sort(g):
    topo = []
    ready = []
    incount = []
    for u in g.vertices():
        incount[u] = g.degree(u,False)
        if incount[u] == 0:
            ready.append(u)
    while len(ready) > 0:
        u = ready.pop()
        topo.append(u)
        for e in g.incident_edges(u):
            v = e.opposite(u)
            incount[v] -= 1
            if incount[v] == 0:
                ready.append(v)
    return topo