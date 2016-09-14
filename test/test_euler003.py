__author__ = 'anna'

import unittest
import euler003


class Euler003Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_largest_prime_factor(self):
        self.assertEquals(euler003.largest_prime_factor(10), 5)
        self.assertEquals(euler003.largest_prime_factor(17), 17)

if __name__ == '__main__':
    unittest.main()

