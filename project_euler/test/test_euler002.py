import unittest

from project_euler import euler002

__author__ = 'anna'


class Euler002Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_sum_even_fib(self):
        self.assertEquals(euler002.sum_even_fib(10), 10)
        self.assertEquals(euler002.sum_even_fib(100), 44)


if __name__ == '__main__':
    unittest.main()
