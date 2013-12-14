import curses
from lib import buffinput

screen = curses.initscr()
buff_in = buffinput.BuffInput()
running = True

def begin():
	"Initialize curses and gameloop."
	curses.cbreak()
	curses.curs_set(0)
	curses.noecho()
	gameloop()
	quit()

def gameloop():
	"Loop the game functions and display until game ends."
	while running:
		screen.clear()
		screen.addstr(0,0, "Word 1")
		screen.addstr(1,0, "Word 2")
		screen.addstr(2,0, buff_in.get())
		screen.refresh()
		prompt()

def prompt():
	"Get next immediate key press from user."
	global running

	key = screen.getch()
	if   key == 27:   # escape
		running = False
	elif key == 32: # space
		pass
	elif key == 8 or key == 127: # bs, del
		buff_in.clear()
	elif key >= 97 and key <= 122: # 'a' - 'z'
		buff_in.add(chr(key))
	elif key >= 65 and key <= 90: # 'A' - 'Z'
		buff_in.add(chr(key))

def quit():
	"Cleans up and exits."
	curses.cbreak(False)
	curses.echo()
	curses.curs_set(1)
	screen.clear()
	curses.endwin()
	exit()
	print "Goodbye"
	reset

begin()