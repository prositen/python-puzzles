__author__ = 'anna'

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of a given number N?
"""
from util.prime import prime_factors


def largest_prime_factor(n):
    return max(prime_factors(n))


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(largest_prime_factor(n))

if __name__ == '__main__':
    main()