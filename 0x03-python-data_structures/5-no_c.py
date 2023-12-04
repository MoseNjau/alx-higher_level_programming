#!/usr/bin/python3
"""No C or c"""


def no_c(my_string):
    """
    What i do
    """
    newstr = ""
    for i in my_string:
        if i not in "cC":
            newstr += i
    return newstr
