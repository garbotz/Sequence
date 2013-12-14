import curses
from lib import buffinput
from lib import wordlist

screen = curses.initscr()
buff = buffinput.BuffInput()
wordl = wordlist.WordList()
running = True

def begin():
	curses.cbreak()
	curses.curs_set(0)
	curses.noecho()
	while running:
		screen.clear()
		
		if wordl.get_word(1).get_special():
			screen.addstr(2, 2, wordl.get_word(1).get_string(), curses.A_REVERSE)
		else:
			screen.addstr(2, 2, wordl.get_word(1).get_string())
			
		if wordl.get_word(0).get_special():
			screen.addstr(3, 2, wordl.get_word(0).get_string(), curses.A_STANDOUT)
		else:
			screen.addstr(3, 2, wordl.get_word(0).get_string())

		screen.addstr(3, 2, buff.get_string(),curses.A_UNDERLINE)
		screen.refresh()
		prompt()
	quit()

def prompt():
	"""Get next immediate key press from user."""
	global running
	key = screen.getch()
	if   key == 27:   # escape
		running = False
	elif key == 32: # space
		if wordl.get_word(0).get_special():
			pass
		wordl.cycle()			
		buff.clear()

	elif key == 8 or key == 127: # bs, del
		buff.clear()
	elif key >= 97 and key <= 122: # 'a' - 'z'
		buff.add(chr(key))
		check()
	elif key >= 65 and key <= 90: # 'A' - 'Z'
		buff.add(chr(key))
		check()
	else:
		pass

def check():
	if buff.get_string() == wordl.get_word(0).get_string():
		wordl.cycle()
		buff.clear()

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