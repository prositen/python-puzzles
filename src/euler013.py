__author__ = 'anna'

import fileinput
import math
"""
Work out the first ten digits of the sum of N 50-digit numbers.
"""


def boring_solution(num_iterator):
    """
    Python handles big numbers out of the box. Just sum them up and return the 10 first digits.
    """
    s = 0
    for line in num_iterator:
        s += int(line)
    return int(str(s)[:10])


def interesting_solution(n, num_iterator):
    """
    On other platforms one might need to put a little more thought into it.
    We can't just look at the 10 leftmost digits for each term, since the following
    digits might add upp to something that would change the sum.

    Worst case scenario: All nines. N * 9 on a position will shift the value log10(N)
    positions to the left. So let's use the 10 + log10(N) leftmost digits.
    """

    s = 0
    digits = int(10 + math.log10(n))
    for line in num_iterator:
        s += int(line[:digits])
    return int(str(s)[:10])


def stdin_iterator(n):
    for _ in range(n):
        yield(input())


def main():
    n = int(input())
    lines = stdin_iterator(n)
    print(interesting_solution(n, lines))

if __name__ == '__main__':
    main()