# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 22:22:18 2018

Taken from Data Structures and Algorithms using Python text book...

@author: sid
"""

def shortest_path_tree(g,s,d):
    tree = {}
    for v in d:
        if v is not s:
            for e in g.incident_edges(v,False):
                u = e.opposite(v)
                wgt = e.element()
                if d[v] == d[u] + wgt:
                    tree[v] = e
    return tree
