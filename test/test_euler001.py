__author__ = 'anna'

import unittest
import euler001


class Euler001Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_sum_divisible(self):
        self.assertEquals(euler001.sum_divisible(1, 10), 55)
        self.assertEquals(euler001.sum_divisible(3, 10), 18)
        self.assertEquals(euler001.sum_divisible(5, 10), 15)

    def test_euler001(self):
        self.assertEquals(euler001.euler001(10), 23)
        self.assertEquals(euler001.euler001(100), 2318)

if __name__ == '__main__':
    unittest.main()

