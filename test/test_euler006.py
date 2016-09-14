__author__ = 'anna'

import unittest
import euler006


class Euler006Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_sum_of_squares(self):
        self.assertEquals(euler006.sum_of_squares(10), 385)
        self.assertEquals(euler006.sum_of_squares(0), 0)

    def test_square_of_sums(self):
        self.assertEquals(euler006.square_of_sums(10), 3025)
        self.assertEquals(euler006.square_of_sums(0), 0)

if __name__ == '__main__':
    unittest.main()

