# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:54:52 2017

@author: Devlin
"""

## DND Character Creator

## To Do - Allow for class, race, and background input
##       - Allow for name, allignment input
##       - Spell Selection
##       - Allow to randomize the whole thing or just pecies of it
##       - Auto-roll stats but allow for 3 rerolls
##       - save character to a .txt
##       - save character to an acrobat doc

import random as rn

traits = {
        'language' : ['Common',
             'Elvish',
             'Draconic',
             'Dwarvish',
             'Giant',
             'Gnomish',
             'Goblin',
             'Halfling',
             'Orc',
             'Abyssal',
             'Celestial',
             'Deep Speech',
             'Infernal',
             'Primordial',
             'Sylvan',
             'Undercommon'
             ],
        'tools' : ['Alchemist\'s Supplies',
            'Brewer\'s Supplies',
             'Caligrapher\'s Supplies',
             'Carpenter\'s Tools',
             'Cartographer\'s Tools',
             'Cobbler\'s Tools',
             'Cook\'s Utensils',
             'Glassblower\'s Tools',
             'Jewler\'s Tools',
             'Leatherworker\'s Tools',
             'Mason\'s Tools'
             'Painter\'s Supplies',
             'Potter\'s Tools',
             'Smith\'s Tools',
             'Tinker\'s Tools',
             'Weaver\'s Tools',
             'Woodcarver\'s Tools'
             ],
        'instrument' : ['Bagpipes',
             'Drums',
             'Dulcimer',
             'Flute',
             'Lute',
             'Lyre',
             'Horn',
             'Pan Flute',
             'Shawm',
             'Viol'
               ],
        'game' : ['Dice Set',
             'Dragonchess Set',
             'Playing Card Set',
             'Three Dragon Ante Set'
         ]
        }



names = {'dwarf': {'Male': ['Adrik', 'Albreich', 'Morgran', 'Orsik', 'Travok', 'Ulfgar', 'Veit'],
                   'Female': ['Amber', 'Audhild', 'Diesa', 'Finellen', 'Hlin', 'Gurdis', 'Sannl'],
                   'clan': ['Balderk', 'Battlehammer', 'Fireforge', 'Frostbeard', 'Ironfist']},
         'elf': {'Male': ['Adran', 'Aramil', 'Arannis', 'Galinndan', 'Carric', 'Paelias', 'Thamior'],
                 'Female': ['Adrie', 'Birel', 'Caelynn', 'Lia', 'Mialee', 'Sariel', 'Thia', 'Vadnia'],
                 'clan': ['Amakiir', 'Galanodel', 'Holimion', 'Ilphelkiir', 'Nailo', 'Siannodel']},
         'halfling': {'Male': ['Alton', 'Cade', 'Corrin', 'Garret', 'Lyle', 'Perrin', 'Welby'],
                      'Female': ['Andry', 'Bree', 'Callie', 'Cora', 'Portia', 'Seraphina', 'Verna'],
                      'clan': ['Brushgather', 'Goodbarrel', 'Greenbottle', 'High-hill', 'Tealeaf']},
         'human': {'Male': ['Aesir', 'Mehmen', 'Darvin', 'Devlin', 'Chen', 'Ander', 'Blath', 'Fodel', 'Randal'],
                   'Female': ['Atla', 'Hama', 'Shandri', 'Jia', 'Mara', 'Hulmarra', 'Immith', 'Luisa', 'Vonda'],
                   'clan': ['Cherboga', 'Pisacar', 'Stormwind', 'Amblecrown', 'Tallstag', 'Starag', 'Mostana']},
         'dragonborn': {'Male': ['Arjhan', 'Balasar', 'Donaar', 'Ghesh', 'Patrin', 'Torinn'],
                        'Female': ['Akra', 'Biri', 'Jheri', 'Raiann', 'Sora', 'Surina'],
                        'clan': ['Clethtinthiallor', 'Kerrhylon', 'Norixius', 'Yarjerit', 'Linxakascendalor']},
         'gnome': {'Male': ['Alston', 'Boddynock', 'Brocc', 'Dimble', 'Kellen', 'Wrenn', 'Zook'],
                   'Female': ['Breena', 'Carlin', 'Donella', 'Duvamil', 'Lorilla', 'Shamil'],
                   'clan': ['Beren', 'Daergel', 'Folkor', 'Garrick', 'Murnig', 'Timbers']},
        'half orc': {'Male': ['Dench', 'Feng', 'Holg', 'Keth', 'Ront', 'Thokk'],
                     'Female': ['Baggi', 'Emen', 'Myev', 'Neega', 'Ovak', 'Sutha']},
        'tiefling': {'Male': ['Akemonos', 'Amnen', 'Damakos', 'Ekemon', 'Leucis', 'Mordai', 'Skamos'],
                     'Female': ['Akta', 'Criella', 'Ea', 'Kallista', 'Orianna', 'Phelaia', 'Rieta'],
                     'virtue': ['Art', 'Chant', 'Creed', 'Despair', 'Excellence', 'Open', 'Poetry']}     
         }

ascore_names = ['Strength',
                'Dexterity', 
                'Constitution', 
                'Intelligence',
                'Wisdom',
                'Charisma'
                ]

align = ['Lawful Good',
          'Lawful Neutral',
          'Lawful Evil',
          'Neutral Good',
          'Neutral',
          'Neutral Evil',
          'Chaotic Good',
          'Chaotic Neutral',
          'Chaotic Evil'
          ]

skills = {'Acrobatics': 0,                              # The zero indicates lack of proficiency
          'Animal Handling': 0,                         # will be changed to 1 to indicate proficieny
          'Arcana': 0,
          'Athletics': 0,
          'Deception': 0,
          'History': 0,
          'Insight': 0,
          'Intimidation': 0,
          'Investigation': 0,
          'Medicine': 0,
          'Nature': 0,
          'Perception': 0,
          'Performance': 0,
          'Persuasion': 0,
          'Religion': 0,
          'Sleight of Hand': 0,
          'Stealth': 0,
          'Survival': 0
          }

sprofs = []    # stands for skill proficiency
gprofs = []    # Stands for given proficiency
aprofs = []    # stands for additional proficiency
wprofs = []    # stands for weapon proficiency
feats = []     # stands for feats
name = ''
sex = ''
alignment = ''
age = ''
height = ''
weight = ''
speed = ''


####################################################################################################
class stat(object):
    
    def __init__(self, name, short, value):
        
        self.name = name
        self.short = short
        self.value = value
        self.mod = (value - 10) // 2
        
####################################################################################################
class skill(object):
    
    def __init__(self, prof, stat):
        
        self.prof = prof
        self.stat = stat
        self.mod = stat.mod + (2*prof)

####################################################################################################
class cbground(object):
    '''A Background!
    each background comes with 2 skill prificiencies
    two additional proficiencies
    and a feat'''
    
    def __init__(self, name, sprof1, sprof2, aprof1, aprof2, feat):
        
        self.name = name         # The name for the sake of printing
        self.sprof1 = sprof1     # Skill Prof 1                               
        self.sprof2 = sprof2     # Skill Prof 2
        self.aprof1 = aprof1     # Additional Prof 1
        self.aprof2 = aprof2     # Additional Prof 2
        self.feat = feat         # The Feat
                
    def select(self):
        '''This enables the user to fill the proficiency choices offered by the background'''
        
        get_profs = ['language', 'tools', 'instrument', 'game']  # These are the kinds of profs players get from their background that have sub choices
        cbg_profs = [self.aprof1, self.aprof2]                   # This list contains the two additional profs given from the bg 
    
        common = []                                              # common is set up to contain the elements that are in both lists
        for i in cbg_profs:
            if i in get_profs:
                common.append(i)                                 # I really struggled with this and the solution was so simple, I'm a dumass
                
        if len(common) > 0:
            print('You get to pick a ' + common[0])
            print('Pick from this list')
            for i in traits[common[0]]:                          # prints the list all pretty like
                print(i)

            while True:
                pick = input(' > ')
                if pick in aprofs:
                    print('You are already proficient in that')
                elif pick not in traits[common[0]]:
                    print('That selection is not currently valid. Speak to your DM')
                else:
                   aprofs.append(pick)                         # adds their choice to the aprofs list
                   break
        
            if len(common) > 1:                                # this if is only triggered when the player has two choices
                print('You also get to pick a ' + common[1])
                print('Pick from this list')
                for i in traits[common[1]]:
                    print(i)
                
                while True:
                    pick = input(' > ')
                    if pick in aprofs:
                        print('You are already proficient in that')
                    elif pick not in traits[common[1]]:
                        print('That selection is not currently valid. Speak to your DM')
                    else:
                        aprofs.append(pick)
                        break
                            
    
####################################################################################################
def ascore_get():
    '''This function is used to get ability scores, duh. It includes a random feature
    that lets the program randomly generate stats. When I look too closely at it, I can
    honestly say I have no idea how it works, but it does! Just don't ask any questions
    and be happy'''
    
    global ability_scores, rc
    
    ability_scores = []
    
    rolls = 3
    
    finalized = False
    while finalized == False:
        score = []
        score.append(rn.randint(1,6))
        score.append(rn.randint(1,6))
        score.append(rn.randint(1,6))
        score.append(rn.randint(1,6))
        
        f_score = sum(score) - min(score)
        ability_scores.append(f_score)
        
        if len(ability_scores) == 6:
            for name, score in list(zip(ascore_names, ability_scores)):
                print(name + ': ' + str(score))
            if rolls > 0 and 'y' not in rc.lower():
                while True:
                    print()
                    print('Do you accept these results?')
                    yn = input('Y/N > ')
                    if 'y' in yn.lower():
                        finalized = True
                        break
                    elif 'n' in yn.lower():
                        finalized = False
                        del ability_scores[:]
                        rolls -= 1
                        break
                    else:
                        print('Ruh Roh')
            else: 
                print('Your scores have been finalized by the computer')
                print('I hope you\'re happy with them')
                finalized = True

####################################################################################################
def generate(d):
    '''If I store all the customization options in dicts, I can use this function
    to make randomization that much easier'''
    
    r = rn.randint(0, len(d.keys())-1)
    return sorted(list(d.keys()))[r]

####################################################################################################
def dice_roll(num, d):
    '''This is used to generate the rolling of multiple dice
    num is the number of rolls
    d is the dice used
    mostly usefull when rolling heights and weights'''
    
    rolls = 0
    res = []
    while rolls < num:
        res.append(rn.randint(1, d))
        rolls += 1
        
    return sum(res)
       
####################################################################################################
def name_me(race, sex):
    '''Names a character, either randomly or by determination of the user
    random names are stored in a dict 'names' and in sub dicts and lists
    within 'names'
    '''
    
    
    global rc, name, alignment
    
    if 'y' in rc.lower():
        
        if race != 'orc' and race != 'tiefling':
            rcname = names[race]['clan'][rn.randint(0, len(names[race]['clan'])-1)]
        else:
            rcname = ''
        
        if race == 'tiefling' and 'Good' in alignment:
            rfname = names[race]['virtue'][rn.randint(0, len(names[race]['virtue'])-1)]
        else:
            rfname = names[race][sex][rn.randint(0, len(names[race][sex])-1)]

    else:
        print('Would you like to select a random name?')
        rname = input('Yes or No: ')
        
        if 'y' in rname.lower():
            if race != 'orc' and race != 'tiefling':
                rcname = names[race]['clan'][rn.randint(0, len(names[race]['clan'])-1)]
            else:
                rcname = ''
        
            if race == 'tiefling' and 'Good' in alignment:
                rfname = names[race]['virtue'][rn.randint(0, len(names[race]['virtue'])-1)]
            else:
                rfname = names[race][sex][rn.randint(0, len(names[race][sex])-1)]
        else:
            rfname = input('Your First Name: ')
            rcname = input('Your Last Name: ')
         
    name = rfname + ' ' + rcname    

        
####################################################################################################
def m_f():
    '''Picks male or female, to be used within race functions'''
    
    global sex, rc
    
    if 'y' in rc.lower():
        rsex = rn.randint(1,2)
        if rsex == 1:
            sex = 'Male'
        else:
            sex = 'Female'
    else:
        while True:
            sex = input('Male or Female: ')
            if sex != 'Male' and sex != 'Female':
                print('Its a very basic program, not a tumblr, use a normal gender')
            elif sex == 'Male' or sex == 'Female':
                break
            else:
                print('I dunno what you did but pick Male or Female')   
                
####################################################################################################
def align_me():
    '''Helps pick an alignment, can randomly pick one from a list called align'''
    
    global alignment, rc    
    
    if 'y' in rc:
        alignment = align[rn.randint(0, len(align)-1)]
    else:
        print('Would you like a random alignment?')
        ral = input('Yes or No: ')
        if 'y' in ral.lower():
            alignment = align[rn.randint(0, len(align)-1)]
        else:
            print('Whats your characters alignment?')
            for i in align:
                print(i)
            while True:
                alignment = input(' > ')
                if alignment not in align:
                    print('Thats not an alignment')
                else:
                    break

####################################################################################################
def age_me(age_max):
    '''picks an age between 1 and the age max determined by race
    can be randomy determied from the inital but not within the function'''
     
    global rc, age
    
    if 'y' in rc.lower():
        age = rn.randint(1, age_max)
    else:
        print("How old are you?")
        while True:
            age = input(' > ')
            try:
                int(age)
            except ValueError:
                print('Thats no number!')
                continue
        
            if int(age) > age_max:
                print('Yeah, you\'d be dead. Pick a younger character')
            elif int(age) <= 0:
                print('How the hell is that possible? Be older')
            else:
                break
           
####################################################################################################
def mdwarf():
    '''Mountain Dwarf'''
    
    global name, rc, sex, alignment, speed, height, weight, ability_scores, aprofs, wprofs, feats
    
    print("You're a Mountain Dwarf!")    
    m_f()
    align_me()
    name_me('dwarf', sex)
    age_me(350)    
    speed = 25
    height = 48 + dice_roll(2, 4)
    weight = 130 * dice_roll(2, 6)
    
    r_bens = [2,0,2,0,0,0]
    
    ability_scores = [x + y for x, y in zip(ability_scores, r_bens)]
        
    aprofs += ['Common', 'Dwarvish']
    wprofs += ['Battleaxe', 'Hand Axe', 'Throwing Hammer', 'War Hammer', 'Light Armor', 'Medium Armor']
    feats += ['Darkvision', 'Dwarven Resilience']

####################################################################################################
def hdwarf():
    '''Hill Dwarf'''
    
    global name, rc, sex, alignment, speed, height, weight, ability_scores, aprofs, wprofs, feats
    
    print("You're a Hill Dwarf!")
    m_f()
    align_me()
    name_me('dwarf', sex)
    age_me(350)
    speed = 25
    height = 44 + dice_roll(2, 4)
    weight = 115 * dice_roll(2, 6)
    
    r_bens = [0,0,2,0,1,0]
    ability_scores = [x + y for x, y in zip(ability_scores, r_bens)]
    
    aprofs += ['Common', 'Dwarvish']
    wprofs += ['Battleaxe', 'Hand Axe', 'Throwing Hammer', 'War Hammer']
    feats += ['Darkvision', 'Dwarven Resilience', 'Dwarven Toughness']
    
####################################################################################################
def helf():
    '''High Elf'''
    
    global name, rc, sex, alignment, speed, height, weight, ability_scores, aprofs, wprofs, feats, sprofs
    
    print("You're a High Elf!")
    m_f()
    align_me()
    name_me('elf', sex)
    age_me(750)
    speed = 30
    height = 54 + dice_roll(2, 10)
    weight = 90 * dice_roll(1, 4)
    
    r_bens = [0,2,0,1,0,0]
    
    ability_scores = [x + y for x, y in zip(ability_scores, r_bens)]
    
    aprofs += ['Common', 'Elvish']
    sprofs += ['Perception']
    wprofs += ['Longsword', 'Shortsword', 'Longbow', 'Shortbow']
    feats += ['Darkvision', 'Trance', 'Fey Ancestry', '+1 Wizzard Cantrip']
    
    if 'y' in rc:
        aprofs.append(traits['language'][rn.randint(0, len(traits['language']-1))])
    else:
        print('You get to pick a language')
        print('Pick from this list')
        for i in traits['language']:
            print(i)
        while True:
            new_lang = input(' > ')
            if new_lang not in traits['language']:
                print('Thats not a language, consult your DM')
            elif new_lang in aprofs:
                print('You\'re already proficient in that language!')
            else:
                aprofs.append(new_lang)
                break

####################################################################################################
def welf():
    '''Wood Elf'''
        
    global name, rc, sex, alignment, speed, height, weight, ability_scores, aprofs, wprofs, feats
    
    print('You\'re a Wood Elf!')
    m_f()
    align_me()
    name_me('elf', sex)
    age_me(750)
    speed = 35
    height = 54 + dice_roll(2, 10)
    weight = 100 * dice_roll(1, 4)
    
    r_bens = [0,2,0,0,1,0]
    
    ability_scores = [x + y for x, y in zip(ability_scores, r_bens)]
    
    aprofs += ['Common', 'Elvish']
    wprofs += ['Longsword', 'Shortsword', 'Longbow', 'Shortbow']
    feats += ['Darkvision', 'Trance', 'Fet Ancestry', 'Mask of the Wild']
    
####################################################################################################
def drow():
    ''' Stupid Drow'''
    
    global name, rc, sex, alignment, speed, height, weight, ability_scores, aprofs, wprofs, feats
    
    print('You\'re a Drow, you edgey rebel, you!')
    m_f()
    align_me()
    name_me('elf', sex)
    age_me(750)
    speed = 30
    height = 53 + dice_roll(2, 6)
    weight = 75 * dice_roll(1, 6)
    
    r_bens = [0,2,0,0,0,1]
    
    ability_scores = [x + y for x, y in zip(ability_scores, r_bens)]
    
    aprofs += ['Common', 'Elvish']
    wprofs += ['Rapier', 'Shortsword', 'Hand Crossbow', 'Shortbow']
    feats += ['Superior Darkvision', 'Fey Ancestry', 'Trance', 'Drow Magic']

####################################################################################################
def lhalf():
    '''Lightfoot Halfling'''
    
    global name, rc, sex, alignment, speed, height, weight, ability_scores, aprofs, wprofs, feats
    
    print('You\'re a Lightfoot Halfling!')
    m_f()
    align_me()
    name_me('gnome', sex)
    age_me(300)
    speed = 25
    height = 35 + dice_roll(2, 4)
    weight = 35
    
    r_bens = [0,2,0,0,0,1]
    
    ability_scores = [x + y for x, y in zip(ability_scores, r_bens)]
    
    aprofs += ['Common', 'Halfling']
    feats += ['Lucky', 'Brave', 'Halfling Numbleness', 'Naturally Stealthy']

####################################################################################################
def shalf():
    '''Stout Halfling'''

    global name, rc, sex, alignment, speed, height, weight, ability_scores, aprofs, wprofs, feats
      
    print('You\'re a Stout Halfling!')
    m_f()
    align_me()
    name_me('gnome', sex)
    age_me(300)
    speed = 25
    height = 35 + dice_roll(2, 4)
    weight = 35
    
    r_bens = [0,2,1,0,0,0]

    ability_scores = [x + y for x, y in zip(ability_scores, r_bens)]

    aprofs += ['Common', 'Halfling']
    feats += ['Lucky', 'Brave', 'Halfling Numbleness', 'Stout Resilience']
    
####################################################################################################
def human():
    '''Human'''
    
    global name, rc, sex, alignment, speed, height, weight, ability_scores, aprofs, wprofs, feats
    
    print('You\'re Human')
    m_f()
    align_me()
    name_me('human', sex)
    age_me(120)
    speed = 25
    height = 56 + dice_roll(2, 10)
    weight = 110 * dice_roll(2, 4)
    
    r_bens = [1,1,1,1,1,1]

    ability_scores = [x + y for x, y in zip(ability_scores, r_bens)]
    
    aprofs += ['Common']
    
    if 'y' in rc:
        aprofs.append(traits['language'][rn.randint(0, len(traits['language']-1))])
    else:
        print('You get to pick a language')
        print('Pick from this list')
        for i in traits['language']:
            print(i)
        while True:
            new_lang = input(' > ')
            if new_lang not in traits['language']:
                print('Thats not a language, consult your DM')
            elif new_lang in aprofs:
                print('You\'re already proficient in that language!')
            else:
                aprofs.append(new_lang)
                break
    
####################################################################################################
races = {"Mountain Dwarf": mdwarf,
        "Hill Dwarf": hdwarf,
        "High Elf": helf,
        "Wood Elf": welf,
        "Drow": drow,
        "Lightfoot Halfling": lhalf,
        "Stout Halfling": shalf,
       # "Human": human,
       # "Dragonborn": dragonborn,
       # "Forest Gnome": fgnome,
       # "Rock Gnome": rgnome,
       # "Half Elf": halfe,
       # "Half Orc": halfo,
       # "Tiefling": tiefling
        }
    
####################################################################################################                
Acolyte = cbground('Acolyte', 'Insight', 'Religion', 'language', 'language', 'Shelter of the Faithful')
Charlatan = cbground('Charlatan', 'Deception', 'Sleight of Hand', 'Diguise Kit', 'Forgery Kit', 'False Identity')
Criminal = cbground('Criminal', 'Deception', 'Stealth', 'game', 'Thieves Tools', 'Criminal Contact')
Entertainer = cbground('Entertainer', 'Acrobatics', 'Performance', 'Disguise Kit', 'instrument', 'By Popular Demand')
Folk_Hero = cbground('Folk Hero', 'Animal Handling', 'Survival', 'tools', 'Land Vehicles', 'Rustic Hospitality')
Guild_Artisan = cbground('Guild Artisan', 'Insight', 'Persuasion', 'tools', 'language', 'Guild Membership')
Hermit = cbground('Hermit', 'Medicine', 'Religion', 'Herbalism Kit', 'language', 'Discovery')
Noble = cbground('Noble', 'History', 'Persuasion', 'game', 'language', 'Position of Privelege')
Outlander = cbground('Outlander', 'Athletics', 'Survival', 'instrument', 'language', 'Wanderer')
Sage = cbground('Sage', 'Arcana', 'History', 'language', 'language', 'Researcher')
Sailor = cbground('Sailor', 'Athletics', 'Perception', 'Navigators Tools', 'Water Vehicles', 'Ships Passage')
Soldier = cbground('Soldier', 'Athletics', 'Intimidation', 'game', 'Land Vehicles', 'Military Rank')
Urchin = cbground('Urchin', 'Sleight of Hand', 'Stealth', 'Disguise Kit', 'Thieves Tools', 'City Secrets')

bgs = {'Acolyte': Acolyte,
       'Charlatan': Charlatan,
       'Criminal': Criminal,
       'Entertainer': Entertainer,
       'Folk Hero': Folk_Hero,
       'Guild Artisan': Guild_Artisan,
       'Hermit': Hermit,
       'Noble': Noble,
       'Outlander': Outlander,
       'Sage': Sage,
       'Sailor': Sailor,
       'Soldier': Soldier,
       'Urchin': Urchin
       }

####################################################################################################
################################   Character Creation   ############################################
print('We\'re going to build a DND character')
print('Would you like to randomize the entire process?')
print('You will still be able to randomize parts of it if you say no')
rc = input('Yes or No: ')

print()
print('Lets Roll Stats')
ascore_get()

print()


if 'y' not in rc.lower():
    print('First Select a Race')
    print('Would you like to get a random race?')
    rrace = input('Yes or No: ')
    if 'y' in rrace.lower():
        race = generate(races)
    else:
        print('Pick from this list')
        for i in races.keys():
            print(i)
        while True:
            race = input(' > ')
            if race not in races:
                print('That is not a valid race, talk to your DM')
            else:
                break
else:
    race = generate(races)
    
races[race]()

strn = stat('Strength', 'strn', ability_scores[0]) 
dex = stat('Dexterity', 'dex', ability_scores[1])
con = stat('Constitution', 'con', ability_scores[2])
intn = stat('Intelligence', 'intn', ability_scores[3])
wis = stat('Wisdom', 'wis', ability_scores[4])
char = stat('Charisma', 'char', ability_scores[5])

print()
if 'y' not in rc.lower():
    print('Now lets select a Background')
    print('Would you like to select a random background for your character?')
    rbg = input('Yes or No: ')
    if 'y' in rbg.lower():
        bg_choice = generate(bgs)
    else:    
        print('Pick from this list')
        for i in bgs.keys():
            print(i)
        while True:
            bg_choice = input(' > ')
            if bg_choice not in bgs:
                print('Thats not a Valid Background, talk to your DM')
            else:
                break
else:
    bg_choice = generate(bgs)

background = bgs[bg_choice]
background.select()
sprofs.append(background.sprof1)
sprofs.append(background.sprof2)
feats.append(background.feat)

for i in sprofs:
    skills[i] = 1
## Begining plan to print x where proficient and nothing if not
## hit snag, dicts unordered, prevents easy iteration
## look into sorted()
for p in skills.values():
    if p == 0:
        gprofs.append('')
    else:
        gprofs.append('x')

acrobatics = skill(skills['Acrobatics'], dex)
animal_handling = skill(skills['Animal Handling'], wis)
arcana = skill(skills['Arcana'], intn)
athletics = skill(skills['Athletics'], strn)
deception = skill(skills['Deception'], char)
history = skill(skills['History'], intn)
insight = skill(skills['Insight'], wis)
intimidation = skill(skills['Intimidation'], char)
investigation = skill(skills['Investigation'], intn)
medicine = skill(skills['Medicine'], wis)
nature = skill(skills['Nature'], intn)
perception = skill(skills['Perception'], wis)
performance = skill(skills['Performance'], char)
persuasion = skill(skills['Persuasion'], char)
religion = skill(skills['Religion'], intn)
sleight_of_hand = skill(skills['Sleight of Hand'], dex)
stealth = skill(skills['Stealth'], dex)
survival = skill(skills['Survival'], wis)

####################################################################################################
############################# Print My Character Please ############################################
####################################################################################################
print('----------------------------------------------------------------------------')
print(name)
print(str(age) + ' year old')
print(alignment)
print(sex)
print(race)
print(background.name)
print()
print(strn.name + ': ' + str(strn.value) + ' (' + str(strn.mod) + ')')
print(dex.name + ': ' + str(dex.value) + ' (' + str(dex.mod) + ')')
print(con.name + ': ' + str(con.value) + ' (' + str(con.mod) + ')')
print(intn.name + ': ' + str(intn.value) + ' (' + str(intn.mod) + ')')
print(wis.name + ': ' + str(wis.value) + ' (' + str(wis.mod) + ')')
print(char.name + ': ' + str(char.value) + ' (' + str(char.mod) + ')')
print()

print()
for a in aprofs:
    print(a)
print()
for w in wprofs:
    print(w)
print()
for s in sprofs:
    print(s)
print()
for f in feats:
    print(f)
print('----------------------------------------------------------------------------')


