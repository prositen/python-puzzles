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


def prepare_primes(N):
    """
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    sieve = [True] * N

    # Go from 3 to sqrt(N), only look at odd numbers
    for i in range(3, int(N**0.5)+1, 2):
        if sieve[i]:
            # Remove all multiples of i  2*i because we already ignore even numbers.
            sieve[i*i::2*i] = [False] * ((N - i*i - 1) // (2*i)+1)
    return [2] + [i for i in range(3, N, 2) if sieve[i]]