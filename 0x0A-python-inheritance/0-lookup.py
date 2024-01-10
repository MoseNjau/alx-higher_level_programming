#!/usr/bin/python3
'''Contains the lookup function'''


def lookup(obj):
    '''Returns a list of available attr & methods of an object'''
    return dir(obj)
