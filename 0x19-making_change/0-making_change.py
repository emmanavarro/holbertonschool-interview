#!/usr/bin/python3
"""
Make change module
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins
    needed to meet a given amount 'total'
    Args:
        coins ([list]): a list of the values of the coins in your possession
        total ([number]): amount
    Return: fewest number of coins needed to meet total
    """
    count, aux, i = 0, 0, 0

    coins.sort(reverse=True)

    if total == 0:
        return count

    while i < len(coins):
        if coins[i] <= total and coins[i] + aux <= total:
            count += 1
            aux += coins[i]
        else:
            i += 1

    if aux < total:
        return -1
    return count
