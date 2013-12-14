class BuffInput:
	""" An unbuffered input string reference object for the player. """
	player_input = ""

	def add(c):
		player_input + c

	def clear():
		player_input = ""

	def get():
		return player_input