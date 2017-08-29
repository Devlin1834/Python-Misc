# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:27:26 2017

@author: Devlin
"""

## Lucky Numbers ##
### Challenge: EASY
### https://www.reddit.com/r/dailyprogrammer/comments/6wjscp/2017828_challenge_329_easy_nearest_lucky_numbers/

# Lucky numbers are started with a list of positive numbers begining with 1, and removing numbers at
# intervals dictated by the next number in the sequence

def lucky(number, lrange = 100):
    lucky = list(range(1, lrange+1))
    del lucky[lucky[0]::lucky[0]+1]
    seive = 1
    
    while lucky[seive] <= lrange/2:
        del lucky[lucky[seive]-1::lucky[seive]]
        seive += 1
    
    for i in lucky:
        if i < number:
            pass
        if i > number:
            nearest = (lucky[lucky.index(i)-1], i)
            break
    
    return lucky, nearest
