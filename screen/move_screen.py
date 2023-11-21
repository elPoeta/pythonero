import curses

def main(stdscr):

	while True:
		key = stdscr.getch()

		stdscr.clear()

		if key == curses.KEY_UP:
			stdscr.addstr(0, 0, "You pressed Up key!")
		elif key == curses.KEY_DOWN:
			stdscr.addstr(0, 0, "You pressed Down key!")
		elif key == curses.KEY_ENTER or key in [10, 13]:
			stdscr.addstr(0, 0, "You pressed Enter.")
		else:
			break

		stdscr.refresh()

if __name__ == '__main__':
    curses.wrapper(main)