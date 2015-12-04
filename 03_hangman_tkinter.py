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
import pickle

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

filename = "wordbank"
wordList = []

#functions

def menu():
	"game menu, check, remove, add word in bank words or play new game"
	removeWidgets()
	cleanScreen()
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
	cleanScreen()
	#remove menu button
	#define game entry input
	#define game button ok validation

def wordBank():
	"word bank, to check, add and remove words"
	removeWidgets()
	#open wordBank to display it
	displayWords()

	#define the bank widgets
	inputUser = StringVar()
	wordEntry = Entry(gameInput, textvariable=inputUser, width=20)
	wordEntry.bind('<Return>', lambda e:addWord(inputUser))
	butAdd = Button(gameInput, text="Add Word", command=lambda:addWord(inputUser), height=1, width=13)
	butRem = Button(gameInput, text="Remove Word", command=lambda:remWord(inputUser), height=1, width=13)
	butQt = Button(gameInput, text="Q", command=menu, height=1, width=2)
	gridBankSetup(wordEntry, butAdd, butRem, butQt)

def displayWords():
	"display the words in wordBank"
	global wordList
	cleanScreen()
	px, py = 50, 20
	f = open(filename, 'rb')
	wordList = pickle.load(f) #save a list from the file
	for word in wordList:
		gameScreen.create_text(px, py, text=word, fill=COLORS[3])
		py += 20
		if py > 380:
			px += 100
			py = 20
	f.close()

def cleanBank():
	"clean the Bank file"
	print("cleanBank tests")
	wordBank = open(filename, 'rb')
	words = pickle.load(wordBank)
	print(words)
	wordBank.close()

	wordBank = open(filename, 'wb')
	pickle.dump(wordList, wordBank)
	wordBank.close()

	wordBank = open(filename, 'rb')
	words = pickle.load(wordBank)
	print(words)
	wordBank.close()


def addWord(iu):
	"add word to the wordbank"
	global wordList
	newWord = iu.get().lower()
	if newWord not in wordList and len(newWord) < 9:
		wordList.append(newWord)
		print(newWord,"added to file.")
	elif len(newWord) >= 9:
		print("You word have too much characters. (8 maximum)")
	else:
		print(newWord, "is already in the bank.")
	f = open(filename, 'wb')
	pickle.dump(wordList, f)
	f.close()
	iu.set("")
	displayWords()


def remWord(iu):
	"remove word from the wordbank"
	global wordList
	newWord = iu.get().lower()
	if newWord in wordList:
		wordList.remove(newWord)
		print(newWord,"removed from file.")
	else:
		print(newWord, "is not in the bank.")
	f = open(filename, 'wb')
	pickle.dump(wordList, f)
	f.close()
	iu.set("")
	displayWords()


def gridBankSetup(entry, but1, but2, but3):
	"set the grid for the word bank screen"
	entry.grid(row="1", column="1", padx=10, pady=20)
	but1.grid(row="1", column="2", padx=5, pady=10)
	but2.grid(row="1", column="3", padx=5, pady=10)
	but3.grid(row="1", column="4", padx=5, pady=10)

def gridGameSetup():
	pass

def gridMenuSetup(butStart, butBank, butQuit):
	"set the grid of the menu"
	butStart.grid(row='1', column="1", padx=5, pady=10)
	butBank.grid(row='1', column="2", padx=5, pady=10)
	butQuit.grid(row='1', column="3", padx=5, pady=10)

def gridSetup():
	"set the grid of the main program"
	gameScreen.grid(row="1", column="1", columnspan="3", padx=0, pady=5)
	gameInput.grid(row="2", column="1", columnspan="3", padx=10, pady=5)

def removeWidgets():
	"remove the widget in the main canva and frame"

	for widget in gameInput.winfo_children():
		widget.destroy()

def cleanScreen():
	gameScreen.delete(ALL)

def windowSetup():
	"center in screen the window"
	root.title(TITLE)
	root.resizable(0, 0)
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

	gridSetup()
	menu()
	windowSetup() 
	root.mainloop()