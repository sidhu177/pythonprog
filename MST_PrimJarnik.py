# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:05:05 2018

Taken from Data Structures and Algorithms using Python text book...

@author: sid
"""

def MST_PrimJarnik(g):
    d = {}
    tree =[]
    pq = AdaptableHeapPriorityQueue()
    pqlocator = {}
    for v in g.vertices():
        if len(d)==0:
            d[v] = 0
        else:
            d[v] = float('inf')
        pqlocator[v] = pq.add(d[v], (v,None))
        
    while not pq.is_empty():
        key,value = pq.remove_min()
        u, edge = value
        del pqlocator[u]
        if edge is not None:
            tree.append(edge)
        for link in g.incident_edges(u):
            v = link.opposite(u)
            if v in pqlocator:
                wgt = link.element()
                if wgt<d[v]:
                    d[v] = wgt
                    pq.update(pqlocator[v],d[v],(v,link))
    return tree