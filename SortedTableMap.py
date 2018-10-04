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