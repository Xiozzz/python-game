# -*- coding:Utf-8 -*-
# Le jeu de nim : https://fr.wikipedia.org/wiki/Jeux_de_Nim


import random
import sys
import os
import time

TITRE = "=============\nLe jeu de Nim\n============="

BATON = {'a' : ' _  ', 'b' : '|x| ', 'c' : '|_| '}

NOMBRE = 20

PYRAMIDE = {"1" : 1, "2" : 3, "3" : 5, "4" : 7}

AIDE = {
"Ligne" : "Dans cette variante sur une seule ligne de baton, le gagnant est celui qui\
 prend le dernier baton, celui qui est le dernier à jouer en retirant ce baton, gagne.",
"Pyramide" : "Dans cette variante sur cinqs lignes de batons de quantités différentes (1, 3, 5, 7),\
 on prend sur une ligne autant de baton que l'on souhaite celui qui prend le dernier baton à gagné."
 }

class Ligne():
	'''Variante 1, jeu de nim sur une seule ligne'''

	def __init__(self):
		self.nbBaton = NOMBRE

	def afficher_baton(self, nb):
		print(BATON['a'] * nb)
		print(BATON['b'] * nb)
		print(BATON['b'] * nb)
		print(BATON['c'] * nb)

	def boucle(self):

		os.system('cls')
		print(TITRE, '\n')
		print(AIDE["Ligne"], '\n')
		input("Appuyez sur <<Entrée>> pour commencer.")

		while True:

			#mise à jour de l'affichage du jeu
			os.system('cls')
			self.afficher_baton(self.nbBaton)

			#tour du joueur
			self.turn = 1
			self.nbJoueur = self.tour_joueur()
			self.baton_update(self.nbJoueur)
			self.verif_victoire(self.nbBaton, self.nbJoueur, self.turn)

			if self.nbBaton <= 0:
				break

			#mise à jour de l'affichage du jeu
			os.system('cls')
			self.afficher_baton(self.nbBaton)

			#tour de l'ordinateur
			self.turn = 0
			self.nbOrdi = self.tour_ordi()
			self.baton_update(self.nbOrdi)
			self.verif_victoire(self.nbBaton, self.nbOrdi, self.turn)

			if self.nbBaton <= 0:
				break


	def tour_joueur(self):
		print("------\nTour du joueur :\n------")
		self.nb = input("Combien de baton souhaitez vous retirer de la ligne ?\n>>>")
		while self.nb not in ['1', '2', '3']:
			self.nb = input("Vous ne pouvez choisir qu'entre 1, 2 ou 3\n>>>")
		return self.nb

	def tour_ordi(self):
		print("------\nTour de l'ordinateur :\n------")
		time.sleep(1)
		self.nb = random.randint(1, 3)
		return self.nb

	def baton_update(self, nb):
		self.nbBaton -= int(nb)
		#print(self.nbBaton)

	def verif_victoire(self, nb, choix, turn):
		if turn == 1 and self.nbBaton <= 0:
			print('Vous retirez le dernier baton.\nVous avez gagné ! :)')
			time.sleep(2)

		elif turn == 1:
			print("Vous choisissez de retirer", choix, "baton(s).")
			time.sleep(2)

		elif turn == 0 and self.nbBaton <= 0:
			print("L'ordinateur retire le dernier baton.\nVous avez perdu ! :(")
			time.sleep(2)

		elif turn == 0:
			print("L'ordinateur enlève", choix, "baton(s).")
			time.sleep(2)


class Pyramide():
	'''Variante 2, jeu de nim sur une pyramide'''

	def _init_(self):
		print("pyramide!!")
		pass

	def boucle(self):
		print(TITRE, '\n')
		print(AIDE["Pyramide"])


def menu():
	while True:
		os.system('cls')
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
			jeu.boucle()

		else:
			print("Bye")
			os.exit()


if __name__ == "__main__":
	#menu()
	jeu = Pyramide()
	jeu.boucle()