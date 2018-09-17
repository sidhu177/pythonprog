# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 21:56:41 2018

Taken from Data structures and Algorithms using Python by T.Goodrich et al

@author: SIDHARTH
"""

if __name__=='__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman','California Savings','5391037593875709',2500))
    wallet.append(CreditCard('John Bowman','California Federal','3485039933951954',3500))
    wallet.append(CreditCard('John Bowman','California Finance','5391037593875309',5000))
    
    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
        
    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance()>100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        print()
        
        
