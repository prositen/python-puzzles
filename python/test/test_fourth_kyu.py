import unittest

from python import fourth_kyu


class Test4Kyu(unittest.TestCase):
    def test_is_interesting(self):
        tests = [
            {'n': 3, 'interesting': [1337, 256], 'expected': 0},
            {'n': 123, 'interesting': [1337, 256], 'expected': 2},
            {'n': 1336, 'interesting': [1337, 256], 'expected': 1},
            {'n': 1337, 'interesting': [1337, 256], 'expected': 2},
            {'n': 11208, 'interesting': [1337, 256], 'expected': 0},
            {'n': 11209, 'interesting': [1337, 256], 'expected': 1},
            {'n': 11211, 'interesting': [1337, 256], 'expected': 2},
        ]
        for t in tests:
            self.assertEquals(t['expected'], fourth_kyu.is_interesting(t['n'], t['interesting']))
