#!/usr/bin/python3
""" Pascal's triangle

This function generates Pascal's triangle for a given integer.

It is an arithmetic triangle in which each number
is the sum of the numbers directly above it.

Args:
    n: Number of rows in the triangle.

Return:
    List of lists representing Pascal's triangle.
"""


def pascal_triangle(n):

    """ Generating Pascal's triangle for a given  integer.

    Args:
        n: Number of rows in the triangle.

    Return:
        List of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        next_row = [1]
        for j in range(1, i):
            next_row.append(triangle[i-1][j-1] + triangle[i-1][j])
        next_row.append(1)
        triangle.append(next_row)

    return triangle
