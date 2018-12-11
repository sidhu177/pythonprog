# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 21:33:21 2018

Taken from Data Structures and Algorithms using Python text book...

@author: sid
"""

def MST_Kruskal(g):
    tree = []
    pq = HeapPriorityQueue()
    forest = Partition()
    position = {}
    
    for v in g.vertices():
        position[v] = forest.make_group(v)
        
    for e in g.edges():
        pq.add(e.element(),e)
        
    size = g.vertex_count()
    while len(tree)!=size-1 and not pq.is_empty():
        weight, edge = pq.remove_min()
        u,v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a!=b:
            tree.append(edge)
            forest.union(a,b)