import unittest
from grid import Grid
from game import Game
from block import Block
from colors import Colors
from blocks import *
from position import Position

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.t_grid = Grid()
        self.t_grid.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]

    def tearDown(self):
        del self.t_grid


    def test_grid_is_empty_true(self):
        self.assertTrue(self.t_grid.is_empty(0, 0))

    def test_grid_is_empty_false(self):
        self.t_grid.grid[0][0] = 1
        self.assertFalse(self.t_grid.is_empty(0, 0))

    def test_grid_is_inside_true(self):
        self.assertTrue(self.t_grid.is_inside(0, 0))
        self.assertTrue(self.t_grid.is_inside(19, 0))
        self.assertTrue(self.t_grid.is_inside(0, 9))
        self.assertTrue(self.t_grid.is_inside(19, 9))
        self.assertTrue(self.t_grid.is_inside(2, 7))

    def test_grid_is_inside_false(self):
        self.assertFalse(self.t_grid.is_inside(-1, 0))
        self.assertFalse(self.t_grid.is_inside(20, 0))
        self.assertFalse(self.t_grid.is_inside(0, 10))
        self.assertFalse(self.t_grid.is_inside(20, 10))

    def test_grid_is_row_full_true(self):
        for i in range(self.t_grid.num_cols):
            self.t_grid.grid[0][i] = 1 
        self.assertTrue(self.t_grid.is_row_full(0))

    def test_grid_is_row_full_false(self):
        self.t_grid.grid[1][3] = 1 
        self.assertFalse(self.t_grid.is_row_full(0))
        self.assertFalse(self.t_grid.is_row_full(1))

    def test_grid_clear_row(self):
        for i in range(self.t_grid.num_cols):
            self.t_grid.grid[0][i] = 1 
        self.t_grid.clear_row(0)

        for i in range(self.t_grid.num_cols):
            self.assertEqual(self.t_grid.grid[0][i], 0)

    def test_grid_move_row_down(self):
        pass

    def test_grid_clear_full_rows(self):
        pass

    def test_grid_reset(self):
        for row in range(self.t_grid.num_rows - 5):
            for column in range(self.t_grid.num_cols - 2):
                self.t_grid.grid[row][column] = 1

        self.t_grid.reset()

        for row in range(self.t_grid.num_rows):
            for column in range(self.t_grid.num_cols):
                self.assertEqual(self.t_grid.grid[row][column], 0)

    def test_grid_all_cells_above_are_empty_true(self):
        #self.t_grid.grid[0][5] = 1
        self.assertTrue(self.t_grid.all_cells_above_are_empty(5, 0))
        self.assertTrue(self.t_grid.all_cells_above_are_empty(19, 6))

    def test_grid_all_cells_above_are_empty_false(self):
        for row in range(self.t_grid.num_rows):
            self.t_grid.grid[row][6] = 1
        self.assertFalse(self.t_grid.all_cells_above_are_empty(5, 6))
        self.assertFalse(self.t_grid.all_cells_above_are_empty(19, 6))

    def test_grid_search_first_row_with_empty_cell_all_empty(self):
        self.assertEqual(self.t_grid.search_first_row_with_empty_cell(), 19)

    def test_grid_search_first_row_with_empty_cell_not_all_empty(self):
        for column in range(self.t_grid.num_cols - 1):
            self.t_grid.grid[19][column] = 1
        self.t_grid.grid[18][9] = 1
        self.assertEqual(self.t_grid.search_first_row_with_empty_cell(), 18)

    def test_grid_search_empty_cells_all_empty(self):
        result = {19: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                  18: []}
        self.assertEqual(self.t_grid.search_empty_cells(), result)

    def test_grid_search_empty_cells_not_all_empty1(self):
        self.t_grid.grid[19][2] = 1
        self.t_grid.grid[18][9] = 1
        result = {19: [0, 1, 3, 4, 5, 6, 7, 8],
                  18: [2]}
        self.assertEqual(self.t_grid.search_empty_cells(), result)

    def test_grid_search_empty_cells_not_all_empty2(self):
        for column in range(self.t_grid.num_cols):
            self.t_grid.grid[19][column] = 1 
        self.t_grid.grid[18][9] = 1

        result = {18: [0, 1, 2, 3, 4, 5, 6, 7, 8],
                  17: [9]}
        self.assertEqual(self.t_grid.search_empty_cells(), result)

if __name__ == '__main__':
    unittest.main()
