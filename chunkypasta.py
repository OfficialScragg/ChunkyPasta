#!/usr/bin/env python3

import os
import pyperclip
import base64
import sys
import time
import pyautogui as pg
import argparse as ap

# Get command line args
parser = ap.ArgumentParser(description="Base64 encode files and copy paste them into an RDP window or something like that")
parser.add_argument("-f", "--filename", help="File to transfer", required=True)
parser.add_argument("-c", "--chunk", help="Size of chunks (in characters)", required=True)
parser.add_argument("-d", "--delay", help="Time to wait after pasting (lag compensation)", required=True)
args = parser.parse_args()
filename = args.filename
chunk_size = int(args.chunk)
delay = float(args.delay)

# Get the file and encode it with Base64
data = ""
try:
    file = open(filename, 'rb')
    print("Encoding your spaghetti...")
    data = base64.b64encode(file.read()).decode('ascii')
except Exception as e:
    print(e)
    sys.exit(1)

# Chop up the Base64 string into chunks of X amount of characters
print("Chopping up pasta...")
chunks = []
num_chunks = int(len(data)/chunk_size)
for c in range(0, num_chunks+1):
    chunks.append('')
    if c == num_chunks:
        chunks[c] = data[c*chunk_size::]
    else:
        chunks[c] = data[c*chunk_size:int(c+1)*chunk_size]

# 5 Second countdown timer so you can click into the RDP notepad
input("Ready for the pasta?\nPress any key...")
print("Click in your open notepad window (pasta starts in 5sec)")
for i in range(0, 5):
    time.sleep(1)
print("SeRVing PAsTa!")

# Copy to clipboard paste with CTRL+V and then wait for the set delay
total = len(chunks)
for i,c in enumerate(chunks):
    print("Progress: "+str(i+1)+"/"+str(total)+" chunks", end="\r")
    pyperclip.copy(c) # add to clipboard
    time.sleep(0.1)
    pg.hotkey('ctrl', 'v') # paste
    time.sleep(delay)

