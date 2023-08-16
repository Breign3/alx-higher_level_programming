#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Compute the sqaure_matris """
    return ([list(map(lambda x: x * x, row)) for row in matrix])
