import curses


def main(stdsrc):
    # Clear screen

    stdsrc = curses.initscr()
    stdsrc.keypad(True)

    stdsrc.addstr('hello world!!')
    stdsrc.addstr('hello world!!', 10, 10)
    print(stdsrc.getkey())


curses.wrapper(main)
