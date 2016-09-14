__author__ = 'anna'
"""
The sum of the squares of the first ten natural numbers is, 1² + 2² + ... + 10² = 385.

The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)² = 3025.

Hence the absolute difference between the sum of the squares of the first ten natural numbers and
the square of the sum is 3025 - 385 = 2640.

Find the absolute difference between the sum of the squares of the first N natural numbers
and the square of the sum.

"""


def square_of_sums(n):
    """
    The sum of N first numbers is  n(n+1)/2  = (n^2 + n)/2
    The square of this is (n^4 + 2n^3 + n^2) / 4
    """
    return (n**4 + 2*n**3 + n**2) // 4


def sum_of_squares(n):
    return (n*(n+1)*(2*n+1)) // 6


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(abs(sum_of_squares(n) - square_of_sums(n)))


if __name__ == '__main__':
    main()