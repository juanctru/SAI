__author__ = 'Juan Carlos Trujillo'

# from multiprocessing import Pool, TimeoutError
from platform import system
import sai_console_ui as ui
import sai_methods.core_methods as corelib
from sai_globals import *

systemOS = system().lower()

core = corelib.core_state_machine


def saicore():
    for process, method in core.iteritems():
        print process
        method()


def start():
    while True:
        r = ui.ui_main()
        if r == EXIT_CMD:
            print 'Exiting...'
            return
        saicore()


if __name__ == '__main__':
    start()
