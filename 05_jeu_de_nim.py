# -*- coding:Utf-8 -*-
# Le jeu de nim : https://fr.wikipedia.org/wiki/Jeux_de_Nim

import random
import sys
import os
import time

TITRE = "=============\nLe jeu de Nim\n============="

BATON = {'a' : ' _  ', 'b' : '|x| ', 'c' : '|_| '}

NOMBRE = 13

PYRAMIDE = {"1" : 1, "2" : 3, "3" : 5, "4" : 7}

AIDE = {
"Ligne" : "Dans cette variante sur une seule ligne de baton, le gagnant est celui qui\
 prend le dernier baton.\nCelui qui est le dernier à jouer en retirant ce baton, gagne.",
"Pyramide" : "Dans cette variante sur cinqs lignes de batons de quantités différentes (1, 3, 5 et 7).\
 \nOn prend sur une ligne autant de baton que l'on souhaite celui qui prend le dernier baton à gagné."
 }

class Ligne():
	'''Variante 1, jeu de nim sur une seule ligne'''

	def __init__(self):
		self.nbBaton = NOMBRE

	def afficher_baton(self, nb):
		"affiche le baton par le nombre de fois nb"
		print(BATON['a'] * nb)
		print(BATON['b'] * nb)
		print(BATON['b'] * nb)
		print(BATON['c'] * nb)

	def boucle(self):
		"boucle principale du jeu"

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
		self.dernier = self.verif_ligne()
		if self.dernier:
			return self.dernier
		return self.nb

	def baton_update(self, nb):
		self.nbBaton -= int(nb)

	def verif_ligne(self):
		"vérifie s'il y a 3 batons, et en retire suffisamment pour gagner"
		if self.nbBaton == 3:
			return 3
		elif self.nbBaton == 2:
			return 2
		else:
			return 0

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

	def __init__(self):
		self.nbBaton = PYRAMIDE.copy()

	def boucle(self):
		"boucle principale du jeu"

		os.system('cls')
		print(TITRE, '\n')
		print(AIDE["Pyramide"], '\n')
		input("Appuyez sur <<Entrée>> pour commencer.")

		while True:

			#mise à jour écran
			time.sleep(2)
			os.system('cls')
			self.afficher_baton()

			#tour du joueur
			self.turn = 1
			self.chxJoueur = self.choix_joueur()
			self.update_baton(self.chxJoueur)
			self.v = self.verif_victoire(self.turn)
			if self.v:
				break

			#mise à jour écran
			time.sleep(2)
			os.system('cls')
			self.afficher_baton()

			#tour de l'ordinateur
			self.turn = 0
			self.chxOrdi = self.choix_ordi()
			self.update_baton(self.chxOrdi)
			self.v = self.verif_victoire(self.turn)
			if self.v:
				break


	def choix_joueur(self):
		"le joueur choisi une colonne et un baton"
		print("\n=====À votre tour====")
		print("\nDans quelle ligne souhaitez vous prendre des batons ?")
		self.ligne = self.verif_nb("ligne")

		while True:

			if self.nbBaton[self.ligne] <= 0:
				print("Il n'y a plus de baton à la ligne", self.ligne, end='.\n')
				self.ligne = input("Choisissez de nouveau une ligne.\n>>>")

			else:
				self.baton = self.verif_baton(self.ligne)
				return [self.ligne, self.baton]


	def choix_ordi(self):
		"prend aléatoirement un baton dans une des ligne disponible"
		print("\n=====Tour de l'ordinateur====")
		self.ligne = str(random.randint(1, 4))
		self.dernierJeu = self.verif_lignes() 

		while True:

			if self.dernierJeu: #voir fonction self.verif_lignes()
				return [self.dernLigne, self.nbBaton[self.dernLigne]]

			elif self.nbBaton[self.ligne] <= 0:
				self.ligne = str(random.randint(1, 4))

			else:
				self.baton = random.randint(1, self.nbBaton[self.ligne])
				print("\nL'ordinateur retire", self.baton, "baton(s) de la ligne", self.ligne, end='.\n')
				return [self.ligne, self.baton]

	def verif_lignes(self):
		"cette fonction retourne la ligne s'il ne reste qu'une seule ligne"
		self.resteUneLigne = 0
		self.dernLigne = ""

		for i in self.nbBaton:
			if self.nbBaton[i] > 0:
				self.resteUneLigne += 1
				self.dernLigne = i

		if self.resteUneLigne == 1:
			return 1

		else:
			return 0

	def verif_baton(self, ligne):
		"vérifie si il reste suffisamment de baton pour répondre à la demande du joueur"
		
		self.bMax = self.nbBaton[ligne]
		print("Il reste", self.bMax, "baton(s) sur la ligne", ligne)
		print("Combien de baton souhaitez vous retirer de la ligne", ligne, "?")
		
		while True:
			self.b = self.verif_nb('baton')

			if self.b <= 0 and self.bMax == 1:
				print("Vous devez retirer le dernier baton.")

			elif self.b <= 0 and self.bMax != 1:
				print("Il faut que vous preniez entre 1 et", self.bMax, "batons.")

			elif self.b > self.bMax:
				print("Vous ne pouvez pas prendre plus que", self.bMax, "batons.")

			elif self.b <= self.bMax:
				print("Vous retirez", self.b, "batons de la ligne", ligne)
				return self.b


	def verif_nb(self, ch):
		"vérifie si l'input est bien numérique"
		while True:
			
			if ch == "baton":
				self.nb = input(">>> ") 

				if self.nb in list("1234567890"):
					self.nb = int(self.nb)
					return self.nb

				else:
					print("Vous devez entrer une valeur numérique entre 1 et 9.")

			if ch == "ligne":
				self.nb = input(">>> ")

				if self.nb in list("1234"):
					return self.nb

				else:
					print("Vous devez entrer une valeur numérique entre 1 et 4.")



	def verif_victoire(self, turn):
		"vérifie s'il reste des batons dans la pyramide et si non, annonce le vainceur"
		self.end = 0

		for i in self.nbBaton:
			if self.nbBaton[i] > 0:
				self.end += 1

		if self.end == 0 and turn == 0:
			print("L'ordinateur à retiré le dernier baton, vous avez perdu ! :(")
			input()
			return True

		elif self.end == 0 and turn == 1:
			print("Vous avez retiré le dernier baton, vous avez gagné ! :)")
			input()
			return True

		else:
			return False

	def update_baton(self, chx):
		"mise à jour du nombre de batons"
		ligne = chx[0]
		baton = chx[1]
		self.nbBaton[ligne] -= baton

	def afficher_baton(self):
		"affichage du tableau de jeu"
		x = 1
		while x < 5:
			print("\nLigne", x, ":")
			print(BATON['a'] * self.nbBaton[str(x)])
			print(BATON['b'] * self.nbBaton[str(x)])
			print(BATON['b'] * self.nbBaton[str(x)])
			print(BATON['c'] * self.nbBaton[str(x)])
			x += 1


def menu():
	while True:
		os.system('cls')
		print(TITRE, '\n')
		print("Quelle variante du jeu de nim souhaitez vous jouer ?")
		print("1) Batons en ligne")
		print("2) Batons en pyramide")
		print("q) Quitter")
		answer = input("\n>>> ")
		
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
			sys.exit()


if __name__ == "__main__":
	menu()