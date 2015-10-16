# -*- coding:Utf-8 -*-
#  fichier game.py

from tkinter import *
from src_jeu_de_role import player

class Jeu():
	'''boucle principale du jeu'''

	def __init__(self, master):
		intro="C'est parti !"
		txt1 = Label(master, text=intro)
		txt1.pack()

	def boucle(self, master):
		joueur = player.Joueur(master)

		