# -*- coding:Utf-8 -*-
"jeu quatre en ligne"

#bibliothèques importé (random sera utilisé pour l'IA)
import random
import sys

# variables

TABLEAU = { 
"r1" : {"c1":0, "c2":0, "c3":0},
"r2" : {"c1":0, "c2":0, "c3":0},
"r3" : {"c1":0, "c2":0, "c3":0},
}

JOUEUR = "O"
ORDI = "X"

TITRE = "=======\nJeu de Morpion\n=======\n"

MENU = [
"Choisissez une option :", 
"1) Commencer une nouvelle partie.", 
"2) Quitter", 
"Vous ne pouvez choisir qu'entre 1 et 2 :"
]

#fonctions

def afficherTableau(tableau):
	"une grille de 7x6"
	for i in range(7):
		print(i, end=' |')
	print()


def verifNombre():
	"vérification que l'input est bien d'un nombre"
	answer = input(">>>")
	while answer not in list("1234567890"):
		print("Choisissez un nombre s'il vous plait :")
		answer = input(">>>")
	return answer
	 


def programme():
	"boucle principale, affichage, input et vérification"
	# instance du tableau
	tableau = TABLEAU
	 
	while True:
		# affichage jeu
		afficherTableau(tableau)
		input()

		# tour du joueur

		# vérification victoire

		# tour de l'ordinateur

		# vérification victoire


def menu():
	print(TITRE)
	print(MENU[0])
	print(MENU[1])
	print(MENU[2])
	
	reponse = verifNombre()

	while True:
		if reponse == "1":
			programme()

		elif reponse == "2":
			sys.exit()

		else:
			print(MENU[3])
			reponse = verifNombre()

if __name__ == "__main__":
	menu()