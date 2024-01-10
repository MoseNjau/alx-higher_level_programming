#!/usr/bin/python3
'''Function that writes a string to a textfile and returns no. of chars written
'''


def write_file(filename="", text=""):
    '''write a textfile and return no of chars'''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
