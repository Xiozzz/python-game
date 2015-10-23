# -*- coding:Utf-8 -*-
# display py version 2, utilisation de grid à la place de pack

from tkinter import *
from tkinter import messagebox

TITRE = "Jeu de rôle tkinter"

WIDTH, HEIGHT = 600, 400

MENU = [
"01 : Commencer une nouvelle partie ?",
"02 : Charger une ancienne partie ?",
"03 : Ouvrir l'éditeur du jeu ?"
]

QUESTION = "Que souhaitez vous faire ?"

ASTUCE = "Sélectionnez et cliquer sur OK."

ERREUR = "Rien n'est selectionné dans la liste."


class Affichage:

	def __init__(self):
		#mise en place de la fenêtre
		self.fenetre = Tk()
		self.fenetre.title(TITRE)
		self.positioningScreen()

		#instantiation des différentes frames et canvas du jeu
		self.fGauche = Frame(self.fenetre, width= 100, height= 350)
		self.fBas = Frame(self.fenetre, width = 600, height = 50)
		self.fDroitTop = Canvas(self.fenetre, width = 500, height = 250)
		self.fDroitBottom = Canvas(self.fenetre, width = 500, height = 100)
		self.positioningGrid()

		#boucle attente d'events
		self.menu()
		self.boutons()
		self.fenetre.mainloop()
		

	def positioningScreen(self):
		"positionne la fenêtre au centre de l'écran"
		self.wS = self.fenetre.winfo_screenwidth()
		self.hS = self.fenetre.winfo_screenheight()
		self.xW = self.wS/2 - WIDTH/2
		self.yW = self.hS/2 - HEIGHT/2
		self.fenetre.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, self.xW, self.yW))


	def positioningGrid(self):
		"positionne la grille des frames et canvas dans la fenêtre"
		self.fGauche.grid(row=0, column=0, rowspan=2)
		self.fBas.grid(row=2, column=0, columnspan=2)
		self.fDroitTop.grid(row=0, column=1)
		self.fDroitBottom.grid(row=1, column=1)

	def menu(self):
		self.question = Label(self.fDroitBottom, text=QUESTION)
		self.menu = Listbox(self.fDroitBottom, width=40, height=3)
		for i in MENU:
			self.menu.insert(END, i)
		self.question.grid(row="0", column="0")
		self.menu.grid(row="1", column="0")

	def boutons(self):
		self.bOk = Button(self.fBas, text="Ok", command=self.validation)
		self.bQt = Button(self.fBas, text="Quitter", command=self.quitter)
		self.text = Label(self.fBas, text=ASTUCE)
		self.text.grid(row="0", column="1", pady=5)
		self.bOk.grid(row="0", column="2", padx = 10)
		self.bQt.grid(row="0", column="3", padx = 10)

	def validation(self):
		"Ce qu'il se passe selon notre selection dans la liste"
		self.erreur = self.fDroitTop.create_text(250, 240, text="")
		select = self.menu.curselection()

		if select == ():
			self.fDroitTop.itemconfig(self.erreur, text=ERREUR)
				
		elif select[0] == 0: #lancement d'une nouvelle partie
			self.clean()
			self.jeu = game.Jeu(self.fenetre)
			self.jeu.chargement(self.fenetre)
		
		elif select[0] == 1: #charger une partie
			print("No saving system feature implemented yet")
		
		elif select[0] == 2: #éditeur
			print("No editor system feature implemented yet")


	def clean(self):
		self.fDroitTop.delete("all")
		self.fDroitBottom.delete("all")
		self.menu.destroy()
		self.bOk.destroy()
		self.question.destroy()
		self.text.destroy()

	def quitter(self):
		# sys.exit()
		answer = messagebox.askquestion("Quitter le jeu ?", "Souhaitez vous quitter le jeu ?", 
			icon='warning')
		if answer == "yes":
			print("Au revoir!")
			sys.exit()
		