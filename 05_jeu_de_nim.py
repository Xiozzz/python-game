# -*- coding:Utf-8 -*-
'''jeu de nim; 
https://fr.wikipedia.org/wiki/Jeux_de_Nim
deux variantes :
- une seule ligne de baton, le gagnant est celui qui prend le dernier baton, celui qui est le dernier à jouer, gagne.
- cinqs lignes de batons de quantités différentes (1, 3, 5, 7), on prend sur une ligne autant de baton que l'on souhaite
celui qui prend le dernier baton à perdu.
'''

#https://www.youtube.com/watch?v=NqsZ8DD6WHU

BATON = ('''
  _ 
 | | 
 | | 
 |_| 

 ''')

BATON2 = {'a' : ' _ ', 'b' : '| | ', 'c' : '|_| '}

NOMBRE = 20

PYRAMIDE = {"1" : 1, "2" : 3, "3" : 5, "4" : 7}

def jeu_pyramide():
	print("pyramide")
	pass

def jeu_ligne():
	print("ligne")
	pass


def afficher_baton():
	x = BATON
	print(BATON2['a'])
	print(BATON2['b'])
	print(BATON2['b'])
	print(BATON2['c'])
	#for i in range(NOMBRE):
	#	print(BATON)

def menu():
	print("Jeu de Nim")
	print("Quelle variante du jeu souhaitez vous jouer ?")
	print("1) Batons en ligne (nim)")
	print("2) Batons en pyramide (marienbad)")
	answer = input(">>>")
	while answer != "1" and answer != "2" and answer != "q":
		answer = input("Variante 1 ou 2 ?")
	if answer == "1":
		jeu_ligne()
	elif answer == "2":
		jeu_pyramide()
	else:
		print("Bye")

if __name__ == "__main__":
	#menu()
	afficher_baton()