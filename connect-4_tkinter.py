# -*- coding:utf-8 -*-
"connect 4 // puissance 4"

'''
- don't win if I play a6, b6, b5, b4, b3. why?
- no IA yet ?
'''


#librairies
from tkinter import *
from prettytable import PrettyTable
from random import choice
import sys
import os

#datas
TITLE = "Connect 4 - Puissance 4"
WIDTH, HEIGHT = 400, 400

COLORS = ["lemon chiffon", "dark salmon", "light blue", "chocolate", "firebrick", "ivory"]

ALPHA = "abcdefg"

POSITIONS = [
'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 
'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 
'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 
'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 
'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 
'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6'
]

#variables
spaces = []

tableOccupation = {
'd4': 0, 'b4': 0, 'c6': 0, 'c1': 0, 'e4': 0, 'b6': 0, 'f3': 0, 'g4': 0, 'g2': 0, 
'e6': 0, 'g5': 0, 'c4': 0, 'f1': 0, 'a4': 0, 'a2': 0, 'a1': 0, 'e3': 0, 'c5': 0,
'd5': 0, 'c3': 0, 'b2': 0, 'c2': 0, 'e2': 0, 'e5': 0, 'd2': 0, 'b3': 0, 'e1': 0,
'd1': 0, 'd6': 0, 'g6': 0, 'a5': 0, 'g1': 0, 'a3': 0, 'd3': 0, 'b1': 0, 'a6': 0,
'f2': 0, 'g3': 0, 'b5': 0, 'f4': 0, 'f5': 0, 'f6': 0
}

#functions
def newGame():
	"start a new game"
	buildTable()
	tableOccupationDefault()
	gameScrn.bind("<Button-1>", click)

def tableOccupationDefault():
	"set tableOccupation to default"
	for pos in POSITIONS:
		tableOccupation[pos] = 0

def click(event):
	"game turn when player use click event"
	victory = 0
	flag = 0
	x = event.x
	y = event.y

	for space in reversed(spaces):
		coord = gameScrn.coords(space[1])
		if x > coord[0] and x < coord[2] and y > 30 and y < 320:
			if checkOccupation(space[0]):
				#draw circle
				drawCircle(coord, COLORS[0])
				tableOccupation[space[0]] = 1
				flag = 1
				break
	
	victory = checkVictory('player')

	if flag == 1 and victory == 0: #computer turn
		spaceName = checkComputer()
		coord = findCoord(spaceName)
		drawCircle(coord, COLORS[1])
		victory = checkVictory('computer')

	debugTable()

def checkComputer():
	"check the computer choice"
	while True:
		compChoice = choice(list(ALPHA))
		for c in range(6, 0, -1):
			spaceName = compChoice+str(c)
			if tableOccupation[spaceName] == 0:
				tableOccupation[spaceName] = 2
				return spaceName 

def findCoord(name):
	"find the coordinates with space name"
	for space in spaces:
		if name in space:
			return gameScrn.coords(space[1])

def checkOccupation(name):
	"check occupation"
	if tableOccupation[name] == 0:
		return True
	else:
		return False

def drawCircle(coord, color):
	"draw the circle in coord from color"
	coordx = coord[0]+20
	coordy = coord[1]+20
	gameScrn.create_oval(coordx-15, coordy-15, coordx+15, coordy+15, fill=color)

def debugTable():
	"print the table occupation in console"
	os.system('cls')
	table = PrettyTable(["a","b","c","d","e","f","g"])
	table.padding_width = 2
	newRow = []
	c = 0
	for pos in POSITIONS:
		newRow.append(pos+':'+str(tableOccupation[pos]))
		c += 1
		if c % 7 == 0:
			c = 0
			table.add_row(newRow)
			newRow = []
	print(table)

def checkVictory(turn):
	print(turn)
	playerOccupation = []
	computerOccupation = []

	for letter in ALPHA:
		for number in range(6, 0, -1):
			position = letter+str(number)
			if tableOccupation[position] == 1:
				playerOccupation.append(position)
			if tableOccupation[position] == 2:
				computerOccupation.append(position)

	if turn == "player":
		win = victoryPositions(playerOccupation)
		if win == 1:
			victory(turn)
			return 1
		else:
			return 0

	if turn == "computer":
		win = 0
		win = victoryPositions(computerOccupation)
		if win == 1:
			victory(turn)
			return 1
		else:
			return 0

def victoryPositions(occupation):
	"check all the victory position"
	for pos in occupation:
		up = 0
		right = 0
		diagonal = 0

		posIndex = ALPHA.index(pos[0]) #index of the position in ALPHA
		#check up of position
		if int(pos[1]) > 3:
			for x in range(0, 4):
				tocheck = pos[0] + str(int(pos[1]) - x)
				print(tocheck)
				if tocheck in occupation:
					up += 1
			# print("DEBUG up =", up)
			tocheck = ''

		#check right of position
		if posIndex < 4:
			for x in range(0, 4):
				tocheck = (ALPHA[posIndex+x] + pos[1])
				print(tocheck)
				if tocheck in occupation:
					right += 1
			# print("DEBUG right =", right)
			tocheck = ''
		
		#check diagonal of position
		if int(pos[1]) > 3 and posIndex < 4:
			for x in range(0, 4):
				tocheck = (ALPHA[posIndex+x] + str(int(pos[1]) - x))
				print(tocheck)
				if tocheck in occupation:
					diagonal += 1
			# print("DEBUG diagonale =", diagonal)
			tocheck = ''

		if up == 4 or right == 4 or diagonal == 4:
			return 1
		else:
			return 0
				

def victory(turn):
	"display a game victory screen"
	print("VICTORY of", turn)	
	gameScrn.unbind("<Button-1>")
	gameScrn.create_text(WIDTH/2, HEIGHT/2, text=turn.upper()+" WON", font=('Arial', 30))

def buildTable():
	global spaces
	# spaces = []
	# main framework
	gameScrn.create_rectangle(20, 20, WIDTH-20, HEIGHT-20, fill=COLORS[2], width=0)
	# 6 x 7 spaces
	c = 0
	x, y = 30, 30
	size = 40
	while c < 42:
		space = gameScrn.create_rectangle(x, y, x+size, y+size, fill=COLORS[5], width=0)
		spaces.append((POSITIONS[c], space))
		c += 1
		x += size+10

		if c % 7 == 0:
			x = 30
			y += size+10

def configWindow():
	root.title(TITLE)
	root.bind('<Escape>', lambda e: exitWindow())
	root.resizable(0,0)
	root.update_idletasks()
	width = root.winfo_width()
	height = root.winfo_height()
	x = root.winfo_screenwidth()//2 - width//2
	y = root.winfo_screenheight()//2 - height//2
	root.geometry("{}x{}+{}+{}".format(width, height, x, y))

def setGrid():
	gameScrn.grid(row=1, column=1, padx=0, pady=0)
	gameMenu.grid(row=2, column=1, padx=0, pady=0)
	butST.grid(row=1, column=1, padx=20, pady= 5)
	butQT.grid(row=1, column=2, padx=20, pady= 5)

def exitWindow():
	sys.exit()

#program
if __name__ == "__main__":
	root = Tk()

	gameScrn = Canvas(root, width= WIDTH, height=HEIGHT, highlightthickness=0)
	gameMenu = Frame(root, width= WIDTH, height=HEIGHT/4, highlightthickness=0)
	
	butST = Button(gameMenu, text="New Game", command=newGame)
	butQT = Button(gameMenu, text="Quit", command=exitWindow)

	setGrid()
	configWindow()
	root.mainloop()