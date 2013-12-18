class WordItem:

	def __init__(self, string, block):
		self.string = string
		self.block = block

	def __len__(self): 
		return len(self.string)