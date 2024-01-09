#!/usr/bin/python3
"""
The module contains the function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """True if object is an instance or inheritance from a_class, else false"""
    return (isinstance(obj, a_class))
