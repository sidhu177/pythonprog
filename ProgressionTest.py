# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 22:05:53 2018

@author: SIDHARTH
"""

if __name__=='__main__':
    print('Default Progression:')
    Progression().print_progression(10)
    
    print('Arithmetic Progression with increment 5:')
    ArithmeticProgression(5).print_progression(10)
    
    print('Arithmetic Progression with increment 5 and start 2:')
    ArithmeticProgression(5,2).print_progression(10)
    
    print('Geometric Progression with default base:')
    GeometricProgression().print_progression(10)
    
    print('Arithmetic Progression with base 3:')
    GeometricProgression(3).print_progression(10)
    
    