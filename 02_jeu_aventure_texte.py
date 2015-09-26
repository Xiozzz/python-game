# -*- coding:Utf-8 -*-

#bibliothèques

import time


#variables

VERBES = ["aller", "regarder", "ouvrir", "prendre"]


#classes

class objet():
    def __init__(self):
        self.name = "couteau"

class joueur():
    def __init__(self):
        self.name = input("Quel est votre nom ?")

#class lieu():
    


#fonctions

def menu():
    print("Jeux d'aventure")
    time.sleep(1)

def nouvelle_partie():
    #mise à zéro des variables

    #instances du jeu
    joueur = nouveau_joueur()


#programme

if __name__ == '__main__':
    menu()