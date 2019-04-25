# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:17:16 2019


taken from Data Structures and Algorithms using Python, Lee and Hubbard, Springer
"""

class PyList:
    def __getitem__(self,index):
        if index >= 0 and index < self.numItems:
            return self.items[index]
        raise IndexError("Pylist index out of range")
        
    def __setitem__(self,index,val):
        if index >= 0 and index < self.numItems:
            self.items[index] = val
            return 
        
        raise IndexError("Pylist assignment index out of range")
        
            