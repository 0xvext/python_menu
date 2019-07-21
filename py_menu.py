#!/usr/bin/python3

# Python 2.x backward compatibility
from __future__ import division
from __future__ import print_function

# Protection from Python 2.x input vulnerability
try:
    input = raw_input
except:
    pass

import os

# Banner design variables
banner_chr = "#"
banner_wid = 26
banner_edg = banner_chr * banner_wid

# Function to pad banner rows
def pad_banner(a_str):
    padded = a_str + " " * (banner_wid - len(a_str) - 6)
    return padded

# Print banner
print(banner_edg)
print(banner_chr, pad_banner(" "), banner_chr, sep="  ")
print(banner_chr, pad_banner("Select an option: "), banner_chr, sep="  ")
print(banner_chr, pad_banner(" "), banner_chr, sep="  ")
print(banner_chr, pad_banner("[1] - SSH localhost"), banner_chr, sep="  ")
print(banner_chr, pad_banner("[2] - SSH 127.0.0.1"), banner_chr, sep="  ")
print(banner_chr, pad_banner("[3] - SSH 127.1.1.1"), banner_chr, sep="  ")
print(banner_chr, pad_banner("[4] - SSH 127.2.2.2"), banner_chr, sep="  ")
print(banner_chr, pad_banner(" "), banner_chr, sep="  ")
print(banner_edg)

# Prompt user for selection
user_choice = input()

# Define command options
command_1 = "ssh localhost"
command_2 = "ssh 127.0.0.1"
command_3 = "ssh 127.1.1.1"
command_4 = "ssh 127.2.2.2"

# Run command based on selection
if user_choice == str(1):
    os.system(command_1)
elif user_choice == str(2):
    os.system(command_2)
elif user_choice == str(3):
    os.system(command_3)
elif user_choice == str(4):
    os.system(command_4)
else:
    print("Please make a valid selection.")
