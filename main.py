import curses
from lib import wordlist, timer, score, buffinput

screen  = curses.initscr()
wordl   = wordlist.WordList()
timer   = timer.Timer()
score   = score.Score()
buff    = buffinput.BuffInput()
buff_color  = 2
block_color = 3
running = True

def setup():
	curses.cbreak()
	curses.curs_set(0)
	curses.noecho()
	curses.start_color()
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
	curses.init_pair(3, curses.COLOR_RED,   curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_RED,  curses.COLOR_MAGENTA)
	curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_WHITE)
	curses.init_pair(6, curses.COLOR_BLUE, curses.COLOR_WHITE)
	curses.init_pair(7, curses.COLOR_YELLOW,curses.COLOR_BLACK)
	curses.init_pair(8, curses.COLOR_BLACK,   curses.COLOR_RED)
	curses.init_pair(9, curses.COLOR_WHITE,   curses.COLOR_RED)

def run_game():
	"""Game instance."""
	wordl.reset()
	score.reset()
	timer.reset()
	buff.reset()
	running = True
	timer.start_round_time()
	while running:
		gameloop()

def gameloop():
	"""Main game loop. Redraws canvas and waits for input."""

	# update screen
	screen.clear()
	for i,w in enumerate(wordl.active):
		if w.block:
			if i == 1:
				screen.addstr(4+(i), 2, w.string, curses.color_pair(8))
			elif i == 0:
				screen.addstr(4+(i), 2, w.string, curses.color_pair(9))
			else:
				screen.addstr(4+(i), 2, w.string, curses.color_pair(block_color))
		else:
			if i == 1:
				screen.addstr(4+(i), 2, w.string, curses.color_pair(6))
			elif i == 0:
				screen.addstr(4+(i), 2, w.string, curses.color_pair(5))
			else:
				screen.addstr(4+(i), 2, w.string, curses.color_pair(1))
	screen.addstr(1, 2,  score.get_val_str())
	screen.addstr(1, 20, score.get_cnt_str())
	screen.addstr(2, 2,  timer.get_avg_str())
	screen.addstr(2, 10, timer.get_rem_str())
	screen.addstr(4, 2,  buff.string, curses.color_pair(buff_color))
	screen.refresh()

	# wait for next input
	timer.turn_start()
	key = screen.getch()
	timer.turn_end()

	# act on input
	if   key == 27: # escape
		quit()
	elif key == 9: # tab
		run_game()
	elif key == 32: # space
		wordl.cycle()
		buff.reset()
	elif key == 8 or key == 127: # bs, del
		buff.reset()
	elif key >= 97 and key <= 122: # 'a' - 'z'
		buff.add(chr(key))
		score.inc_key_count()
		key_action(key)
	else:
		pass

def key_action(key):
	"""Alphanumeric input to be matched against play word."""
	global buff_color
	word = wordl.active[0]

	# validate input against game word
	if word.block:
		score.inc_misses()
		score.err_block()
	elif buff.string == word.string:
		score.inc_hits()
		score.add_word()
		score.inc_word_count()
		wordl.cycle()
		buff.reset()
	elif buff.string == word.string[:len(buff.string)]:
		score.inc_hits()
		score.add_norm()
		if buff_color == 4: buff_color = 2
	else:
		score.inc_misses()
		score.err_norm()
		if buff_color == 2: buff_color = 4

	if timer.end_round_check():
		end()

def end():
	""" Operations for end of game. """
	global running
	scstr = "%s %s" % (score.get_cumul(), timer.get_avg_str())
	score.add_prev_score(scstr)
	screen.clear()
	while True:
		screen.addstr(1, 2, "Most recent scores:")
		for i,s in enumerate(reversed(score.prev_scores)):
			screen.addstr(2+i, 2, s)
		screen.refresh()
		key = screen.getch()
		if key == 9: # tab
			run_game()
		if key == 27:
			quit()

def quit():
	"""Cleans up and exits."""
	screen.clear()
	curses.cbreak(False)
	curses.echo()
	curses.curs_set(1)
	curses.endwin()
	exit()
	reset

setup()
run_game()
quit()