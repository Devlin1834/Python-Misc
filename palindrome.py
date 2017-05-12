# -*- coding: utf-8 -*-
"""
Created on Thu May 11 23:27:06 2017

@author: Devlin
"""

## Palindromes ##
### Challenge: EASY
### https://www.reddit.com/r/dailyprogrammer/comments/3kx6oh/20150914_challenge_232_easy_palindromes/

# Find Palindromes

import collections as c
import matplotlib.pyplot as plt

values = open('D:\Files\Psdir\enable1.txt').readlines()

words = []
for i in range(0, len(values)-1):
    words.append(values[i].rstrip())
    
def palindrome(word):
    
    palindrome = [word[l] for l in range(len(word)) if word[l] == word[-1 - l]]
    
    if sorted(palindrome) == sorted(word):
        return True
    else:
        return False

all_palindromes = [p for p in words if palindrome(p)]
print('There are {} palindromes in enable1.txt'.format(len(all_palindromes)))

palindrome_len = c.Counter([len(p) for p in all_palindromes])

d_xs = list(palindrome_len.keys())
d_ys = list(palindrome_len.values())

plt.bar(d_xs, d_ys, align = 'center')
plt.xlabel('Number of Palindromes')
plt.ylabel('Word Length')
plt.title('Distribution of Palindromes over Word Length')
plt.show
