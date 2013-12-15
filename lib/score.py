class Score:
	value      = 0
	key_count  = 0
	word_count = 0

	def __init__(self):
		pass

	#

	def add_score(self,i):
		self.value += i

	def remove_score(self,i):
		self.value -= i

	def reset_score(self):
		self.value = 0

	def inc_key_count(self):
		self.key_count += 1

	def reset_key_count(self):
		self.key_count = 0

	def inc_word_count(self):
		self.word_count += 1

	def reset_word_count(self):
		self.word_count = 0

	#

	def get_score(self):
		return self.value

	def get_key_count(self):
		return self.key_count

	def get_word_count(self):
		return self.word_count