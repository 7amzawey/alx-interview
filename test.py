#!/usr/bin/python3
"""Rotate the matrix."""
import copy


def transpose(matrix):
    """Rotate the matrix 90 degrees."""
    n = len(matrix)
    mtrx = copy.deepcopy(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = mtrx[n-j-1][i]
    return matrix
