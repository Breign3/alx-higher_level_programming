#!/usr/bin/python3
def safe_print_integer_err(value):
        """Function that prints an integer.

    Args:
        value: can be any type.

    Returns: True if value has been correctly printed,
    Otherwise, returns False and prints in stderr the error precede by,
    Exception:
    """
    import sys
    try:
        print("{:d}".format(value))
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        return (False)
    else:
        return (True)
