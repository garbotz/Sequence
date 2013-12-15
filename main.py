import curses
from lib import buffinput
from lib import wordlist
from lib import score

screen  = curses.initscr()
buff    = buffinput.BuffInput()
score   = score.Score()
wordl   = wordlist.WordList()
running = True

def begin():
	curses.cbreak()
	curses.curs_set(0)
	curses.noecho()
	while running:
		gameloop()
	quit()

def gameloop():
	global running

	# update values
	wd0s = wordl.get_word(0).get_special()
	dwd0 = wordl.get_word(0).get_string()
	wd1s = wordl.get_word(1).get_special()
	dwd1 = wordl.get_word(1).get_string()
	dscr = score.get_score()
	dkct = score.get_key_count()
	dwct = score.get_word_count()
	dinp = buff.get_string()
	
	# update screen
	screen.clear()
	if wd1s: screen.addstr(2,2,dwd1,curses.A_REVERSE)
	else: screen.addstr(2, 2, dwd1)
	if wd0s: screen.addstr(3,2,dwd0,curses.A_REVERSE)
	else: screen.addstr(3, 2, dwd0)
	screen.addstr(1, 15, "{} ({}:{})".format(dscr,dkct,dwct))
	screen.addstr(3, 2, dinp, curses.A_UNDERLINE)
	screen.refresh()
	
	# wait for next input
	key = screen.getch()

	# act on input
	if   key == 27: # escape
		running = False
	elif key == 32: # space
		wordl.cycle()			
		buff.clear()
	elif key == 8 or key == 127: # bs, del
		buff.clear()
	elif key >= 97 and key <= 122: # 'a' - 'z'
		if wd0s:
			score.remove_score(40)
		buff.add(chr(key))
		score.inc_key_count()
		if buff.get_string() in dwd0:
			score.add_score(1)
		else:
			score.remove_score(20)
		if buff.get_string() == dwd0:
			score.inc_word_count()
			wordl.cycle()
			buff.clear()
	else:
		pass

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