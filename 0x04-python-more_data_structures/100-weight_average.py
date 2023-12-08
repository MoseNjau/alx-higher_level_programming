#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    n = 0
    d = 0
    for tp in my_list:
        n += tp[0] * tp[1]
        d += tp[1]
    return n / d
