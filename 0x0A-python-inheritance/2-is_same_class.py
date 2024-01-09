#!/usr/bin/python3
"""
This module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """Returns true if object is the exact class a_class, otherise false"""
    return (type(obj) == a_class)
