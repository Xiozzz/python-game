# -*- coding: utf-8 -*-
#Text based patience card game

#libraries
import os
import sys
from random import randint, shuffle
from prettytable import PrettyTable

#datas
TITLE = "\n\t\t\t========\n\t\t\tPATIENCE\n\t\t\t========"
INTRO = "Welcome in the Patience Game"

#all the differents cards of the game
CARDS = [
'A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A10', 'A11', 'A12', 'A13',
'B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09', 'B10', 'B11', 'B12', 'B13',
'C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08', 'C09', 'C10', 'C11', 'C12', 'C13',
'D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09', 'D10', 'D11', 'D12', 'D13'
]

POSITIONS = [
'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7',
'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7',
'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7',
'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7',
'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7',
'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7',
'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7',
'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7',
'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7',
'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7',
'k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7',
'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7',
'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7',
'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7',
'o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7'
]

#coordinates of the game table
COORDX = list('abcdefghijklmno')
COORDY = list('1234567')

#names of each position in the game table
POSNAMES ={
'a1' : 'bigStk', 'a2' : 'cardVw', 'a3' : 'freeSp', 'a4' : 'cardC1',	'a5' : 'cardC2', 'a6' : 'cardC3', 'a7' : 'cardC4',
'b1' : 'stack0', 'b2' : 'stack1', 'b3' : 'stack2', 'b4' : 'stack3',	'b5' : 'stack4', 'b6' : 'stack5', 'b7' : 'stack6',
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

TEXTS = [
"What do you want to do?",
"1. Start a New Game?",
"2. Quit",
"1. (W)atch. Watch a card from a stack",
"2. (M)ove. Move a card",
"3. (H)elp. Read the rules",
"Please give the coordinates of the stack you want to watch a card.",
"Please give the coordinates or the name of the card you wish to move.",
"Thanks. Please give now the coordinates where you wish your card to be moved.",
"Sorry. This answer is not valid."
]

RULES = """
When the game start, there is 52 cards hidden, there is 4 family (A, B, C, D) and each family have 13 members.
The cards are distributed randomly on the game table.
31 cards are in the big stack in position a1, 6 cards are in position b7, 5 in b6, 4 in b5, 3 in b4, 2 in b3 and 1 in b2.
You can choose to watch a card from one of the stacks, the card will appear next to the stack you have chosen.
For the big stack you can continue to watch all the cards as much as you want, there is a rotation, 
but for the others stack, you can watch a card only if the space under is free.
You can move the cards in any column starting from line c. But to put a card under an other one, the
card must be of value one less than the one up on the column.
You can also move the cards to the cells a4, a5, a6, a7 and class them together by family. And must start
with the first card (A1, B1, C1 ou D1), once a cell have been filled with a first card, the cell stick to this 
family.
"""

#variables
#where are positioned each cards
cardsPositions  = [
['A01', None], ['A02', None], ['A03', None], ['A04', None], ['A05', None], ['A06', None], ['A07', None], ['A08', None], ['A09', None], ['A10', None], ['A11', None], ['A12', None], ['A13', None],
['B01', None], ['B02', None], ['B03', None], ['B04', None], ['B05', None], ['B06', None], ['B07', None], ['B08', None], ['B09', None], ['B10', None], ['B11', None], ['B12', None], ['B13', None],
['C01', None], ['C02', None], ['C03', None], ['C04', None], ['C05', None], ['C06', None], ['C07', None], ['C08', None], ['C09', None], ['C10', None], ['C11', None], ['C12', None], ['C13', None],
['D01', None], ['D02', None], ['D03', None], ['D04', None], ['D05', None], ['D06', None], ['D07', None], ['D08', None], ['D09', None], ['D10', None], ['D11', None], ['D12', None], ['D13', None]
]


#occupation of each space 'name':[ #index0 numbers of cards max, #index1 numbers of cards now]
tableOccupation = {
'a1':[31, 0], 'a2':[31, 0], 'a3':[0, 0], 'a4':[13, 0], 'a5':[13, 0], 'a6':[13, 0], 'a7':[13, 0],
'b1':[0, 0], 'b2':[1, 0], 'b3':[2, 0], 'b4':[3, 0], 'b5':[4, 0], 'b6':[5, 0], 'b7':[6, 0],
'c1':[1, 0], 'c2':[1, 0], 'c3':[1, 0], 'c4':[1, 0], 'c5':[1, 0], 'c6':[1, 0], 'c7':[1, 0],
'd1':[1, 0], 'd2':[1, 0], 'd3':[1, 0], 'd4':[1, 0], 'd5':[1, 0], 'd6':[1, 0], 'd7':[1, 0],
'e1':[1, 0], 'e2':[1, 0], 'e3':[1, 0], 'e4':[1, 0], 'e5':[1, 0], 'e6':[1, 0], 'e7':[1, 0],
'f1':[1, 0], 'f2':[1, 0], 'f3':[1, 0], 'f4':[1, 0], 'f5':[1, 0], 'f6':[1, 0], 'f7':[1, 0],
'g1':[1, 0], 'g2':[1, 0], 'g3':[1, 0], 'g4':[1, 0], 'g5':[1, 0], 'g6':[1, 0], 'g7':[1, 0],
'h1':[1, 0], 'h2':[1, 0], 'h3':[1, 0], 'h4':[1, 0], 'h5':[1, 0], 'h6':[1, 0], 'h7':[1, 0],
'i1':[1, 0], 'i2':[1, 0], 'i3':[1, 0], 'i4':[1, 0], 'i5':[1, 0], 'i6':[1, 0], 'i7':[1, 0],
'j1':[1, 0], 'j2':[1, 0], 'j3':[1, 0], 'j4':[1, 0], 'j5':[1, 0], 'j6':[1, 0], 'j7':[1, 0],
'k1':[1, 0], 'k2':[1, 0], 'k3':[1, 0], 'k4':[1, 0], 'k5':[1, 0], 'k6':[1, 0], 'k7':[1, 0],
'l1':[1, 0], 'l2':[1, 0], 'l3':[1, 0], 'l4':[1, 0], 'l5':[1, 0], 'l6':[1, 0], 'l7':[1, 0],
'm1':[1, 0], 'm2':[1, 0], 'm3':[1, 0], 'm4':[1, 0], 'm5':[1, 0], 'm6':[1, 0], 'm7':[1, 0],
'n1':[1, 0], 'n2':[1, 0], 'n3':[1, 0], 'n4':[1, 0], 'n5':[1, 0], 'n6':[1, 0], 'n7':[1, 0],
'o1':[1, 0], 'o2':[1, 0], 'o3':[1, 0], 'o4':[1, 0], 'o5':[1, 0], 'o6':[1, 0], 'o7':[1, 0]
}

#sacks where cards are distributed in the beginning
SACKS = ['a1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7']

CELLS = ['a4', 'a5', 'a6', 'a7']

#functions


def displayTable():
	"check occupation of the table and draw the game grid"
	print(TITLE)
	table = PrettyTable()
	table.padding_width = 2
	table.field_names = list(' 1234567')

	c = 1

	for x in COORDX:
		newRow = [x]
		emptRw = ["","","","","","","",""]
		while c <= 7:
			position = x+str(c)
			if position in CELLS:
				newRow.append('CLL')
			elif position in SACKS and tableOccupation[position][1] != 0:
				newRow.append('SCK')
			elif tableOccupation[position][1] != 0:
				if position == 'a2': #special case for the big sack in a1
					newRow.append(tableOccupation[position][-1])
				else: # others sack b2 to b7
					newRow.append(tableOccupation[position][2])
			else:
				newRow.append(' ')
			c += 1
		table.add_row(newRow)
		table.add_row(emptRw)
		c = 1

	print(table)

def distributeCards(cards):
	"distribute the card in a free socket" 
	c = 0
	while c < 52:
		for sack in SACKS:
			if tableOccupation[sack][1] < tableOccupation[sack][0]:  #check if their is free space for a card
				tableOccupation[sack][1] += 1 #increment by one and take a free space
				for cardPos in cardsPositions:
					if cardPos[0] == cards[c]:
						cardPos[1] = sack #give card its position
						tableOccupation[sack].append(cards[c])
				c += 1
	
	# for sack in SACKS:
	# 	print(tableOccupation[sack])
	# 	print()
	# print(tableOccupation['a1'][-1])
	# input("DEBUG MODE")


def cleanScreen():
	"cleaning the screen"
	os.system('cls')

def newGame():
	"set a new game and start"
	#set the variables to default
	setDefault()

	#copy a set of 52 cards
	gameCards = shuffleCopy(CARDS)

	#distribute the 52 cards in the table
	distributeCards(gameCards)

	#DEBUG TOOLS
	# findCardPos(position="a1", card="A01")
	# input()
	#display the table
	game()


def game():
	"main loop of the game"
	action = "Play"

	while action:
		#update the table display
		cleanScreen()
		displayTable()

		#ask player for a command
		action = question(0, 3, 4, "action")

		#1. see a card from a stack if possible
		if action in ["watch", "w", "1"]:
			watchCoord = coordInput(6, "watch") #coordinates of the stack
			input(watchCard(watchCoord))

		#2. move a card
		if action in ["move", "m", "2"]: 
			#ask player for a coordinate a1 or 1a, whatever or the card name (visible)
			moveFrom = coordInput(7, "moveFrom")
			#move the card to coordinate if possible
			moveTo = coordInput(8, "moveTo") 
			# print(moveFrom, moveTo)
			#check if movement possible
			#then cardUpdate()

		#debug tools
		#input("DEBUG MODE")
			

		#check if table if cells are complete and game finished, if yes, victory and break loop
		# if win, action = false

	#the game is finished, restart menu
	input("The game is finished, press <Enter> to go to menu.")
	menu()

def question(a, b, c, f):
	"ask the player for an action"
	flag = f
	print("\n", TEXTS[a],"\n========================\n")
	print(TEXTS[b])
	print(TEXTS[c])
	print(TEXTS[5])

	while True:
		answer = input(">>>").lower()
		check = checkAnswer(answer, flag)
		if check:
			return answer
		else:
			print(TEXTS[9])

def checkAnswer(answer, flag):
	"check if the answer is correct and return accordingly"
	if answer in ['h', 'help', '3']:
		help()
		return True

	if flag == "menu":
		if answer in ['1', 'start', '2', 'q', 'quit', 'new', 's', 'n']:
			return True

	if flag == "action":
		if answer in ['w', 'watch', '1', 'm', 'move' , '2']:
			return True

def coordInput(a, action):
	"ask in and check if it is good coordinates"
	print(TEXTS[a])
	userInput = input('>>>')
	while True:
		if checkCoords(userInput, action): #if coords valid
			return userInput
		else:
			print(TEXTS[9])
			print(TEXTS[a])
			userInput = input('>>>')

def checkCoords(userInput, action):
	"check if coords or card name is valid"

	for coord in POSITIONS:
		if coord == userInput:
			return True
		if coord[::-1] == userInput: #reversed sting, 1a, 7i, ...works
			return True

	for name in CARDS:
		if name == userInput and action == "moveFrom":
			return True
	
	return False

def watchCard(coord):
	"show a card from the stack if a card is present"
	stacksFrom = ["a1", 'b2', 'b3','b4', 'b5', 'b6', 'b7'] #stack in which there is card to watch
	stacksTo = ["a2", 'c2', 'c3','c4', 'c5', 'c6', 'c7'] #stack where the card can go
	
	if coord not in stacksFrom:
		return "There is no stack at this coordinates."
	
	indexCoord = stacksFrom.index(coord) #index in stack of coordinates
	relatedCoord = stacksTo[indexCoord]
	

	for stack in stacksFrom:
		if coord == stack:
			#Special, for bigStack a1, if all the cards have been moved, and the player ask again, then all the cards from a2 go back to a1
			if coord == "a1":
				flag = 0

			elif tableOccupation[coord][1] > 0: #check if there is a card to coordinates
				flag = 1

			else:
				flag = 2

	if flag == 0:
		cardUpdate(coord, relatedCoord)
		return "Main stack a1 to a2"		

	if flag == 1: #check if free space for b stacks
		if coord[0] == "b" and tableOccupation[relatedCoord][1] == 0:
			cardUpdate(coord, relatedCoord)
			return "Stack "+coord+" to "+relatedCoord
		else:
			return "There is already a card in "+tableOccupation[relatedCoord]
		#if yes move the card from stack to new position, update tableOccupation et cardsPositions
		#need to build an array with the card in order in stakcs and keep the same order as I move them

	if flag == 2:
		return "There is no card in this stack anymore."

	#debug	
	# print("DEBUG :\ncards positions :")
	# print(cardsPositions)
	# print("spaces occupations :")
	# for c in stacksFrom:
	# 	print(c, ':', tableOccupation[c])
	# for c in stacksTo:
	# 	print(c, ':', tableOccupation[c])
	# input("DEBUG INPUT")

def cardUpdate(CoordFrom, CoordTo):
	"update data variables"
	#remove the last card
	card = tableOccupation[CoordFrom].pop()
	tableOccupation[CoordFrom][1] -= 1
	#add it to the related stack
	tableOccupation[CoordTo].append(card)
	tableOccupation[CoordTo][1] += 1
	#update position of card in cardsPositions
	cardIndex = cardsPositions.index([card, CoordFrom]) #find the index of the current card
	# print("The index is :", cardIndex)
	cardsPositions[cardIndex][1] = CoordTo

def moveCard():
	pass

def help():
	"help screen"
	print(RULES)
	input("<Enter> to continue")

def findCardPos(card=None, position=None):
	"used to find the card or the position in list cardPositions"
	for cardPos in cardsPositions:
		if position == cardPos[1]:
			print("index de la position", position,":", cardsPositions.index(cardPos), "card", cardPos[0])
		if card == cardPos[0]:
			print("index de la carte", card,":", cardsPositions.index(cardPos), "position", cardPos[1])

def shuffleCopy(CARDS):
	#used to randomly shuffle cards
	copy = CARDS[:]
	shuffle(copy)
	return copy

def setDefault():
	"function who put the dictionnary to default values"

	#set to None each card position
	for cardPos in cardsPositions:
		cardPos[1] = None

	#set 0 to each space occupation #index1
	for key in tableOccupation:
		tableOccupation[key][1] = 0

def debugTest():
	"function use to make tests"
	pass

def menu():
	"start a new game or quit"
	cleanScreen()
	print(INTRO)
	action = question(0, 1, 2, "menu")

	if action in ['1', 'start', 'new', 's', 'n']:
		newGame()
	if action in ['h', 'help', '3']:
		menu()
	else:
		sys.exit()

#program
if __name__ == "__main__":
	menu()
	# newGame()