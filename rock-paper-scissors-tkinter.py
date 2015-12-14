# -*- coding:Utf-8 -*-

#libraries
from tkinter import *
from random import randint, choice
import sys


#variables
TITLE = "Rock, Paper, Scissors"
TEXT = ["You have won. :)", "You have lost. :(", "This is tie"]

CHOIX = ["paper", "rock", "scissors"]
WIDTH, HEIGHT = 400, 400
COLOR = ["blue", "yellow", "red", "light grey"]
INTRO = "Welcome in Rock, Paper, Scissors"


flag = 0

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
	
def setGrid():
	"set the grid system for each widgets"
	gameScreen.grid(row=1, column=1, columnspan=4)
	scoreScreen.grid(row=2, column=1, columnspan=4)
	butStart.grid(row=3, column=1, columnspan=3)
	butQuitter.grid(row=3, column=4, pady=5)

def setGame():
	"set the grid for the new game"
	global flag
	flag = 1
	clean()
	setImages()
	butStart.grid_forget()
	butPaper.grid(row=3, column=1, sticky="e")
	butRock.grid(row=3, column=2)
	butScissor.grid(row=3, column=3, sticky="w")
	scoreScreen.itemconfig(scoreTexte, text="Please, Choose Rock, Paper or Scissors.", font=("Helvetica", 10, "bold italic"))

def createImage(x, y, img):
	return gameScreen.create_image(x, y, image=img)

def exit(event):
	sys.exit()

def setImages():
	"bind the mouse to the canvas images"
	
	imgRock = createImage(200, 300, rockimg)
	imgPaper = createImage(300, 150, paperimg)
	imgScissors = createImage(100, 150, scissorsimg)
	
	gameScreen.tag_bind(imgPaper, "<Button-1>", lambda e: play(CHOIX[0]))
	gameScreen.tag_bind(imgRock, "<Button-1>", lambda e: play(CHOIX[1]))
	gameScreen.tag_bind(imgScissors, "<Button-1>", lambda e: play(CHOIX[2]))

def play(chx):
	global flag

	victoire = ""

	if flag == 1:
		clean()
		computer = choice(CHOIX)

		if computer == chx:
			victoire = TEXT[2]
		elif computer == "rock":
			if chx == "paper":
				victoire = TEXT[0]
			if chx == "scissors":
				victoire = TEXT[1]
		elif computer == "scissors":
			if chx == "rock":
				victoire = TEXT[0]
			if chx == "paper":
				victoire = TEXT[1]
		elif computer == "paper":
			if chx == "scissors":
				victoire = TEXT[0]
			if chx == "rock":
				victoire = TEXT[1]

		updateScreen(chx, computer, victoire)
		flag = 0

	else:
		pass

def clean():
	gameScreen.delete("all")

def updateScreen(chxJoueur, chxComputer, victoire):
	butPaper.grid_forget()
	butRock.grid_forget()
	butScissor.grid_forget()
	butStart.grid(row=3, column=1, columnspan=3)

	#recréer les images correspondantes en fonction des choix
	if chxJoueur == CHOIX[0] or chxComputer == CHOIX[0]:
		imgPaper = createImage(300, 150, paperimg)
	if chxJoueur == CHOIX[1] or chxComputer == CHOIX[1]:
		imgRock = createImage(200, 300, rockimg)
	if chxJoueur == CHOIX[2] or chxComputer == CHOIX[2]:
		imgScissors = createImage(100, 150, scissorsimg)



	#changer le scoreTexte
	scoreScreen.itemconfig(scoreTexte, text="You choose {}, computer choose {}, {}".format(chxJoueur, chxComputer, victoire))

#program
if __name__ == "__main__":
	root = Tk()

	#create the differents outputs screen of the game
	gameScreen = createCanva(WIDTH, HEIGHT, COLOR[3])
	scoreScreen = createCanva(WIDTH, 40, COLOR[3])
	scoreTexte = scoreScreen.create_text(200, 20, text=INTRO, font=("Arial", 10))
	
	#create the differents input button of the game
	butPaper = createButton(CHOIX[0], lambda: play(CHOIX[0]))
	butRock = createButton(CHOIX[1], lambda: play(CHOIX[1]))
	butScissor = createButton(CHOIX[2], lambda: play(CHOIX[2]))
	butQuitter = createButton("Q", root.quit)
	butStart = createButton("Start A New Game", setGame)

	#create the differents images of the game
	rockimg = PhotoImage(file="src_rock-paper-scissors/rock.gif")
	paperimg = PhotoImage(file="src_rock-paper-scissors/paper.gif")
	scissorsimg = PhotoImage(file="src_rock-paper-scissors/scissors.gif")

	setGrid()

	setWindow()
	root.mainloop()