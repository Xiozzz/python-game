# -*- coding:Utf-8 -*-
    
'''
En gros, un jeu d'aventure avec du combat, l'inspiration des muds
Fonctionalités :
-Une interface graphique tkinter ?? 
-Je reprends le jeu d'aventure précédent et j'ajoute les NPCs
-possibilité de discussion et de recevoir des quêtes
-lire un journal des quêtes
-possibilité de combats, d'expérience (voir score du jeu précédent)
-le choix de son arme, de sa race (nain, elfe, homme), de sa classe (guerrier, voleur, magicien)
-la possibilité de lancer des sorts magiques (diminution point de magie)
-système de combat, de dégats, de points de vie, de potion de soin et potion de magie
-la possibilité de sauvegarder et reprendre la partie (open, read on file) à partir de données enregistrées 
d'une partie précédente dans un fichier
-ennemis, pnj, carte plus grande, trésors, porte fermés, clés
- la carte du monde et la position du joueur sur la carte
- créer un programme éditeur qui permet de rajouter des données
(ajouter une arme, un lieu, un objet, un npc)
'''

# bibliothèques

from src_jeu_de_role import display

# variables

# fonctions

# programme

"Ce fichier ne fait qu'importer la bibliothèque display et lancer le jeu"

if __name__ == "__main__":
	menu = display.Programme()
	menu.boucle()