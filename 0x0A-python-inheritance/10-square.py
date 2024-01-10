#!/usr/bin/python3
'''contains Rectangle and BaseGeometry classes'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A square'''
    def __init__(self, size):
        '''instantiation of the square'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''returns the area of the square'''
        return self.__size ** 2
