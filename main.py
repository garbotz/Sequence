import curses
from lib import buffinput

screen = curses.initscr()
buff = buffinput.BuffInput()
running = True

def begin():
	curses.cbreak()
	curses.curs_set(0)
	curses.noecho()
	while running:
		screen.clear()
		screen.addstr(2,2,"Word1")
		screen.addstr(3,2,"Word1")
		screen.addstr(4,2,buff.get_string())
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
		pass
	elif key == 8 or key == 127: # bs, del
		buff.clear()
	elif key >= 97 and key <= 122: # 'a' - 'z'
		buff.add(chr(key))
	elif key >= 65 and key <= 90: # 'A' - 'Z'
		buff.add(chr(key))
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