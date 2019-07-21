# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 21:09:23 2018

Taken from Data Structures and Algorithms using Python
"""

def shortest_path_lengths(g,src):
    d = {}
    cloud = {}
    pq = AdaptableHeapPriorityQueue()
    pqlocator = {}
    
    for v in g.vertices():
        if v is src:
            d[v]=0
        else:
            d[v] = float('inf')
        pqlocator[v] = pq.add(d[v],v)
        
    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u]=key
        del pqlocator[u]
        for e in g.incident_edges(u):
            v = e.opposite(u)
            if v not in cloud:
                wgt = e.element()
                if d[u] + wgt<d[v]:
                    d[u] = d[u]+wgt
                    pq.update(pqlocator[v],d[v],v)
                    
