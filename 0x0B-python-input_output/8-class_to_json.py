#!/usr/bin/python3
'''Return the Dict description with simple data structure for
   JSON serialization of an object
'''


def class_to_json(obj):
    '''returns the simple dictionary description'''
    return obj.__dict__
