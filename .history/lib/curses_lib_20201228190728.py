import curses


def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        stdscr.addstr("----------")

    stdscr.refresh()
    stdscr.getkey()


curses.wrapper(main)
