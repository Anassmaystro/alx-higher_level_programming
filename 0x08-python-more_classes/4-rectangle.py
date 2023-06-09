#!/usr/bin/python3
'''rectangle class'''


class Rectangle:
    '''Rectangle class'''

    def __init__(self, width=0, height=0):
        '''rectangle initialization

        Args:
            width (int): rectangle width
            height (int): rectangle height

        Raise:
            TypeError: if width or height is not int
            ValueError: if width or height is less than 0
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Return width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Return height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Return Area'''
        return self.__width * self.__height

    def perimeter(self):
        '''Return perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (2 * self.__height))

    def rectangle(self):
        '''Make a printable visual of the Rectangle based on dimensions'''
        s = ""
        if self.__width == 0 or self.__height == 0:
            s += " "
            return s
        for w in range(self.__height):
            for h in range(self.__width):
                s += "#"
            s += "\n"
        return s

    def __str__(self):
        '''Return printable rectangle'''
        return self.rectangle()[:-1]

    def __repr__(self):
        '''return internal representation of the function'''
        return "Rectangle(" + str(self.__width) + ", " + \
            str(self.__height) + ")"
