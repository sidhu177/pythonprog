# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 17:44:21 2018

Taken from Python 3 Object Oriented Programming by Dusty Phillips, Apress

@author: SIDHARTH
"""

point1 = Point()
point2 = Point()
point1.reset()
point2.move(5,0)
print(point2.calculate_distance(point1))
assert (point2.calculate_distance(point1) == point1.calculate_distance(point2))
point1.move(3,4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))