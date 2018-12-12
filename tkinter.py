from tkinter import *
import random

HEIGHT=500
WIDTH=500

# window = Tk()
# window.title('Yahtzee by Reyrey and Danni')
# # Frame(width=WIDTH, height=HEIGHT).pack()

# name1 = Label(window, text="Please enter your name Player 1: ")
# enter1 = Entry(window)
# save1 = Button(window, text="Save name")
# name2 = Label(window, text="Please enter your name Player 2: ")
# enter2 = Entry(window)
# name1.grid(row=0)
# enter1.grid(row=0, column=1)
# name2.grid(row=1)
# enter2.grid(row=1, column=1)

# topFrame = Frame(window)
# topFrame.pack()
# bottomFrame = Frame(window)
# bottomFrame.pack(side = BOTTOM) 
# # video 2
# button1 = Button(topFrame, text="Button 1", fg='red')
# button2 = Button(topFrame, text="Button 2", fg='blue')
# button3 = Button(topFrame, text="Button 3", fg='green')
# button4 = Button(bottomFrame, text="Button4", fg='yellow')
# button1.pack(side = LEFT)
# button2.pack(side = LEFT)
# button3.pack(side = LEFT)
# button4.pack(side = LEFT)
# # video 3
# label1 = Label(window, text='One', bg='red', fg='white')
# label1.pack()
# label2 = Label(window, text='Two', bg='green', fg='black')
# label2.pack(fill=X)
# label3 = Label(window, text='Three', bg='black', fg="yellow")
# label3.pack(side=LEFT, fill=Y)
# video 4
# label41 = Label(window, text='Name')
# label42 = Label(window, text='Password')
# entry1 = Entry(window)
# entry2 = Entry(window)


# label41.grid(row=0, sticky=E)
# label42.grid(row=1, sticky=E)
# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)
# # video 5
# check = Checkbutton(window, text='Keep me logged in')
# check.grid(columnspan=2)

# # video 6
# def printName():
#     print("Reynir er nafnid")
# takki1 = Button(window, text="Print my name", command=printName)
# takki1.pack()


# # video 8
# class takkar:
#     def __init__(self, master):
#         frame = Frame(master)
#         frame.pack()

#         self.printButton = Button(frame, text='Print message', command=self.printMessage)
#         self.printButton.pack(side=LEFT)

#         self.quitButton = Button(frame, text='Quit', command=frame.quit)
#         self.quitButton.pack(side=LEFT)

#     def printMessage(self):
#         print("Wow, this works!")

# t = takkar(window)

# window.mainloop()






# # Texti
# def welcomeLabel():
#     welcome = Label(text= "Welcome to a game of Yahtzee!")
#     welcome.pack()
#     welcome.place(relx = 0.5, anchor = N)
# welcomeLabel()

# # Takki
# def closeButton():
#     closeButton = Button(text="Close Application", command=quit)
#     closeButton.pack()
#     closeButton.place(relx = 0.5, rely = 0.1, anchor = CENTER)
# closeButton()











# class MyFirstGUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("A simple GUI")

#         self.label = Label(master, text="This is our first GUI!")
#         self.label.pack()

#         self.greet_button = Button(master, text="Greet", command=self.greet)
#         self.greet_button.pack()

#         self.close_button = Button(master, text="Close", command=master.quit)
#         self.close_button.pack()

#     def greet(self):
#         print("Greetings!")

# window = Tk()
# my_gui = MyFirstGUI(window)



from tkinter import *

window = Tk()
window.title('Yahtzee by Reyrey and Danni')
window.geometry("600x600")

frame1 = Frame(window)
frame1.pack()
frame2 = Frame(window)
frame2.pack(anchor=S)
frame3 = Frame(window)
frame3.pack(anchor=S)

def play():
    welcome.forget()
    playButton.forget()

    rollButton = Button(frame2, text="Roll dice", command=rollDice)
    rollButton.pack(anchor=S)

    # ten1 = Button(frame2, text='1', width=dicew, height=diceh)
    # ten2 = Button(frame2, text='2', width=dicew, height=diceh)
    # ten3 = Button(frame2, text='3', width=dicew, height=diceh)
    # ten4 = Button(frame2, text='4', width=dicew, height=diceh)
    # ten5 = Button(frame2, text='5', width=dicew, height=diceh)
    # ten6 = Button(frame2, text='6', width=dicew, height=diceh)
    # ten1.pack(side=LEFT)
    # ten2.pack(side=LEFT)
    # ten3.pack(side=LEFT)
    # ten4.pack(side=LEFT)
    # ten5.pack(side=LEFT)
    # ten6.pack(side=LEFT)
def rollDice():
    ten1 = Button(frame3, text=str(random.randint(1,6)), width=dicew, height=diceh)
    ten2 = Button(frame3, text=str(random.randint(1,6)), width=dicew, height=diceh)
    ten3 = Button(frame3, text=str(random.randint(1,6)), width=dicew, height=diceh)     # bætist bara aftanvið, þarf að hreinsa
    ten4 = Button(frame3, text=str(random.randint(1,6)), width=dicew, height=diceh)     # eða halda einhverjum teningum og kasta aftur
    ten5 = Button(frame3, text=str(random.randint(1,6)), width=dicew, height=diceh)
    ten6 = Button(frame3, text=str(random.randint(1,6)), width=dicew, height=diceh)
    ten1.pack(side=LEFT)
    ten2.pack(side=LEFT)
    ten3.pack(side=LEFT)
    ten4.pack(side=LEFT)
    ten5.pack(side=LEFT)
    ten6.pack(side=LEFT)

welcome = Label(frame1, text="Welcome to Yahtzeee!")
welcome.pack()

playButton = Button(frame1, text="Let's Play", command=play)
playButton.pack(anchor=S)

dicew = 10
diceh = 5



stopButton = Button(frame3, text='Quit game', command=quit)
stopButton.pack()


window.mainloop()