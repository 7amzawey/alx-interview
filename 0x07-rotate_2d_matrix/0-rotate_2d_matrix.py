#!/usr/bin/python3
"""Rotate the matrix."""
import copy
from typing import List


def rotate_2d_matrix(matrix: List[List[int]]):
    """Rotate the matrix 90 degrees."""
    n = len(matrix)
    mtrx = copy.deepcopy(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = mtrx[n-j-1][i]
