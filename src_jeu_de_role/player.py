# -*- coding:Utf-8 -*-
#  fichier player.py

from tkinter import *
# l'objet joueur, toutes ces interaction avec le monde et les objets

class Joueur():

	def __init__(self, master):
		self.name = self.name(master)

	def name(self, master):
		"Une fonction qui demande le nom du joueur dans le programme"
		question = Label(master, text="Quel est votre nom aventurier ?")
		question.pack()
		reponse = StringVar()
		entree = Entry(master, width=30)
		entree.pack()