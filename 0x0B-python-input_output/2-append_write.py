#!/usr/bin/python3
'''Append a string to a textfile and returns no. of chars written'''


def append_write(filename="", text=""):
    '''append a textfile and return no of chars'''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
