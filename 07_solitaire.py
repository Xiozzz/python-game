# -*- coding: utf-8 -*-
#Text based solitaire game using a grid, row/col, to place number

"""
- (instead of classical playing card, I just use numbers and letters)
- four cells to fill, A, B, C, D*
- one stack of hiden cards and one cell for the card we check
- seven cascades, with each, hidden cards
- 13 * 4 = 52 cards (Ex: 1A, 2A, 12C, 13D, 11A, 9B, etc)
- see isdigit/isalpha/isdecimal for checkers
- more rows needed after 'i', from 'c' to 13 rows
- dynamic card row, display only if there is card on it.
"""

#libraries
import os
from sys import exit
from random import randint, choice

#datas
#all the differents cards of the game
CARDS = [
'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13',
'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13',
'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13',
'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13'
]

#coordinates of the game table
COORDX = list('abcdefghijklmno')
COORDY = list('1234567')

#names of each position in the game table
POSITIONS ={
	'a1' : 'stackHide', 'a2' : 'stackView', 'a3' : 'freeSpace', 'a4' : 'cell1',	'a5' : 'cell2',	'a6' : 'cell3',	'a7' : 'cell4',
	'b1' : 'minStack0', 'b2' : 'minStack1', 'b3' : 'minStack2', 'b4' : 'minStack3',	'b5' : 'minStack4', 'b6' : 'minStack5', 'b7' : 'minStack6',
	'c1' : 'cardc1', 'c2' : 'cardc2', 'c3' : 'cardc3', 'c4' : 'cardc4', 'c5' : 'cardc5', 'c6' : 'cardc6', 'c7' : 'cardc7',
	'd1' : 'cardd1', 'd2' : 'cardd2', 'd3' : 'cardd3', 'd4' : 'cardd4', 'd5' : 'cardd5', 'd6' : 'cardd6', 'd7' : 'cardd7', 
	'e1' : 'carde1', 'e2' : 'carde2', 'e3' : 'carde3', 'e4' : 'carde4', 'e5' : 'carde5', 'e6' : 'carde6', 'e7' : 'carde7', 
	'f1' : 'cardf1', 'f2' : 'cardf2', 'f3' : 'cardf3', 'f4' : 'cardf4', 'f5' : 'cardf5', 'f6' : 'cardf6', 'f7' : 'cardf7', 
	'g1' : 'cardg1', 'g2' : 'cardg2', 'g3' : 'cardg3', 'g4' : 'cardg4', 'g5' : 'cardg5', 'g6' : 'cardg6', 'g7' : 'cardg7', 
	'h1' : 'cardh1', 'h2' : 'cardh2', 'h3' : 'cardh3', 'h4' : 'cardh4', 'h5' : 'cardh5', 'h6' : 'cardh6', 'h7' : 'cardh7', 
	'i1' : 'cardi1', 'i2' : 'cardi2', 'i3' : 'cardi3', 'i4' : 'cardi4', 'i5' : 'cardi5', 'i6' : 'cardi6', 'i7' : 'cardi7', 
	'j1' : 'cardj1', 'j2' : 'cardj2', 'j3' : 'cardj3', 'j4' : 'cardj4', 'j5' : 'cardj5', 'j6' : 'cardj6', 'j7' : 'cardj7', 
	'k1' : 'cardk1', 'k2' : 'cardk2', 'k3' : 'cardk3', 'k4' : 'cardk4', 'k5' : 'cardk5', 'k6' : 'cardk6', 'k7' : 'cardk7', 
	'l1' : 'cardl1', 'l2' : 'cardl2', 'l3' : 'cardl3', 'l4' : 'cardl4', 'l5' : 'cardl5', 'l6' : 'cardl6', 'l7' : 'cardl7', 
	'm1' : 'cardm1', 'm2' : 'cardm2', 'm3' : 'cardm3', 'm4' : 'cardm4', 'm5' : 'cardm5', 'm6' : 'cardm6', 'm7' : 'cardm7', 
	'n1' : 'cardn1', 'n2' : 'cardn2', 'n3' : 'cardn3', 'n4' : 'cardn4', 'n5' : 'cardn5', 'n6' : 'cardn6', 'n7' : 'cardn7', 
	'o1' : 'cardo1', 'o2' : 'cardo2', 'o3' : 'cardo3', 'o4' : 'cardo4', 'o5' : 'cardo5', 'o6' : 'cardo6', 'o7' : 'cardo7'
}

#variables
#where are positioned each cards
cardsCoordinates = {
'A1':None, 'A2':None, 'A3':None, 'A4':None, 'A5':None, 'A6':None, 'A7':None, 'A8':None, 'A9':None, 'A10':None, 'A11':None, 'A12':None, 'A13':None,
'B1':None, 'B2':None, 'B3':None, 'B4':None, 'B5':None, 'B6':None, 'B7':None, 'B8':None, 'B9':None, 'B10':None, 'B11':None, 'B12':None, 'B13':None,
'C1':None, 'C2':None, 'C3':None, 'C4':None, 'C5':None, 'C6':None, 'C7':None, 'C8':None, 'C9':None, 'C10':None, 'C11':None, 'C12':None, 'C13':None,
'D1':None, 'D2':None, 'D3':None, 'D4':None, 'D5':None, 'D6':None, 'D7':None, 'D8':None, 'D9':None, 'D10':None, 'D11':None, 'D12':None, 'D13':None
}

