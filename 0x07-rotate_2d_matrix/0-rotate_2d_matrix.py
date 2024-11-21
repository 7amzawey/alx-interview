#!/usr/bin/python3
"""Rotate the matrix."""
from typing import List


def rotate_2d_matrix(matrix: List[List[int]]):
    """Rotate the matrix 90 degrees."""
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print(matrix)
    for i in range(n):
        for j in range(n-1, n):
            print(f'matrix[{i},{j}] = {matrix[i][j]}')
            print(f'matrix[{i},{j-n+1}] = {matrix[i][j-n+1]}')
            matrix[i][j], matrix[i][j-n+1] = matrix[i][j-n+1], matrix[i][j]
