# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 23:42:10 2018

@author: SIDHARTH
"""

def recursiveSum(n):
    if n== 0:
        return 0
    else:
        return recursiveSum(n-1) + n
        
def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
        
def main():
    x = int(input("Please enter a non-negetive integer: "))
    s = recursiveSum(x)
    n = int(input("Please enter a non-negetive power index: "))
    print("The sum of the first",x,"integers is ", str(s)+".")
    q = power(x,n)
    print("The power result",str(q)+".")
    
    
if __name__ == "__main__":
    main()