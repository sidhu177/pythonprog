# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 23:45:47 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

def construct_path(u,v,discovered):
    path = []
    if v in discovered:
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()
    return path