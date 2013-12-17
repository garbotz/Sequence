class BuffInput:
	""" An unbuffered input string reference object for the player. """
	string = ""

	def __init__(self): pass
	def __len__(self): return len(string)

	def get(self): return self.string	
	def add(self, c): self.string += c
	def reset(self): self.string = ""