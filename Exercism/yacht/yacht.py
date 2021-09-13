"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if (category == 0):
        if (dice.count(dice[0]) == 5):
            return(50)
        return (0)
    if (category == 1):
        return(dice.count(1)*1)
    if (category == 2):
        return(dice.count(2)*2)
    if (category == 3):
        return(dice.count(3)*3)
    if (category == 4):
        return(dice.count(4)*4)
    if (category == 5):
        return(dice.count(5)*5)
    if (category == 6):
        return(dice.count(6)*6)
    if (category == 7):
        for i in dice:
            if (dice.count(i) != 2 and dice.count(i) != 3):
                return(0)
        return(sum(dice))
    if (category == 8):
        for i in dice:
            if(dice.count(i) >= 4):
                return(4*i)
            if (dice.count(i) != 1):
                return (0)
    if (category == 9):
        for i in range(1,6):
            if (dice.count(i) != 1):
                return(0)
        return(30)        
    if (category == 10):
        for i in range(2,7):
            if (dice.count(i) != 1):
                return(0)
        return(30)      
    if (category == 11):
        return(sum(dice))
            
    
    
