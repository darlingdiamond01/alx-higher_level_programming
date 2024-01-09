#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public insance method attribute area"""
    def area(self):
        """Raises an exception when called"""
        raise Exception("area() is not implemented")
