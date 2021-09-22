#!/usr/bin/env python

import subprocess

def change_Mac(interface, newMacAddress):
  print("[=] changeing MAC Address for wlan0 to" + newMacAddress)
  subprocess.call(["ifconfig", interface ,"down"],shell=True)
  subprocess.call(["ifconfig wlan0 hw ether", newMacAddress], shell=True)
  subprocess.call("ifconfig",interface, "up", shell=True)

print("enter the Mac address you want to change (eg: 00:11:22:33:44:55) -")
newMacAddress = int(input("New MAC >"))
interface = input("Which one do you want to change \n [+] 1. wlan0 \n [+] 2. eth0 >")

if (interface == 1):
  change_Mac(wlan0, newMacAddress)
elif(interface == 2):
  change_Mac(eth0, newMacAddress)
else:
  print("Error!!")
 


