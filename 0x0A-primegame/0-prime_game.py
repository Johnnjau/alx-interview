#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """Method determine prime game winner"""
    mariaCount = 0
    benCount = 0

    for num in nums:
        roundSet = list(range(1, num + 1))
        primeSet = primes_in_range(1, num)

        if not primeSet:
            benCount += 1
            continue

        MariaTurn = True

        while(True):
            if not primeSet:
                if MariaTurn:
                    benCount += 1
                else:
                    mariaCount += 1
                break

            smallestPrime = primeSet.pop(0)
            roundSet.remove(smallestPrime)

            roundSet = [x for x in roundSet if x % smallestPrime != 0]

            MariaTurn = not MariaTurn

    if mariaCount > benCount:
        return "Maria"

    if mariaCount < benCount:
        return "Ben"

    return None


def is_prime(n):
    """Return True in case n is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """Return prime noms list"""
    primes = [n for n in range(start, end+1) if is_prime(n)]
    return primes
