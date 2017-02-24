from collections import deque


class SlidingPuzzle(object):
    def __init__(self, width, height, state=None):
        self.width = width
        self.height = height
        self.solution = list(range(1, len(self))) + [0]
        if state:
            self.cells = [x for x in state]
        else:
            self.cells = [x for x in self.solution]
        self.moves_from_start = []
        self.move = {'U': -self.width,
                     'L': -1,
                     'D': self.width,
                     'R': 1}

    def next_grid(self, move):
        pos_from = self.cells.index(0)
        pos_to = pos_from + self.move[move]

        g = self.__class__(self.width, self.height)
        g.cells = [x for x in self.cells]
        g.cells[pos_from], g.cells[pos_to] = g.cells[pos_to], g.cells[pos_from]
        g.moves_from_start = self.moves_from_start + [move]
        return g

    def __len__(self):
        return self.width * self.height

    def __str__(self):
        r = []
        for x in range(self.width):
            r.append("".join("{:2d}".format(self.cells[self.width * x + y])
                             for y in range(self.height)))
        return "\n".join(r)

    def __repr__(self):
        return "<{} width={} height={} cells={}>".format(self.__class__.__name__, self.width, self.width, self.cells)

    def moves(self):
        empty = self.cells.index(0)
        possible_moves = []
        if empty >= self.width:
            possible_moves.append('U')
        if empty % self.width > 0:
            possible_moves.append('L')
        if empty < self.width * (self.height - 1):
            possible_moves.append('D')
        if empty % self.width < self.width - 1:
            possible_moves.append('R')

        return sorted([self.next_grid(move) for move in possible_moves], key=lambda x: x.score())

    @staticmethod
    def solve(grid):
        return grid


class DFSSlidingPuzzle(SlidingPuzzle):
    """
    This implementation uses DFS to solve the puzzle, with manhattan distance as scoring.
    Works ok for 3x3 puzzles but is horrendously slow for 4x4
    """

    def manhattan_distance(self, goal, position):
        if goal == 0 or goal == position:
            return 0
        goal_y = goal // self.height
        goal_x = goal % self.width
        pos_y = position // self.height
        pos_x = position % self.width
        return abs(pos_x - goal_x) + abs(pos_y - goal_y)

    def score(self):
        return sum(self.manhattan_distance(self.solution[x], self.cells[x]) for x in range(len(self)))

    def key(self):
        return ",".join(str(x) for x in self.cells)

    @staticmethod
    def solve(grid):
        moves = deque()
        moves.append((grid, 0))

        visited = set()
        visited.add(grid.key())

        while moves:
            current, num_moves = moves.popleft()
            if current.score() == 0:
                return current
            elif num_moves < len(grid) ** 2:
                for next_move in current.moves():
                    if next_move.key() not in visited:
                        visited.add(next_move.key())
                        moves.append((next_move, num_moves + 1))



def main():
    g = DFSSlidingPuzzle(3, 3, state=[1, 2, 3, 7, 4, 5, 0, 8, 6])
    print(repr(g))
    print(g)

    solution = DFSSlidingPuzzle.solve(g)
    print("Puzzle solved in {} steps, {}".format(len(solution.moves_from_start), ''.join(solution.moves_from_start)))

    for move in solution.moves_from_start:
        g = g.next_grid(move)
        print(move)
        print(g)
        print("-------")


if __name__ == '__main__':
    main()
