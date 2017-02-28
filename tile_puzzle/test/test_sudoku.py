import unittest

from tile_puzzle.sudoku import Sudoku


class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.s = Sudoku(state=[[0, 9, 1, 0, 6, 0, 7, 0, 0],
                               [0, 0, 0, 0, 8, 2, 0, 3, 9],
                               [5, 0, 3, 0, 0, 0, 2, 0, 0],
                               [0, 0, 0, 9, 1, 3, 0, 6, 2],
                               [0, 0, 2, 4, 0, 6, 8, 0, 0],
                               [1, 4, 0, 8, 2, 5, 0, 0, 0],
                               [0, 0, 9, 0, 0, 0, 5, 0, 7],
                               [6, 7, 0, 1, 5, 0, 0, 0, 0],
                               [0, 0, 5, 0, 4, 0, 6, 9, 0]])

    def test_get_row(self):
        self.assertListEqual([5, 0, 3, 0, 0, 0, 2, 0, 0], self.s.get_row(2))

    def test_get_col(self):
        self.assertListEqual([0, 2, 0, 3, 6, 5, 0, 0, 0], self.s.get_col(5))

    def test_get_box(self):
        self.assertListEqual([9, 1, 3, 4, 0, 6, 8, 2, 5], self.s.get_box(4))

    def test_get_box_from_coords(self):
        self.assertListEqual([0, 6, 2, 8, 0, 0, 0, 0, 0], self.s.get_box_from_coords(5, 8))

    def test_moves(self):
        self.assertListEqual([4, 8], self.s.get_moves(7, 2))
        self.assertListEqual([7], self.s.get_moves(4, 4))

    def test_solve_1(self):
        g = Sudoku.solve(self.s)
        self.assertIsNotNone(g)
        self.assertTrue(g.is_solved)

    def test_solve_2(self):
        solution = Sudoku.solve(Sudoku(state=[[0, 0, 1, 0, 0, 0, 0, 0, 0],
                                              [5, 0, 0, 0, 0, 0, 0, 0, 4],
                                              [3, 0, 2, 0, 6, 1, 0, 7, 5],
                                              [0, 0, 8, 0, 0, 4, 0, 0, 0],
                                              [0, 0, 0, 9, 2, 3, 0, 0, 0],
                                              [0, 0, 0, 8, 0, 0, 1, 0, 0],
                                              [2, 6, 0, 7, 1, 0, 8, 0, 3],
                                              [9, 0, 0, 0, 0, 0, 0, 0, 7],
                                              [0, 0, 0, 0, 0, 0, 2, 0, 0]]))
        self.assertIsNotNone(solution)
        self.assertTrue(solution.is_solved)
