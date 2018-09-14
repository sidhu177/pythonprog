# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 22:38:23 2018

Taken from Data Structures and Algorithms using Python 

@author: SIDHARTH
"""

class EulerTour:
    def __init__(self,tree):
        self.tree = tree
        
    def tree(self):
        return self.tree
        
    def execute(self):
        if len(self._tree)>0:
            return self._tour(self._tree.root(),0,[])
            
    def _tour(self,p,d,path):
        self._hook_previsit(p,d,path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c,d+1,path))
            path[-1]+=1
        path.pop()
        answer = self._hook_postvist(p,d,path,results)
        return answer
        
    def _hook_previsit(self,p,d,path):
        pass
    
    def _hook_postvisit(self,p,d,path,results):
        pass