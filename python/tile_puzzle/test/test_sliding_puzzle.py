import unittest

from tile_puzzle.sliding_puzzle import DFSSlidingPuzzle


class TestSlidingPuzzle(unittest.TestCase):
    def test3x3Puzzle(self):
        cases = [([1, 2, 3, 4, 0, 5, 7, 8, 6], 2),
                 ([1, 2, 3, 7, 4, 5, 0, 8, 6], 4),
                 ([1, 2, 3, 4, 8, 0, 7, 6, 5], 5),
                 ([4, 1, 3, 7, 2, 6, 5, 8, 0], 8),
                 ([1, 6, 2, 5, 3, 0, 4, 7, 8], 9)]

        for case, moves in cases:
            g = DFSSlidingPuzzle(3, 3, state=case)
            print(g)
            self.assertEqual(moves, len(g.solve(g).moves_from_start))
            print("Done")

