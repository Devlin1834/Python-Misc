# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

## Fallout Hacking ##
### Challenge: INTERMEDIATE
### https://www.reddit.com/r/dailyprogrammer/comments/3qjnil/20151028_challenge_238_intermediate_fallout/

# Pull words from enable.txt
# give the user a difficulty choice
# give user multiple words of saimilar length
# One of those words is a password
# user must guess the password
# after a guess, computer will tell player how many letters they guessed correctly

import random as rn

diffs = {'sleepy': [],
         'easy': [],
         'medium': [],
         'hard': [],
         'impossible': []
         }

values = open('D:\Files\Psdir\enable1.txt').readlines()

words = []
for i in range(0, len(values)-1):
    words.append(values[i].rstrip())

for i in words:
    if len(i) == 4:
        diffs['sleepy'].append(i)
    elif len(i) == 5:
        diffs['easy'].append(i)
    elif len(i) == 6:
        diffs['medium'].append(i)
    elif len(i) == 9:
        diffs['hard'].append(i)
    elif len(i) == 12:
        diffs['impossible'].append(i)
    
print('Let\'s play a guessing game')
print('first choose a difficulty')
while True:
    for i in diffs.keys():
        print(i)
    difficulty = input('> ')
    if difficulty not in diffs.keys():
        print('Thats not of our difficulty settings, try again')
    else:
        break
    
rn.shuffle(diffs[difficulty])
challenge_set = diffs[difficulty][0:11]
password = challenge_set[rn.randint(1,10)]
for i in challenge_set:
    print(i)

print('\nOne of those words is the password')
print('You\'ll get four guesses')
print('Make your first guess now\n')

guesses = 0
while guesses <= 3:
    guess = input('> ')
    guess_letters = list(guess)
    password_letters = list(password)
    count = 0

    if guess == password:
        print('%d/%d letters correct. You win!' %(len(password), len(password)))
        break
    else:
        guesses += 1
        for i in guess_letters:
            if i in password_letters:
                if guess_letters.index(i) == password_letters.index(i):
                    count += 1
                else:
                    count += 0
            else:
                count += 0
        print('%d/%d letters correct' %(count, len(password)))
if guesses == 4:
    print('Your ran out of guesses. TOO BAD')