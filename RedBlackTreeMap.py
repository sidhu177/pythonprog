# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:11:33 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

class RedBlackTreeMap(TreeMap):
    class _Node(TreeMap._Node):
        __slots__ = '_red'
        
        def __init__(self,element,parent=None,left=None, right=None):
            super().__init__(element,parent,left,right)
            self._red = True
            
        def _set_red(self,p): p._node._red = True
        def _set_black(self,p): p._node._red = False
        def _set_color(self,p,make_red): p._node._red = make_red
        def _is_red(self,p): return p is not None and p._node._red
        def _is_red_leaf(self,p): return self._is_red(p) and self.is_leaf(p)
            
        def _get_red_child(self,p):
            for child in (self.left(p), self.right(p)):
                if self._is_red(child):
                    return child
            return None
            
        def _rebalance_insert(self,p):
            self._resolve_red(p)
            
        def _resolve_red(self,p):
            if self.is_root(p):
                self._set_black(p)
            else:
                parent = self.parent(p)
                if self._is_red(parent):
                    uncle = self.sibling(parent)
                    if not self._is_red(uncle):
                        middle = self._restructure(p)
                        self._set_black(middle)
                        self._set_red(self.left(middle))
                        self._set_red(self.right(middle))
                    else:
                        grand = self.parent(parent)
                        self._set_red(grand)
                        self._set_black(self.left(grand))
                        self._set_black(self.right(grand))
                        self._resolve_red(grand)
                        
            
            
        
