# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 23:21:27 2019

Functions for Forward,Backward and Central Difference
Taken from the book "A primer on Scientific Programming using Python by Springer"

"""

class Diff:
    def __init__(self,f,h=1E-5):
        self.f = f
        self.h = float(h)
        
class Forward(Diff):
    def __call__(self,x):
        f,h = self.f, self.h
        return (f(x+h) -f(x))/h
    
class Backward(Diff):
    def __call__(self,x):
        f,h = self.f, self.h
        return (f(x) - f(x-h))/h
    
class Central2(Diff):
    def __call__(self,x):
        f,h = self.f, self.h
        return (f(x+h)-f(x-h))/(2*h)
    
    