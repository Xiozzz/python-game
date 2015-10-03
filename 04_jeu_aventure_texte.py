# -*- coding:Utf-8 -*-
'''
Un jeu d'aventure texte simple, exploration, interaction avec objets,
-Les fonctionnalités que je souhaite ajouter :
-La possibilité de prendre un objet dans le monde - ok #il me reste à debugger, 
le fait de ne pas recréer l'objet dans le monde si le joueur le possède déjà dans son inventaire. bug!!
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
soit accompagnée d'un objet ou d'un lieu, mais les articles (un, le, les) ne fonctionneront pas.
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
"choix_lieu" : ["couloir"],
"choix_objet" : ["porte", "couteau"]
}, 
"salon" : {
"nom" : "un salon", 
"description" : "Il s'agit d'une pièce avec une petite table, les murs frais ont été repeints il n'y a pas longtemps.",
"choix_lieu" : ["couloir"],
"choix_objet" : ["porte", "tomate"]
},
"couloir" : {
"nom" : "un couloir",
"description" : "Il s'agit d'un couloir étroit, il y a deux portes, l'une allant vers la chambre, l'autre vers le salon.",
"choix_lieu" : ["chambre", "salon"],
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
        self.lx_possibles = []
    
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

    def afficher_info(self):
        os.system("cls")
        print("Vous vous appelez :", self.nom)
        print("Vous vous trouvez dans", self.nou_situation.nom)
        print("Vous avez", self.score, "points sur", SCORE_MAX, ".")
        if len(self.inventaire):
            print("Vous avez dans votre inventaire :")
            for i in self.inventaire:
                print("-", i.nom)
        else:
            print("Vous n'avez rien dans votre inventaire.")
        print("---\n")


class Lieu():
    def __init__(self, dictl):
        self.nom = dictl["nom"]
        self.description = dictl["description"]
        self.choix_lieu = dictl["choix_lieu"]
        self.choix_objet = dictl["choix_objet"]

#fonctions


def decoupage_commande(commande):
    '''découpe l'action du joueur pour produire deux str séparées'''
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
        print("ce n'est pas une commande valide.\n")
        return c0, c1

def verification_action(a):
    if a in ACTIONS:
        #print("vous avez choisi l'action", a, "OK") #debug
        return False

    else:
        print("Erreur :", a, "n'est pas une bonne commande.\n")
        return True

def verification_objet(o, j):
    if o in j.nou_situation.choix_lieu or o in j.nou_situation.choix_objet:
        #print("vous avez choisi l'objet ou le lieu", o, "OK") #debug
        return False

    elif o in j.nou_situation.nom.split():
        return False

    elif len(o) == 0:
        return False
    
    else:
        print("Erreur :", o, "n'est pas un objet ou un lieu possible.\n")
        return True
    
def choix_action(joueur):
    verifa, verifo = True, True
    while verifa or verifo:
        print("Quelle est votre action ?")
        print("Tapez 'aide' si vous avez besoin d'informations sur le jeu.")
        commande = input(">>>").lower()
        action, objet = decoupage_commande(commande)
        verifa = verification_action(action)
        verifo = verification_objet(objet, joueur)
    return action, objet

def redirection_commande(a, j):
    '''fonction centrale du jeu qui redirigine l'action du joueur vers la fonction correspondante'''
    #print('debug', a, j)
    if a[0] == "aller":
        if a[1] in j.nou_situation.choix_lieu:
            l = Lieu(LIEUX[a[1]]) # une nouvelle instance lieu est créé
            j.changement_situation(l) # et permet de mettre à jour la situation du joueur

        elif a[1] in j.nou_situation.nom.split():
            print("Vous vous trouvez déjà dans", a[1], end=".\n\n")

        elif a[1] == "":
            print("Où souhaitez vous aller ?\n")

    elif a[0] == "regarder":
        if a [1] == "":
            afficher_situation(j)
        
        elif a[1] in j.nou_situation.nom.split():
            print(j.nou_situation.description, '\n')

        for i in j.obj_possibles or i in j.inventaire:
            if i.nom.lower() == a[1]:
                print("\n")
                print(i.description)
                print("\n")


    elif a[0] == "prendre":
        if a[1] == "":
            print("Que souhaitez vous prendre ?\n")

        for i in j.obj_possibles:
            #le nombre de points de l'objet permet de distinguer ce que l'on peut prendre ou pas 
            if i.nom.lower() == a[1] and i.points > 0:
                print("Vous ramassez", a[1], end=".\n\n")
                j.ajout_inventaire(i)
                #j.inventaire.append(i)
                #j.score += i.points
            elif  i.nom.lower() == a[1] and i.points == 0: 
                print("Vous ne pouvez pas prendre", a[1], end=".\n\n")

    
    elif a[0] == "quitter":
        os.system("cls")
        print("merci et au revoir !")
        sys.exit()

    elif a[0] == "info":
        j.afficher_info()

    elif a[0] == "aide":
        os.system("cls")
        print(AIDE)

    elif a[0] == "carte":
        print(PLAN)

def afficher_situation(j):
    print("\n----")
    print("Vous vous trouvez dans", j.nou_situation.nom, ".")
    print(j.nou_situation.description)
    for o in j.obj_possibles:
        if len(o1.situation) < 1:
            pass
        else:
            print(o.situation)

    print("----\n")


def obj_lex_possibles(j):
    j.obj_possibles = []
    j.lex_possibles = []
    for o in j.nou_situation.choix_objet:
        no = Objet(OBJETS[o])
        j.obj_possibles.append(no)
    for l in j.nou_situation.choix_lieu:
        nl = Lieu(LIEUX[l])
        j.lex_possibles.append(nl)


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
        obj_lex_possibles(joueur) #mise à jour du joueur et des objets et lieu avec lesquels il peut entrer en relation
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