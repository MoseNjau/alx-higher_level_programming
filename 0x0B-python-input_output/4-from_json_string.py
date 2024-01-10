#!/usr/bin/python3
'''Return an object represented by a json string'''


import json


def from_json_string(my_str):
    '''return an object from a json string'''
    return json.loads(my_str)
