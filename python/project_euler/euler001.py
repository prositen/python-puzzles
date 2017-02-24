__author__ = 'anna'

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_divisible(divisor, n):
    """
    1 + 2 + ... + n = n(n+1) / 2
    5 + 10 + ... + n = 5*(1 + 2 + ... n/5)

    :param divisor:
    :param n:
    :return: The sum of all terms up to n that are divisible by divisor
    """
    n2 = n//divisor
    return divisor * (n2*(n2+1)//2)


def euler001(n):
    n = n-1
    sum3 = sum_divisible(3, n)
    sum5 = sum_divisible(5, n)
    sum15 = sum_divisible(15, n)
    return sum3 + sum5 - sum15


def main():
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        print(euler001(n))


if __name__ == '__main__':
    main()
