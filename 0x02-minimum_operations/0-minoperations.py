#!/usr/bin/python3
"""Calculate the fewest number of operations needed to result in exactly n."""


def largest_prime_number(n):
    """Calculate the largest_prime_number."""
    factor = 2
    last_prime = None

    while n > 1:
        if n % factor == 0:
            last_prime = factor
            n //= factor
        else:
            factor += 1
    return last_prime


def minOperations(n):
    """Calculate the fewest number of operations."""
    largest_pn = largest_prime_number(n)
    the_div = n / largest_pn

    return int(largest_pn + the_div)
