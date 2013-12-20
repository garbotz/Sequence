class Player:

	def __init__(self):
		self.input_enabled = True
		self.hit_enabled = False
		self.hit_lvl = 1 # only option
		self.err_enabled = True
		self.err_lvl = 2 # 0-2

		self.slot = [{None}] * 8
		self.slot[0] = {'active':True,'vis':3,'neg':5}
		self.slot[1] = {'active':True,'vis':3,'neg':4}
		self.slot[2] = {'active':True,'vis':3,'neg':3}
		self.slot[3] = {'active':True,'vis':0,'neg':0}
		self.slot[4] = {'active':False,'vis':0,'neg':0}
		self.slot[5] = {'active':False,'vis':0,'neg':0}
		self.slot[6] = {'active':False,'vis':0,'neg':0}
		self.slot[7] = {'active':False,'vis':0,'neg':0}

	def get_slot(self, s):
		return self.slot[s]

