# -*- coding: utf-8 -*-
"""
Created on Mon May  1 22:56:07 2017

@author: Devlin
"""

## Game of Threes ##
### Challenge: EASY
### https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/

# Take an input number
# IF divisble by threem divide by three, otherwise add or subtract one to make it divisible by three
# Game ends at 1

import time as t

print('This is the game of three\'s')
print('Taking a starting number, we either divide by three or add/subtract 1 to make it divisible by three')
print('You can give us the input')
number = int(input('> '))
turns = 0
start = t.time()


while number != 1:
    if number % 3 == 0:
        turns += 1
    elif number % 3 == 1:
        number -= 1
        turns += 1
    elif number % 3 == 2:
        number += 1
        turns += 1
    number /= 3

end = t.time()
duration = end - start
        
print('%d turns' %turns)
print('%d seconds' %duration)