#!/usr/bin/python3
"""rotate matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix: list):
    """Rotate a 2D matrix by 90 degrees"""
    matrix[:] = [list(row) for row in zip(*matrix[::-1])]
