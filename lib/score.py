import time

class Score:

	value    = 0
	key_cnt  = 0
	word_cnt = 0
	start_time = 0
	game_length = 60
	prev_scores = ""

	def __init__(self): pass
	
	def start_game(self):       self.start_time = time.time()
	def add_score(self,i):      self.value += i
	def add_prev_score(self,s): self.prev_scores = s + self.prev_scores
	def remove_score(self,i):   self.value -= i
	def inc_key_count(self):    self.key_cnt += 1
	def inc_word_count(self):   self.word_cnt += 1
	def get_duration(self): return time.time() - self.start_time
	def get_time_left(self): return self.game_length - self.get_duration()
	
	def check_end_game(self):
		if self.get_duration() >= self.game_length:
			return True
		else:
			return False
	
	def reset(self):
		self.value    = 0
		self.key_cnt  = 0
		self.word_cnt = 0
	