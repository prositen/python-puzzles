__author__ = 'anna'
"""
By listing the first six prime numbers: 2,3,5,7,11 and 13, we can see that the 6th prime is 13.
What is the N'th prime number?
"""

from util import prime


def main():
    N = 10**6 + 1
    primes = prime.prepare_primes(N)
    for _ in range(int(input())):
        n = int(input())
        print(primes[n-1])

if __name__ == '__main__':
    main()
