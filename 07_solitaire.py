# -*- coding: utf-8 -*-
#Text based solitaire game using a grid, row/col, to place number

"""
- (instead of classical playing card, I just use numbers and letters)
- four cells to fill, A, B, C, D*
- one stack of hiden cards and one cell for the card we check
- seven cascades, with each, hidden cards
- 13 * 4 = 52 cards (Ex: 1A, 2A, 12C, 13D, 11A, 9B, etc)
"""

#libraries
from random import randint, choice
from os import clean
from sys import exit

#datas
CARDS = [
'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13',
'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13',
'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13',
'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13'
]

CARDSCOORDS = {
'A1':None, 'A2':None, 'A3':None, 'A4':None, 'A5':None, 'A6':None, 'A7':None, 'A8':None, 'A9':None, 'A10':None, 'A11':None, 'A12':None, 'A13':None,
'B1':None, 'B2':None, 'B3':None, 'B4':None, 'B5':None, 'B6':None, 'B7':None, 'B8':None, 'B9':None, 'B10':None, 'B11':None, 'B12':None, 'B13':None,
'C1':None, 'C2':None, 'C3':None, 'C4':None, 'C5':None, 'C6':None, 'C7':None, 'C8':None, 'C9':None, 'C10':None, 'C11':None, 'C12':None, 'C13':None,
'D1':None, 'D2':None, 'D3':None, 'D4':None, 'D5':None, 'D6':None, 'D7':None, 'D8':None, 'D9':None, 'D10':None, 'D11':None, 'D12':None, 'D13':None
}

COORDX = ['1', '2', '3', '4', '5', '6', '7']
COORDY = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

POSITIONS ={
	'a1' : 'stackHide',
	'a2' : 'stackView'
}

#variable

#functions


def drawTable():
	print()





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
drawCard()