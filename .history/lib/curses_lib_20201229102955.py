import curses


def main():
    # Clear screen
    stdsrc = curses.initscr()
    stdsrc.keypad(True)
    curses.cbreak()
    stdsrc.addstr('hello world!!')

    print(stdsrc.getkey())


main()
