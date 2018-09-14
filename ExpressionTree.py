# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 22:38:14 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

class ExpressionTree(LinkedBinaryTree):
      
      def __init__(self,token,left=None,right=None):
          
          super().__init__()
          if not isinstance(token, str):
              raise TypreError('Token must be a string')
          self._add_root(token)
          if left is not None:
              if token not in '+-*x/':
                  raise ValueError('token must be valid operator')
              self._attach(self.root(),left,right)
                 
      def __str__(self):
          pieces = []
          self._parenthesize_recur(self.root(),pieces)
          return ''.join(pieces)
          
      def _parenthesize_recur(self,p,result):
          if self.is_leaf(p):
              result.append(str(p.element()))
          else:
              result.append('(')
              self._parenthesize_recur(self.left(p),result)
              result.append(p.element())
              self._parenthesize_recur(self.right(p),result)
              result.append(')')
              
