#!/usr/bin/python3
"""Calculate the fewest number of operations needed to result in exactly n."""


def minOperations(n):
    """Calculate the fewest number of operations."""
    if n < 2:
        return 0

    factor = 2
    ops = 0
    current_number = n

    while current_number > 1:
        while current_number % factor == 0:
            ops += factor
            current_number //= factor
        factor += 1
    return ops
