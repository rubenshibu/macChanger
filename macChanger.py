#!/usr/bin/env python

import subprocess
interface = input("Which one do you want to change \n [+] 1. wlan0 \n [+] 2. eth0")

if (interface == 1):
  newMacAddress = int(input("enter the Mac address you want to change (eg: 00:11:22:33:44:55) -"))
  print("[=] changeing MAC Address for wlan0 to" + newMacAddress)
  subprocess.call("ifconfig wlan0 down",shell=True)
  subprocess.call("ifconfig wlan0 hw ether" + newMacAddress, shell=True)
  subprocess.call("ifconfig wlan0 up", shell=True)
elif(interface == 2):
  newMacAddress = int(input("enter the Mac address you want to change (eg: 00:11:22:33:44:55) -"))
  print("[=] changeing MAC Address for eth0 to" + newMacAddress)
  subprocess.call("ifconfig eth0 down",shell=True)
  subprocess.call("ifconfig eth0 hw ether" + newMacAddress, shell=True)
  subprocess.call("ifconfig eth0 up", shell=True)
else:
  print("Error!!")
 


