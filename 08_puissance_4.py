# -*- coding:Utf-8 -*-
"jeu quatre en ligne"

#bibliothèques importé (random sera utilisé pour l'IA)
import random

# variables

TABLEAU = { 
"r1" : {"c1":0, "c2":0, "c3":0, "c4":0, "c5":0, "c6":0, "c7":0},
"r2" : {"c1":0, "c2":0, "c3":0, "c4":0, "c5":0, "c6":0, "c7":0},
"r3" : {"c1":0, "c2":0, "c3":0, "c4":0, "c5":0, "c6":0, "c7":0},
"r4" : {"c1":0, "c2":0, "c3":0, "c4":0, "c5":0, "c6":0, "c7":0},
"r5" : {"c1":0, "c2":0, "c3":0, "c4":0, "c5":0, "c6":0, "c7":0},
"r6" : {"c1":0, "c2":0, "c3":0, "c4":0, "c5":0, "c6":0, "c7":0},
}

JOUEUR = "O"
ORDI = "X"

#fonctions

def afficherPlanche():
	"une grille de 7x6"
	for i in range(7):
		print(i, end=' |')
	print()




def programme():

	# affichage jeu

	# tour du joueur

	# vérification victoire

	# tour de l'ordinateur

	# vérification victoire


def menu():
	print("=======\nJeu de quatre en ligne\n=======")

if __name__ == "__main__":
	afficherPlanche()