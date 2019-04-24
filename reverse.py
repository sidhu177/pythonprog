# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:50:56 2019

taken from Data Structures and Algorithms using Python, Lee and Hubbard, Springer
"""

def revList(lst):
    accumulator = []
    for x in lst:
        accumulator = [x] + accumulator
        
    return accumulator

def main():
    print(revList([1,2,3,4]))
    
if __name__=="__main__":
    main()