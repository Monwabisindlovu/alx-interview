#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """rotate it 90 degrees clockwise"""
    s = 0
    e = len(matrix) - 1
    while (s < e):
        for i in range(s, e):
            new = matrix[i][e]
            matrix[i][e] = matrix[s][i]
            new2 = matrix[e][s + e - i]
            matrix[e][s + e - i] = new
            new = matrix[s + e - i][s]
            matrix[s + e - i][s] = new2
            matrix[s][i] = new
        s += 1
        e -= 1
