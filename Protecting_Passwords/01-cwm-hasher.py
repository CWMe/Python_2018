#! /usr/local/bin/python3.6
# name: 	01-cwm-hasher.py
# author: 	Sunday Wiley
# details: 	(script 1 of 2) to hash 10K plaintext into 
#		md5 encrypted hashes and to save output to
#		a RAINBOW_TABLE.txt" file.

import hashlib

# copy and hash 10K plaintext passwords
lines = [line.rstrip("\n") for line in open("10K_PLAINTEXT_PASSWORDS.txt")]

rainbow = open("RAINBOW_TABLE.txt", "w")
for line in lines:
	md5_hashed = hashlib.md5(line.encode())
	rainbow.write(md5_hashed.hexdigest() + "\n")
rainbow.close();
