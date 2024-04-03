#!/usr/bin/python3

    """
    Divides 2 integers and prints the result.

            Args:
            a: Integer
            b: Integer
            Returns: The value of the division, otherwise: None
    """

def safe_print_division(a, b):
    quotient = None
    try:
        quotient = a / b
        print("Inside result: {}".format(quotient))
    except:
        print("Inside result: {}".format(quotient))
    finally:
        return quotient
