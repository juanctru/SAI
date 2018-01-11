__author__ = 'Juan Carlos Trujillo'

# from multiprocessing import Pool, TimeoutError
from platform import system
import sai_ui as ui
import sai_methods.core_methods as corelib

systemOS = system().lower()

core = corelib.core_state_machine


def saicore():
    for process in core:
        print process


def start():
    while True:
        ui.ui_main()
        saicore()



if __name__ == '__main__':
    start()
