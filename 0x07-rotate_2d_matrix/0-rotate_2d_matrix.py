#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix by 90 degrees clockwise in-place.

    Args:
    matrix (list of lists): The input 2D matrix.
    """
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
