#!/usr/bin/python3
"""
This is the "3-say_my_name" module.

This 3-say_my_name module supplies one function
"""

def say_my_name(first_name, last_name=""):
    """prints "My name is" followed by the first_name and last_name"""
    if type(first_name) is not a str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not a str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
