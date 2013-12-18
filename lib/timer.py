import time

class Timer:
	
	def __init__(self):
		self.GAME_LENGTH = 20
		self.HISTORY_MAX = 20
		self.key_speeds  = []
		self.avg_speeds  = []
		self.move_start  = 0
		self.speed_avg   = 0
		self.start_time  = 0

	def move_time_start(self):
		"Starts timing between key presses."
		self.move_start = time.time()

	def move_time_end(self):
		"On end of key press timing."
		key_gap = time.time() - self.move_start

		# Append unless history_max reached, otherwise cycle
		if len(self.key_speeds) < self.HISTORY_MAX: 
			self.key_speeds.append(key_gap)
		else: 
			l = len(self.key_speeds)
			x = 0
			while x < l-1:
				self.key_speeds[x] = self.key_speeds[x+1]
				x += 1
			self.key_speeds[l-1] = key_gap

		self.speed_avg = sum(self.key_speeds) / self.HISTORY_MAX	

	def start_game_time(self):
		"Start timing a new round."
		self.start_time = time.time()

	def get_duration(self): 
		"Return how long the round has lasted."
		return time.time() - self.start_time
	
	def get_time_left(self): 
		"Return how long is left in the round."
		return self.GAME_LENGTH - self.get_duration()
	
	def check_end_game(self):
		"End game if timer has expired."
		if self.get_duration() >= self.GAME_LENGTH:
			self.avg_speeds.append(self.speed_avg)
			return True
		else: 
			return False

	def reset(self):
		self.key_speeds = []
		self.move_start = 0
		self.speed_avg = 0
		self.start_time = 0