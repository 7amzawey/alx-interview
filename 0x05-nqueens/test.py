#!/usr/bin/python3
sum = 0;
def sum_of_digits(n):
    """Return sum of digits."""
    if len(str(n)) == 1:
        return n
    length = len(str(n))
    print(n)
    return sum_of_digits(str(n)[length-1] + sum)

print(sum_of_digits(1234))