__author__ = 'anna'

import unittest
import euler007


class Euler007Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_nth_prime(self):
        primes = euler007.prepare_primes(100)
        self.assertEquals(primes[3-1], 5)
        self.assertEquals(primes[6-1], 13)
if __name__ == '__main__':
    unittest.main()


