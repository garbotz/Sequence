import random
import worditem

class WordList:
	word_1 = worditem.WordItem('alpha')
	word_0 = worditem.WordItem('beats')

	select = "defaults"
	dictionary = open('data/%s.txt'%select).read().splitlines()

	def __init__(self):
		pass

	def cycle(self):
		self.word_0 = self.word_1
		self.word_1 = worditem.WordItem(random.choice(self.dictionary))

	def get_word(self,i):
		if i == 0:
			return self.word_0.get_string()
		elif i == 1:
			return self.word_1.get_string()