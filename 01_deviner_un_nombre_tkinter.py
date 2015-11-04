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

#variables ?

#fonctions

def start():
	can1.itemconfig(txt1, text="Essayez de deviner le nombre !")
	tours = 6

def exit(event):
	sys.exit()

#programme

tours = 6
fenetre = Tk() #fenêtre principale
fenetre.bind("<Escape>", exit)
fenetre.resizable(0,0)

#mise en place du canvas
can1 = Canvas(fenetre, width=200, height=100, bg="light grey")
txt1 = can1.create_text(100, 10, text="Hello, World!")

#mise en place des inputs
ent1 = Entry(fenetre, width=15)
txt2 = Label(fenetre, text="Choisissez un nombre :")
bouOk = Button(fenetre, text="Ok") #bouton ok pour valider le nombre entrée dans ent1
bouQt = Button(fenetre, text="Quitter", command=fenetre.quit)#bouton quitter

can1.grid(row=1, columnspan=2, column=1, padx=5, pady=5)
ent1.grid(row=3, column=1, sticky="w", padx=10, pady=5)
txt2.grid(row=2, column=1)
bouOk.grid(row=3, column=1, sticky="e", padx=5)
bouQt.grid(row=3, column=2, padx=5, pady=5)

#nouvelle partie
start()

#définition d'un bouton qui apparait seulement quand tours est à 0
bouNP = Button(fenetre, text="Nouvelle Partie", command=start)

fenetre.mainloop() #boucle principale