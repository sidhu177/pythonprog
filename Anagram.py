# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 23:15:50 2019

Creating list of Anagrams from a given word taken from Impractical Python Projects by Lee Vaughan Published by No Starch Press

@author: sid ramesh
"""

import sys

file = 'C:/Users/Sidra/Downloads/WordList.txt'

def load(file):
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split('\n')
            loaded_text = [x.lower() for x in loaded_text]
            return loaded_text
    except IOError as e:
        print("{}\n Error opening {}. Terminating Program.".format(e,file),file=sys.stderr)
        sys.exit(1)
        
word_list = load(file)
anagram_list = []
name = 'one'
name = name.lower()
##print("Input name = {}".format(name))
##print("Using name = {}".format(name))
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word!=name:
        if sorted(word)==name_sorted:
            anagram_list.append(word)

total_anagrams = len(anagram_list)
print("total anagrams found ", total_anagrams)
if len(anagram_list)==0:
    print("\n you need a bigger dictionary")
else:
    print("Anagrams =", *anagram_list, sep='\n')
    
