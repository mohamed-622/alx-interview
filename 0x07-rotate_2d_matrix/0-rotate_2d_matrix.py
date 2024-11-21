#!/usr/bin/python3
"""module rotate_2d_matrix function"""


def rotate_2d_matrix(matrix):
    """n x n, 2D matrix, rotate it 90 degrees clockwise"""
    matrix[:] = [list(row) for row in zip(*matrix[::-1])]
