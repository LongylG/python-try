import curses


def main(stdscr):

    curses.use_default_colors()


curses.wrapper(main)