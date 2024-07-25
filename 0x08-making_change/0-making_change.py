#!/usr/bin/python3
"""Making Change method
"""


def makeChange(coins, total):
    """makeChange method definition

    Args:
        coins:int
        total:int

    Returns:
        int:int
    """
    if total <= 0 or len(coins) == 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    for i in coins:
        count += total // i
        total = total % i
    if total != 0:
        return -1
    return count
