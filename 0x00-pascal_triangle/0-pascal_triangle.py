#!/usr/bin/python3
"""
pascal's triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    Returns an empty list if n <= 0
    n will be always an integer
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # First element in each row is always 1

        for j in range(1, i):
            # Each middle element is the sum of the two elements above it
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)  # Last element in each row is always 1
        triangle.append(row)

    return triangle
