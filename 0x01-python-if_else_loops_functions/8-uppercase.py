#!/usr/bin/python3
def uppercase(str):
    for i in str:
        a = ord(i)
        if a >= 97 and a <= 122:
            i = chr(ord(i) - (ord('a') - ord('A')))
        print("{:s}".format(i), end="")
    print("")
