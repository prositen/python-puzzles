from collections import deque
from functools import lru_cache


class Sudoku(object):
    class Move(object):
        def __init__(self, row, col, values):
            self.row = row
            self.col = col
            self.values = values

        def key(self):
            return "{},{}:{}".format(self.row, self.col, ",".join(str(x) for x in self.values))

        def is_unique(self):
            return len(self.values) == 1

        def __len__(self):
            return len(self.values)

        def __repr__(self):
            return "<Move row={} col={} value={}>".format(self.row, self.col, self.values)

    ALL_MOVES = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def __init__(self, state):
        self.state = [[col for col in row] for row in state]

    @lru_cache(maxsize=16)
    def get_row(self, row):
        return [x for x in self.state[row]]

    @lru_cache(maxsize=16)
    def get_col(self, col):
        return [self.state[row][col] for row in range(9)]

    @lru_cache(maxsize=16)
    def get_box(self, box):
        col_start = (box % 3) * 3
        row_start = (box // 3) * 3
        return [self.state[row][col]
                for row in range(row_start, row_start + 3)
                for col in range(col_start, col_start + 3)]

    @lru_cache(maxsize=16)
    def get_box_from_coords(self, row, col):
        col_start = (col // 3) * 3
        row_start = (row // 3) * 3
        return [self.state[row][col]
                for row in range(row_start, row_start + 3)
                for col in range(col_start, col_start + 3)]

    def get_moves(self, row, col):
        return sorted(list(self.ALL_MOVES -
                           set(self.get_row(row) + self.get_col(col) + self.get_box_from_coords(row, col))))

    def make_board(self, moves):
        g = Sudoku(self.state)
        for move in moves:
            g.state[move.row][move.col] = move.values[0]
        return g

    def format_board(self):
        r = []
        for row in range(9):
            if row % 3 == 0:
                r.append('-' * 25)
            r.append(" ".join("{}{}".format("| " if col % 3 == 0 else "",
                                            self.state[row][col] if self.state[row][col] > 0 else " ")
                              for col in range(9)) + " |")
        r.append('-' * 25)
        return "\n".join(r)

    def key(self):
        return "".join(str(x) for y in self.state for x in y)

    def next_moves(self):
        moves = []
        for row in range(9):
            for col in range(9):
                if self.state[row][col] == 0:
                    moves.append(Sudoku.Move(row, col, self.get_moves(row, col)))
        return sorted(moves, key=lambda x: -len(x))

    def is_solved(self):
        """ Board must be valid, and there may be no zeroes """
        return self.is_valid() and not any(0 in row for row in self.state)

    def is_valid(self):
        """
        The board is valid if there are no duplicate numbers (except 0) within
        a row, column or box
        """
        for i in range(9):
            for fun in self.get_row, self.get_col, self.get_box:
                values = list(filter(lambda x: x > 0, fun(i)))
                if len(set(values)) != len(values):
                    return False
        return True

    @staticmethod
    def solve(grid):
        to_visit = deque()
        to_visit.append(grid)
        visited = set()
        while to_visit:
            grid = to_visit.popleft()
            if grid.is_solved():
                return grid
            else:
                moves = grid.next_moves()
                unique_moves = list(filter(lambda x: x.is_unique(), moves))
                if unique_moves:
                    # Set all cells which have only one possible move in one swoop,
                    # to save some iterations.
                    next_grid = grid.make_board(unique_moves)
                    if next_grid.is_valid():
                        visited.add(next_grid.key())
                        to_visit.append(next_grid)
                else:
                    # Here we have a bunch of possible moves to do. Pop a position from the list
                    # and create optional boards for each value. If neither of them were unique, pop the
                    # next.

                    added = False
                    while moves and not added:
                        move = moves.pop()
                        for possible_value in move.values:
                            possible_move = Sudoku.Move(move.row, move.col, [possible_value])
                            next_grid = grid.make_board([possible_move])
                            if next_grid.key() not in visited:
                                if next_grid.is_valid():
                                    added = True
                                    visited.add(next_grid.key())
                                    to_visit.append(next_grid)
        return None


def main():
    s = Sudoku(state=[[0, 0, 0, 9, 7, 0, 0, 0, 0],
                      [5, 0, 0, 0, 0, 6, 0, 1, 0],
                      [6, 0, 0, 0, 0, 0, 8, 0, 2],
                      [0, 7, 0, 0, 0, 9, 2, 0, 0],
                      [0, 0, 5, 0, 3, 0, 6, 0, 0],
                      [0, 0, 9, 1, 0, 0, 0, 7, 0],
                      [3, 0, 4, 0, 0, 0, 0, 0, 7],
                      [0, 8, 0, 2, 0, 0, 0, 0, 3],
                      [0, 0, 0, 0, 1, 7, 0, 0, 0]])
    solution = Sudoku.solve(s)
    if solution:
        print(solution.format_board())
    else:
        print("No solution for ", s.format_board())


if __name__ == '__main__':
    main()
