# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 12:13:02 2018

@author: Devlin
"""

## Drinks Ingredient Counter

import collections as c
import matplotlib.pyplot as plt
import csv

drinks_lol = list(csv.reader(open('D:\Files\Psdir\drinks.csv')))
drinks_list = [d[0] for d in drinks_lol]

drinks_counted = c.Counter(drinks_list)

drinks_items = list(drinks_counted.items())
drinks_sorted = sorted(drinks_items, key = lambda x: x[1]) 
   

ingredients = [i[0] for i in drinks_sorted[-50:]]
ingredients_enum = [e for e, i in enumerate(ingredients)]
counts = [i[1] for i in drinks_sorted[-50:]]

plt.figure(figsize = (6,10))
plt.barh(ingredients_enum, counts)
plt.ylabel('Drink Ingredient')
plt.yticks(ingredients_enum, ingredients)
plt.xlabel('Count')
plt.title("Distribution of drink ingredients in the '12 Bottle Bar'")
plt.grid()
plt.show()