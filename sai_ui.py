# import cgi
# import cgitb
# import sys
# import libs.sai_library as lib
import sai_methods.uii_methods as uimethods

homeobj = []
homeareas = []
homedevices = []


def ui_main():
    answer = print_menu()
    if answer == 'a':
        add_home_menu()
    if answer == 'b':
        add_room_menu()
    if answer == 'c':
        return
    if answer == 'd':
        show_homes()
    if answer == 'e':
        show_room()
    if answer == 'f':
        return


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
        print home.get_name()


def add_room_menu():
    print "\t*** Add new room ***"
    raw_input("which home do you want to add the room? <{}>\n> ".format(homeobj))
    roomname = raw_input("Enter new room name:> ")
    uimethods.add_hmarea(roomname)


def show_room():
    for room in homeareas:
        print room.get_name()