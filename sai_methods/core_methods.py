from sai_ui import *
from sai_globals import *


def chkdevstat():
    devices = homedevices
    for device in devices:
        print device.get_name()
        device.method_call(action=CHKSTAT)
    return 0


def chknetwork():
    print "Here will scan network to find devices"
    return 0


core_state_machine = dict(checkDevStatus=chkdevstat,
                          checkNetwork=chknetwork)
