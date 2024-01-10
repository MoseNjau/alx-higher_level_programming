#!/usr/bin/python3
'''Create an object from a JSON file'''


import json


def load_from_json_file(filename):
    '''create the object'''
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
