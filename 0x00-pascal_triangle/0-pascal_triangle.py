#!/usr/bin/python3
"""Module for working with Pascal's triangle"""


def pascal_triangle(n):
    """
    Creates list of lists of int representing
    the Pascal's triangle of a given int.
    """
    triangle = []
    if not isinstance(n, int) or n <= 0:
        return triangle

    for i in range(n):
        r = []
        for v in range(i + 1):
            if v == 0 or v == i:
                r.append(1)
            elif i > 0 and v > 0:
                r.append(triangle[i - 1][v - 1] + triangle[i - 1][v])
        triangle.append(r)

    return triangle
