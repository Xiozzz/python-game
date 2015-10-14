# -*- coding:Utf-8 -*-
#  fichier display.py 

#fichier qui concerne le menu du jeu et le journal des quêtes ainsi que l'affichage de l'écran et du jeu

# bibliothèques

import tkinter as tk

# variables

TITRE = "Jeu de rôle"
Introduction = "Bonjour et bienvenu dans ce nouveau jeu de rôle !"

WIDTH, HEIGHT = 100, 100




# fonctions

class Programme():
	'''boucle principale du jeu'''

	def __init__(self):
		self.fenetre = tk.Tk()
		#self.canvas = tk.Canvas(self.fenetre, width=WIDTH, height=HEIGHT)
		self.texte = tk.Label(self.fenetre, text=Introduction)

		self.MENU = tk.Listbox(self.fenetre)
		self.MENU.insert(1, "Que souhaitez vous faire ?")
		self.MENU.insert(2, "01 : Commencer une nouvelle partie ?")
		self.MENU.insert(3, "02 : Charger une ancienne partie ?")
		self.MENU.insert(4, "03 : Ouvrir l'éditeur du jeu ?")

	def boucle(self):
		self.texte.pack()
		self.fenetre.title(TITRE)
		self.fenetre.geometry("800x600+500+200")
		#self.canvas.pack()
		self.MENU.pack()
		self.fenetre.mainloop()


# programme
