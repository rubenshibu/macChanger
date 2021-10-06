#!/usr/bin/env python

import subprocess
import optparse

# userinput
def get_arguments():
  parser = optparse.OptionParser()
  parser.add_option("-i","--interface",dest="interface",help="interface to change its MAC address")
  parser.add_option("-m","--new_mac", help="New MAC Address")
  (options,arguments) = parser.parse_args()
  if not options.interface:
    parser.error("[-] please specify an interface, use --help for more info")
    #handle
  elif not options.newMacAddress:
    #handle
    parser.error("[-] please specify an MAC address, use --help for more info")
  return options
def change_Mac(interface, newMacAddress):
  print("[=] changeing MAC Address for wlan0 to" + newMacAddress)
  subprocess.call(["ifconfig", interface ,"down"],shell=True)
  subprocess.call(["ifconfig wlan0 hw ether", newMacAddress], shell=True)
  subprocess.call("ifconfig",interface, "up", shell=True)

options = get_arguments()
# print("enter the Mac address you want to change (eg: 00:11:22:33:44:55) -")
# newMacAddress = int(input("New MAC >"))
# interface = input("Which one do you want to change \n [+] 1. wlan0 \n [+] 2. eth0 >")
change_Mac(options.interface, options.newMacAddress)


