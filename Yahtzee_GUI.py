#Yahtzee GUI
import random
import statistics
from tkinter import *
from functools import partial

window = Tk()
window.title('Yahtzee by Reynir and Daniel')
window.geometry("600x400")
titleFrame = Frame(window)
titleFrame.pack()
diceFrame = Frame(window)
diceFrame.pack(side=TOP)
optionsFrame = Frame(window)
optionsFrame.pack(side=TOP)
answerFrame = Frame(window)
answerFrame.pack(side=TOP)
quitFrame = Frame(window)
quitFrame.pack(side=BOTTOM)


DICEHEIGHT = 5
DICEWIDTH = 10
numberToAdd = 0
upper = [0] * 6
lower = [0] * 7
seeScoreBoolean = False

class Player:
    def __init__(self):
        self.upperSection = upper
        self.upperSectionBool = [False] * 6
        self.lowerSection = lower
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
        def addToScore(value):
            global numberToAdd
            numberToAdd = value
            Player().setScore(value, Player().dice_checker(Game().dice), Game().dice)
        if possible_options[0] == True:
            acesLabel = Button(optionsFrame, text='Aces available', command=partial(addToScore, 1))
            acesLabel.pack(side=TOP)
        if possible_options[1] == True:
            twosLabel = Button(optionsFrame, text="Two's available", command=partial(addToScore, 2))
            twosLabel.pack(side=TOP)
        if possible_options[2] == True:
            threesLabel = Button(optionsFrame, text="Threes available", command=partial(addToScore, 3))
            threesLabel.pack(side=TOP)
        if possible_options[3] == True:
            foursLabel = Button(optionsFrame, text="Fours available", command=partial(addToScore, 4))
            foursLabel.pack(side=TOP)
        if possible_options[4] == True:
            fivesLabel = Button(optionsFrame, text="Fives available", command=partial(addToScore, 5))
            fivesLabel.pack(side=TOP)
        if possible_options[5] == True:
            sixesLabel = Button(optionsFrame, text="Sixes available", command=partial(addToScore, 6))
            sixesLabel.pack(side=TOP)
        if possible_options[6] == True:
            threeKindLbael = Button(optionsFrame, text="3 of a kind available", command=partial(addToScore, 7))
            threeKindLbael.pack(side=TOP)
        if possible_options[7] == True:
            fourKindLabel = Button(optionsFrame, text="4 of a kind available", command=partial(addToScore, 8))
            fourKindLabel.pack(side=TOP)
        if possible_options[8] == True:
            fullHouseLabel = Button(optionsFrame, text="Full House available", command=partial(addToScore, 9))
            fullHouseLabel.pack(side=TOP)
        if possible_options[9] == True:
            smallStraightLabel = Button(optionsFrame, text="Small Straight available", command=partial(addToScore, 10))
            smallStraightLabel.pack(side=TOP)
        if possible_options[10] == True:
            largeStraightLabel = Button(optionsFrame, text="Large Straight available", command=partial(addToScore, 11))
            largeStraightLabel.pack(side=TOP)
        if possible_options[11] == True:
            yahtseeLabel = Button(optionsFrame, text="Yahtsee available", command=partial(addToScore, 12))
            yahtseeLabel.pack(side=TOP)
        if possible_options[12] == True:
            chanceLabel = Button(optionsFrame, text="Chance available", command=partial(addToScore, 13))
            chanceLabel.pack(side=TOP)
    
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
        self.counter = 0
        self.dicesToKeep = []
        self.dice = []

    def dice_generator(self, n):
        self.dice = []
        for i in range(n):
            self.dice.append(random.randint(1,6))
        return self.dice

    def game_generator(self):

        def playAgain():
            global upper
            upper = self.player.upperSection
            global lower
            lower = self.player.lowerSection
            for child in titleFrame.winfo_children():
                child.destroy()
            for child in diceFrame.winfo_children():
                child.destroy()
            for child in optionsFrame.winfo_children():
                child.destroy()
            for child in answerFrame.winfo_children():
                child.destroy()
            for child in quitFrame.winfo_children():
                child.destroy()
            Game().game_generator()

        def afterNextScreen2():
            for child in diceFrame.winfo_children():
                child.destroy()
            for child in titleFrame.winfo_children():
                child.destroy()
            theseAreYourDicesNow = Label(titleFrame, text="These are your dices now:")
            theseAreYourDicesNow.pack()
            colCount = 0
            for item in self.dice:
                dices = Button(diceFrame, text=item, height=DICEHEIGHT, width=DICEWIDTH)
                dices.grid(row=1, column=colCount)
                colCount += 1
            for child in optionsFrame.winfo_children():
                    child.destroy()
            for child in answerFrame.winfo_children():
                    child.destroy()
            self.player.option_display(self.player.dice_checker(self.dice))
            seeScoreButton = Button(answerFrame, text="See score", command=partial(answer1, 'N'))
            seeScoreButton.pack(pady=30)
            
        def nextScreen2(value):
            self.dice = self.dicesToKeep + self.dice_generator(5-value)
            afterNextScreen2()

        def addToDTK2(value):
            self.counter += 1
            self.dicesToKeep.append(self.dice[value])
            if self.counter == self.number:
                nextScreen2(self.number)

        def pick2(value):
            self.counter = 0
            self.dicesToKeep = []
            self.number = value
            if value == 0:
                for child in diceFrame.winfo_children():
                    child.destroy()
                for child in answerFrame.winfo_children():
                    child.destroy()
                nextScreen2(value)
            elif value == 5:
                self.dicesToKeep = self.dice
                nextScreen2(value)
            else:
                for child in titleFrame.winfo_children():
                        child.destroy()
                for child in optionsFrame.winfo_children():
                        child.destroy()
                selectDiceLabel = Label(optionsFrame, text="Select dice to keep (1 for the first, 2 for the second etc.)")
                selectDiceLabel.grid(row=0, columnspan=5)
                for i in range(5):
                    selectDiceButtons = Button(answerFrame, text=i+1, command=partial(addToDTK2, i))
                    selectDiceButtons.grid(row=1, column=i)

        def answer2(value):
            if value == 'Y':
                for child in optionsFrame.winfo_children():
                    child.destroy()
                for child in answerFrame.winfo_children():
                    child.destroy()
                howManyDice = Label(optionsFrame, text="How many dices would you like to keep?")
                howManyDice.grid(row=0, columnspan=5)
                for i in range(0, 6):
                    pick = Button(optionsFrame, text=i, command=partial(pick2, i))
                    pick.grid(row=1, column=i)
            else:
                answer1('N')
            
        def afterNextScreen1():
            for child in diceFrame.winfo_children():
                child.destroy()
            for child in titleFrame.winfo_children():
                child.destroy()
            theseAreYourDicesNow = Label(titleFrame, text="These are your dices now:")
            theseAreYourDicesNow.pack()
            colCount = 0
            for item in self.dice:
                dices = Button(diceFrame, text=item, height=DICEHEIGHT, width=DICEWIDTH)
                dices.grid(row=1, column=colCount)
                colCount += 1
            for child in optionsFrame.winfo_children():
                    child.destroy()
            for child in answerFrame.winfo_children():
                    child.destroy()
            self.player.option_display(self.player.dice_checker(self.dice))
            answer2Label = Label(answerFrame, text='You have 1 more throw, would you like to use it?')
            answer2Label.grid(row=0, columnspan=2)
            yesButton2 = Button(answerFrame, text="Yes", command=partial(answer2, 'Y'))
            yesButton2.grid(row=1, column=0)
            noButton2 = Button(answerFrame, text="No", command=partial(answer2, 'N'))
            noButton2.grid(row=1, column=1)

        def nextScreen1(value):
            self.dice = self.dicesToKeep + self.dice_generator(5-value)
            afterNextScreen1()
            
        def addToDTK1(value):
            self.counter += 1
            self.dicesToKeep.append(self.dice[value])
            if self.counter == self.number:
                nextScreen1(self.number)

        def pick1(value):
            self.number = value
            if value == 0:
                for child in diceFrame.winfo_children():
                    child.destroy()
                for child in answerFrame.winfo_children():
                    child.destroy()
                nextScreen1(value)
            elif value == 5:
                self.dicesToKeep = self.dice
                nextScreen1(value)
            else:
                for child in titleFrame.winfo_children():
                        child.destroy()
                for child in optionsFrame.winfo_children():
                        child.destroy()
                selectDiceLabel = Label(optionsFrame, text="Select dice to keep (1 for the first, 2 for the second etc.)")
                selectDiceLabel.grid(row=0, columnspan=5)
                for i in range(0, 5):
                    selectDiceButtons = Button(answerFrame, text=i+1, command=partial(addToDTK1, i))
                    selectDiceButtons.grid(row=1, column=i)

        def answer1(value):
            if value == 'Y':
                for child in optionsFrame.winfo_children():
                    child.destroy()
                for child in answerFrame.winfo_children():
                    child.destroy()
                howManyDice = Label(optionsFrame, text="How many dices would you like to keep?")
                howManyDice.grid(row=0, columnspan=6)
                for i in range(0, 6):
                    pick = Button(optionsFrame, text=i, command=partial(pick1, i))
                    pick.grid(row=1, column=i)    
            else:
                for child in answerFrame.winfo_children():
                    child.destroy()
                self.player.setScore(numberToAdd, self.player.dice_checker(self.dice), self.dice)
                upperSectionLabel = Label(answerFrame, text="Upper section score: ")
                upperSectionLabel.grid(row=2, column=0)
                upperSectionScoreLabel = Label(answerFrame, text=self.player.upperSection)
                upperSectionScoreLabel.grid(row=2, column=1)
                upperSectionSumLabel = Label(answerFrame, text="Upper section sum: ")
                upperSectionSumLabel.grid(row=2, column=2)
                upperSectionSum = Label(answerFrame, text=sum(self.player.upperSection))
                upperSectionSum.grid(row=2, column=3)
                lowerSectionLabel = Label(answerFrame, text="Lower section score: ")
                lowerSectionLabel.grid(row=3, column=0)
                lowerSectionScoreLabel = Label(answerFrame, text=self.player.lowerSection)
                lowerSectionScoreLabel.grid(row=3, column=1)
                lowerSectionScoreLabel.grid(row=3, column=1)
                lowerSectionSumLabel = Label(answerFrame, text="Lower section sum: ")
                lowerSectionSumLabel.grid(row=3, column=2)
                lowerSectionSum = Label(answerFrame, text=sum(self.player.lowerSection))
                lowerSectionSum.grid(row=3, column=3)
                totalSumLabel = Label(answerFrame, text="Total sum: " + str(sum(self.player.upperSection + self.player.lowerSection)))
                totalSumLabel.grid(row=4, columnspan=4)
                playAgainButton = Button(quitFrame, text="Play again", command=playAgain)
                playAgainButton.pack(side=BOTTOM)
                
        quitButton = Button(quitFrame, text="Quit game", command=quit)
        quitButton.pack(side=BOTTOM, pady=20)
        self.dices = self.dice_generator(5)
        theseAreYourDices = Label(titleFrame, text='These are your dices for this throw: ')
        theseAreYourDices.pack()
        colCount = 0
        for item in self.dice:
            dices = Button(diceFrame, text=item, height=DICEHEIGHT, width=DICEWIDTH)
            dices.grid(row=0, column=colCount)
            colCount += 1
        self.player.option_display(self.player.dice_checker(self.dice))
        answerLabel = Label(answerFrame, text='You have 2 more throws, would you like to use them?')
        answerLabel.grid(row=0, columnspan=2)
        yesButton = Button(answerFrame, text="Yes", command=partial(answer1, 'Y'))
        yesButton.grid(row=1, column=0)
        noButton = Button(answerFrame, text="No", command=partial(answer1, 'N'))
        noButton.grid(row=1, column=1)
        
game = Game()
game.game_generator()


window.mainloop()
