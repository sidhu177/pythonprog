# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:56:44 2018

@author: SIDHARTH
"""

class CostPerformanceDatabase:
    def __init__(self):
        self._M = SortedTableMap()
        
    def best(self, c):
        return self._M.find_le(c)
        
    def add(self,c,p):
        other = self._M.find_le(c)
        if other is not None and other[1] >= p:
            return
        self._M[c] = p
        other = self._M.find_gt(c)
        while other is not None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_gt(c)
            
        
