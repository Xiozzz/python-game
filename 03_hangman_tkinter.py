# -*- coding:Utf-8 -*-
"hangman game with tkinter"

'''
- pixel art custom gif format
- start game, make vanish title and start button, make appear drawing, score, letter found, letter asked, user entry input, button ok
'''
#libraries
from tkinter import *
from sys import exit

#datas
TITLE = "Hangman"
WIDTH, HEIGHT = 400, 400
COLORS = ["lemon chiffon", "dark salmon", "light blue"]
#functions
def newGame():
	print("Hello, World!")

def gridSetupStart():
	"set the grid of the main program"
	gameScreen.grid(row="1", column="1", columnspan="3", padx=0, pady=5)
	gameInput.grid(row="2", column="1", columnspan="3", padx=10, pady=5)
	butStart.grid(row='1', column="2", padx=(WIDTH//2)-75, pady=10)

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

	#define game 
	gameTitle = gameScreen.create_text(WIDTH/2, HEIGHT/2, text=TITLE, fill=COLORS[1], font=("sans-serif", 20))

	#define game entry

	#define game buttons, start new game, ok validation inpu, exit game
	butStart = Button(gameInput, text="Start a New Game", command=newGame, height=2, width=20)

	gridSetupStart()
	windowSetup() 
	root.mainloop()