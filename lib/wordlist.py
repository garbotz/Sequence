import random
import worditem

class WordList:

	def __init__(self):
		self.dictionary = open('data/w_any_(4-12)_(30-50).txt').read().splitlines()
		self.active = []
		self.active.append(worditem.WordItem('one',True))
		self.active.append(worditem.WordItem('two',True))
		self.active.append(worditem.WordItem('three',True))
		self.active.append(worditem.WordItem('four',True))
		# self.active.append(worditem.WordItem('five',True))
		# self.active.append(worditem.WordItem('six',True))		
	
	def cycle(self):
		l = len(self.active)
		x = 0
		while (x < l-1):
			self.active[x] = self.active[x+1]
			x+=1 
		self.active[l-1] = self.getrand()

	def getrand(self):
		return worditem.WordItem(random.choice(self.dictionary),random.choice([True,False, False, False]))