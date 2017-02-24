__author__ = 'anna'
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible(divisible with no remainder) by
all of the numbers from 1 to N?
"""


from collections import Counter
from util.prime import prime_factors


def smallest_multiple(n):
    """
    * Find the prime factors of all values 1..n.
    * For each unique prime factor find the max multiple of the factor used
    * The smallest multiple is the product of all prime factors * the max multiple
    """
    factors = [prime_factors(i) for i in range(1, n+1)]
    unique_factors = set([x for sublist in factors for x in sublist])
    counters = [Counter(f) for f in factors]

    num = 1
    for uf in unique_factors:
        max_uf = max([c[uf] for c in counters])
        num *= (uf**max_uf)
    return num


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(smallest_multiple(n))

if __name__ == '__main__':
    main()