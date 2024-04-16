#!/usr/bin/python3
"""3-to_json_string module"""
import json

def to_json_string(my_obj):
    """Returns JSON representation of obj (string)
    Args:
        my_obj: python object
    Return:
        json representation in string format
    """

    return json.dumps(my_obj)
