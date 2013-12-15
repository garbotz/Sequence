import time

class Score:
	value      = 0
	key_count  = 0
	word_count = 0
	game_start_time = 0
	game_length = 60

	def __init__(self): pass
	#
	def start_game(self):       self.game_start_time = time.time()
	def add_score(self,i):      self.value += i
	def remove_score(self,i):   self.value -= i
	def inc_key_count(self):    self.key_count += 1
	def inc_word_count(self):   self.word_count += 1
	def check_end_game(self):
		if self.get_game_duration() >= self.game_length:
			return True
		else:
			return False
	#
	def reset_key_count(self):  self.key_count = 0
	def reset_score(self):      self.value = 0
	def reset_word_count(self): self.word_count = 0
	#
	def get_key_count(self):    return self.key_count
	def get_score(self):        return self.value
	def get_game_duration(self):return time.time() - self.game_start_time
	def get_time_left(self):    return self.game_length - self.get_game_duration()
	def get_word_count(self):   return self.word_count
	#