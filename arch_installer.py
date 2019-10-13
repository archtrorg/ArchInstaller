#!usr/bin/env python3

import os
import sys


#Colors
DEFAULT = "\33[37m"
GREEN = "\33[32m"
RED = "\33[31m"

#Welcome message function
def welcome():
    print(GREEN)    #For green output format
    print(" █████╗ ██████╗  ██████╗██╗  ██╗")
    print("██╔══██╗██╔══██╗██╔════╝██║  ██║")
    print("███████║██████╔╝██║     ███████║")
    print("██╔══██║██╔══██╗██║     ██╔══██║")
    print("██║  ██║██║  ██║╚██████╗██║  ██║")
    print("╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝")
    print("                                ")
    print("██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗")
    print("██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗")
    print("██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝")
    print("██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗")
    print("██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║")
    print("╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝")
    print(DEFAULT)  #For default output format

    to_continue = input("Press any key to continue..")
    os.system("clear")


def manuel_partitioning():
    os.system("cfdisk")
    os.system("clear")
    os.system("lsblk")
    response = input("Are you sure about this configuration? [Y/n]")
    if response == 'Y' or response == 'y' or response == '':
        os.system("clear")
        return
    else:
        disk_partitioning()


def uefi_partitioning():
    os.system("parted /dev/sda mklabel gpt --script")

def dos_partitioning():
    os.system("parted /dev/sda mklabel msdos --script")

def auto_partitioning():
    selection = input("1-UEFI (new) ,2-DOS (old) \nSelection [1/2] :")
    if selection == '1':
        uefi_partitioning()
    elif selection == '2':
        dos_partitioning()
    else:
        os.system("clear")
        print(RED+"Wrong Selection"+DEFAULT)


#Disk partitioning function
def disk_partitioning():
    selection = input("1-Auto Partitioning, 2-Manuel Partitioning\nSelection [1/2] : ")
    if selection == '1':
        auto_partitioning()
    elif selection == '2':
        manuel_partitioning()




def main():
    if os.geteuid() != 0:   #Check whether user have root privileges or not
        print(RED+"You are not root"+DEFAULT)
        sys.exit(1)
    welcome()
    disk_partitioning()

if __name__ == '__main__':
    main()
