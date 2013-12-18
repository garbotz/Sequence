import curses
from lib import wordlist
from lib import timer
from lib import score
from lib import buffinput

screen  = curses.initscr()
wordl   = wordlist.WordList()
timer   = timer.Timer()
score   = score.Score()
buff    = buffinput.BuffInput()
buff_color  = 2
block_color = 5
running = True

def begin():
	curses.cbreak()
	curses.curs_set(0)
	curses.noecho()
	curses.start_color()
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
	curses.init_pair(3, curses.COLOR_RED,   curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_BLUE,  curses.COLOR_RED)
	curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_WHITE)
	curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(7, curses.COLOR_YELLOW,curses.COLOR_BLACK)
	score.reset()
	timer.reset()
	wordl = wordlist.WordList()
	buff.reset()
	running = True
	timer.start_round_time()
	while running:
		gameloop()
	quit()

def gameloop():
	global running, buff_color
	words = wordl.active

	# update screen
	screen.clear()
	for i,w in enumerate(words):
		if w.block:
			screen.addstr(4+(i*2), 2+i, w.string, curses.color_pair(block_color))
		else:
			screen.addstr(4+(i*2), 2+i, w.string)
	screen.addstr(1, 2, "{:4>}".format(score.value))
	screen.addstr(2, 2, "{} ms".format(int(timer.speed_avg * 1000)))
	screen.addstr(2, 10, "{:.3f} s".format(timer.get_time_left()))
	screen.addstr(1, 20, "({: >4}:{: >4})".format(score.key_cnt,score.word_cnt))

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
		begin()
	elif key == 32: # space
		wordl.cycle()
		buff.reset()
	elif key == 8 or key == 127: # bs, del
		buff.reset()
	elif key >= 97 and key <= 122: # 'a' - 'z'
		key_action(key)
	else:
		pass

def key_action(key):
	global buff_color

	buff.add(chr(key))
	score.inc_key_count()

	if wordl.active[0].block: # if special, remove points
		score.err_block()

	if buff.string in wordl.active[0].string: # check validity of input
		score.add_norm()
		if buff_color == 4: buff_color = 2

	else:
		score.err_norm()
		if buff_color == 2: buff_color = 4

	if buff.get() == wordl.active[0].string: # cycle if input is correct
		score.add_word()
		score.inc_word_count()
		wordl.cycle()
		buff.reset()

	if timer.end_round_check(): # check if game should be ended
		end()

def end():
	""" Operations for end of game. """
	global running
	score.add_prev_score("{: >6} ({: >4}:{: >4})\n".format(score.value,score.key_cnt,score.word_cnt))
	screen.clear()
	while True:
		x = 0
		while x < len(score.prev_scores):
			screen.addstr(1+x, 0, score.prev_scores[x])
			screen.addstr(1+x, 20, "{}".format(int(timer.avg_speeds[x]*1000)))
			x+=1
		screen.refresh()
		key = screen.getch()
		if key == 9: # tab
			begin()
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

begin()