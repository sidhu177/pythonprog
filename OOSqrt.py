# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 17:33:07 2018

Taken from Python 3 Object Oriented Programming  by Dusty Phillips, Apress

@author: SIDHARTH
"""

import math

class Point:
    def move(self, x,y):
        self.x = x
        self.y = y
        
    def reset(self):
        self.move(0,0)
        
    def calculate_distance(self,other_point):
        return math.sqrt((self.x-other_point.x)**2+(self.y - other_point.y)**2)
        

    
    
    
    
