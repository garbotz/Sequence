import random
import worditem

class WordList:
	words = [None,None,None,None]
	words[0] = worditem.WordItem('one', False)
	words[1] = worditem.WordItem('two', False)
	words[2] = worditem.WordItem('three', False)
	words[3] = worditem.WordItem('four', False)

	choice_counter = 0
	dict_equal = open('data/weight_equal_8_12.txt').read().splitlines()
	# dict_left = open('data/onlyleft.txt').read().splitlines()
	# dict_right = open('data/onlyright.txt').read().splitlines()
	# dict_3left = open('data/3left.txt').read().splitlines()
	# dict_3right = open('data/3right.txt').read().splitlines()
	dict_r_left = open('data/rhythm_left_6_20.txt').read().splitlines()

	def __init__(self):
		pass

	def cycle(self):
		self.words[0] = self.words[1]
		self.words[1] = self.words[2]
		self.words[2] = self.words[3]
		self.words[3] = self.list_choice()

		if self.choice_counter == 7:
			self.choice_counter = 0
		else: 
			self.choice_counter += 1		

	def list_choice(self):
		return worditem.WordItem(random.choice(self.dict_r_left),random.choice([True,False, False, False]))
		"""
			0 - left
			1 - sorta left
			2 - equal
			3 - sorta right
			4 - right
			5 - sorta right
			6 - equal
			7 - sorta left

		# LEFT
		if self.choice_counter == 0:
			return worditem.WordItem(random.choice(self.dict_left),random.choice([True,False]))
		# SORTA LEFT	
		elif self.choice_counter == 1 or self.choice_counter == 7:
			return worditem.WordItem(random.choice(self.dict_3left),random.choice([True,False]))		
		# EQUAL
		elif self.choice_counter == 2 or self.choice_counter == 6:
			return worditem.WordItem(random.choice(self.dict_equal),random.choice([True,False,False,False]))
		# SORTA RIGHT
		elif self.choice_counter == 3 or self.choice_counter == 5:
			return worditem.WordItem(random.choice(self.dict_3right),random.choice([True,False]))
		# RIGHT
		elif self.choice_counter == 4:
			return worditem.WordItem(random.choice(self.dict_right),random.choice([True,False]))		
		"""


	def get_word(self,i):
		return self.words[i]