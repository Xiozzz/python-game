# -*- coding:Utf-8 -*-
#hangman game with tkinter

'''
- drawing custom gif format
- the game need to end
'''

#libraries
from tkinter import *
from sys import exit
import pickle
import random

#datas
TITLE = "Hangman"

WIDTH, HEIGHT = 400, 400

COLORS = ["lemon chiffon", "dark salmon", "light blue", "chocolate"]

INFO = [
"Welcome, what do you want to do ?",
"1. Start a new game",
"2. Add or remove words in the bank.",
"3. Quit the game",
"Please write a guess to find the hidden word"
]

filename = "wordbank"
wordList = []
gameWord = ""
hiddenWord = ""
letter_found = []
letter_guesses = []
guesses = 0

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
	"start a new game, get a new random word and start"
	global guesses
	#remove menu buttons and clean game screen
	removeWidgets()
	cleanScreen()
	#det variable to default
	guesses = 0
	#define game entry input
	inputUser = StringVar()
	gameEntry = Entry(gameInput, textvariable=inputUser, width=20)
	gameEntry.bind("<Return>", lambda e:checkGuess(inputUser))
	#define game button ok validation and quit
	butOk = Button(gameInput, text="Submit", command=lambda:checkGuess(inputUser), height=1, width=10)
	butQt = Button(gameInput, text="Quit", command=menu, height=1, width=10)
	gridGameSetup(gameEntry, butOk, butQt)
	#choose a word in the wordList for the game
	gameWord = chooseWord()
	print("DEBUG #1:", gameWord)
	#display an introduction message, the first hidden word and the first picture
	displayWord()
	#update the first game picture
	updatePicture()

def chooseWord():
	"random choice"
	global gameWord
	f = open(filename, 'rb')
	wordList = pickle.load(f) #save the word list from the file
	f.close()
	#choose a random word from list
	gameWord = random.choice(wordList)
	return gameWord

def hideWord():
	"build the hidden word"
	global hiddenWord
	hiddenWord = ""
	for letter in gameWord:
		if letter in letter_found:
			hiddenWord += letter
		else:
			hiddenWord += " _ "
	return hiddenWord

def checkGuess(iu):
	"check if guess right or wrong, redirect to updtabePicture and updateWord"
	global guesses
	cleanScreen() #clean the screen
	guess = iu.get().lower()

	if len(guess) > 0:
		guesses += 1

	if guesses < 7: #max turn before end of the game
		if guess == gameWord:
			#victory
			print("You won! :)")
		elif guess.isalpha() and len(guess) == 1: #if letter
			#add in list letter_guesses
			letter_guesses.append(guess)
			#add in list letter_found if the letter is correct
			if guess in gameWord: 
				letter_found.append(guess)
			else:
				print(guess, "is not in the hidden word.")	
		else:
			#is not alpha or is not a letter or is not the good guess
			print("Sorry, this guess is not correct.")
	else:
		#no more turn avalable, end
		print("You have not saved the man from hanging, game finished. :(")
	
	print("DEBUG #3 : turn", guesses,":", guess)
	print("DEBUG #4 : guesses :", letter_guesses, "found :", letter_found)
	updatePicture()
	displayWord()
	iu.set("")

def updatePicture():
	"display picture depending number of guesses and game message about sucess, lose"
	#change depending the number of turn
	gameScreen.create_rectangle(WIDTH/2+70, HEIGHT/2+70, WIDTH/2-70, HEIGHT/2-70, fill=COLORS[2])

def displayWord():
	"display the Word in gameScreen, the letter/words already tried, number of turn"
	
	#display the hidden word _ _ _
	hiddenWord = hideWord()
	turn = "Turn number : " + str(guesses)
	letters = "Letters : "
	for letter in letter_guesses:
		letters += letter + " "
	
	print("DEBUG #2:", hiddenWord, letters, turn)

	gameScreen.create_text(WIDTH/2, HEIGHT-20, text=INFO[4], fill=COLORS[3], font=("sans-serif", 10) )
	gameScreen.create_text(WIDTH/2, HEIGHT-60, text=hiddenWord, fill=COLORS[1], font=("sans-serif", 20) )
	gameScreen.create_text(WIDTH/2, HEIGHT-80, text=turn, fill=COLORS[3], font=("sans-serif", 10) )
	gameScreen.create_text(WIDTH/2, HEIGHT-100, text=letters, fill=COLORS[3], font=("sans-serif", 10) )


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
	if newWord not in wordList and len(newWord) <= 10:
		wordList.append(newWord)
		print(newWord,"added to file.")
	elif len(newWord) >= 9:
		print("You word have too much characters. ("+str(len(newWord))+" for 10 maximum)")
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

def gridGameSetup(entry, but1, but2):
	entry.grid(row="1", column="1", padx=25, pady=20)
	but1.grid(row="1", column="2", padx=15, pady=10)
	but2.grid(row="1", column="3", padx=15, pady=10)

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