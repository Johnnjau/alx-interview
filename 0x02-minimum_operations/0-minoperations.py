#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Minimum Operations"""
    if n <= 1:
        return 0

    n_ops = 0
    div = 2

    while n > 1:
        while n % div == 0:
            n_ops += div
            n //= div
        div += 1

    return n_ops
