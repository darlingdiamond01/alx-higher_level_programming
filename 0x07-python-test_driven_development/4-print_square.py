#!/usr/bin/python3
"""
This is the "4-print_square" module.

The 4-print_square gives one function, prin_square(size)
"""


def print_square(size):
    """prints a square with "#" that has a length of size"""
    if type(size) is not an int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size, float) and < 0:
        raise TypeError("size must be and integer")

    for _ in range(size):
    print("#" * size)
