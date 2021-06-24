import curses


def main(stdsrc):
    # Clear screen

    stdsrc = curses.initscr()
    stdsrc.keypad(True)
    stdsrc.echo()

    stdsrc.addstr('hello world!!')
    stdsrc.addstr(10, 0, 'hello world!!', 0)
    print(stdsrc.getkey())


curses.wrapper(main)
