#!/usr/bin/python3
"""
Contains the write_file function
"""


def write_file(filename="", text=""):
    """Returns the number of characters written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
