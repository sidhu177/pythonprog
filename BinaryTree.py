# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:42:09 2018

Taken from Data Structures and Algorithms using Python text book

@author: SIDHARTH
"""

class BinaryTree(Tree):
    def left(self,p):
        raise NotImplementedError('must be implemented by subclass')
    def right(self,p):
        raise NotImplementedError('must be implemented by subclass')
    def siblings(self,p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p==self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    def children(self,p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
            