# -*- coding:Utf-8 -*-

import random
import sys

def choix_nombre():
    nb = random.randint(0, 101)
    return nb

def deviner(nombre):
    nb = int(input("Choisissez un nombre \n>>>"))
    if nb < nombre:
        print("le nombre à trouver est plus grand que", nb)
    elif nb > nombre:
        print("le nombre à trouver est plus petit que", nb)
    elif nb == nombre:
        print("Bravo il s'agit bien de", nombre)
        sys.exit()

def jeu():
    essais = 0
    essais_max = 10
    nombre = choix_nombre()
        
    while essais <= essais_max:
        print("essai n°:", essais)
        deviner(nombre)
        essais += 1
    
    if essais == essais_max:
        print("Vous avez perdu")
        sys.exit()

jeu()
