#!/usr/bin/python3
"""
Method to calculate the minimum operatios needed
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H
    characters in the file.
    Arg:
        - n: is the number of H characters to print.
    Return:
        An integer (minimum operations) if success or 0 if failure.
    """
    if not isinstance(n, int) or n <= 1:
        return 0
    minimum = 0
    operations = 2
    while operations <= n:
        if n % operations == 0:
            minimum += operations
            n /= operations
            operations -= 1
        operations += 1
    return minimum
