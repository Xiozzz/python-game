# -*- coding:Utf-8 -*-

#libraries
from tkinter import *
from random import randint
import sys

#variables
TITLE = "Rock, Paper, Scissors"
CHOIX = ["papier", "feuille", "ciseau"]
WIDTH, HEIGHT = 400, 400
COLOR = ["blue", "yellow", "red", "light grey"]

#functions
def createButton(t, c):
	return Button(root, text=t, command=c)

def createCanva(w, h, c):
	return Canvas(root, width=w, height=h, bg=c)

def setWindow():
	"set the different options of our window"
	root.update_idletasks()
	root.title(TITLE)
	root.bind("<Escape>", exit)
	width = root.winfo_width()
	height = root.winfo_height()
	x = (root.winfo_screenwidth()//2) - width//2
	y = (root.winfo_screenheight()//2) - height//2
	root.geometry("{}x{}+{}+{}".format(width, height, x, y))
	root.update()
	
def setGrid():
	"set the grid system for each widgets"
	gameScreen.grid(row=1, column=1, columnspan=4)
	scoreScreen.grid(row=2, column=1, columnspan=4)
	butPaper.grid(row=3, column=1)
	butRock.grid(row=3, column=2)
	butScissor.grid(row=3, column=3)
	butQuitter.grid(row=3, column=4)

def exit(event):
	sys.exit()

def choice(chx):
	print(chx)

#program
if __name__ == "__main__":
	root = Tk()

	#create the differents outputs screen of the game
	gameScreen = createCanva(WIDTH, HEIGHT, COLOR[3])
	scoreScreen = createCanva(WIDTH, HEIGHT/8, COLOR[3])
	
	#create the differents input button of the game
	butPaper = createButton(CHOIX[0], lambda: choice(CHOIX[0]))
	butRock = createButton(CHOIX[1], lambda: choice(CHOIX[1]))
	butScissor = createButton(CHOIX[2], lambda: choice(CHOIX[2]))
	butQuitter = createButton("Q", root.quit)

	setGrid()

	setWindow()
	root.mainloop()