__author__ = 'anna'

from math import sqrt
from functools import lru_cache


@lru_cache(maxsize=None)
def prime_factors(n):
    for f in range(2, int(sqrt(n) + 1)):
        d, m = divmod(n, f)
        if not m:
            return [f] + prime_factors(d)
    return [n]
