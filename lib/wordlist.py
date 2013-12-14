import random
import worditem

class WordList:
	word_1 = worditem.WordItem('alpha', False)
	word_0 = worditem.WordItem('beats', False)

	select = "defaults"
	dictionary = open('data/%s.txt'%select).read().splitlines()

	def __init__(self):
		pass

	def cycle(self):
		self.word_0 = self.word_1
		self.word_1 = worditem.WordItem(random.choice(self.dictionary),random.choice([True,False,False]))

	def get_word(self,i):
		if i == 0:
			return self.word_0
		elif i == 1:
			return self.word_1