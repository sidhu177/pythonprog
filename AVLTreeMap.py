# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 22:00:05 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

class AVLTreeMap(TreeMap):
    class _Node(TreeMap._Node):
        __slots__ = '_height'
        
        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0
            
        def left_height(self):
            return self._left._height if self._left is not None else 0
            
        def right_height(self):
            return self._right._height if self._right is not None else 0
            
        def _recompute_height(self,p):
            p._node._height = 1+max(p._node.left_height(),p._node.right_height())
            
        def _isbalanced(self,p):
            return abs(p._node.left_height()-p._node.right_height()) < 1