# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:48:09 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

class MultiMap:
    _MapType = dict
    
    def __init__(self):
        self._map = self._MapType()
        self._n = 0
        
    def __iter__(self):
        for k,secondary in self._map.items():
            for v in secondary:
                yield(k,v)
                
    def add(self,k,v):
        container = self._map.setdefault(k,[])
        container.append(v)
        self._n += 1
        
    def pop(self,k):
        secondary = self._map[k]
        v = secondary.pop()
        if len(secondary)==0:
            del self._map[k]
        self._n-=1
        return(k,v)
        
    def find(self,k):
        secondary = self._map[k]
        return(k,secondary[0])
        
    def find_all(self,k):
        secondary = self._map.get(k,[])
        for v in secondary:
            yield(k,v)
            
            