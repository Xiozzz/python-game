# -*- coding:Utf-8 -*-
#  fichier player.py

from tkinter import *
# l'objet joueur, toutes ces interaction avec le monde et les objets

class Joueur(fenetre):

	def __init__(self):
		self.name = self.name()

	def name(self, fenetre):
		"Une fonction qui demande le nom du joueur dans le programme"
		question = Label(fenetre.canvas3, text="Quel est votre nom aventurier ?")
		question.pack()
		reponse = StringVar()
		entree = Entry(fenetre.canvas4, width=30)
		entree.pack()