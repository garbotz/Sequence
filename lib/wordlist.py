import random
import worditem

class WordList:
	"""Handles the dictionary that game words are pulled from."""

	def __init__(self):
		self.file = "w_any_(4-12)_(30-50)"
		self.dictionary = open('data/'+self.file+'.txt').read().splitlines()
		self.active = []
		self.active.append(worditem.WordItem('one',  False))
		self.active.append(worditem.WordItem('two',  False))
		self.active.append(worditem.WordItem('three',False))
		self.active.append(worditem.WordItem('four', False))
		self.active.append(worditem.WordItem('five',  False))
		self.active.append(worditem.WordItem('six',  False))
		self.active.append(worditem.WordItem('seven',False))
		self.active.append(worditem.WordItem('eight', False))

	def cycle(self):
		l = len(self.active)
		x = 0
		while (x < l-1):
			self.active[x] = self.active[x+1]
			x+=1
		self.active[l-1] = self.getrand()

	def getrand(self):
		d = random.choice(self.dictionary)
		r = random.choice([True,False,False,False])
		return worditem.WordItem(d,r)

	def reset(self):
		self.active[:] = []
		self.active.append(worditem.WordItem('one',  False))
		self.active.append(worditem.WordItem('two',  False))
		self.active.append(worditem.WordItem('three',False))
		self.active.append(worditem.WordItem('four', False))
		self.active.append(worditem.WordItem('five',  False))
		self.active.append(worditem.WordItem('six',  False))
		self.active.append(worditem.WordItem('seven',False))
		self.active.append(worditem.WordItem('eight', False))