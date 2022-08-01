#!/usr/bin/python3
""" creating BaseGeometry class """


class BaseGeometry:
    """ creating a method 'area' """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ checks if 'value' is a positive integer """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


""" defining 'Rectangle' class """


class Rectangle(BaseGeometry):
    """ initializing class """
    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    """ returns area of rectangle """
    def area(self):
        return self.__width * self.__height
class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
