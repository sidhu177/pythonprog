# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 22:47:14 2018

@author: SIDHARTH
"""

class Progression:
    def __init__(self,start=0):
        self._current = start
        
    def _advance(self):
        self._current +=1
        
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
            
    def __iter__(self):
        return self
        
    def print_progression(self,n):
        print(' '.join(str(next(self)) for j in range(n)))
        