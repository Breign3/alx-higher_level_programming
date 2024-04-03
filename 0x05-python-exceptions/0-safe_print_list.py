#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):


"""Print x elememts of a list.
Arguments:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
Returns:
The number of elements printed.
"""
            count = 0
    for item in range(x):
        try:
            print(my_list[item], end='')
        except IndexError:
            break
        else:
            count += 1
    print()
    return count
