#!/usr/bin/python3
'''Function that reads a textfile and prints it to stdout'''


def read_file(filename=""):
    '''read a textfile only'''
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
