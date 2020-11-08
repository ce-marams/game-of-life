import unittest
from unittest.mock import patch
from components import Cell, Board
from numpy import random


class TestComponents(unittest.TestCase):

    def setUp(self):
        self.test_dead_board = Board(n=5)

        self.where_seed111_is_active = ((1, 0), (1, 1), (2, 2), (3, 2), (3, 3))
        self.test_active_board = Board(n=5)
        for entry in self.where_seed111_is_active:
            self.test_active_board.board[entry[0]][entry[1]].state = True

    def tearDown(self):
        pass

    def test_random_population(self):
        random.seed(111)
        self.test_dead_board.random_population()

        for i, row in enumerate(self.test_dead_board.board):
            for j, cell in enumerate(row):
                state_cell_seed111 = (i, j) in self.where_seed111_is_active
                self.assertEqual(cell.state, state_cell_seed111)

    def test_str_board(self):
        str_seed111 = "## ## ## ## ## \n-- -- ## ## ## \n## ## -- ## ## \n## ## -- -- ## \n## ## ## ## ## "
        self.assertEqual(self.test_active_board.str_board(), str_seed111)

    def test_neighbour_matrix(self):
        neighbour_matrix = [[2, 2, 1, 0, 0], [1, 2, 2, 1, 0], [2, 4, 3, 3, 1],
                            [0, 2, 2, 2, 1], [0, 1, 2, 2, 1]]

        self.assertEqual(
            self.test_active_board.neighbour_matrix(), neighbour_matrix)

    def test_next_gen(self):
        self.test_active_board.next_gen()

        where_next_is_active = ((1, 1), (2, 2), (2, 3), (3, 2), (3, 3))

        for i, row in enumerate(self.test_active_board.board):
            for j, cell in enumerate(row):
                state_cell_next = (i, j) in where_next_is_active
                self.assertEqual(cell.state, state_cell_next)


if __name__ == '__main__':
    unittest.main()
