# -*- coding:Utf-8 -*-
#  fichier game.py

from tkinter import *
from src_jeu_de_role import player

class Jeu():
	'''boucle principale du jeu'''

	def __init__(self, parent):
		intro="C'est parti !"
		txt1 = Label(parent, text=intro)
		txt1.pack()

	def chargement(self, parent):
		"met en place les éléments du jeu"
		#Le joueur
		self.joueur = player.Joueur(parent)
		#Le monde

		