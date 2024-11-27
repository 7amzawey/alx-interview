#!/usr/bin/python3
"""Make a change."""


def makeChange(coins, total):
    """Find the fewest number of coisn needed to get total."""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    return count if total == 0 else -1
