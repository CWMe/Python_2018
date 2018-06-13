#! /usr/local/bin/python3.6
# name: 	02-cwm-fetcher.py
# author: 	Sunday Wiley
# details: 	(script 2 of 2) to hash 10K plaintext into 
#		md5 encrypted hashes and to save output to
#		a RAINBOW_TABLE.txt" file.

import hashlib, re, sys

hashes = [line.rstrip("\n") for line in open("RECOVERED_PASSWORD_HASHES.txt")]
rainbow = [line.rstrip("\n") for line in open("RAINBOW_TABLE.txt")]

passwords = open("10K_PLAINTEXT_PASSWORDS.txt", "r")
plaintext = passwords.readlines()

# start timer
from datetime import datetime
# run through retrievable hashes
def findme(text): 
	for i in range(len(rainbow)): 
		if text == rainbow[i]: 
			return str(i) + ":FOUND"
for hashed_password in hashes:
	start_time = datetime.now()
	found_index = findme(hashed_password)
	if (found_index): 
		str_index, OK = found_index.split(":")
		index = int(str_index)	
		time = datetime.now() - start_time 
		print(hashed_password + " found"
				+ " at index " + str(index)
				+ " in " + str(time) + " seconds."
				+ " The password is: " + plaintext[index].rstrip("\n") + ".")
	else: 
		time = datetime.now() - start_time 
		print("Spent " + str(time) + " seconds searching, but couldn't find " + hashed_password)
