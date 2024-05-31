#!/usr/bin/python3
"""rotate a 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """ perform rotation 90 of a 2D matrix
        return None
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range((n + 1) // 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
