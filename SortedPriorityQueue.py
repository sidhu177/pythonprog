# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 21:06:14 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()
    
    def __len__(self):
        return len(self._data)
        
    def add(self,key,value):
        newest = self._Item(key,value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk,newest)
            
    def min(self):
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        p = self._data.first()
        item = p.element()
        return (item._key,item._value)
        
    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        item =self._data.delete(self._data.first())
        return (item._key, item._value)