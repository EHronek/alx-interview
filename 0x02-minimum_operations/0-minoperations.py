#!/usr/bin/python3
"""
Module defines a method that calculates the fewest number of operations
needed to result in exactly n H characters in a file
"""


def minOperations(n):
    """
    funtion gets fewest # of operations needed to result in exactly
    n H characters
    """
    if n < 2:
        return 0
    opers, divisor = 0, 2
    while root <= n:
        if n % divisor == 0:
            opers += divisor
            n = n / divisor
            root -= 1
        divisor += 1
    return opers
