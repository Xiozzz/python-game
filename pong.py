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

TITLE = "Pong Game"
COLORS = ["cornflower blue", "dark salmon", "royal blue", "chocolate", "firebrick", "ivory", "gainsboro"]
WIDTH, HEIGHT = 550, 350
TURNS = ["PLAYER", "COMPUTER"]

#variables

score = [0, 0]
gameFlag = 0

#class

class Paddle:
	''' paddle object '''

	def __init__(self, x, y, color):
		self.paddle = gameScrn.create_rectangle(x-10, y-40, x+10, y+40, fill=color, width=0)
		self.xcoord = x
		self.ycoord = y

	def moveUp(self):
		if gameFlag == 1:
			self.ycoord -= 5
			gameScrn.coords(self.paddle, self.xcoord-10, self.ycoord-40, self.xcoord+10, self.ycoord+40)

	def moveDown(self):
		if gameFlag == 1:
			self.ycoord += 5
			gameScrn.coords(self.paddle, self.xcoord-10, self.ycoord-40, self.xcoord+10, self.ycoord+40)

class Ball:
	''' ball object '''

	def __init__(self, x, y):
		self.ball = gameScrn.create_oval(x-10, y-10, x+10, y+10, fill=COLORS[1], width=0)
		self.xcord = x
		self.ycord = y

	def movement(self):
		if gameFlag == 0:
			#move
			pass

#functions

def newGame():
	"reset to default variables and launch a new game"
	global gameFlag
	print("New Game !! Yes Pong !!")
	gameFlag = 1
	pass

def pauseGame():
	"pause the game"
	gameFlag = 0

def stopGame():
	"stop game and return to menu"
	gameFlag = 0

#Game display
def displayBoardgame():
	"display background"
	gameScrn.create_line(WIDTH/2, 10, WIDTH/2, HEIGHT-10, fill=COLORS[6], width=2) #center
	gameScrn.create_line(10, 10, WIDTH-10, 10, fill=COLORS[6], width=2) #up side
	gameScrn.create_line(10, HEIGHT-10, WIDTH-10, HEIGHT-10, fill=COLORS[6], width=2) #down side
	gameScrn.create_line(10, 10, 10, HEIGHT-10, fill=COLORS[6], width=2) #left side
	gameScrn.create_line(WIDTH-10, 10, WIDTH-10, HEIGHT-10, fill=COLORS[6], width=2) #right side

def displayScore():
	"score in background"
	#player score
	gameScrn.create_text(WIDTH/4*3, 20, text=TURNS[0], fill=COLORS[0], font=("Helvetica", 12))
	gameScrn.create_text(WIDTH/4*3, 35, text=score[0], fill=COLORS[0], font=("Helvetica", 12))
	#computer score
	gameScrn.create_text(WIDTH/4, 20, text=TURNS[1], fill=COLORS[3], font=("Helvetica", 12))
	gameScrn.create_text(WIDTH/4, 35, text=score[1], fill=COLORS[3], font=("Helvetica", 12))

#Window parameters
def configWindow():
	"main parameters of the program"
	root.update_idletasks()
	root.title(TITLE)
	root.bind('<Escape>', lambda e: exitWindow())
	root.resizable(0,0)
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

	gameScrn = Canvas(root, width = WIDTH, height = HEIGHT, bg=COLORS[5], highlightthickness=0)
	gameMenu = Frame(root, width= WIDTH, height=HEIGHT/4)

	butST = Button(gameMenu, text="New Game", command=newGame)
	butQT = Button(gameMenu, text="Quit", command=exitWindow)

	# draw background and score
	displayBoardgame()
	displayScore()

	# create paddles
	playerPad = Paddle(WIDTH-20, HEIGHT/2, COLORS[2])
	computerPad = Paddle(20, HEIGHT/2, COLORS[4])

	# create ball
	gameBall = Ball(WIDTH/2, HEIGHT/2)

	# bind up and down to the game screen
	gameScrn.bind("<Down>", lambda e: playerPad.moveDown())
	gameScrn.bind("<Up>", lambda e: playerPad.moveUp())
	gameScrn.focus_set()

	setGameGrid()
	configWindow()
	root.mainloop()
