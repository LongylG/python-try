import curses


def main():
    # Clear screen
    stdsrc = curses.initscr()
    stdsrc.keypad(True)
    stdsrc.addstr('hello world!!')

    stdsrc.getstr
