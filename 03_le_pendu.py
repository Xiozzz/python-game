# -*- coding:Utf-8 -*-

# bibliothèques

import random
import sys


# variables

TABLEAU = [
'  +---+   \n  |   |   \n      |   \n      |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n      |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n  |   |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|   |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n /    |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n / \\  |   \n      |   \n========= \n'
]

BANQUE_MOTS = ['voiture', 'deux', 'coucou', 'cheval', 'banane', 'pompier', 'tomate', 'radar']

ACCEPTÉS = list('azertyuiopqsdfghjklmwxcvbn')

ESSAIS_MAX = 6


# fonctions

def ajouter_mot(BANQUE_MOTS):
    mot = input("Quel mot souhaitez vous ajouter à la banque ?\n>>>")
    print(mot, 'est ajouté à la banque, merci.')
    BANQUE_MOTS.append(mot)

def choix_mot():
    x = random.randint(0, len(BANQUE_MOTS)-1)
    mot = BANQUE_MOTS[x]
    return mot

def cacher_mot(mot_choisi):
    mot_caché = " _" * len(mot_choisi)
    return mot_caché

def nouvelle_lettre(mot, essai, lettres):
    '''Si correcte, ajoute la lettre au stock lettre_trouvées'''
    for i in mot:
        if len(essai) == 1 and essai == i:
            lettres.append(essai)
            return lettres
    return lettres

def ajouter_lettre(essai, lettres):
    '''Ajoute la lettre de l'essai au stock des lettres_essayées'''
    if len(essai) == 1:
        lettres.append(essai)
    return lettres

def nouveau_mot(mot_cherché, lettres_trouvé):
    mot_caché = ""
    for i in mot_cherché:
        if i in lettres_trouvé:
            mot_caché += i
        else:
            mot_caché += ' _'
    return mot_caché
    
def deviner():
    réponse = input("Essayez de deviner le mot secret, ou une lettre:\n>>>").lower()
    while True:
        if réponse == ":q" or réponse == ":quit":
            sys.exit()
        elif réponse in ACCEPTÉS and len(réponse) == 1:
            print("Vous choisissez la lettre", réponse)
            break
        elif len(réponse) > 1:
            if vérif_mot(réponse):
                print("Vous choisissez le mot", réponse)
                break
        réponse = input("Il ne s'agit ni d'une lettre accepté, ni d'un mot \
(vous pouvez quitter avec :q ou :quit)\n>>>").lower()
    return réponse

def vérif_mot(mot):
    c = 0
    for i in mot:
        if i in ACCEPTÉS:
            c += 1 #si tout les caractères sont permis, c sera égale à la quantité de caractère totale
    if c == len(mot):
        return True
    else:
        return False


def vérif_victoire(mot_cherché, mot_caché, essai):
    if  mot_cherché == mot_caché or mot_cherché == essai:
        print("BRAVO ! \n:) \nVous avez deviné le mot %s"%(mot_cherché))
        sys.exit()
    elif len(essai) > 1 and mot_cherché != essai:
        print("Malheureusement, le mot", essai, "n'est pas celui cherché.")

def nouvelle_partie():

    #mise à zéro des variables
    nombre_essai = 1
    essai_raté = 0
    lettres_trouvés = []
    lettres_essayés = []

    #préparation du mot cherché
    mot_cherché = choix_mot()
    mot_caché = cacher_mot(mot_cherché)

    #boucle du jeu
    while nombre_essai <= ESSAIS_MAX:
        #Affichage du nombre d'essai restant
        print("\n***\nEssai n°: %s sur %s essais"% (nombre_essai, ESSAIS_MAX))
        if nombre_essai == ESSAIS_MAX:
            print("Attention, dernier essai.")
        #Affichage du pendu
        print(TABLEAU[nombre_essai-1])
        #Affichage des lettres déjà demandé
        if len(lettres_essayés) > 0:
            print("Lettres que vous avez déjà cherché :", end=' ' )
            for i in lettres_essayés:
                print(i, end=' ')
            print("\n***")
        #Affichage du mot caché
        print(mot_caché, "\n")

        #Nouvel essai
        essai = deviner()
        #Mise à jour de la liste de mots essayé
        lettres_essayés = ajouter_lettre(essai, lettres_essayés)
        #Mise à jour de la liste de mots trouvé
        lettres_trouvés = nouvelle_lettre(mot_cherché, essai, lettres_trouvés)
        #Nouveau mot caché en fonction des lettres trouvés
        mot_caché = nouveau_mot(mot_cherché, lettres_trouvés)
        #Vérification du mot
        vérif_victoire(mot_cherché, mot_caché, essai)
        #Mise à jour des variables
        if nombre_essai == ESSAIS_MAX:
            print("\nPerdu :( !\n", TABLEAU[nombre_essai], "\nVous avez dépassé le nombre \
d'essai possibles, une nouvelle partie ?")
        nombre_essai += 1

def menu():
    print("============\nJeu du pendu\n============")
    print("Deviner un mot avant que le nombre d'essais soit passé")
    print("Tapez banque ou b si vous souhaitez ajouter un mot à la banque.")
    réponse = input("Commencer une partie ?\n>>>").lower()
    
    if réponse == "oui" or réponse == "o":
        nouvelle_partie()
        return True
    elif réponse == "non" or réponse == "n":
        return False
    elif réponse == "banque" or réponse == "b":
        ajouter_mot(BANQUE_MOTS)
        return True    
    else:
        print("Cette réponse n'est pas valable, oui, non ou banque.")
        return True

# programme

jeu = True
while jeu == True:
    jeu = menu()
    
