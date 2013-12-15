import random
import worditem

class WordList:
	words = [None,None,None,None]
	words[0] = worditem.WordItem('one', False)
	words[1] = worditem.WordItem('two', False)
	words[2] = worditem.WordItem('three', False)
	words[3] = worditem.WordItem('four', False)

	select = "defaults"
	dictionary = open('data/%s.txt'%select).read().splitlines()

	def __init__(self):
		pass

	def cycle(self):
		self.words[0] = self.words[1]
		self.words[1] = self.words[2]
		self.words[2] = self.words[3]
		self.words[3] = worditem.WordItem(random.choice(self.dictionary),random.choice([True,False,False]))

	def get_word(self,i):
		return self.words[i]