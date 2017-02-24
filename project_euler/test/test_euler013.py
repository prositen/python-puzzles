import os
import unittest

from project_euler import euler013

__author__ = 'anna'
basedir = os.path.abspath(os.path.dirname(__file__))


class Euler013Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_euler013(self):
        n = 5
        lines = ["37107287533902102798797998220837590246510135740250",
                 "46376937677490009712648124896970078050417018260538",
                 "74324986199524741059474233309513058123726617309629",
                 "91942213363574161572522430563301811072406154908250",
                 "23067588207539346171171980310421047513778063246676"]
        self.assertEquals(euler013.interesting_solution(n, lines), 2728190129)

    def test_euler013_from_file(self):
        print(basedir)
        n = 100
        with open(os.path.join(basedir, "data", "euler013.txt"), "r") as fh:
            lines = fh.readlines()
            self.assertEquals(euler013.interesting_solution(n, lines), 5537376230)

if __name__ == '__main__':
    unittest.main()
