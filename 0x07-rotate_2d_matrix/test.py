#!/usr/bin/python3
"""Rotate the matrix."""
import copy
from typing import List


def rotate_2d_matrix(matrix: List[List[int]]):
    """Rotate the matrix 90 degrees."""
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i][j], matrix[j][i] = matrix[n-j-1][i], matrix[n-i-1][j]
