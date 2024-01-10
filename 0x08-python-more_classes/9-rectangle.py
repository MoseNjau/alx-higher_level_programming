#!/usr/bin/python3
'''Define a class Rectangle'''


class Rectangle:
    '''Create a rectangle'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''initializes the rectangle'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''getter for the private instance attribute width'''
        return(self.__width)

    @width.setter
    def width(self, value):
        '''setter for the private instance attribute width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''getter for the private instance attribute height'''
        return(self.__height)

    @height.setter
    def height(self, value):
        '''setter for the private instance attribute height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''returns the area of the rectangle'''
        return(self.__width * self.__height)

    def perimeter(self):
        '''returns the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return(0)
        return((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        '''print rectangle'''
        rec = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rec += str(self.print_symbol)
            rec += '\n'
        return(rec.strip('\n'))

    def __repr__(self):
        '''returns a string representatiion of the rectangle'''
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        '''deletes an instance of rectangl and prints this string'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''returns the biggest rectangle based on the area'''
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return(rect_1)
        return(rect_2)

    @classmethod
    def square(cls, size=0):
        '''returns a new rectangle instance that has width=height=size'''
        return cls(size, size)
