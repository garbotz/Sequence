import time

class Timer:
	"""Handles round and turn/keypress timing."""

	def __init__(self):
		self.GAME_LENGTH = 60 # seconds
		self.move_start  = 0
		self.key_speeds  = []
		self.speed_avg   = 0

		self.start_time  = 0
		self.avg_speeds  = []

	# Turn operations

	def key_start(self):
		"Starts timing between key presses."
		self.move_start = time.time()

	def key_end(self):
		"On end of key press timing."
		key_gap = time.time() - self.move_start
		self.key_speeds.append(key_gap)
		self.speed_avg = sum(self.key_speeds) / len(self.key_speeds)

	# Round operations

	def get_time(self):
		return time.time()

	def start_round_time(self):
		"Start timing a new round."
		self.start_time = time.time()

	def get_duration(self):
		"Return how long the round has lasted."
		return time.time() - self.start_time

	def get_time_left(self):
		"Return how long is left in the round."
		return self.GAME_LENGTH - self.get_duration()

	def end_round_check(self):
		"End game if timer has expired."
		if self.get_duration() >= self.GAME_LENGTH:
			self.avg_speeds.append(self.speed_avg)
			return True
		else:
			return False

	def reset(self):
		self.key_speeds[:] = [] # clear key_speeds
		self.move_start = 0
		self.speed_avg = 0
		self.start_time = 0

	def get_avg_str(self):
		"""Returns current average speed between keypresses as a string."""
		a = "{} ms".format(int(self.speed_avg * 1000))
		return a

	def get_rem_str(self):
		"""Returns remaining round time as a string."""
		a = "{:.3f} s".format(self.get_time_left())
		return a