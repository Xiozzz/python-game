# -*- coding:Utf-8 -*-
"deviner un nombre avec interface tkinter"

'''
- un menu pour démarrer la partie ou quitter
- l'affichaque du nombre de tours qui diminu (grosse police/font dans une case colorée)
- affichage d'une information qui annonce si le nombre est plus grand ou plus petit dans un rectangle jaune
- si le nombre de tour passe, perdu dans un rectangle rouge
- affichage rectangle vert victoire !
'''

from tkinter import *
import sys
from random import randint
import tkinter.messagebox
import time

#variables

nbChoix = 0
nbTours = 6
nbEssai = []
listNb = ""

#fonctions

def start():
	"Remise à zéro pour une nouvelle partie"
	global nbTours, nbChoix, nbEssai, listNb
	nbTours = 6
	nbChoix = randint(0, 100)
	nbEssai = []
	listNb = ""
	can1.itemconfig(txt1, text="Essayez de deviner le nombre !")
	can1.itemconfig(recJeu, fill="light grey")
	can1.itemconfig(txtJeu, text="")
	can1.itemconfig(txtEssai, text="")
	can1.itemconfig(txtTour, text="Nombre de tours restants : {}".format(nbTours))

def exit():
	sys.exit()

def nouvellePartie():
	"demande si l'on souhaite faire une nouvelle partie"

	answer = tkinter.messagebox.askquestion("Nouvelle partie ?","Voulez vous faire une nouvelle partie ?")
	if answer == "yes":
		start()
	else:
		exit()

def verifNombre(nb):
	"vérifie si le nombre est un nombre"
	c = 0
	
	for i in nb:
		if i in list("1234567890"):
			c += 1

	if c == len(nb):
		return True
	else:
		return False


def escapeKey(event):
	exit()

def returnKey(event):
	jeu()

def jeu():
	global nbTours, nbEssai, listNb
	

	nombre = ent1.get()
	ent1.delete(0, END)
	nbEssai.append(nombre)

	if len(nombre) == 0:
		can1.itemconfig(txt1, text="Vous n'avez rien choisi.")
	elif verifNombre(nombre):
		can1.itemconfig(txt1, text="Vous choisissez {}.".format(nombre))
		comparaison(nombre)
	else:
		can1.itemconfig(txt1, text="Vous n'avez pas choisis un nombre.")

	nbTours -= 1
	can1.itemconfig(txtTour, text="Nombre de tours restants : {}".format(nbTours))
	
	nbEssai.sort()
	for i in nbEssai:
		listNb += " " + i

	can1.itemconfig(txtEssai, text="Vous avez déjà essayé : {}".format(listNb))
	
	if nbTours == 0:
		can1.itemconfig(recJeu, fill="red")
		can1.itemconfig(txtJeu, text="Vous avez\n perdu ! :(")
		nouvellePartie()

def comparaison(nb):
	global nbChoix

	nbComp = int(nb)

	if nbComp == nbChoix:
		can1.itemconfig(recJeu, fill="green")
		can1.itemconfig(txtJeu, text="Vous avez trouvé\n le nombre {} !".format(nbChoix))
	elif nbComp < nbChoix:
		can1.itemconfig(recJeu, fill="orange")
		can1.itemconfig(txtJeu, text="Le nombre est\n plus grand.")
	elif nbComp > nbChoix:
		can1.itemconfig(recJeu, fill="orange")
		can1.itemconfig(txtJeu, text="Le nombre est\n plus petit.")

def flecheHaut():
	"une fleche avec un rectangle et un triangle filled black"
	pass

def flecheBas():
	"une fleche avec un rectangle et un triangle filled black"
	pass

def centrer():
	fenetre.update_idletasks()
	width = fenetre.winfo_width()
	height = fenetre.winfo_height()
	x = fenetre.winfo_screenwidth() // 2 - width // 2
	y = fenetre.winfo_screenheight() // 2 - height // 2
	fenetre.geometry("{}x{}+{}+{}".format(width, height, x, y))

#programme

fenetre = Tk() #fenêtre principale
fenetre.bind("<Escape>", escapeKey)
fenetre.resizable(0,0)

#mise en place du canvas
can1 = Canvas(fenetre, width=200, height=100, bg="light grey")
txt1 = can1.create_text(100, 10, text="Hello, World!")
txtTour = can1.create_text(100, 25, text="Nombre de tours restants : {}".format(nbTours), font="Arial 10 bold")
recJeu = can1.create_rectangle(55, 55, 150, 95, fill="light grey", outline="light grey")
txtJeu = can1.create_text(100, 75, text="")
txtEssai = can1.create_text(100, 40, text="")

#mise en place des inputs
ent1 = Entry(fenetre, width=15)
ent1.bind("<Return>", returnKey)
txt2 = Label(fenetre, text="Choisissez un nombre :")
bouOk = Button(fenetre, text="Ok", command=jeu) #bouton ok pour valider le nombre entrée dans ent1
bouQt = Button(fenetre, text="Quitter", command=fenetre.quit)#bouton quitter

can1.grid(row=1, columnspan=2, column=1, padx=5, pady=5)
ent1.grid(row=3, column=1, sticky="w", padx=10, pady=5)
txt2.grid(row=2, column=1)
bouOk.grid(row=3, column=1, sticky="e", padx=5)
bouQt.grid(row=3, column=2, padx=5, pady=5)

#première partie à remplacer par nouvellePartie()
start()

#définition d'un bouton qui apparait seulement quand nbTours est à 0
bouNP = Button(fenetre, text="Nouvelle Partie", command=start)

centrer()
fenetre.mainloop() #boucle principale