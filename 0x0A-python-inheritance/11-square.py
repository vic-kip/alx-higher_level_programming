#!/usr/bin/python3
"""
Module 10-square
Defines a Square class that inherits from Rectangle (9-rectangle.py).
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a Square.
    """
    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square's sides.

        Raises:
            ValueError: If size is not a positive integer.
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: A string in the format '[Square] <width>/<height>'.
        """
        return f"[Square] {self.__width}/{self.__height}"
