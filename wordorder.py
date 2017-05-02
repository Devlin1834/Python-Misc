# -*- coding: utf-8 -*-
"""
Created on Tue May  2 17:35:55 2017

@author: Devlin
"""

## Alphabetical Order ##
### Challenge: EASY
### https://www.reddit.com/r/dailyprogrammer/comments/3h9pde/20150817_challenge_228_easy_letters_in/

# Pull words from enable.txt
# record how many are in alphabetical order

values = open('D:\Files\Psdir\enable1.txt').readlines()

words = []
for i in range(0, len(values)-1):
    words.append(values[i].rstrip())
    
order = 0
not_order = 0

for i in words:
    if i == ''.join(sorted(i)):
        order += 1
    else:
        not_order += 1
        
print('%d words are in order' %order)
print('%d words are not' %not_order)