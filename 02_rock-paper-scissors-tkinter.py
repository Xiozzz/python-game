# -*- coding:Utf-8 -*-

#libraries
from tkinter import *
from random import randint
import sys


#variables
TITLE = "Rock, Paper, Scissors"
CHOIX = ["paper", "rock", "scissors"]
WIDTH, HEIGHT = 400, 400
COLOR = ["blue", "yellow", "red", "light grey"]
INTRO = "Welcome in Rock, Paper, Scissors"

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
	butStart.grid(row=3, column=1, columnspan=3)
	butQuitter.grid(row=3, column=4, pady=5)

def setGame():
	butStart.grid_forget()
	butPaper.grid(row=3, column=1, sticky="e")
	butRock.grid(row=3, column=2)
	butScissor.grid(row=3, column=3, sticky="w")
	scoreScreen.itemconfig(scoreTexte, text="Please, Choose Rock, Paper or Scissors.", font=("Helvetica", 10, "bold italic"))

def createImage(x, y, img):
	return gameScreen.create_image(x, y, image=img)

def exit(event):
	sys.exit()

def choice(chx):
	print(chx)

#program
if __name__ == "__main__":
	root = Tk()

	#create the differents outputs screen of the game
	gameScreen = createCanva(WIDTH, HEIGHT, COLOR[3])
	scoreScreen = createCanva(WIDTH, 40, COLOR[3])
	scoreTexte = scoreScreen.create_text(200, 20, text=INTRO, font=("Arial", 10))
	
	#create the differents input button of the game
	butPaper = createButton(CHOIX[0], lambda: choice(CHOIX[0]))
	butRock = createButton(CHOIX[1], lambda: choice(CHOIX[1]))
	butScissor = createButton(CHOIX[2], lambda: choice(CHOIX[2]))
	butQuitter = createButton("Q", root.quit)
	butStart = createButton("Start A New Game", setGame)

	#create the differents images of the game
	rockimg = PhotoImage(file="src02_rock-paper-scissors/rock.gif")
	paperimg = PhotoImage(file="src02_rock-paper-scissors/paper.gif")
	scissorsimg = PhotoImage(file="src02_rock-paper-scissors/scissors.gif")
	imgRock = createImage(100, 100, rockimg)
	imgPaper = createImage(100, 200, paperimg)
	imgScissors = createImage(100, 300, scissorsimg)

	setGrid()

	setWindow()
	root.mainloop()