# -*- coding:Utf-8 -*-
# Le jeu de nim : https://fr.wikipedia.org/wiki/Jeux_de_Nim


import random
import sys
import os

BATON = {'a' : ' _  ', 'b' : '|x| ', 'c' : '|_| '}

NOMBRE = 20

PYRAMIDE = {"1" : 1, "2" : 3, "3" : 5, "4" : 7}

AIDE = {
"Ligne" : "Dans cette variante,une seule ligne de baton, le gagnant est celui qui\
 prend le dernier baton, celui qui est le dernier à jouer, gagne.",
"Pyramide" : "cinqs lignes de batons de quantités différentes (1, 3, 5, 7), on prend\
 sur une ligne autant de baton que l'on souhaite celui qui prend le dernier baton à perdu."
 }

class Ligne():
	'''Variante 1, jeu de nim sur une seule ligne'''

	def __init__(self):
		self.nbBaton = NOMBRE

	def boucle(self):
		os.system('cls')
		print(AIDE["Ligne"])
		while self.nbBaton > 0:
			afficher_baton(self.nbBaton)
			self.nbJoueur = self.tour_joueur()
			self.baton_update(self.nbJoueur)

	def tour_joueur(self):
		print("------\nTour du joueur :\n------")
		self.nb = input("Combien de baton souhaitez vous retirer de la ligne ?\n>>>")
		while self.nb not in ['1', '2', '3']:
			self.nb = input("Vous ne pouvez choisir qu'entre 1, 2 ou 3\n>>>")
		print("Vous choisissez de retirer", self.nb, "baton(s).")
		return self.nb

	def tour_ordi(self):
		pass

	def baton_update(self, nb):
		self.nbBaton -= int(nb)
		print(self.nbBaton)

class Pyramide():
	'''Variante 2, jeu de nim sur une pyramide'''

	def _init_(self):
		print("pyramide!!")
		pass

	def boucle():
		print(AIDE["Pyramide"])




def afficher_baton(x):
	print(BATON['a']*x)
	print(BATON['b']*x)
	print(BATON['b']*x)
	print(BATON['c']*x)

def menu():
	print("Jeu de Nim")
	print("Quelle variante du jeu de nim souhaitez vous jouer ?")
	print("1) Batons en ligne")
	print("2) Batons en pyramide")
	answer = input(">>>")
	
	while answer != "1" and answer != "2" and answer != "q":
		answer = input("Variante 1 ou 2 ?")
	
	if answer == "1":
		jeu = Ligne()
		jeu.boucle()

	elif answer == "2":
		jeu = Pyramide()

	else:
		print("Bye")

if __name__ == "__main__":
	menu()