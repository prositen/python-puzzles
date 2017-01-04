import re

from python.utils import is_palindrome


def is_incrementing(n):
    return str(n) in '1234567890'


def is_decrementing(n):
    return str(n) in '9876543210'


def is_all_same(n):
    return re.match(r'^(\d)\1+$', str(n)) is not None


def is_all_zeroes(n):
    return re.match(r'^[1-9]0+$', str(n)) is not None


def is_interesting(number, awesome_phrases):
    for n, r in [(number, 2), (number + 1, 1), (number + 2, 1)]:
        if n < 100:
            continue
        if any([is_palindrome(str(n)),
                is_all_zeroes(n),
                is_decrementing(n),
                is_incrementing(n),
                is_all_same(n),
                n in awesome_phrases]):
            return r
    return 0
