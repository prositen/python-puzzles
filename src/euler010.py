__author__ = 'anna'

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

Find the sum of all the primes not greater than given N.
"""

from util.prime import prepare_primes


def prepare_sums(n_max):
    sums = [0] * n_max
    so_far = 0
    last_prime = 0
    primes = prepare_primes(n_max)
    for prime in primes:
        sums[last_prime:prime] = (prime-last_prime)*[so_far]
        so_far += prime
        last_prime = prime
    return sums


def main():
    n_max = 3*10**6
    sums = prepare_sums(n_max)
    for _ in range(int(input())):
        n = int(input())
        print(sums[n])


if __name__ == '__main__':
    main()
