#!/usr/bin/python3
# Function to check for lowercase characters
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
