import unittest

from codewars import eight_kyu


class Test8kyu(unittest.TestCase):
    def test_count_positives_sum_negatives(self):
        self.assertListEqual([10, -65],
                             eight_kyu.count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
        self.assertListEqual(eight_kyu.count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),
                             [8, -50])
        self.assertListEqual([1, 0], eight_kyu.count_positives_sum_negatives([1]))
        self.assertListEqual([0, -1], eight_kyu.count_positives_sum_negatives([-1]))
        self.assertListEqual([0, 0], eight_kyu.count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]))
        self.assertListEqual([], eight_kyu.count_positives_sum_negatives([]), )
