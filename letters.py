# -*- coding: utf-8 -*-
"""
Created on Sun May 14 22:32:13 2017

@author: Devlin
"""

## Letter use frequency in enable1.txt

import collections as c
import matplotlib.pyplot as plt
import string
from numpy import mean

values = open('D:\Files\Psdir\enable1.txt').readlines()

words = []
for i in range(0, len(values)-1):
    words.append(values[i].rstrip())

letters = []
for w in words:
    for l in list(w):
        letters.append(l)

letters_count = c.Counter(letters)

l_xs = []
l_ys = []
print('Letters Raw Distribution')
for key in sorted(letters_count):
    print('{}: {}'.format(key, letters_count[key]))
    l_xs.append(key)
    l_ys.append(letters_count[key])
print('Mean Count: {}'.format(round(mean(list(letters_count.values()))), 0))

print('\nPercent Frequency')
freq_sum = 0
for key in sorted(letters_count):
    print('{}: {}%'.format(key, round((letters_count[key]/len(letters))*100, 2)))
    freq_sum += round((letters_count[key]/len(letters))*100, 2)
    
print('Mean Frequency: {}%'.format(round(freq_sum / 26), 4))

l_nxs = list(range(1,27))
all_letters = list(string.ascii_uppercase)

count_tuples = sorted(letters_count.items())
count_list = [l[1] for l in count_tuples]
sorted_letters = []
for i in sorted(count_list):
    for t in count_tuples:
        if i in t:
            sorted_letters.append(t[0].upper())
        else:
            pass

# Alphabetized Point Distribution
plt.bar(l_nxs, l_ys, align = 'center')
plt.xticks(l_nxs, all_letters)
plt.title('Alphabetized Letter Distribution in enable1.txt')
plt.ylabel('Count')
plt.xlabel('Letters')
plt.show()

# Sorted Letter Distribution
plt.bar(l_nxs, sorted(count_list), align = 'center')
plt.xticks(l_nxs, sorted_letters)
plt.title('Sorted Letter Distribution in enable1.txt')
plt.ylabel('Count')
plt.xlabel('Letters')
plt.show()

## Lets see if scrabble points line up
scrabble = {}
for l in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']:
    scrabble[l] = 1
for l in ['D', 'G']:
    scrabble[l] = 2
for l in ['B', 'C', 'M', 'P']:
    scrabble[l] = 3
for l in ['F', 'H', 'V', 'W', 'Y']:
    scrabble[l] = 4
scrabble['K'] = 5
for l in ['J', 'X']:
    scrabble[l] = 8
for l in ['Q', 'Z']:
    scrabble[l] = 10

scrabble_tuples = sorted(scrabble.items())
scrabble_points = [l[1] for l in scrabble_tuples]  

sorted_points = []
for l in sorted_letters:
    for r in scrabble_tuples:
        if l in r:
            sorted_points.append(r[1])

# Sorted Scrabble Point Distribution
plt.bar(l_nxs, sorted_points, align = 'center')
plt.xticks(l_nxs, sorted_letters)
plt.title('Sorted Point Distribution in Scrabble')
plt.ylabel('Count')
plt.xlabel('Letters')
plt.figtext(.26, -0.01, 'Sorting based on frequency in enable1.txt')
plt.show()

# Alphabetized Scrabble Point Distribution
plt.bar(l_nxs, [i[1] for i in scrabble_tuples], align = 'center')
plt.xticks(l_nxs, [i[0] for i in scrabble_tuples])
plt.xlabel('Letters')
plt.ylabel('Count')
plt.title('Alphabetized Point Distribution in Scrabble')
plt.show()

## They don't quite line up properly
## J is worth less points than it should be and z is worth more points than it should be
## U is worth too little
## C is worth too much