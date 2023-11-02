# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: curses\wrapper.pyc
# Compiled at: 2011-05-30 06:53:52
"""curses.wrapper

Contains one function, wrapper(), which runs another function which
should be the rest of your curses-based application.  If the
application raises an exception, wrapper() will restore the terminal
to a sane state so you can read the resulting traceback.

"""
import curses

def wrapper(func, *args, **kwds):
    """Wrapper function that initializes curses and calls another function,
    restoring normal keyboard/screen behavior on error.
    The callable object 'func' is then passed the main window 'stdscr'
    as its first argument, followed by any other arguments passed to
    wrapper().
    """
    try:
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(1)
        try:
            curses.start_color()
        except:
            pass

        return func(stdscr, *args, **kwds)
    finally:
        if 'stdscr' in locals():
            stdscr.keypad(0)
            curses.echo()
            curses.nocbreak()
            curses.endwin()