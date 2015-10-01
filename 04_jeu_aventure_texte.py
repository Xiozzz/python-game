# -*- coding:Utf-8 -*-
'''
Un jeu d'aventure texte simple,
-Les fonctionnalités que je souhaite ajouter :
-La possibilité de prendre un objet dans le monde
-La possibilité de regarder les objets du monde ou de l'inventaire
-La possibilité de regarder son inventaire ou la carte du monde
-La possibilité d'interagir avec un objet
-La mise à jour de la carte du monde en fonction de son déplacement
-La possibilité d'avoir de l'aide, pour connaître les commandes (+ introduction au départ)
-Un système de score pour pouvoir finir le jeu (gagner des points en ramassant les objet et en les utilisant)
'''
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
},
"porte" : {
"nom" : "Porte",
"description" : "une porte en bois",
"situation" : "",
"points" : 0
}
}

LIEUX ={
"chambre" : {
"nom" : "une chambre", 
"description" : "Il s'agit d'une petite salle avec un lit sans draps, tout les meubles sont vides.",
"choix_situation" : ["couloir"],
"choix_objet" : ["porte", "couteau"]
}, 
"salon" : {
"nom" : "un salon", 
"description" : "Il s'agit d'une pièce avec une petite table, les murs frais ont été repeints il n'y a pas longtemps.",
"choix_situation" : ["couloir"],
"choix_objet" : ["porte", "tomate"]
},
"couloir" : {
"nom" : "un couloir",
"description" : "Il s'agit d'un couloir étroit, il y a deux portes, l'une allant vers la chambre, l'autre vers le salon.",
"choix_situation" : ["chambre", "salon"],
"choix_objet" : ["porte"]
}
}

ACTIONS = ["aller", "regarder", "ouvrir", "prendre", "utiliser", "info", "aide", "carte"]

PLAN ='''
 _________
|  |      |
|  /      |
|  |______|
|X |      |
|  /      |
|__|______|

''' 

#classes

class Objet():
    def __init__(self, dicto):
        self.nom = dicto["nom"]
        self.description = dicto["description"]
        self.situation = dicto["situation"]
        self.points = dicto["points"]

class Joueur():
    def __init__(self):
        #self.nom = input("Quel est votre nom ?")
        self.nom = "Charlie" #debug
        self.score = 0
        self.pre_situation = ""
        self.nou_situation = ""
    
        self.inventaire = []
        self.obj_possibles = []

    def ajout_inventaire(self, objet):
        self.inventaire.append(objet)
        self.score += objet.points

    def control_inventaire(self):
        for i in self.inventaire:
            print(i)

    def changement_situation(self, ns):
        self.pre_situation = self.nou_situation
        self.nou_situation = ns


class Lieu():
    def __init__(self, dictl):
        self.nom = dictl["nom"]
        self.description = dictl["description"]
        self.choix_situation = dictl["choix_situation"]
        self.choix_objet = dictl["choix_objet"]

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
        #print("vous avez choisi l'action", a, "OK") #debug
        return False

    else:
        print(a, "n'est pas une bonne commande")
        return True

def verification_objet(o, j):
    if o in j.nou_situation.choix_situation or o in j.nou_situation.choix_objet:
        #print("vous avez choisi l'objet ou le lieu", o, "OK") #debug
        return False

    elif len(o) == 0:
        return False
    
    else:
        print(o, "n'est pas un objet ou un lieu possible")
        return True
    
def choix_action(joueur):
    verifa, verifo = True, True
    while verifa or verifo:
        commande = input("Que souhaitez vous faire ?\n>>>").lower()
        action, objet = decoupage_commande(commande)
        verifa = verification_action(action)
        verifo = verification_objet(objet, joueur)
    return action, objet

def redirection_commande(a, j):
    '''fonction centrale du jeu qui redirigine l'action du joueur vers la fonction correspondante'''
    if a[0] == "aller" and a[1] in j.nou_situation.choix_situation:
        l = Lieu(LIEUX[a[1]]) # une nouvelle instance lieu est créé
        j.changement_situation(l) # et permet de mettre à jour la situation du joueur

    elif a == "regarder":
        afficher_situation(j)

    elif a == "quitter":
        pass

    elif a == "info":
        pass

    elif a == "aide":
        pass

def afficher_situation(j):
    if j.pre_situation != j.nou_situation:
        print("\n----")
        print("Vous vous trouvez dans ", j.nou_situation.nom, ".")
        print(j.nou_situation.description)
        for o in j.obj_possibles:
            if o in j.inventaire or len(o.situation) < 1:
                pass
            else:
                print(o.situation)

        print("----\n")
        j.pre_situation = j.nou_situation


def objets_possibles(j):
    j.obj_possibles = []
    for o in j.nou_situation.choix_objet:
        no = Objet(OBJETS[o])
        j.obj_possibles.append(no)


def nouvelle_partie():

    # création des objets instances
    joueur = Joueur()

    # situation de départ
    joueur.pre_situation = Lieu(LIEUX["salon"])
    joueur.nou_situation = Lieu(LIEUX["couloir"])

    print("Bonjour %s \nC'est parti !" % joueur.nom)
    time.sleep(1)

    # déroulement du jeu  
    while joueur.score < 10:
        objets_possibles(joueur) #mise à jour du joueur et des objets avec lesquels il peut entrer en relation
        afficher_situation(joueur)
        action = choix_action(joueur)
        redirection_commande(action, joueur)

    print('Victoire !')

def menu():
    print("\n===============\nJeux d'aventure\n===============")
    print(PLAN)
    nouvelle_partie()

#programme

if __name__ == '__main__':
    menu()