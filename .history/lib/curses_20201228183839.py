import curses
from curses import wrapper


def main(stdscr):

    # 清屏
    stdscr.clear()
    for i in range(0, 11):
        v = i - 10
        stdscr.addstr("------")

    stdscr.refresh()
    stdscr.getkey()


wrapper(main)
