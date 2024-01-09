#!/usr/bin/python3
"""
Contains the inheritance inherits_from
"""


def inherits_from(obj, a_class):
    """Returns true if the object is a subclass of a_class, otherwise false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
