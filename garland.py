# -*- coding: utf-8 -*-
"""
Created on Thu May 11 21:23:20 2017

@author: Devlin
"""

## Garland Words ##
### Challenge: EASY
### https://www.reddit.com/r/dailyprogrammer/comments/3d4fwj/20150713_challenge_223_easy_garland_words/

# Garland words start and end with the same letters
# The number of same letters determined order
# i.e onion is order 2
#     ceramic is order 1
#     alfalfa is order 4

import time as t
import matplotlib.pyplot as plt

values = open('D:\Files\Psdir\enable1.txt').readlines()

words = []
for i in range(len(values)):
    words.append(values[i].rstrip())
    
def garland(word, print_reps = False,  rep = 10):
    '''
    set print_reps = True to print the garland string
    set reps = number of times to repeat the word in the string
    the garland string is kinda broken; sometimes works, sometimes doesnt
    Garland order is sometimes broken too,
    Alfalfa returns 5 instead if 4, kind of a bummer
    '''
    order = 0
    for i in range(len(word)):
        if word[:i] == word[-i:]:
            order += i
    
    if print_reps == True:
        print((word[:len(word) - order] * rep) + word[-order:])
    
    return order

garlands = [(w, garland(w)) for w in words]
    
start = t.time()
garland_orders = [g[1] for g in garlands]
garland_max = max(garland_orders)
garland_max_words = [g[0] for g in garlands if g[1] == garland_max]
end = t.time()
duration = end - start

print('The max garland order in enable1.txt is ' + str(garland_max))
for i in garland_max_words:
    print(i)
print('Duration: {}'.format(duration))

garland_plot = [(len(g[0]), g[1]) for g in garlands]
g_ys = [i[0] for i in garland_plot]
g_xs = [i[1] for i in garland_plot]

plt.scatter(g_ys, g_xs)
plt.xlabel('Word Length')
plt.ylabel('Garland Order')
plt.title('Garland Order compared to Word Length')
plt.show()


