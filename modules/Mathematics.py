import sys
from typing import Tuple
sys.setrecursionlimit(1000000)

def MultiplicativeModularInverse(a, m):
    # We calculate the multiplicative inverse of a in the group of integers modulo m.
    gcd, x, y = ExtendedEuclidianAlgorithm(a, m)
    if (gcd != 1):
        return None
    else:
        return x % m

def ExtendedEuclidianAlgorithm(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = ExtendedEuclidianAlgorithm(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y

def GCD(a, b):
    # We calculate the greatest common divisor of two integers a, b by the extended Euclidian Algorithm.
    g, x, y = ExtendedEuclidianAlgorithm(a, b)
    return g
