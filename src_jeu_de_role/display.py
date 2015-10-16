# -*- coding:Utf-8 -*-
#  fichier display.py 

#fichier qui concerne le menu du jeu et le journal des quêtes ainsi que l'affichage de l'écran et du jeu

# bibliothèques

from tkinter import *
from tkinter import messagebox
import sys

# variables

TITRE = "Jeu de rôle"
Introduction = "Bonjour et bienvenu dans ce nouveau jeu de rôle !"

WIDTH, HEIGHT = 250, 50

MENU = [
"Que souhaitez vous faire ?",  
"01 : Commencer une nouvelle partie ?",
"02 : Charger une ancienne partie ?",
"03 : Ouvrir l'éditeur du jeu ?",
"Choisissez une option et cliquer sur OK."
]

# fonctions

class Programme():
	'''boucle principale du jeu'''

	def __init__(self):
		self.fenetre = Tk()
		
		self.canvas1 = Canvas(self.fenetre, width=WIDTH, height=HEIGHT)
		self.canvas2 = Canvas(self.fenetre, width=WIDTH, height=HEIGHT)
		self.canvas3 = Canvas(self.fenetre, width=WIDTH, height=HEIGHT)
		self.canvas4 = Canvas(self.fenetre, width=WIDTH, height=HEIGHT)

		self.c1Text = Label(self.canvas1, text=Introduction)

		self.c2Text = self.canvas2.create_text(100, 25, text=MENU[0])

		self.c3Menu = Listbox(self.canvas3, width=40, height=3)
		self.c3Menu.insert(1, MENU[1])
		self.c3Menu.insert(2, MENU[2])
		self.c3Menu.insert(3, MENU[3])

		self.c4text = self.canvas4.create_text(120, 25, text=MENU[4])

		self.frame1 = Frame(self.fenetre, borderwidth=2)

		self.bouOK = Button(self.frame1, text='OK', command=self.choix).pack(side="left")
		self.bouQT = Button(self.frame1, text='QUITTER', command=self.quitter).pack(side="right")


	def boucle(self):
		self.fenetre.title(TITRE)
		self.fenetre.geometry("800x600+500+200")
		self.canvas1.pack()
		self.canvas2.pack()
		self.canvas3.pack()
		self.canvas4.pack()
		self.c3Menu.pack()
		self.c1Text.pack()
		self.frame1.pack()
		self.fenetre.mainloop()

	def choix(self):
		"Ce qu'il se passe selon notre selection dans la liste"
		if True: #if 01 selected
			game.Jeu()
		elif True: #charger une partie
			save.OuvrirFichier()
		else: #éditeur
			editor.Editeur()

	def quitter(self):
		answer = messagebox.askquestion("Quitter le jeu ?", "Souhaitez vous quitter le jeu ?", 
			icon='warning')
		if answer == "yes":
			print("Au revoir!")
			sys.exit()


# programme
