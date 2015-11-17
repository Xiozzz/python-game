# -*- coding:Utf-8 -*-
#  fichier player.py

from tkinter import *
# l'objet joueur, toutes ces interaction avec le monde et les objets

class Joueur():

	def __init__(self, parent):
		self.valide = '' #Une variable qui recueille les réponses aux questions.

		self.nom = self.nom(parent)

	def nom(self, parent):
		"Une fonction qui demande le nom du joueur dans le programme"
		self.text1 = "Quel est votre nom aventurier ?"
		self.text2 = "Votre nom"
		self.question(parent, self.text1, self.text2)
		print("DEBUG 1, nom cherché")
		# self.debug = Label(parent, text=self.nom).pack()

	def question(self, parent, question, temp):
		"return une valeur entrée dans un widget Entry"
		self.question = Label(parent, text=question)
		self.question.pack()
		self.reponse = StringVar()
		self.input = Entry(parent, width=30, textvariable=self.reponse)
		self.input.pack()
		self.reponse.set(temp)
		self.bouton(parent, "Ok", self.validation)
		self.bouton(parent, "Afficher Nom", self.afficherNom)
		# self.bouOK = Button(parent, text="Ok", command=self.validation)
		# self.bouOK.pack()
		print("DEBUG 2 question")

	def validation(self):
		self.valide = self.reponse.get() 
		#self.question.destroy()
		#self.input.destroy()
		# self.bouOK.destroy() // Créer un canvas avec le bouOk pour le détruire
		print("DEBUG 3, boutton OK pressed")

	def bouton(self, parent, texte, commande):
		self.bou = Button(parent, text=texte, command=commande)
		self.bou.pack()

	def afficherNom(self):
		print(self.valide, self.nom)