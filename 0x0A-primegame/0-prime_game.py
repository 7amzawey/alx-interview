#!/usr/bin/python3
"""Prime game."""


def isprime(x):
    """Check if the number is prime."""
    n = x
    count = 0
    while n > 0:
        if x % n == 0:
            count += 1
        n -= 1
    if count == 2:
        return True
    return False


def toggle_values(d):
    """Toggel the playes."""
    for key in d:
        if d[key] == 'off':
            d[key] = 'on'
        else:
            d[key] = 'off'
    return d


def isWinner(x, nums):
    """Determine the Winner of the prime game."""
    players = {'Maria': 'on', 'Ben': 'off'}
    nums_list = []
    for n in nums:
        if isprime(n):
            toggle_values(players)
            for i in nums:
                if i % n == 0:
                    if i not in nums_list:
                        nums_list.append(i)
    for j in nums_list:
        nums.remove(j)
    for key, value in players.items():
        if value == 'on':
            return key
