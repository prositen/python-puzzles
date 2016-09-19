__author__ = 'anna'

import unittest
import euler004


class Euler004Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_max_palindrome(self):
        self.assertEquals(euler004.find_palindrome(101110), 101101)
        self.assertEquals(euler004.find_palindrome(800000), 793397)
        self.assertEquals(euler004.find_palindrome(793397), 780087)

if __name__ == '__main__':
    unittest.main()

