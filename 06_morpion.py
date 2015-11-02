# -*- coding:Utf-8 -*-
"le jeu du morpion/Tic Tac Toe"

#bibliothèques importé (random sera utilisé pour l'IA)
import random
import sys
import os
import time

# variables

# définition des noms des RANGS et des COLONNES
RANG = ["r1", "r2", "r3"]
COLN = ["c1", "c2", "c3"]

# traduction des coordonnées visuelles CASE en coordonées RANG/COLONNES
CASES = {
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

# disposition du plateau de jeu
TABLEAU = { 
"r1" : {"c1":0, "c2":0, "c3":0},
"r2" : {"c1":0, "c2":0, "c3":0},
"r3" : {"c1":0, "c2":0, "c3":0},
}

# définition de toutes les victoires possibles
VICTOIRES = [
	["a1", "b2", "c3"],
	["a3", "b2", "c1"],
	["a1", "a2", "a3"],
	["a1", "b1", "c1"],
	["a2", "b2", "c2"],
	["a3", "b3", "c3"],
	["b1", "b2", "b3"],
	["c1", "c2", "c3"]
]

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
"Dommage vous avez perdu ! :(",
"C'est au tour de l'ordinateur de jouer.",
"L'ordinateur choisi de jouer"
]

#fonctions

def afficherTableau(tableau):
	"une grille de 7x6"
	os.system('cls')
	c = 1
	print("\n     a   b   c")
	print("")
	for i in RANG:
		print("%s  | " % c, end="")
		c += 1
		# print("\nligne :", i)
		for x in COLN:
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
		answer = inputPrompt().lower()
		
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
	"retourne une position valide en renversant une valeur qui serait donnée tel que 3a ou c1"
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
	coords = CASES[chx]
	case = tb[coords[0]][coords[1]]
	if case == 0:
		return True
	else:
		return False


def updateTableau(chx, tr, tb):
	"met à jour le tableau en fonction du choix envoyé"
	coords = CASES[chx] #traduit le choix en coordonnées dans le tableau
	if tr == 1:
		tb[coords[0]][coords[1]] = 1
	elif tr == 2:
		tb[coords[0]][coords[1]] = 2
	return tb

def nettoyerTableau(tb):
	"remet toutes les cases à 0"
	for i in RANG:
		for c in COLN:
			tb[i][c] = 0

def verifVictoire(tab, tr):
	"retourne true si une ligne du tableau est complète"
	compteur = 0

	for i in VICTOIRES:
		xy1 = CASES[i[0]]
		xy2 = CASES[i[1]]
		xy3 = CASES[i[2]]
		c1 = tab[xy1[0]][xy1[1]]
		c2 = tab[xy2[0]][xy2[1]]
		c3 = tab[xy3[0]][xy3[1]]
		if c1 == tr and c2 == tr and c3 == tr:
			compteur = 1
		# print("debug01", xy1, xy2, xy3, c1, c2, c3, c1 == tr and c2 == tr and c3 == tr)

	# print("debug02, compteur =", compteur)		
	if compteur == 1:
		return True
	else:
		return False

def tourOrdinateur(tab):
	"vérifie le tableau et les victoires possibles et choisit en conséquence"
	
	casesTop = []
	index = 0

	for i in VICTOIRES:
		compteur = 0 

		#les coordonées de chaque cases
		xy1 = CASES[i[0]]
		xy2 = CASES[i[1]]
		xy3 = CASES[i[2]]
		
		#le contenu de chaque cases :
		c1 = tab[xy1[0]][xy1[1]]
		c2 = tab[xy2[0]][xy2[1]]
		c3 = tab[xy3[0]][xy3[1]]

		#vérifie chaque case et signale le compteur si elle sont occupé
		if c1 > 0:
			compteur += 1
		if c2 > 0:
			compteur += 1
		if c3 > 0:
			compteur += 1

		if compteur == 2:
			casesTop.append({i[0]:"", i[1]:"", i[2]:"", "flag":0})
			casesTop[index][i[0]] = c1
			casesTop[index][i[1]] = c2
			casesTop[index][i[2]] = c3
			index += 1

	if len(casesTop) > 0:
		print(casesTop) #DEBUG
		#écrire le choix de l'ordinateur en fonction de ce qui se présente ici :
		choice = None
		flag1, flag2 = 0, 0

		for i in casesTop:
			print(i)
			for c in i:
				print(c, "case :", i[c])
				if i[c] == 1:
					flag1 += 1
				if i[c] == 2:
					flag2 += 1
			
			if flag1 >= 2:
				i["flag"] = 1
			elif flag2 >= 2:
				i["flag"] = 2
		
		print(casesTop)
		input() #DEBUG

		if choice is not None:
			return choice
		else:
			return random.choice(list(CASES))



	else:
		return random.choice(list(CASES))



def programme():
	"boucle principale, affichage, input et vérification"
	# variable référence du tableau TABLEAU
	tableau = TABLEAU
	nettoyerTableau(tableau) # nettoyage à zéro pour une nouvelle partie
	afficherTableau(tableau) # un premier affichage avant la boucle

	while True:

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
		
		# affichage du jeu pour tour 1
		afficherTableau(tableau)

		# vérification victoire
		if verifVictoire(tableau, tour):
			print(JEU[6])
			time.sleep(2)
			break

		# tour de l'ordinateur
		tour = 2
		print(JEU[8])
		time.sleep(1)

		chxOrdi = tourOrdinateur(tableau)

		while True:
			print("debug:", chxOrdi)
			if verifTableau(chxOrdi, tableau):
				tableau = updateTableau(chxOrdi, tour, tableau)
				break
			else:
				chxOrdi = tourOrdinateur(tableau)

		print(JEU[9], chxOrdi, end=".\n")

		# affichage jeu du tour 2
		afficherTableau(tableau)

		# vérification victoire
		if verifVictoire(tableau, tour):
			print(JEU[7])
			time.sleep(2)
			break


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
			break

		elif reponse == "2":
			sys.exit()

		else:
			print(MENU[3])
			reponse = verifNombre()

if __name__ == "__main__":
	while True:
		menu()