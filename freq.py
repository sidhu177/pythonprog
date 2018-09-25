# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 22:03:50 2018

Taken from Data Structures and Algorithms using Python

@author: SIDHARTH
"""

filename = open("c:/Users/SIDHARTH/Python/pythonprog/freq.txt", "rb").read()
freq = {}
for piece in open(filename).read().lower().split:
    word = ''.join(c for c in piece if c.isalpha())
    if word:
        freq[word] = 1+freq.get(word,0)
        
max_word = ''
max_count = 0
for (w,c) in freq.items():
    if c>max_count:
        max_word = w
        max_count = c
print('The most frequent word is ', max_word)
print('Its number of occurances is ', max_count)
