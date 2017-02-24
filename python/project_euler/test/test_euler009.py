import unittest
from project_euler import euler009

__author__ = 'anna'


class Euler009Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_find_triplet_product(self):
        self.assertEquals(euler009.find_triplet_product(12), 60)
        self.assertEquals(euler009.find_triplet_product(4), -1)

if __name__ == '__main__':
    unittest.main()

