import curses


def main():
    # Clear screen

    stdsrc = curses.initscr()
    curses.cbreak()
    stdsrc.keypad(True)

    stdsrc.addstr('hello world!!')

    print(stdsrc.getkey())


main()
