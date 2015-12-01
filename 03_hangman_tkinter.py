# -*- coding:Utf-8 -*-
"hangman game with tkinter"

'''
- pixel art custom gif format
- start game, make vanish title and start button, make appear drawing, score, letter found, letter asked, user entry input, button ok
- datas in text file (open, read, w, r, readline, readlines, etc) for bank words
- menu, add or remove word in the wordbank
'''
#libraries
from tkinter import *
from sys import exit

#datas
TITLE = "Hangman"

WIDTH, HEIGHT = 400, 400

COLORS = ["lemon chiffon", "dark salmon", "light blue", "chocolate"]

INFO = [
"Welcome, what do you want to do ?",
"1. Start a new game",
"2. Add or remove words in the bank.",
"3. Quit the game"
]

wordBank = "wordbank.txt"

#functions

def menu():
	"game menu, check, remove, add word in bank words or play new game"
	gameTitle = gameScreen.create_text(WIDTH/2, HEIGHT/6, text=TITLE, fill=COLORS[1], font=("sans-serif", 20))
	menuInfo1 = gameScreen.create_text(WIDTH/2, HEIGHT/2, text=INFO[0], fill=COLORS[3], font=("sans-serif", 12))
	menuInfo2 = gameScreen.create_text(WIDTH/2, HEIGHT/2+30, text=INFO[1], fill=COLORS[3], font=("sans-serif", 10))
	menuInfo3 = gameScreen.create_text(WIDTH/2, HEIGHT/2+60, text=INFO[2], fill=COLORS[3], font=("sans-serif", 10))
	menuInfo4 = gameScreen.create_text(WIDTH/2, HEIGHT/2+90, text=INFO[3], fill=COLORS[3], font=("sans-serif", 10))

	#define menu buttons, start new game, bank access, exit game
	butStart = Button(gameInput, text="1. Start a New Game", command=newGame, height=2, width=20)
	butBank = Button(gameInput, text="2. Word Bank Access", command=wordBank, height=2, width=20)
	butQuit = Button(gameInput, text="Quit", command=exitRoot, height=2, width=8)
	gridMenuSetup(butStart, butBank, butQuit)

def newGame():
	print("Hello, World!")
	removeWidgets()
	#remove menu button
	#define game entry input
	#define game button ok validation

def wordBank():
	"word bank, to check, add and remove words"
	print("Time to go to the bank")
	removeWidgets()
	#check the file wordbanb.txt and display all the words

def addWord(word):
	"menu"
	words = open(wordBank, "a")
	words.write(word)
	words.close()


def gridBankSetup():
	pass

def gridGameSetup():
	pass

def gridMenuSetup(butStart, butBank, butQuit):
	"set the grid of the main program"
	gameScreen.grid(row="1", column="1", columnspan="3", padx=0, pady=5)
	gameInput.grid(row="2", column="1", columnspan="3", padx=10, pady=5)
	butStart.grid(row='1', column="1", padx=5, pady=10)
	butBank.grid(row='1', column="2", padx=5, pady=10)
	butQuit.grid(row='1', column="3", padx=5, pady=10)

def removeWidgets():
	"remove the widget in the main canva and frame"

	for widget in gameInput.winfo_children():
		widget.destroy()

	gameScreen.delete(ALL)

def windowSetup():
	"center in screen the window"
	root.title(TITLE)
	root.bind("<Escape>", lambda e: exitRoot())
	root.update_idletasks()
	width = root.winfo_width()
	height = root.winfo_height()
	x = root.winfo_screenwidth()//2 - width//2
	y = root.winfo_screenheight()//2 - height//2
	root.geometry("{}x{}+{}+{}".format(width, height, x, y))

def exitRoot():
	sys.exit()

#main program

if __name__ == "__main__":
	root = Tk()

	#define main canva and frame
	gameScreen = Canvas(root, width=WIDTH, height=HEIGHT, bg=COLORS[0])
	gameInput = Frame(root, bg=COLORS[2])

	menu()
	windowSetup() 
	root.mainloop()