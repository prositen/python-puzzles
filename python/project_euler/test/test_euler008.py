import unittest
from project_euler import euler008

__author__ = 'anna'


class Euler008Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_largest_product(self):
        self.assertEquals(euler008.largest_product(3675356291, 5), 3150)
        self.assertEquals(euler008.largest_product(2709360626, 5), 0)

if __name__ == '__main__':
    unittest.main()
