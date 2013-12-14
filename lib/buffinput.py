class BuffInput:
	""" An unbuffered input string reference object for the player. """
	buff = ""

	def __init__(self):
		pass

	def add(self, c):
		self.buff += c

	def clear(self):
		self.buff = ""

	def get_string(self):
		return self.buff