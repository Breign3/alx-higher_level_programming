#!/usr/bin/python3
"""Module for class Student."""


class Student():
    """
    Public Attributes:
        first_name
        last_name
        age
    Public Methods:
        to_json: retrieves its dictionary representation
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes student with full name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):

        """
            retrieves a dictionary representation of Student.
        """
        return self.__dict__
