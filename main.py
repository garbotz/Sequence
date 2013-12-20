import curses
from lib import wordlist, timer, score, buffinput, player

screen  = curses.initscr()
wordl   = wordlist.WordList()
timer   = timer.Timer()
score   = score.Score()
buff    = buffinput.BuffInput()
player  = player.Player()

colors  = {}
buff_color  = 7
running = True

def setup():
	curses.cbreak()
	curses.curs_set(0)
	curses.noecho()
	curses.start_color()

	curses.init_pair(1,curses.COLOR_BLACK,   curses.COLOR_WHITE)
	curses.init_pair(2,curses.COLOR_RED,     curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_WHITE,   curses.COLOR_RED)
	curses.init_pair(4,curses.COLOR_YELLOW,  curses.COLOR_BLACK)

	curses.init_pair(5,curses.COLOR_WHITE,   curses.COLOR_WHITE)
	curses.init_pair(6,curses.COLOR_BLACK,   curses.COLOR_BLACK)
	curses.init_pair(7,curses.COLOR_MAGENTA, curses.COLOR_RED)
	curses.init_pair(8,curses.COLOR_RED,     curses.COLOR_RED)

	curses.init_pair(9,curses.COLOR_BLUE,     curses.COLOR_YELLOW)

	colors['vis_0'] = curses.color_pair(6) # magenta buffer '.'
	colors['vis_1'] = curses.color_pair(5) # white '.'
	colors['vis_2'] = curses.color_pair(9) # blue on yellow
	colors['vis_3'] = curses.color_pair(0) # white on black

	colors['neg_0'] = curses.color_pair(6) # magenta buffer '.'
	colors['neg_1'] = curses.color_pair(5) # white '.'
	colors['neg_2'] = curses.color_pair(9) # blue on yellow
	colors['neg_3'] = curses.color_pair(2) # red on black
	colors['neg_4'] = curses.color_pair(3) # white on red
	colors['neg_5'] = curses.color_pair(8) # red on red

	colors['input_hit_0'] = curses.color_pair(0) # black on white
	colors['input_hit_1'] = curses.color_pair(1) # black on white
	colors['input_err_0'] = curses.color_pair(4) # yellow on black
	colors['input_err_1'] = curses.color_pair(3) # white on red
	colors['input_err_2'] = curses.color_pair(8) # red on red
	colors['input'] = curses.color_pair(0)

def run_game():
	"""Game instance."""
	wordl.reset()
	score.reset()
	timer.reset()
	buff.reset()
	running = True
	timer.start_round_time()
	while running:
		screen.clear()
		update_display()
		update_input()

def update_display():
	"""Updates all words on screen."""
	for i,w in enumerate(wordl.active):
		if player.slot[i]['active']:
			y = 4 + i
			x = 2
			if w.block:
				n = player.slot[i]['neg']
				if n == 0:
					screen.addstr(y, x, '!'*12, colors['neg_0'])
				elif n == 1:
					screen.addstr(y, x, '!'*len(w), colors['neg_1'])
				elif n == 5:
					screen.addstr(y, x, ' '*12, colors['neg_%s'%n])
				else:
					screen.addstr(y, x, w.string, colors['neg_%s'%n])
			else:
				v = player.slot[i]['vis']
				if v == 0:
					screen.addstr(y, x, '.'*12, colors['vis_0'])
				elif v == 1:
					screen.addstr(y, x, '.'*len(w), colors['vis_1'])
				else:
					screen.addstr(y, x, w.string, colors['vis_%s'%v])

	screen.addstr(1, 2,  score.get_val_str())
	screen.addstr(1, 10, timer.get_rem_str())
	# screen.addstr(1, 20, score.get_cnt_str())
	# screen.addstr(2, 2,  timer.get_avg_str())
	# if player.input_enabled:

	if player.input_enabled:
		screen.addstr(4, 2, buff.string, colors['input'])
	else:
		screen.addstr(4, 2, wordl.active[0].string, colors['input'])


	# screen.addstr(4, 2 + len(buff.string), '', colors['vis_0']) # caret
	screen.move(0,0)
	screen.refresh()

def update_input():
	global colors

	timer.key_start()
	key = screen.getch()
	timer.key_end()

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
		word = wordl.active[0]
		buff.add(chr(key))
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
			score.inc_key_count()
			score.inc_hits()
			score.add_norm()
			if player.err_enabled:
				colors['input'] = colors['input_hit_%s'%player.hit_lvl]
		else:
			score.inc_misses()
			score.err_norm()
			if player.err_enabled:
				colors['input'] = colors['input_err_%s'%player.err_lvl]
		if timer.end_round_check():
			end_round()
	else:
		pass

def end_round():
	""" Operations for end of game. """
	global running
	scstr = "%s %s" % (score.get_cumul(), timer.get_avg_str())
	wpm = "%s" % (int(score.key_cnt) / 5)
	score.add_prev_score("%s %s" % (scstr, wpm))
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