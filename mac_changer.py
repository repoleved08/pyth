#!/usr/bin/env python3

# changing mac address (ifconfig)

import subprocess

import optparse

# parser is for use in arguments and help message



parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

# variables used in the program

# interface = input("Interface >")
# new_mac = input("MAC >")
print("=========================================================")
print("[+] Changing MAC address for " +interface+ " to " +new_mac)
print("=========================================================")

# To avoid misuse of the program, we use []
# and execution of inappropriate commands

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

# Final message indicating the successful change

print("[+] Your mac address has been successfully changed.")
print(":::....")
print("[+] Your new MAC address for " +interface+ " is now : " +new_mac+ " check by typing: ifconfig "+interface)
print(" ")
print(" ")
print("..........................@normangeek...............................")
print(" ")

# Use and Enjoy it.
# Credits @norman_kipngetich