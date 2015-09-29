# -*- coding:Utf-8 -*-

# bibliothèques

from random import randint

# données

CHOIX = ["Pierre", "Feuille", "Ciseaux"]

# fonctions

def choix_joueur():
	choix = input("Choisissez Pierre, Feuille, Ciseaux !\n>>>")
	while choix != CHOIX[0] and choix != CHOIX[1] and choix != CHOIX[2]:	
		choix = input("Pierre, Feuille ou Ciseaux ?\n>>>")
	print("Vous choisissez", choix)
	return choix

def choix_ordinateur():
	choix = randint(0, 2)
	print("L'ordinateur à choisi", CHOIX[choix])
	return CHOIX[choix]

def verification_jeu(choixJoueur, choixOrdinateur):

	if choixJoueur == choixOrdinateur:
		print("Vous avez tout les deux choisi", choixJoueur, "et vous faites égalité. :)")
	elif choixJoueur == "Pierre":
		if choixOrdinateur == "Feuille":
			print("La feuille recouvre la pierre, vous avez perdu. :(")
		elif choixOrdinateur == "Ciseaux":
			print("Les Ciseaux sont cassé par la pierre, vous avez gagné. :D")
	elif choixJoueur == "Feuille":
		if choixOrdinateur == "Pierre":
			print("La feuille recouvre la pierre, vous avez gagné. :D")
		elif choixOrdinateur == "Ciseaux":
			print("Les ciseaux coupe la feuille, vous avez perdu. :(")
	elif choixJoueur == "Ciseaux":
		if choixOrdinateur == "Pierre":
			print("Les Ciseaux sont cassé par la pierre, vous avez perdu. :(")
		if choixOrdinateur == "Feuille":
			print("Les ciseaux coupe la feuille, vous avez gagné. :D")

def jeu():
	print("************************\nPierre, Feuille, Ciseaux\n************************")
	choixJoueur = choix_joueur()
	choixOrdinateur = choix_ordinateur()
	verification_jeu(choixJoueur, choixOrdinateur)

def menu():

	while True:
		answer = input("-----------------------------\nNouvelle partie ou Quitter ?\n\
-----------------------------\n>>>").lower()
		if answer == "q" or answer == "quitter":
			break
		elif answer == "n" or answer == "nouvelle" or answer == "nouvelle partie":
			jeu()

# programme

menu()