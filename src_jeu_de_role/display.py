# -*- coding:Utf-8 -*-
#  fichier display.py 

#fichier qui concerne le menu du jeu et le journal des quêtes ainsi que l'affichage de l'écran et du jeu

# bibliothèques

from tkinter import *
from tkinter import messagebox
import sys

from src_jeu_de_role import game

# variables

TITRE = "Jeu de rôle"
Introduction = "Bonjour et bienvenu dans ce nouveau jeu de rôle !"

WIDTH, HEIGHT = 400, 50

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

		self.c1Text = self.canvas1.create_text(200, 25, text=Introduction)
		self.c2Text = self.canvas2.create_text(200, 25, text=MENU[0])

		self.c3Menu = Listbox(self.canvas3, width=40, height=3)
		self.c3Menu.insert(1, MENU[1])
		self.c3Menu.insert(2, MENU[2])
		self.c3Menu.insert(3, MENU[3])

		self.c4Text = self.canvas4.create_text(200, 25, text=MENU[4])

		self.frame1 = Frame(self.fenetre, borderwidth=2)

		self.bouOK = Button(self.frame1, text='OK', command=self.choix)
		self.bouQT = Button(self.frame1, text='QUITTER', command=self.quitter)

	def boucle(self):
		self.fenetre.title(TITRE)
		self.fenetre.geometry("800x400+550+350")
		self.canvas1.pack()
		self.canvas2.pack()
		self.canvas3.pack()
		self.canvas4.pack()
		self.c3Menu.pack()
		self.frame1.pack(side="bottom")
		self.bouOK.pack(side="left")
		self.bouQT.pack(side="right")
		self.fenetre.mainloop()

	def clean(self):
		self.canvas1.delete(self.c1Text)
		self.canvas2.delete(self.c2Text)
		self.c3Menu.destroy()
		self.canvas4.delete(self.c4Text)
		self.bouOK.destroy()

	def choix(self):
		"Ce qu'il se passe selon notre selection dans la liste"
		select = self.c3Menu.curselection()

		if select == ():
			print("Rien n'est selectionné dans la liste.")
				
		elif select[0] == 0: #lancement d'une nouvelle partie
			self.clean()
			self.jeu = game.Jeu(self.fenetre)
			self.jeu.boucle(self.fenetre)
		
		elif select[0] == 1: #charger une partie
			pass
		
		elif select[0] == 2: #éditeur
			pass

	def quitter(self):
		answer = messagebox.askquestion("Quitter le jeu ?", "Souhaitez vous quitter le jeu ?", 
			icon='warning')
		if answer == "yes":
			print("Au revoir!")
			sys.exit()


# programme
