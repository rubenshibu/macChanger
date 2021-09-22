#!/usr/bin/env python

import subprocess

newMacAddress = int(input("enter the Mac address you want to change (eg: 00:11:22:33:44:55) -"))

subprocess.call("ifconfig wlan0 down",shell=True)
subprocess.call("ifconfig wlan0 hw ether" + newMacAddress, shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)

