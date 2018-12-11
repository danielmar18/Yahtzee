#Yahtzee leikur
import random
'''class ScoreCard:
    def __init__(self):
        self.upperSection = [0] * 6
        self.upperSectionBool = [False] * 6
        self.upperSectionSum = 0
        self.lowerSection = [0] * 7
        self.lowerSectionBool = [False] * 7
        self.lowerSectionSum = 0
        self.bonusCounter = 0'''
class Player:
    def __init__(self):
        self.upperSection = [0] * 6
        self.upperSectionBool = [False] * 6
        self.lowerSection = [0] * 7
        self.lowerSectionBool = [False] * 7
        self.bonusCounter = 0

    def sumOfUpper(self):
        return sum(self.upperSection)

    def sumOfLower(self):
        return sum(self.lowerSection)
    
    def totalSum(self):
        return sum(self.upperSection) + sum(self.lowerSection)
#all() til að tjekka að allt sé True
#any() til að tjekka að eitthvað sé True
def aces(dice):
    aceSum = 0
    for i in dice:
        if i == 1:
            aceSum += 1
    return aceSum

def twos(dice):
    twoSum = 0
    for i in dice:
        if i == 2:
            twoSum += 2
    return twoSum

def threes(dice):
    threeSum = 0
    for i in dice:
        if i == 3:
            threeSum += 3
    return threeSum

def fours(dice):
    fourSum = 0
    for i in dice:
        if i == 4:
            fourSum += 4
    return fourSum

def fives(dice):
    fiveSum = 0
    for i in dice:
        if i == 5:
            fiveSum += 1
    return fiveSum

def sixes(dice):
    sixSum = 0
    for i in dice:
        if i == 6:
            sixSum += 1
    return sixSum

def dice_roll(n):
    dice = []
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice


x = input("How many dice would you like to roll?")
print(dice_roll(int(x)))


