# -*- coding: utf-8 -*-
"""
Created on Mon May  8 22:13:20 2017

@author: Devlin
"""

## How many words in enable1.txt are isograms?

import collections as c
import matplotlib.pyplot as plt

values = open('D:\Files\Psdir\enable1.txt').readlines()

words = []
for i in range(0, len(values)-1):
    words.append(values[i].rstrip())

isograms = []    
for w in words:
    letters = c.Counter(w)
    unique = [l for l in letters if letters[l] == 1]
    
    if sorted(w) == sorted(unique):
        isograms.append(w)

isogram_percent = round(len(isograms) / len(words), 2) * 100
print('There are %d words in enable1.txt' %len(words))            
print('And there are %d isograms' %len(isograms))
print('That means that {}% of the words in enable1.txt are isograms!'.format(isogram_percent))

## All Words ##
word_lengths = [len(w) for w in words]
length_data = c.Counter(word_lengths)

## All Isograms ##
isogram_word_lengths = [len(i) for i in isograms]  
isogram_length_data = c.Counter(isogram_word_lengths)

## Isogram Props ##
props = []
for i in isogram_length_data.keys():
    p = isogram_length_data[i] / length_data[i]
    t = (i, p)
    props.append(t)

## Raw Data ##
print('\nWords Data')
for key in sorted(length_data):
    print('{}: {}'.format(key, length_data[key]))
print('\nIsogram Data')
for key in sorted(isogram_length_data):
    print('{}: {}'.format(key, isogram_length_data[key]))
print('\nIsogram Proportions')
for t in props:
    print('{}: {}'.format(t[0], t[1]))
 
## Graphing ##
ys = list(length_data.keys())
xs = [t[1] for t in length_data.items()]

plt.bar(ys, xs, align = 'center')
plt.title('Distribution of word length in enable.txt')
plt.show()

i_ys = list(isogram_length_data.keys())
i_xs = [i[1] for i in isogram_length_data.items()]

plt.bar(i_ys, i_xs, align = 'center')
plt.title('Distribution of isogram length in enable.txt')
plt.show()
   
p_ys = [i[0] for i in props]
p_xs = [i[1] for i in props]
    
plt.bar(p_ys, p_xs, align = 'center')
plt.title('Proportion of Isograms based on Word Length')
plt.show()
