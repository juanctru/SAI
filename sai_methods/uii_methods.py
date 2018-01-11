import libs.sai_library as lib
import sai_ui as ui


def add_device(properties=None):
    newdev = lib.Device(*properties)
    ui.homedevices.append(newdev)
    return newdev


def add_hmarea(homename):
    newhmarea = lib.HomeArea(homename)
    ui.homeareas.append(newhmarea)
    return newhmarea


def create_home(homename):
    newhome = lib.Home(homename)
    ui.homeobj.append(newhome)
    return newhome
