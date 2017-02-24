import unittest
from collections import Counter

from project_euler import euler005

__author__ = 'anna'


class Euler005tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_find_prime_factors(self):
        self.assertEquals(Counter(euler005.prime_factors(10)), Counter([2, 5]))
        self.assertEquals(Counter(euler005.prime_factors(40)), Counter([2, 2, 2, 5]))

    def test_smallest_multiple(self):
        self.assertEquals(euler005.smallest_multiple(3), 6)
        self.assertEquals(euler005.smallest_multiple(10), 2520)

if __name__ == '__main__':
    unittest.main()


