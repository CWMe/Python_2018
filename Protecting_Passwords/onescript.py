# Shijit Dasgupta
# 05/25/2018

import hashlib

passwords = [line.rstrip("\n") for line in open('plaintext_passwords.txt')]

hashes_target = [recovered.rstrip("\n") for recovered in open('recovered_password_hashes.txt')]

passbook = {} # empty dictionary

for password in passwords:
        hashing = hashlib.md5(password.encode())
        hashed = hashing.hexdigest()
        passbook[password] = hashed
        print(password, ' and now hashed ', passbook[password])

        if str(hashed) in hashes_target:
            print('This plaintext password ', password, ' was recovered hashed as ', hashed)
