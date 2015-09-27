# -*- coding:Utf-8 -*-
'''simple jeu d'aventure'''

#bibliothèques

import time
import random
import sys

# données

OBJETS = {
"couteau" : {"nom" : "couteau", "description" : "long et aiguisé, attention à ne pas se couper"}, 
"tomate" : {"nom" : "tomate", "description" : "bien mûr, elle semble bien juteuse"}
}

LIEUX ={
"chambre01" : {"nom" : "chambre 01", "description" : "Il s'agit d'une petite salle, tout les meubles et objets \
sont renversé sur le sol."}, 
"chambre02" : {"nom" : "chambre 02", "description" : "Il s'agit d'une pièce vide, les murs frais ont été repeints \
il n'y a pas longtemps."},
"couloir" : {"nom" : "couloir", "description" : "Un couloir étroit, il y a deux portes."}
}

ACTIONS = ["aller", "regarder", "ouvrir", "prendre"]

#classes

class Objet():
    def __init__(self, dict):
        self.nom = dict["nom"]
        self.description = dict["description"]

class Joueur():
    def __init__(self):
        self.nom = input("Quel est votre nom ?")
        self.race = ""
        self.inventaire = []
        self.situation = "couloir"

    def ajout_inventaire(self, objet):
        self.inventaire.append(objet)

    def control_inventaire(self):
        for i in self.inventaire:
            print(i)

    def choix_race(self):
        self.race = input("Choix de la race : Elf, Homme ou Nain ?")

class Lieu():
    def __init__(self, dict):
        self.nom = dict["nom"]
        self.description = dict["description"]

#fonctions

def action_joueur():
    action = input("Quel est votre action ?\n>>>")
    while action not in ACTIONS:
        action = input("Ce n'est pas une action possible.\n>>>")
    return action


def nouvelle_partie():
    
    print("C'est parti !")
    #création des variables
    score = 0

    #création des instances
    joueur = Joueur()
    couteau = Objet(OBJETS["couteau"])
    tomate = Objet(OBJETS["tomate"])
    chambre_01 = Lieu(LIEUX["chambre01"])
    chambre_02 = Lieu(LIEUX["chambre02"])
    couloir = Lieu(LIEUX["couloir"])

    #jeu
    print("Debug 01 :", joueur.nom, couteau.nom, ":", tomate.description )
    print("Debut 02 :", chambre_01.nom, ":", couloir.description)
    joueur.choix_race()
    print(joueur.race)
    print("Vous vous trouvez dans :", joueur.situation)
    while score < 10:
        action = action_joueur()

def menu():
    print("Jeux d'aventure")
    time.sleep(1)
    nouvelle_partie()

#programme

if __name__ == '__main__':
    menu()