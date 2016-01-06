# -*- coding:Utf-8 -*-
"pong"

'''
- Two paddles, one for the player controled by keyboard, one by computer using IA.
- Score is displayed in the background.
- Menu bar : Start a new game, Pause the game, Quit the game.
'''

#libraries

from tkinter import *
from sys import exit

#datas

TITLE = "Pong with Tkinter"
COLORS = ["lemon chiffon", "dark salmon", "light blue", "chocolate", "firebrick", "ivory"]
WIDTH, HEIGHT = 500, 300

#variables

score = [0, 0]

#class

class Paddle:
	''' paddle object '''

	def __init__(self, x, y):
		self.xcord = x
		self.ycord = y

class Ball:
	''' ball object '''

	def __init__(self, x, y):
		self.xcord = x
		self.ycord = y

#functions


#Game logic

def newGame():
	"reset to default variables and launch a new game"
	print("New Game !! Yes Pong !!")
	pass

#Game display
def displayBoardgame():
	"display background"
	pass

def updateScore():
	"display score in background"
	pass

#Window parameters
def configWindow():
	"main parameters of the program"
	root.title(TITLE)
	root.bind('<Escape>', lambda e: exitWindow())
	root.resizable(0,0)
	root.update_idletasks()
	width = root.winfo_width()
	height = root.winfo_height()
	x = root.winfo_screenwidth()//2 - width//2
	y = root.winfo_screenheight()//2 - height//2
	root.geometry("{}x{}+{}+{}".format(width, height, x, y))
	

def setGameGrid():
	"display main grid of the program"
	gameScrn.grid(row=1, column=1, padx=0, pady=0)
	gameMenu.grid(row=2, column=1, padx=0, pady=0)
	butST.grid(row=1, column=1, padx=20, pady= 5)
	butQT.grid(row=1, column=2, padx=20, pady= 5)

def exitWindow():
	"used to exit the program"
	sys.exit()

#main program

if __name__ == "__main__":
	root = Tk()

	gameScrn = Canvas(root, width = WIDTH, height = HEIGHT, bg=COLORS[5])
	gameMenu = Frame(root, width= WIDTH, height=HEIGHT/4)
	
	butST = Button(gameMenu, text="New Game", command=newGame)
	butQT = Button(gameMenu, text="Quit", command=exitWindow)

	setGameGrid()
	configWindow()
	root.mainloop()