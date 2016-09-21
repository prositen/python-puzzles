__author__ = 'anna'
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = x^2

For example, 3^2 + 3^2 = 9 + 16 = 25 = 5^2

Given N, Check if there exists any Pythagorean triplet for which a + b + c = N

Find maximum possible value of a*b*c among all such Pythagorean triplets,
If there is no such Pythagorean triplet print -1.
"""

from functools import lru_cache


@lru_cache(maxsize=0)
def find_triplet_product(n):
    """
    We have
    (0) a < b < c
    (1) a^2 + b^2 = c^2
    (2) a + b + c = N

    (3) c = N - a - b
    (4) a^2 + b^2 = (N - a - b)^2
    (5) a^2 + b^2 = n^2+ (a^2 + 2ab + b^2) - 2na - 2nb
    (6) 0 = n^2 + 2ab - 2na - 2nb
    (7) 0 = b(2a - 2n) + n^2 - 2na
    (8) b(2a - 2n) = 2na - n^2
    (9) n(2a - n) / (2a - 2n) = b
    """
    max_found = -1
    for a in range(1, n//2):
        # (9)
        b, m = divmod(n*(2*a - n), 2*(a-n))
        # (0)
        if (a < b) and (m == 0):
            # (2)
            c = n - a - b
            if c > b:
                max_found = max(max_found, a*b*c)
    return max_found


def main():
    for _ in range(int(input())):
        print(find_triplet_product(int(input())))

if __name__ == '__main__':
    main()
