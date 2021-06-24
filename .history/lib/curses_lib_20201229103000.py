import curses


def main():
    # Clear screen
    curses.cbreak()
    stdsrc = curses.initscr()
    stdsrc.keypad(True)

    stdsrc.addstr('hello world!!')

    print(stdsrc.getkey())


main()
