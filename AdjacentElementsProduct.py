# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 21:30:55 2019
"""

def adjacentElementsProduct(inputArray):
    prev = inputArray[0]
    product = prev*inputArray[1]
    for i in inputArray[1::]:
        if (prev*i>product):
            product = prev*i
            
        prev = 1
    else:
        return product
