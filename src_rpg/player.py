# -*- coding:Utf-8 -*-
#  fichier player.py

from tkinter import *

class Joueur():

	def __init__(self):
		self.intro="Hello World !"

	def intro(self, source):
		self.txt1 = Label(source, text=self.intro)
		self.txt1.grid(row=0, column=0)