#occupation of cards for each position 'name':[ #index0 numbers of cards max, #index1 numbers of cards now , #index2 cardname, #index3 cardname, #index4 cardname, etc..]
cardsPositions = {
'stackHide':[40, 0], 'stackView':[40, 0], 'freeSpace':[0, 0], 'cell1':[13, 0], 'cell2':[13, 0], 'cell3':[13, 0], 'cell4':[13, 0],
'minStack0':[0, 0], 'minStack1':[1, 0], 'minStack2':[2, 0], 'minStack3':[3, 0], 'minStack4':[4, 0], 'minStack5':[5, 0], 'minStack6':[6, 0], 'minStack7':[7, 0],
'cardc1':[1, 0], 'cardc2':[1, 0], 'cardc3':[1, 0], 'cardc4':[1, 0], 'cardc5':[1, 0], 'cardc6':[1, 0], 'cardc7':[1, 0], 
'cardd1':[1, 0], 'cardd2':[1, 0], 'cardd3':[1, 0], 'cardd4':[1, 0], 'cardd5':[1, 0], 'cardd6':[1, 0], 'cardd7':[1, 0],
'carde1':[1, 0], 'carde2':[1, 0], 'carde3':[1, 0], 'carde4':[1, 0], 'carde5':[1, 0], 'carde6':[1, 0], 'carde7':[1, 0],
'cardf1':[1, 0], 'cardf2':[1, 0], 'cardf3':[1, 0], 'cardf4':[1, 0], 'cardf5':[1, 0], 'cardf6':[1, 0], 'cardf7':[1, 0], 
'cardg1':[1, 0], 'cardg2':[1, 0], 'cardg3':[1, 0], 'cardg4':[1, 0], 'cardg5':[1, 0], 'cardg6':[1, 0], 'cardg7':[1, 0], 
'cardh1':[1, 0], 'cardh2':[1, 0], 'cardh3':[1, 0], 'cardh4':[1, 0], 'cardh5':[1, 0], 'cardh6':[1, 0], 'cardh7':[1, 0], 
'cardi1':[1, 0], 'cardi2':[1, 0], 'cardi3':[1, 0], 'cardi4':[1, 0], 'cardi5':[1, 0], 'cardi6':[1, 0], 'cardi7':[1, 0], 
'cardj1':[1, 0], 'cardj2':[1, 0], 'cardj3':[1, 0], 'cardj4':[1, 0], 'cardj5':[1, 0], 'cardj6':[1, 0], 'cardj7':[1, 0], 
'cardk1':[1, 0], 'cardk2':[1, 0], 'cardk3':[1, 0], 'cardk4':[1, 0], 'cardk5':[1, 0], 'cardk6':[1, 0], 'cardk7':[1, 0], 
'cardl1':[1, 0], 'cardl2':[1, 0], 'cardl3':[1, 0], 'cardl4':[1, 0], 'cardl5':[1, 0], 'cardl6':[1, 0], 'cardl7':[1, 0], 
'cardm1':[1, 0], 'cardm2':[1, 0], 'cardm3':[1, 0], 'cardm4':[1, 0], 'cardm5':[1, 0], 'cardm6':[1, 0], 'cardm7':[1, 0], 
'cardn1':[1, 0], 'cardn2':[1, 0], 'cardn3':[1, 0], 'cardn4':[1, 0], 'cardn5':[1, 0], 'cardn6':[1, 0], 'cardn7':[1, 0], 
'cardo1':[1, 0], 'cardo2':[1, 0], 'cardo3':[1, 0], 'cardo4':[1, 0], 'cardo5':[1, 0], 'cardo6':[1, 0], 'cardo7':[1, 0]
}


#functions
def drawGameTable():
	jump=0
	print('\n')
	for x in COORDX:
		for y in COORDY:
			position = x + y
			if cardsPositions[POSITIONS[position]][1]: #if there is a card in #index1
				print(POSITIONS[position], cardsPositions[POSITIONS[position]] , sep="", end=" ") #print the card
				jump = 1
			elif POSITIONS[position][:-2] != "card":
			 	print("        X", end="")
			 	jump = 1
			if POSITIONS[position][:-2] == "card":
				jump = 0

		if jump:
			print("\n")
def distributeCards():
	pass

def cleanScreen():
	"cleaning the screen"
	os.system('cls')


# def cardNames():
# 	"une fonction utilisé pour créer les noms des 52 cartes"
# 	c = 1
# 	cards = {'A':[], 'B':[], 'C':[], 'D':[]}
# 	while c <= 13:
# 		cards['A'].append("A"+str(c))
# 		cards['B'].append("B"+str(c))
# 		cards['C'].append("C"+str(c))
# 		cards['D'].append("D"+str(c))
# 		c+=1
# 	return cards

# def positionsNames():
#	"une fonction utilisé pour trouvé les noms rapidement de toutes les positions cards"
# 	lettre = list("cdefghijklmno")
# 	liste = []
# 	liste2 = []
# 	c = 1
# 	for i in lettre:
# 		while c < 8:
# 			liste.append("'"+ i+ str(c)+"'"+ " : 'card"+i+str(c)+"',")
# 			c+=1
# 		c = 1
# 	for i in liste:
# 		print(i, end=" ")
# 	for i in lettre:
# 		while c < 8:
# 			liste2.append("'card"+i+str(c)+"':[1, 0],")
# 			c+=1
# 		c = 1
# 	for i in liste2:
# 		print(i, end=" ")

#program
if __name__ == "__main__":
	drawGameTable()