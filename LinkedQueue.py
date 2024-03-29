# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 21:34:26 2018

Taken from Data Structures and Algorithms using Python text book.
"""

class LinkedQueue:
    class _Node:
        __slots__='_element','_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        return self._self
        
    def is_empty(self):
        return self._self == 0
        
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element
        
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head.element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
        
    def enqueue(self,e):
        newest = self._Node(e,None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1