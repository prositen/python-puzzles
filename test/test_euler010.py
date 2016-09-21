__author__ = 'anna'

import unittest
import euler010


class Euler010Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_sum_of_primes(self):
        sums = euler010.prepare_sums(20)
        self.assertEquals(sums[5], 10)
        self.assertEquals(sums[10], 17)

if __name__ == '__main__':
    unittest.main()



