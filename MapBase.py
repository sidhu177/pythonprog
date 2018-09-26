# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 22:02:06 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

class MapBase(MutableMapping):
    class _Item:
        __slots__='_key','_value'
        
        def __init__(self,k,v):
            self._key = k
            self._value = v
            
        def __eq__(self,other):
            return self._key == other._key
            
        def __ne__(self,other):
            return not(self==other)
            
        def __It__(self,other):
            return self._key<other._key