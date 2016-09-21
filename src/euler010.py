__author__ = 'anna'

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
