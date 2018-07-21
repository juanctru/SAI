import libs.sai_library as lib
import sai_console_ui as ui


def add_device(devname, room):
    newdev = lib.Device(dev_name=devname, dev_area=room)
    ui.homedevices[devname] = newdev
    ui.homeareas[room].add_device(newdev)
    return newdev


def add_hmarea(roomname, home):
    newhmarea = lib.HomeArea(roomname)
    ui.homeareas[roomname] = newhmarea
    ui.homeobj[home].add_area(newhmarea)
    return newhmarea


def create_home(homename):
    newhome = lib.Home(homename)
    ui.homeobj[homename] = newhome
    return newhome
