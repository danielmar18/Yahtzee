from tkinter import *

HEIGHT=500
WIDTH=500

window = Tk()
window.title('Yahtzee by Reyrey and Danni')
Frame(width=WIDTH, height=HEIGHT).pack()

def welcomeLabel():
    welcome = Label(text= "Welcome to a game of Yahtzee!")
    welcome.pack()
    welcome.place(relx = 0.5, anchor = N)
welcomeLabel()
def closeButton():
    closeButton = Button(text="Close Application", command=quit)
    closeButton.pack()
    closeButton.place(relx = 0.5, rely = 0.1, anchor = CENTER)
closeButton()





window.mainloop()

















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
