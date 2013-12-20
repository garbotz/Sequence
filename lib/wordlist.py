import random
import worditem

class WordList:
	"""Handles the dictionary that game words are pulled from."""

	def __init__(self):
		self.number_words = 8
		self.start_names = ["one","two","three","four","five","six","seven","eight"]
		self.file = "w_any_(4-12)_(30-50)"
		self.dictionary = open('data/'+self.file+'.txt').read().splitlines()
		self.active = []
		for n in range(self.number_words):
			self.active.append(worditem.WordItem(self.start_names[n],False))

	def cycle(self):
		l = len(self.active)
		x = 0
		while (x < l-1):
			self.active[x] = self.active[x+1]
			x+=1
		self.active[l-1] = self.getrand()

	def getrand(self):
		d = random.choice(self.dictionary)
		r = random.choice([True,False,False,False,False,False,False])
		return worditem.WordItem(d,r)

	def reset(self):
		self.active[:] = []
		for n in range(self.number_words):
			self.active.append(worditem.WordItem(self.start_names[n],False))