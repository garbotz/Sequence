import curses
from lib import buffinput
from lib import wordlist
from lib import score

screen  = curses.initscr()
buff    = buffinput.BuffInput()
score   = score.Score()
wordl   = wordlist.WordList()
buff_color = 2
running = True

def begin():
	curses.cbreak()
	curses.curs_set(0)
	curses.noecho()
	curses.start_color()
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
	curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_RED)
	curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_WHITE)
	score.reset_key_count()
	score.reset_score()
	score.reset_word_count()
	wordl = wordlist.WordList()
	buff.clear()
	running = True
	score.start_game()
	while running:
		gameloop()
	quit()

def gameloop():
	global running, buff_color

	# update values
	wd0s = wordl.get_word(0).get_special()
	dwd0 = wordl.get_word(0).get_string()
	wd1s = wordl.get_word(1).get_special()
	dwd1 = wordl.get_word(1).get_string()
	wd2s = wordl.get_word(2).get_special()
	dwd2 = wordl.get_word(2).get_string()
	wd3s = wordl.get_word(3).get_special()
	dwd3 = wordl.get_word(3).get_string()
	dscr = score.get_score()
	dkct = score.get_key_count()
	dwct = score.get_word_count()
	dinp = buff.get_string()
	
	# update screen
	screen.clear()
	if wd3s: screen.addstr(2, 2, dwd3,curses.color_pair(3))
	else:    screen.addstr(2, 2, dwd3)	
	if wd2s: screen.addstr(4, 2, dwd2,curses.color_pair(3))
	else:    screen.addstr(4, 2, dwd2)
	if wd1s: screen.addstr(6, 2, dwd1,curses.color_pair(3))
	else:    screen.addstr(6, 2, dwd1)
	if wd0s: screen.addstr(8, 2, dwd0,curses.color_pair(3))
	else:    screen.addstr(8, 2, dwd0)
	screen.addstr(1, 20, "{: >6} ({: >4}:{: >4})".format(dscr,dkct,dwct))
	screen.addstr(2, 20, str(score.get_time_left()))
	screen.addstr(8, 2,  dinp, curses.color_pair(buff_color))
	screen.refresh()
	
	# wait for next input
	key = screen.getch()

	# act on input
	if   key == 27: # escape
		quit()
	elif key == 9: # tab
		begin()
	elif key == 32: # space
		wordl.cycle()			
		buff.clear()
	elif key == 8 or key == 127: # bs, del
		buff.clear()
	elif key >= 97 and key <= 122: # 'a' - 'z'
		if wd0s:
			score.remove_score(20)
		buff.add(chr(key))
		score.inc_key_count()
		#
		if buff.get_string() in dwd0:
			score.add_score(2)
			buff_color = 2
		else:
			score.remove_score(10)
			buff_color = 4
		#
		if buff.get_string() == dwd0:
			score.inc_word_count()
			wordl.cycle()
			buff.clear()
		#
		if score.check_end_game():
			end()
	else:
		pass

def end():
	global running
	dscr = score.get_score()
	dkct = score.get_key_count()
	dwct = score.get_word_count()
	score.add_prev_score("{: >6} ({: >4}:{: >4})\n".format(dscr,dkct,dwct))
	screen.clear()
	waiting = True
	while waiting:
		screen.addstr(1, 0, score.get_prev_scores())
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