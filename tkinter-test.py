#Yahtzee leikur
import random
import statistics

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
    
    def dice_checker(self, dice):
        possible_options = [False] * 13
        if self.upperSectionBool[0] != True and 1 in dice:
            possible_options[0] = True
        if self.upperSectionBool[1] != True and 2 in dice:
            possible_options[1] = True
        if self.upperSectionBool[2] != True and 3 in dice:
            possible_options[2] = True
        if self.upperSectionBool[3] != True and 4 in dice:
            possible_options[3] = True
        if self.upperSectionBool[4] != True and 5 in dice:
            possible_options[4] = True
        if self.upperSectionBool[5] != True and 6 in dice:
            possible_options[5] = True
        if len(set(dice)) == 1 and self.lowerSectionBool[5] != True:
            possible_options[11] = True
        if len(set(dice)) == 2:
            counter = dice.count(max(dice, key = dice.count))
            if self.lowerSectionBool[2] == False and counter == 3:
                possible_options[8] = True
            if self.lowerSectionBool[1] == False and counter == 4:
                possible_options[7]== True
        if self.lowerSectionBool[0] == False and (len(set(dice)) == 3):
            counter = dice.count(max(dice, key = dice.count))
            if counter == 3:
                possible_options[6] = True
        lowerStraight = [1,2,3,4,5]
        higherStraight = [2,3,4,5,6]
        if self.lowerSectionBool[3] != True and sorted(dice) == lowerStraight:
            possible_options[9] = True
        if self.lowerSectionBool[4] != True and sorted(dice) == higherStraight:
            possible_options[10] = True
        if self.lowerSectionBool[6] != True:
            possible_options[12] = True
        return possible_options

    def option_display(self, possible_options):
        if possible_options[0] == True:
            print('1. Aces available')
        if possible_options[1] == True:
            print("2. Two's available")
        if possible_options[2] == True:
            print("3. Threes available")
        if possible_options[3] == True:
            print("4. Fours available")
        if possible_options[4] == True:
            print("5. Fives available")
        if possible_options[5] == True:
            print("6. Sixes available")
        if possible_options[6] == True:
            print("7. 3 of a kind available")
        if possible_options[7] == True:
            print("8. 4 of a kind available")
        if possible_options[8] == True:
            print("9. Full House available")
        if possible_options[9] == True:
            print("10. Small Straight available")
        if possible_options[10] == True:
            print("11. Large Straight available")
        if possible_options[11] == True:
            print("12. Yahtsee available")
        if possible_options[12] == True:
            print("13. Chance available")
    
    def setScore(self, score, options, dice):
        if score == 1 and options[0] == True:
            aceSum = 0
            for i in dice:
                if i == 1:
                    aceSum += 1
            self.upperSection[0] = aceSum
            self.upperSectionBool[0] = True
        if score == 2 and options[1] == True:
            twoSum = 0
            for i in dice:
                if i == 2:
                    twoSum += 2
            self.upperSection[1] = twoSum
            self.upperSectionBool[1] = True
        if score == 3 and options[2] == True:
            threeSum = 0
            for i in dice:
                if i == 3:
                    threeSum += 3
            self.upperSection[2] = threeSum
            self.upperSectionBool[2] = True            
        if score == 4 and options[3] == True:
            fourSum = 0
            for i in dice:
                if i == 4:
                    fourSum += 4
            self.upperSection[3] = fourSum
            self.upperSectionBool[3] = True
        if score == 5 and options[4] == True:
            fiveSum = 0
            for i in dice:
                if i == 5:
                    fiveSum += 5
            self.upperSection[4] = fiveSum
            self.upperSectionBool[4] = True
        if score == 6 and options[5] == True:
            sixSum = 0
            for i in dice:
                if i == 6:
                    sixSum += 6
            self.upperSection[5] = sixSum
            self.upperSectionBool[5] = True
        if score == 7 and options[6] == True:
            threeValue = statistics.mode(dice)
            self.lowerSection[0] = threeValue*3
            self.lowerSectionBool[0] = True
        if score == 8 and options[7] == True:
            fourValue = statistics.mode(dice)
            self.lowerSection[1] = fourValue*4
            self.lowerSectionBool[1] = True
        if score == 9 and options[8] == True:
            self.lowerSection[2] = sum(dice)
            self.lowerSectionBool[2] = True
        if score == 10 and options[9] == True:
            sDice = sorted(dice)
            sDice.remove(sDice[len(dice)-1])
            self.lowerSection[3] = sDice
            self.lowerSectionBool[3] = True
        if score == 11 and options[10] == True:
            sDice = sorted(dice, reverse=True)
            sDice.remove(sDice[len(dice)-1])
            self.lowerSection[4] = sDice
            self.lowerSectionBool[4]
        if score == 12 and options[11] == True:
            self.lowerSection[5] = 50
            self.lowerSectionBool[5] = True
        if score == 13 and options[12] == True:
            self.lowerSection[6] = sum(dice)
            self.lowerSectionBool[6] = True

class Game:
    def __init__(self):
        self.player = Player()

    def dice_generator(self, n):
        self.dice = []
        for i in range(n):
            self.dice.append(random.randint(1,6))
        return self.dice
    
    def game_generator(self):
        self.dices = self.dice_generator(5)
        print('These are your dices for this throw: ')
        print(self.dice)
        self.player.option_display(self.player.dice_checker(self.dice))
        self.answer = input('You have 2 more throws, would you like to use them?(Y for yes)')
        if self.answer == 'Y':
            self.diceNum = input('How many dices would you like to keep? ')
            self.dicesToKeep = self.throw_again(int(self.diceNum), self.dice)
            self.dice = self.dicesToKeep + self.dice_generator(5-int(self.diceNum))
            print('These are your dices now: ')
            print(self.dice)
            self.player.option_display(self.player.dice_checker(self.dice))
            self.answer2 = input('You have 1 more throw, would you like to use it?(Y for yes)')
            if self.answer2 == 'Y':
                self.diceNum = input('How many dices would you like to keep? ')
                self.dicesToKeep = self.throw_again(int(self.diceNum), self.dice)
                self.dice = self.dicesToKeep + self.dice_generator(5-int(self.diceNum))
                print('These are your dices now: ')
                print(self.dice)
                self.player.option_display(self.player.dice_checker(self.dice))
        self.choice = input('Choose option to score: ')
        self.player.setScore(int(self.choice), self.player.dice_checker(self.dice), self.dice)
        print(self.player.upperSection)
        print(self.player.lowerSection)
   
    def throw_again(self, number, diceList):
        self.keepDice = []
        for i in range(number):
            self.d_t_k = input('Select dice to keep(1 for the first, 2 for the second and etc. ')
            self.keepDice.append(diceList[int(self.d_t_k) - 1])
        return self.keepDice
    
game = Game()
while True:
    game.game_generator()
    if all(game.player.lowerSectionBool) and all(game.player.upperSectionBool):
        break 


#all() til að tjekka að allt sé True
#any() til að tjekka að eitthvað sé True





