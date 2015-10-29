# -*- coding:Utf-8 -*-
"le jeu du morpion/Tic Tac Toe"

#bibliothèques importé (random sera utilisé pour l'IA)
import random
import sys
import os

# variables

RANG = ["r1", "r2", "r3"]
CASE = ["c1", "c2", "c3"]

COORDINATES = {
"a1" : ["r1", "c1"],
"a2" : ["r2", "c1"],
"a3" : ["r3", "c1"],
"b1" : ["r1", "c2"],
"b2" : ["r2", "c2"],
"b3" : ["r3", "c2"],
"c1" : ["r1", "c3"],
"c2" : ["r2", "c3"],
"c3" : ["r3", "c3"],
}

TABLEAU = { 
"r1" : {"c1":0, "c2":0, "c3":0},
"r2" : {"c1":0, "c2":0, "c3":0},
"r3" : {"c1":0, "c2":0, "c3":0},
}

TITRE = "==============\nJeu du Morpion\n==============\n"

MENU = [
"Choisissez une option :\n", 
"1) Commencer une nouvelle partie.", 
"2) Quitter", 
"Vous ne pouvez choisir qu'entre 1 et 2 :"
]

JEU = [
"=====Votre tour=====",
"Choisissez la colonne et la ligne dans laquelle vous souhaitez jouer.",
"Choisissez un nombre s'il vous plait.",
"Choisissez la colonne 'a', 'b' ou 'c' ET la ligne '1', '2' ou '3'. (ex : 'a1')",
"Il faut donner seulement deux paramètres, une lettre et un chiffre. (ex : 'a1')",
"Cette case à déjà été choisi, choisissez en une autre s'il vous plaît.",
"Bravo vous avez gagné ! :)",
"Dommage vous avez perdu ! :("
]

#fonctions

def afficherTableau(tableau):
	"une grille de 7x6"
	c = 1
	print("\n     a   b   c")
	print("")
	for i in RANG:
		print("%s  | " % c, end="")
		c += 1
		# print("\nligne :", i)
		for x in CASE:
			# print("case", x, ":", end=" ")
			if tableau[i][x] == 0:
				print(".", "|", end=" ")
			elif tableau[i][x] == 1:
				print("X", "|", end=" ")
			elif tableau[i][x] == 2:
				print("O", "|", end=" ")
		if i == "r3":
			break #permet d'éviter la dernière ligne
		print("\n", "  - - - - - - -")
	print("\n")


def inputPrompt():
	answer = input(">>>")
	return answer


def verifNombre():
	"vérification que l'input est bien d'un nombre"
	answer = inputPrompt()
	while answer not in list("1234567890"):
		print(JEU[2])
		answer = inputPrompt()
	return answer

 
def verifInput():
	"vérification que l'input est bien une lettre"
	print(JEU[0])
	print(JEU[1])
	while True:
		answer = inputPrompt()
		
		if len(answer) == 2:
			answer = reverseText(answer)

		if len(answer) < 2 or len(answer) > 2:
			print(JEU[4])
		elif answer[0] in list("abc") and answer[1] in list("123") and len(answer) == 2:
			verif = 0
			break
		else:
			print(JEU[3])
	return answer


def reverseText(string):
	newString = ""
	if string[0] in list("123"):
		newString += string[1]
	if string[1] in list("abc"):
		newString += string[0]

	if len(newString) == 2:
		return newString
	else:
		return string


def verifTableau(chx, tb):
	"vérifie si la case n'a pas déjà été choisi, return false si elle est prise, true si elle est libre"
	coords = COORDINATES[chx]
	case = tb[coords[0]][coords[1]]
	if case == 0:
		return True
	else:
		return False


def updateTableau(chx, tr, tb):
	"met à jour le tableau en fonction du choix envoyé"
	coords = COORDINATES[chx] #traduit le choix en coordonnées dans le tableau
	if tr == 1:
		tb[coords[0]][coords[1]] = 1
	elif tr == 2:
		tb[coords[0]][coords[1]] = 2
	return tb

def verifVictoire(tab):
	"retourne true si une ligne du tableau est complète"
	return False


def programme():
	"boucle principale, affichage, input et vérification"
	# instance du tableau
	tableau = TABLEAU
	 
	while True:
		# affichage jeu
		os.system('cls')
		afficherTableau(tableau)

		# tour du joueur
		tour = 1
		chxJoueur = verifInput()
		while True:
			if verifTableau(chxJoueur, tableau):
				tableau = updateTableau(chxJoueur, tour, tableau)
				break
			else:
				print("\n", JEU[5], "\n")
				chxJoueur = verifInput()

		# vérification victoire
		if verifVictoire(tableau):
			print(JEU[6])

		# tour de l'ordinateur
		tour = 2

		# vérification victoire
		if verifVictoire(tableau):
			print(JEU[7])


def menu():
	os.system('cls')
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