# -*- coding: utf-8 -*-
"""
Created on Tue May  2 20:30:48 2017

@author: Devlin
"""

## Roman Numeral Converter
# Part 1 takes a roman numeral and converts it to a real number
# Part 2 takes a real number and converts it to a roman numeral

numbers =  [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
numerals = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

print('Type a number')
to_convert = ''
while to_convert == '':
    try:
        to_convert = int(input('> '))
    except ValueError:
        print('You actualy have to input a number for this to work')
        
def int_to_roman(convert):
    
    '''
    I realized halfway through that my lists were in the wrong order, I was too lazy to rewrite them
    so I added [::-1] to all the list calls. Its gross but my laziness knows no such taste.
    
    something about the way it calsulates roman numerals causes it to always come up one short. I added
    the += 1 and it started working PERFECTLY. no compaints here.
    
    This function takes a number and reduces it to a roman numeral. It works pretty well.
    '''
    convert += 1
    as_numerals = []

    for i in range(len(numbers)):
        if convert - numbers[::-1][i] <= 0:
            pass
        elif convert - numbers[::-1][i] > 0:
            while convert - numbers[::-1][i] > 0:
                convert -= numbers[::-1][i]
                as_numerals.append(numerals[::-1][i])
        elif convert - numbers[::-1][i] == 0:
            convert -= numbers[::-1][i]
            as_numerals.append(numbers[::-1][i])
            break
        
    print(''.join(as_numerals))
    
int_to_roman(to_convert)



