# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:39:13 2018

Arcade game at codeSignal

@author: sidharth
"""
import math

def centuryFromYear(year):
    return (math.floor((year-1)/100) + 1)
    
    
year = 5
centuryFromYear(year)
year = 205
centuryFromYear(year)
year = 105
centuryFromYear(year)

