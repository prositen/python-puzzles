__author__ = 'anna'

"""
Find the greatest product of K consecutive digits in the N digit number.
"""
from functools import reduce


def largest_product(N, K):
    max_product = 0
    nstr = str(N)
    for i in range(len(nstr)-K):
        prod = reduce(int.__mul__, map(int, nstr[i:i+K]), 1)
        max_product = max(prod, max_product)
    return max_product


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        N = int(input())
        print(largest_product(N, k))

if __name__ == '__main__':
    main()