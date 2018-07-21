# import cgi
# import cgitb
# import sys
# import libs.sai_library as lib
import sai_methods.uii_methods as uimethods
from sai_globals import *

homeobj = {}
homeareas = {}
homedevices = {}


def ui_main():
    answer = print_menu()
    if answer == 'a':
        add_home_menu()
        return 0
    if answer == 'b':
        add_room_menu()
        return 0
    if answer == 'c':
        add_device_menu()
        return 0
    if answer == 'd':
        show_homes()
        return 0
    if answer == 'e':
        show_room()
        return 0
    if answer == 'f':
        show_devices()
        return 0
    if answer == 'exit':
        return EXIT_CMD
    else:
        print "Not valid option"
        return -1


def print_menu():
    print "\t***** SAI main page ****"
    print "  a) Add home"
    print "  b) Add room"
    print "  c) Add device"
    print "  d) Show homes"
    print "  e) Show rooms"
    print "  f) Show devices"
    print "\n\t {} homes controlling".format(len(homeobj))
    print "\t {} rooms added".format(len(homeareas))
    print "\t {} devices added".format(len(homedevices))
    return raw_input("choose an option: ")


def add_home_menu():
    print "\t*** Add new home ***"
    hname = raw_input("Enter new home name:> ")
    uimethods.create_home(hname)


def show_homes():
    for home in homeobj:
        print "#{}".format(home)


def add_room_menu():
    print "\t*** Add new room ***"
    home = raw_input("which home do you want to add the room? <{}>\n> ".format(homeobj.keys()))
    roomname = raw_input("Enter new room name:> ")
    uimethods.add_hmarea(roomname=roomname, home=home)


def show_room():
    home = raw_input("which home do you want to show the rooms? <{}>\n> ".format(homeobj.keys()))
    for room in homeobj[home].get_areas_list():
        print "*{}".format(room)


def add_device_menu():
    print "\t*** Add new device ***"
    room = raw_input("which room do you want to add the device? <{}>\n> ".format(homeareas.keys()))
    devname = raw_input("Enter new device name:> ")
    uimethods.add_device(devname=devname, room=room)


def show_devices():
    home = raw_input("which home do you want to show the rooms? <{}>\n> ".format(homeobj.keys()))
    for room in homeobj[home].get_areas_obj():
        print "*{}".format(room.get_name())
        for device in room.get_devices_list():
            print "\t-{}".format(device)
