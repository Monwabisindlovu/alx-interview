#!/usr/bin/python3
"""Pascal's triangle of n size"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    pascal = []
    if n <= 0:
        return []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        pascal.append(row)
    return pascal
