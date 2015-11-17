# -*- coding:Utf:8 -*-

from tkinter import *

W, H = 200, 100

class App(Tk):

	def __init__(self):
		Tk.__init__(self)
		self.fra1 = Frame(self, bg="blue", width = W, height = H)
		self.fra2 = Frame(self, bg="red", width = W, height = H)
		self.fra3 = Frame(self, bg="white", width = W, height = H)

		self.bou = Button(self.fra2, text="color", command=self.coloring)

	def boucle(self):
		self.packing()
		self.mainloop()

	def packing(self):
		self.fra1.pack()
		self.fra2.pack(anchor="nw")
		self.fra3.pack()
		self.bou.pack()

	def coloring(self):
		self.bou.destroy()

if __name__ == "__main__":
	app = App()
	app.boucle()