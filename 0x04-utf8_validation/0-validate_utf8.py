#!/usr/bin/python3
"""Validate data if its a utf8 or not."""


def validUTF8(data):
    """Validate data if its a utf8 or not."""
    # number of bytes
    num_bytes = 0

    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        mask = 1 << 7  # 1000000
        if num_bytes == 0:
            while mask & num:
                num_bytes += 1
                mask <<= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:

            if not (mask1 & num and not (mask2 & num)):
                return False

        num_bytes -= 1

    return num_bytes == 0
