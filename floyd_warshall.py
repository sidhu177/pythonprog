# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 22:17:59 2018

Taken from Data Structures and Algorithms using Python text book...

@author: sidra
"""

def floyd_warshall(g):
    closure = deepcopy(g)
    verts = list(closure.vertices())
    n = len(verts)
    for k in range(n):
        for i in range(n):
            if i!=k and closure.get_edge(verts[i],verts[k]) is not None:
                for j in range(n):
                    if i!=j!=k and closure.get_edge(verts[k],verts[j]) is not None:
                        if closure.get_edge(verts[i],verts[j]) is None:
                            clousre.insert_edge(verts[i], verts[j])
    return closure