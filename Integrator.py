# -*- coding: utf-8 -*-
"""
Functions for Integration
Taken from the book "A primer on Scientific Programming using Python by Springer"

"""

class Integrator:
    def __init__(self,a,b,n):
        self.a, self.b, self.n=a,b,n
        self.points, self.weights = self.construct_method()
        
    def construct_method(self):
        raise NotImplementedError('no rule in class %s' %self.__class__.__name__)
        
    def integrate(self,f):
        s = 0
        for i in range(len(self.weights)):
            s += self.weights[i]*f(self.points[i])
        return s
