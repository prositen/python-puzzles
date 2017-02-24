import unittest
from util.prime import prepare_primes

__author__ = 'anna'


class Euler007Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_nth_prime(self):
        primes = prepare_primes(100)
        self.assertEquals(primes[3 - 1], 5)
        self.assertEquals(primes[6 - 1], 13)


if __name__ == '__main__':
    unittest.main()
