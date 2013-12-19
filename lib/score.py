import time
import timer

class Score:

	def __init__(self):
		self.val_letter = 1
		self.val_word = 4
		self.val_err_norm = 10
		self.val_err_block = 30

		self.value    = 0
		self.key_cnt  = 0
		self.word_cnt = 0
		self.prev_scores = []
		self.key_misses = 0
		self.key_hits = 0

	def add_norm(self):
		self.value += self.val_letter

	def add_word(self):
		self.value += self.val_word

	def err_norm(self):
		if self.value - self.val_err_norm > 0:
			self.value -= self.val_err_norm
		else:
			self.value = 0

	def err_block(self):
		if self.value - self.val_err_block > 0:
			self.value -= self.val_err_block
		else:
			self.value = 0

	def inc_misses(self):
		self.key_misses += 1

	def inc_hits(self):
		self.key_hits += 1

	def add_prev_score(self,s):
		self.prev_scores.append(s)

	def inc_key_count(self):
		self.key_cnt += 1

	def inc_word_count(self):
		self.word_cnt += 1

	def get_cumul(self):
		a = self.get_val_str()
		b = self.get_cnt_str()
		c = self.get_acc_str()
		return "%s %s %s" % (a,b,c)

	def get_val_str(self):
		a = "{:0>4}".format(self.value)
		return a

	def get_cnt_str(self):
		a = "{:0>4}".format(self.key_cnt)
		b = "{:0>3}".format(self.word_cnt)
		return "(%sc:%sw)" % (a,b)

	def get_acc_str(self):
		a = "{:0>3} err".format(self.key_misses)
		return "(%s)" % (a)

	def reset(self):
		self.value    = 0
		self.key_cnt  = 0
		self.word_cnt = 0
		self.key_misses = 0
		self.key_hits = 0