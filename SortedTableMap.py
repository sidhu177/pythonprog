# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 22:11:43 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

class SortedTableMap(MapBase):
    def _find_index(self,k,low,high):
        if high<low:
            return high+1
        else:
            mid==(low+high)//2
            if k==self._table[mid]._key:
                return mid
            elif k< self._table[mid]._key:
                return self._find_index(k,low,mid-1)
                
    def __init__(self):
        self._table=[]
        
    def __len__(self):
        return len(self._table)
        
    def __getitem__(self,k):
        j = self._find_index(k,0,len(self._table)-1)
        if j==len(self._table) or self._table[j].key!=k:
            raise KeyError('Key Error: '+ repr(k))
        return self._table[j].value
        
    def __setitem__(self,k,v):
        j = self._find_index(k,o,len(self._table)-1)
        if j<len(self._table) and self._table[j]._key == k:
            self._table[j]._value=v
        else:
            self._table.insert(j,self._item(k,v))
            
    def __delitem__(self,k):
        j = self._find_index(k,0,len(self._table)-1)
        if j==len(self._table) or self._table[j]._key!=k:
            raise KeyError('Key Error: '+repr(k))
        self._table.pop(j)
        
    def __iter__(self):
        for item in self._table:
            yield item._key
            
    def __reversed__(self):
        for item in reversed(self._table):
            yield item._key
            
    def find_min(self):
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[-1]._value)
        else:
            return None