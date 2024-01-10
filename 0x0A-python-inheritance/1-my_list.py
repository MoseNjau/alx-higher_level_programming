#!/usr/bin/python3
'''Contains class MyList'''


class MyList(list):
    '''the class'''
    def print_sorted(self):
        '''prints the sorted list'''
        print(sorted(self))
