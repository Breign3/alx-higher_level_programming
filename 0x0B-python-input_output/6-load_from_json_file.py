#!/usr/bin/python3
"""6-load_from_json_file module"""
import json

def load_from_json_file(filename):
    """Creates a Python obj from JSON file
    Args:
        filename: file
    """
    with open(filename, "r") as f:
        my_obj = json.load(f)
        return my_obj
