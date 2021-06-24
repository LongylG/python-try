import curses


def main(stdscr):
    # Clear screen
    stdscr.clear()
    stdscr = curses.initscr()
    curses.nocbreak()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        stdscr.addstr("----------")

    stdscr.refresh()
    stdscr.getkey()


stdscr = curses.initscr()
begin_x = 20
begin_y = 7
height = 5
width = 40
win = curses.newwin(height, width, begin_y, begin_x)
stdscr.addstr("hello world!!!!")
stdscr.refresh()
stdscr.getkey()
curses.wrapper(main)
