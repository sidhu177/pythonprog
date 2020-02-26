# -*- coding: utf-8 -*-
"""
Taken from Data Structures and Algorithms using Python
"""

def DFS(g,u,discovered):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g,v,discovered)
