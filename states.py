# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 20:34:05 2017

@author: Devlin
"""

## The fifty states game

### Players have 6 minutes to guess all fifty states
### Game is scored based on how much time they have left or how many states they forgot

import time, csv

states = ["Alabama",
          "Alaska",
          "Arizona",
          "Arkansas",
          "California",
          "Colorado",
          "Connecticut",
          "Delaware",
          "Florida",
          "Georgia",
          "Hawaii",
          "Idaho",
          "Illinois",
          "Indiana",
          "Iowa",
          "Kansas",
          "Kentucky",
          "Louisiana",
          "Maine",
          "Maryland",
          "Massachusetts",
          "Michigan",
          "Minnesota",
          "Mississippi",
          "Missouri",
          "Montana",
          "Nebraska",
          "Nevada",
          "New Hampshire",
          "New Jersy",
          "New Mexico",
          "New York",
          "North Carolina",
          "North Dakota",
          "Ohio",
          "Oklahoma",
          "Oregon",
          "Pennsylvania",
          "Rhode Island",
          "South Carolina",
          "South Dakota",
          "Tennessee",
          "Texas",
          "Utah",
          "Vermont",
          "Virginia",
          "Washington",
          "West Virginia",
          "Wisconson",
          "Wyoming"
          ]

print("You will have 6 minutes to guess all 50 states")
print("Spelling counts, as does capitalization, so be careful")
att = []
not_states = []
score = 0
count = 0
start = time.time()
stop = start + 300
while True:
    guess = input("> ")
    if guess in states:
        count += 1
    att.append(guess)
    if time.time() > stop or count == 50:
        end = time.time()
        print("TIME'S UP")
        break
    
for i in att:
    if i in states:
        score += 1
        states.remove(i)
    elif i not in states:
        score -= 1
        not_states.append(i)      
score = score + ((stop - end)/10)
print("Score: " + str(round(score, 0)))

print("\n")
print("You missed the following states")
for i in states:
    print(i)
    
print("\n")
print("You honestly thought these were states?")
for i in not_states:
    print(i)
    
highscores = open('scores.csv', 'w', newline = '')
scorewriter = csv.writer(highscores)
name = input("Save Your Score, Type Your Name: ")
scorewriter.writerow([name, score])
scorereader = csv.reader(highscores)
for row in scorereader:
    print(row)
highscores.close()