# -*- coding: utf-8 -*-
"""
Taken From Data Structures and Algorithms using Python
"""

class PriorityQueueBase:
    class _Item:
        __slots__='_key','_value'
        def __init__(self,k,v):
            self._key = k
            self._value = v
            
        def __It__(self,other):
            return self._key<other._key
            
        def is_empty(self):
            return len(self)==0
            
