#!/usr/bin/python3
"""append_write module"""

def append_write(filename="", text=""):

    """ appends to text file
        returns num chars added
    """
    
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
