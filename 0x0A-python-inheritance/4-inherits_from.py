#!/usr/bin/python3
'''Check if obj is an instance/subclass of the specified class'''


def inherits_from(obj, a_class):
    '''returns true if obj is a subclass of a_class'''
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
