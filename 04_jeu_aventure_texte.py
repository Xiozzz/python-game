# -*- coding:Utf-8 -*-

#bibliothèques

import time
import random
import sys

# données

OBJETS = {
"couteau" : {
"nom" : "Couteau",
"description" : "long et aiguisé, attention à ne pas vous couper",
"situation" : "un couteau se trouve sur le lit",
"points" : 2
}, 
"tomate" : {
"nom" : "Tomate",
"description" : "bien mûr, elle semble bien juteuse",
"situation" : "Il y a une tomate sur la petite table",
"points" : 2
}
}

LIEUX ={
"chambre" : {
"nom" : "Chambre", 
"description" : "Il s'agit d'une petite salle avec un lit sans draps, tout les meubles sont vides.",
"choix" : ["couloir", "couteau"]
}, 
"salon" : {
"nom" : "Salon", 
"description" : "Il s'agit d'une pièce avec une petite table, les murs frais ont été repeints il n'y a pas longtemps.",
"choix" : ["couloir", "tomate"]
},
"couloir" : {
"nom" : "Couloir",
"description" : "Il s'agit d'un couloir étroit, il y a deux portes, l'une allant vers la chambre, l'autre vers le salon.",
"choix" : ["chambre", "salon"]}
}

ACTIONS = ["aller", "regarder", "ouvrir", "prendre", "utiliser", "info", "aide"]

PLAN ='''
 _________
|  |      |
|  /      |
|  |______|
|  |      |
|  /      |
|__|______|

''' 

#classes

class Objet():
    def __init__(self, dict):
        self.nom = dict["nom"]
        self.description = dict["description"]
        self.situation = dict["situation"]
        self.points = dict["points"]

class Joueur():
    def __init__(self):
        self.nom = input("Quel est votre nom ?")
        self.inventaire = []
        self.score = 0
        self.pre_situation = ""
        self.nou_situation = ""

    def ajout_inventaire(self, objet):
        self.inventaire.append(objet)
        self.score += objet.points

    def control_inventaire(self):
        for i in self.inventaire:
            print(i)


class Lieu():
    def __init__(self, dict):
        self.nom = dict["nom"]
        self.description = dict["description"]
        self.choix = dict["choix"]

#fonctions


def decoupage_commande(commande):
    c = commande.split()
    c0, c1 = "", ""
    if len(c) == 1:
        c0 = c[0]
        return c0, c1
    elif len(c) == 2:
        c0 = c[0]
        c1 = c[1]
        return c0, c1
    else:
        print("ce n'est pas une commande valide.")

def verification_action(a):
    if a in ACTIONS:
        print("vous avez choisi", a, "OK")
        return False

    else:
        print(a, "n'est pas une bonne commande")
        return True

def verification_objet(o, j):
    if o in j.nou_situation.choix:
        print("vous avez choisi", o, "OK")
        return False

    elif len(o) == 0:
        return False
    
    else:
        print(o, "n'est pas un objet possible")
        return True
    
def choix_action(joueur):
    verifa, verifo = True, True
    while verifa or verifo:
        commande = input("Que souhaitez vous faire ?\n>>>")
        action, objet = decoupage_commande(commande)
        verifa = verification_action(action)
        verifo = verification_objet(objet, joueur)
        print(verifa, verifo)
    return action, objet

def redirection_commande(action):
    '''fonction centrale du jeu qui redirigine l'action du joueur vers la fonction correspondante'''
    pass

def afficher_situation(j):
    if j.pre_situation != j.nou_situation:
        print("\n----\nVous vous trouvez dans :", j.nou_situation.nom)
        print(j.nou_situation.description, "\n----\n")
        j.pre_situation = j.nou_situation

def nouvelle_partie():

    # création des objets instances
    joueur = Joueur()
    couteau = Objet(OBJETS["couteau"])
    tomate = Objet(OBJETS["tomate"])
    chambre = Lieu(LIEUX["salon"])
    salon = Lieu(LIEUX["salon"])
    couloir = Lieu(LIEUX["couloir"])

    # situation de départ
    joueur.pre_situation = salon
    joueur.nou_situation = couloir

    print("Bonjour %s \nC'est parti !" % joueur.nom)
    time.sleep(1)

    # déroulement du jeu  
    while joueur.score < 10:
        afficher_situation(joueur)
        action = choix_action(joueur)
        print(action)
        redirection_commande(action)

    print('Victoire !')

def menu():
    print("\n===============\nJeux d'aventure\n===============")
    print(PLAN)
    nouvelle_partie()

#programme

if __name__ == '__main__':
    menu()