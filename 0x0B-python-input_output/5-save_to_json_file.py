#!/usr/bin/python3
"""5-save_to_json module"""
import json


def save_to_json_file(my_obj, filename):
    """Writes Python obj to file using JSON represenation
    Args:
        my_obj: python object
        filename: file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
