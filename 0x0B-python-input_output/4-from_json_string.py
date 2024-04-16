#!/usr/bin/python3
"""4-from_json_string module"""
import json

def from_json_string(my_str):
    """Returns python data structure from JSON string
        from_json_string - returns an object (Python data structure)
                    represented by a JSON string:
        return:An object is return
    """
    return json.loads(my_str)
