import curses


def main(stdsrc):
    # Clear screen

    stdsrc = curses.initscr()
    stdsrc.keypad(True)

    stdsrc.addstr('hello world!!')
    stdsrc.addstr(self, 10, 10, 'hello world!!')
    print(stdsrc.getkey())


curses.wrapper(main)
