from sai_globals import *

def switch_deflt():
    return


def lamp_deflt():
    return


def ligh_deflt():
    return


def assign_method(devtype):
    if devtype == LAMP:
        return lamp_deflt
    if devtype == LIGHT:
        return ligh_deflt
    if devtype == SWITCH:
        return switch_deflt
