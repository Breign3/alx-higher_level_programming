#!/usr/bin/python3
def safe_print_integer(value):

"""Print an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
"""

count = 0
    for item in range(x):
        if isinstance(my_list[item], int):
            try:
                print(my_list[item], end='')
            except IndexError:
                break
        else:
            continue
        count += 1
    print()
    return count
