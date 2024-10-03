#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """Pascal_triangle"""
    my_list = []
    if (n <= 0):
        return my_list
    prev_list = []
    for i in range(1, n + 1):
        small_list = []
        for j in range(1, i + 1):
            if (j == 1 or j == i):
                small_list.append(1)
            else:
                small_list.append(prev_list[j - 1] + prev_list[j - 2])
        prev_list = small_list.copy()
        my_list.append(small_list)
    return my_list
