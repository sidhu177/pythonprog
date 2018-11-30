# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:05:06 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

def DFS(g,u,discovered):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g,v,discovered)