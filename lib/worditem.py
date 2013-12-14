class WordItem:
	string = ""
	special = False

	def __init__(self, w, s):
		self.string = w
		self.special = s

	def get_string(self):
		return self.string

	def get_word(self):
		return self

	def get_special(self):
		return self.special