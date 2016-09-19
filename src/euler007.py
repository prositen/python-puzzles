__author__ = 'anna'
"""
By listing the first six prime numbers: 2,3,5,7,11 and 13, we can see that the 6th prime is 13.
What is the N'th prime number?
"""


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


def main():
    N = 10**6 + 1
    primes = prepare_primes(N)
    for _ in range(int(input())):
        n = int(input())
        print(primes[n-1])

if __name__ == '__main__':
    main()
