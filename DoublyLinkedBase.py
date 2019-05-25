# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 21:05:48 2018

Taken from Data structures and Algorithms using Python by T.Goodrich et al.
"""

class _DoublyLinkedBase:
    
    class _Node:
        __slots__ = '_element','_prev','_next'
        def __init__(self,element,prev,next):
            self._element = element
            self._prev = prev
            self._next = next
    
    def __init__(self):
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
        
    def _insert_between(self,e,predecessor,successor):
        newest = self._Node(e,predecessor,successor)
        predecessor._next = newest
        successor._prev = newest
        self._size +=1
        return newest
        
    def _delete_node(self,node):
        predeccesor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element
        
