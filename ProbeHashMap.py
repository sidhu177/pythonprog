# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 22:48:31 2018

Taken from Data Structures and Algorithms using Python
"""

class ProbeHashMap(HashMapBase):
    _AVAIL = object()
    
    def _is_available(self,j):
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL
        
    def _find_slot(self,j,k):
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return (False,firstAvail)
            elif k==self._table[j].key:
                return (True,j)
            j = (j+1)%len(self._table)
            
    def _bucket_getitem(self,j,k):
        found,s = self._find_slot(j,k)
        if not found:
            raise KeyErrorr('Key Error: '+repr(k))
        return self._table[s]._value
        
    def _bucket_setitem(self,j,k,v):
        found,s = self._find_slot(j,k)
        if not found:
            self._table[s] = self._Item(k,v)
            self._n +=1
        else:
            self._table[s]._value = v
            
    def _bucket_delitem(self,j,k):
        found,s = self._find_slot(j,k)
        if not found:
            raise KeyError('Key Error: '+repr(k))
        self._table[s] = ProbeHashMap._AVAIL
        
    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key
                
