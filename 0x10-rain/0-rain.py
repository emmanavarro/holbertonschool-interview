#!/usr/bin/python3
"""
Given a list of non-negative integers representing the heights of
walls with unit width 1
"""


def rain(walls):
    """ calculate how many square units of water will be retained
    after it rains"""
    if (len(walls) <= 2):
        return(0)

    rain_water = 0

    for i in range(1, len(walls) - 1):
        left_walls = walls[i]
        for j in range(i):
            left_walls = max(left_walls, walls[j])

        right_walls = walls[i]
        for k in range(i + 1, len(walls)):
            right_walls = max(right_walls, walls[k])

        rain_water += min(left_walls, right_walls) - walls[i]

    return rain_water
