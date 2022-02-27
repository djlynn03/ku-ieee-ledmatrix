import curses


def main(screen):
    key = ''
    while key != 'q':
        key = screen.getkey()
        screen.addstr(0, 0, 'key: {:<10}'.format(key))


if __name__ == '__main__':
    curses.wrapper(main)