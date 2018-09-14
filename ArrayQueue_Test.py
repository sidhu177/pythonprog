# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 21:50:32 2018

@author: SIDHARTH
"""

Q = ArrayQueue()
print('Adding element 1')
Q.enqueue(1)
print('Adding element 2')
Q.enqueue(2)
print('Adding element 3')
Q.enqueue(3)
print('printing length of Queue')
print(len(Q))
print('removing element 1')
Q.dequeue()
print('printing length of Queue')
print(len(Q))
print('Removing Element 2')
Q.dequeue()
print('Testing to see if Queue is empty')
print(Q.is_empty())
print('Removing Element 3')
Q.dequeue()
print('Returning Queue Empty boolean')
print(Q.is_empty())
