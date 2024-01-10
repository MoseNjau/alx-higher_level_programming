#!/usr/bin/python3
"""function that prints a text with 2 new lines after '.', '?' and ':'"""


def text_indentation(text):
    """the function"""

    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print(i)
            print()
            continue
        print(i, end="")
