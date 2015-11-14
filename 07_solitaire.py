# -*- coding: utf-8 -*-
#Text based solitaire game using a grid, row/col, to place number

"""
- (instead of classical playing card, I just use numbers and letters)
- four cells to fill, A, B, C, D*
- one stack of hiden cards and one cell for the card we check
- seven cascades, with each, hidden cards
- 13 * 4 = 52 cards (Ex: 1A, 2A, 12C, 13D, 11A, 9B, etc)
- see isdigit/isalpha/isdecimal for checkers
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
COORDX = ['1', '2', '3', '4', '5', '6', '7']
COORDY = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

#names of each position in the game table
POSITIONS ={
	'a1' : 'stackHide', 'a2' : 'stackView', 'a3' : 'freeSpace', 'a4' : 'cell1',	'a5' : 'cell2',	'a6' : 'cell3',	'a7' : 'cell4',
	'b1' : 'miniStack0', 'b2' : 'miniStack1', 'b3' : 'miniStack2', 'b4' : 'miniStack3',	'b5' : 'miniStack4', 'b6' : 'miniStack5', 'b7' : 'miniStack6',
	'c1' : 'card1', 'c2' : 'card2', 'c3' : 'card3', 'c4' : 'card4', 'c5' : 'card5', 'c6' : 'card6', 'c7' : 'card7',
	'd1' : 'card1', 'd2' : 'card2', 'd3' : 'card3', 'd4' : 'card4', 'd5' : 'card5', 'd6' : 'card6', 'd7' : 'card7',
	'e1' : 'card1', 'e2' : 'card2', 'e3' : 'card3', 'e4' : 'card4', 'e5' : 'card5', 'e6' : 'card6', 'e7' : 'card7',
	'f1' : 'card1', 'f2' : 'card2', 'f3' : 'card3', 'f4' : 'card4', 'f5' : 'card5', 'f6' : 'card6', 'f7' : 'card7',
	'g1' : 'card1', 'g2' : 'card2', 'g3' : 'card3', 'g4' : 'card4', 'g5' : 'card5', 'g6' : 'card6', 'g7' : 'card7', 
	'h1' : 'card1', 'h2' : 'card2', 'h3' : 'card3', 'h4' : 'card4', 'h5' : 'card5', 'h6' : 'card6', 'h7' : 'card7',
	'i1' : 'card1', 'i2' : 'card2', 'i3' : 'card3', 'i4' : 'card4', 'i5' : 'card5', 'i6' : 'card6', 'i7' : 'card7'
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
'stackHide':[40], 'stackView':[40, 0], 'freeSpace':[0], 'cell1':[13, 0], 'cell2':[13, 0], 'cell3':[13, 0], 'cell4':[13, 0],
'miniStack0':[0], 'miniStack1':[1], 'miniStack2':[2], 'miniStack3':[3], 'miniStack4':[4], 'miniStack5':[5], 'miniStack6':[6], 'miniStack7':[7],
'card1':[1], 'card2':[1], 'card3':[1], 'card4':[1], 'card5':[1], 'card6':[1], 'card7':[1],
'card1':[1], 'card2':[1], 'card3':[1], 'card4':[1], 'card5':[1], 'card6':[1], 'card7':[1],
'card1':[1], 'card2':[1], 'card3':[1], 'card4':[1], 'card5':[1], 'card6':[1], 'card7':[1],
'card1':[1], 'card2':[1], 'card3':[1], 'card4':[1], 'card5':[1], 'card6':[1], 'card7':[1],
'card1':[1], 'card2':[1], 'card3':[1], 'card4':[1], 'card5':[1], 'card6':[1], 'card7':[1],
'card1':[1], 'card2':[1], 'card3':[1], 'card4':[1], 'card5':[1], 'card6':[1], 'card7':[1],
'card1':[1], 'card2':[1], 'card3':[1], 'card4':[1], 'card5':[1], 'card6':[1], 'card7':[1]
}

#functions
def drawGameTable():
	print("Hello, I am a card :)")


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


#program
drawTable()