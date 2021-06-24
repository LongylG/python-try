import curses
from random import randrange, choice  # generate and place new tile
from collections import defaultdict


def main(stdscr):

    curses.use_default_colors()


curses.wrapper(main)
