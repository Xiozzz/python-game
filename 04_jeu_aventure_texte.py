# -*- coding:Utf-8 -*-
'''
Un jeu d'aventure texte simple, exploration, interaction avec objets,
-Les fonctionnalités que je souhaite ajouter :
-La possibilité de prendre un objet dans le monde
-La possibilité de regarder les objets du monde ou de l'inventaire - ok, commande regarder
-La possibilité de regarder son inventaire, son status ou la carte du monde - ok, commande info
-La possibilité d'interagir avec un objet
-La mise à jour de la carte du monde en fonction de son déplacement - pas pour ce jeu
-La possibilité d'avoir de l'aide, pour connaître les commandes (+ introduction au départ) - ok, commande aide
-Un système de score pour pouvoir finir le jeu (gagner des points en ramassant les objet et en les utilisant)
'''
#bibliothèques

import time
import random
import sys, os

# données

AIDE = '''
Bienvenue dans ce jeu d'aventure !
Vous pouvez intéragir avec les lieux et les objets à l'aide de commandes textuelles,
Voici les différentes commandes possibles, il peut y avoir soit une commande seule ou 
soit accompagné de son objet ou du lieu, mais les articles (un, le, les) ne fonctionnera pas.
ex : 'aller chambre'
---
# aller # -- pour déplacer le joueur en donnant le lieu où l'on souhaite se rendre
# regarder # -- pour avoir une description plus détaillé de ce que vous souhaitez observer
# prendre # -- pour ajouter à son inventaire un objet présent dans l'environnement immédiat
# utiliser # -- pour interagir avec les objets de l'inventaire
# carte # -- permet d'afficher le monde et sa position dans celui-ci
# info # -- pour en savoir plus sur les statistiques du Joueur
# aide # -- pour voir cet aide décrivant les différentes commandes
---
'''

SCORE_MAX = 10

OBJETS = {
"couteau" : {
"nom" : "Couteau",
"description" : "Il est long et aiguisé, attention à ne pas vous couper.",
"situation" : "Un couteau se trouve sur le lit.",
"points" : 2
}, 
"tomate" : {
"nom" : "Tomate",
"description" : "Elle est bien mûre et elle semble bien juteuse, miam.",
"situation" : "Il y a une tomate sur la petite table.",
"points" : 2
},
"porte" : {
"nom" : "Porte",
"description" : "Une porte en bois vernis simple.",
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

ACTIONS = ["aller", "regarder", "prendre", "utiliser", "info", "aide", "carte", "quitter"]

PLAN ='''
 _________
|  |      |
|  /   2  |
|  |______|
|1 |      |
|  /   3  |
|__|______|

1 - couloir
2 - chambre
3 - salon

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
 ##       self.nom = input("Quel est votre nom ?")
        self.nom = "Charlie Tango" ## debug
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
        return c0, c1

def verification_action(a):
    if a in ACTIONS:
        #print("vous avez choisi l'action", a, "OK") #debug
        return False

    else:
        print("Erreur : ", a, "n'est pas une bonne commande")
        return True

def verification_objet(o, j):
    if o in j.nou_situation.choix_situation or o in j.nou_situation.choix_objet:
        #print("vous avez choisi l'objet ou le lieu", o, "OK") #debug
        return False

    elif len(o) == 0:
        return False
    
    else:
        print("Erreur :", o, "n'est pas un objet ou un lieu possible")
        return True
    
def choix_action(joueur):
    verifa, verifo = True, True
    while verifa or verifo:
        print("Que souhaitez vous faire ?")
        print("Tapez 'aide' si vous avez besoin d'informations sur le jeu.")
        commande = input(">>>").lower()
        action, objet = decoupage_commande(commande)
        verifa = verification_action(action)
        verifo = verification_objet(objet, joueur)
    return action, objet

def redirection_commande(a, j):
    '''fonction centrale du jeu qui redirigine l'action du joueur vers la fonction correspondante'''
    #print('debug', a, j)
    if a[0] == "aller" and a[1] in j.nou_situation.choix_situation:
        l = Lieu(LIEUX[a[1]]) # une nouvelle instance lieu est créé
        j.changement_situation(l) # et permet de mettre à jour la situation du joueur

    elif a[0] == "regarder":
        if a [1] == "":
            afficher_situation(j)

        for i in j.obj_possibles or i in j.inventaire:
            if i.nom.lower() == a[1]:
                print("\n")
                print(i.description)
                print("\n")

    elif a[0] == "prendre":
        pass

    elif a[0] == "quitter":
        os.system("cls")
        print("merci et au revoir !")
        sys.exit()

    elif a[0] == "info":
        os.system("cls")
        print("Vous vous appelez :", j.nom)
        print("Vous vous trouvez dans :", j.nou_situation.nom)
        print("Vous avez", j.score, "points sur", SCORE_MAX, ".")
        if len(j.inventaire):
            print("Vous avez dans votre inventaire :")
            for i in j.inventaire:
                print("-", i.nom)
        else:
            print("Vous n'avez rien dans votre inventaire.")
        print("---\n")

    elif a[0] == "aide":
        os.system("cls")
        print(AIDE)

    elif a[0] == "carte":
        print(PLAN)

def afficher_situation(j):
    print("\n----")
    print("Vous vous trouvez dans ", j.nou_situation.nom, ".")
    print(j.nou_situation.description)
    for o in j.obj_possibles:
        if o in j.inventaire or len(o.situation) < 1:
            pass
        else:
            print(o.situation)

    print("----\n")


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

##    print("Bonjour %s \nC'est parti !" % joueur.nom)
##    print(AIDE)
##    time.sleep(1)

    print(PLAN)

    # déroulement du jeu  
    while joueur.score < SCORE_MAX:
        objets_possibles(joueur) #mise à jour du joueur et des objets avec lesquels il peut entrer en relation
        if joueur.pre_situation != joueur.nou_situation:
            afficher_situation(joueur)
            joueur.pre_situation = joueur.nou_situation
        action = choix_action(joueur)
        redirection_commande(action, joueur)

    print('Victoire !')

def menu():
    #print("\n"*50)
    os.system("cls")
    print("\n===============\nJeux d'aventure\n===============")
    nouvelle_partie()

#programme

if __name__ == '__main__':
    menu()