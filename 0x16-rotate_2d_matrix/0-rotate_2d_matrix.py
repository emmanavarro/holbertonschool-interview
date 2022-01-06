#!/usr/bin/python3
"""
rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix
    The matrix must be edited in-place.
    the matrix will have 2 dimensions and will not be empty.
    """
    size = len(matrix)
    for i in range(size // 2):
        for j in range(i, size - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[size - 1 - j][i]
            matrix[size - 1 - j][i] = matrix[size - 1 - i][size - 1 - j]
            matrix[size - 1 - i][size - 1 - j] = matrix[j][size - 1 - i]
            matrix[j][size - 1 - i] = temp
