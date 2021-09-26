# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 22:35:34 2018

Taken from Data Structures and Algorithms using Python
"""

class SplayTreeMap(TreeMap):
    def _splay(self,p):
        while p!=self.root():
            parent = self.parent(p)
            grand = self.parent(parent)
            if grand is None:
                self._rotate(p)
            elif (parent==self.left(grand))==(p==self.left(parent)):
                self._rotate(parent)
                self._rotate(p)
            else:
                self._rotate(p)
                self._rotate(p)
                
                
    def _rebalance_insert(self,p):
        self._splay(p)
        
    def _rebalance_delete(self,p):
        if p is not None:
            self._splay(p)
            
    def _rebalance_access(self,p):
        self._splay(p)
        
        
