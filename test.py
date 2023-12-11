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
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 1, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        self.t_grid.move_row_down(18, 1)

        result_grid = [
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
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 1, 1, 0, 0, 0, 1, 0]
            ]
        
        self.assertCountEqual(self.t_grid.grid, result_grid)

    def test_grid_clear_full_rows(self):
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
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 0]
            ]
        
        self.t_grid.clear_full_rows()

        result_grid = [
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
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 0]
            ]
        
        self.assertCountEqual(self.t_grid.grid, result_grid)        

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
        

class TestGame(unittest.TestCase):
    def setUp(self):
        self.t_game = Game()
        self.t_game.grid = Grid()
        #self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.t_game.current_block = OBlock()
        

    def tearDown(self):
        del self.t_game.current_block
        del self.t_game.grid


    def test_move_left_move(self):
        self.t_game.move_left()
        result = [Position(0, 3), Position(0, 4), Position(1, 3), Position(1, 4)]
        
        for i in range(4):
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].row, result[i].row)
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].column, result[i].column)

    def test_move_left_not_move(self):
        for i in range(3):
            self.t_game.move_left()

        result = [Position(0, 1), Position(0, 2), Position(1, 1), Position(1, 2)]

        for i in range(4):
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].row, result[i].row)
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].column, result[i].column)

    def test_move_right_move(self):
        first_pos = []
        for i in range(4):
            first_pos.append(self.t_game.current_block.get_cell_positions()[i])
        self.t_game.move_right()

        for i in range(4):
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].row, first_pos[i].row)
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].column, first_pos[i].column + 1)
        
    def test_move_right_not_move(self):
        for i in range(4):
            self.t_game.move_right()

        result = [Position(0, 8), Position(0, 9), Position(1, 8), Position(1, 9)]

        for i in range(4):
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].row, result[i].row)
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].column, result[i].column)


    def test_move_down_move(self):
        self.t_game.move_down()
        result = [Position(1, 4), Position(1, 5), Position(2, 4), Position(2, 5)]

        for i in range(4):
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].row, result[i].row )
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].column, result[i].column)

     
    def test_move_down_not_move(self):
        for i in range(19):
            self.t_game.move_down()


        if self.t_game.current_block.id in [1, 3]:
            self.assertEqual(self.t_game.current_block.get_cell_positions()[0].row, 1)
        else:
            self.assertEqual(self.t_game.current_block.get_cell_positions()[0].row, 0)
    
    def test_lock_block(self):
        self.t_game.grid.grid = [
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
            [1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
            ]

        self.t_game.current_block.move(18, 0)
        self.t_game.lock_block()

        result_grid = [
          #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
            [0, 0, 0, 0, 4, 4, 0, 0, 0, 0],
            [1, 1, 1, 0, 4, 4, 1, 1, 1, 1],
            ]

        self.assertEqual(self.t_game.grid.grid, result_grid)

        
    def test_lock_block_game_over(self):
        self.t_game.grid.grid = [
            [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
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
            [1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
            ]

        #self.t_game.current_block.move(18, 0)
        self.t_game.lock_block()

        self.assertTrue(self.t_game.game_over)


    def test_rotate_change(self):
        self.t_game.current_block = JBlock()
        first_rotation = self.t_game.current_block.rotation_state
        self.t_game.rotate()
        self.assertEqual(self.t_game.current_block.rotation_state, first_rotation + 1)

    def test_rotate_not(self):
        first_rotation = self.t_game.current_block.rotation_state
        self.t_game.rotate()
        self.assertEqual(self.t_game.current_block.rotation_state, first_rotation)

    def test_rotate_4_times(self):
        self.t_game.current_block = JBlock()
        first_rotation = self.t_game.current_block.rotation_state
        for i in range(4):
            self.t_game.rotate()
        self.assertEqual(self.t_game.current_block.rotation_state, first_rotation)

    def test_reset(self):
        self.t_game.blocks = []
        self.t_game.reset()
        result = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

        self.assertEqual(len(self.t_game.blocks), len(result) - 2)

        for row in range(self.t_game.grid.num_rows):
            for column in range(self.t_game.grid.num_cols):
                self.assertEqual(self.t_game.grid.grid[row][column], 0)

    def test_move_for_rotation_right(self):
        self.t_game.current_block = LBlock()
        self.t_game.rotate()
        self.t_game.current_block.move(0, -4)
        first_rotation = self.t_game.current_block.rotation_state
        self.t_game.rotate()
        self.assertEqual(self.t_game.current_block.rotation_state, first_rotation)

        self.t_game.move_for_rotation(first_rotation + 1)
        self.assertEqual(self.t_game.current_block.rotation_state, first_rotation + 1)

    def test_move_for_rotation_left(self):
        self.t_game.current_block = LBlock()
        self.t_game.rotate()
        self.t_game.current_block.move(0, 5)
        first_rotation = self.t_game.current_block.rotation_state
        self.t_game.rotate()
        self.assertEqual(self.t_game.current_block.rotation_state, first_rotation)

        self.t_game.move_for_rotation(first_rotation + 1)
        self.assertEqual(self.t_game.current_block.rotation_state, first_rotation + 1)


    def test_fall_position_last_row(self):
        self.t_game.grid.grid = [
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
        self.t_game.current_block = LBlock()
        self.assertEqual(self.t_game.fall_position(), 19)
        

    def test_fall_position_1_rotation(self):
        self.t_game.grid.grid = [
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
            [1, 1, 1, 1, 0, 1, 0, 1, 1, 1]
            ]
        self.t_game.current_block = LBlock()
        self.t_game.rotate()
        self.assertEqual(self.t_game.fall_position(), 18)
        

    def test_fall_position_2_rotation(self):
        self.t_game.grid.grid = [
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
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 1, 0, 1, 1, 1]
            ]
        self.t_game.current_block = LBlock()
        self.t_game.rotate()
        self.t_game.rotate()
        self.assertEqual(self.t_game.fall_position(), 12)

    def test_count_of_empty_cells_under_block_no_empty_cells(self):
        self.t_game.grid.grid = [
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
        self.t_game.current_block = LBlock()
        
        self.assertEqual(self.t_game.count_of_empty_cells_under_block(19), 0)
        

    def test_count_of_empty_cells_under_block_1_empty_cells(self):
        self.t_game.grid.grid = [
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
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
            ]
        self.t_game.current_block = LBlock()
        
        self.assertEqual(self.t_game.count_of_empty_cells_under_block(18), 1)

    def test_count_of_empty_cells_under_block_4_empty_cells(self):
        self.t_game.grid.grid = [
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
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
            ]
        self.t_game.current_block = LBlock()

        self.assertEqual(self.t_game.count_of_empty_cells_under_block(17), 3)

    def test_auto_tetris_empty_grid(self):
        self.t_game.grid.grid = [
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
        self.t_game.current_block = LBlock()

        self.t_game.auto_tetris()
        result = [0, 1, 2, 2]

        for i in range(len(result)):
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].column, result[i])
        self.assertEqual(self.t_game.current_block.rotation_state, 0)

    def test_auto_tetris_not_empty_grid_0_rotate(self):
        self.t_game.grid.grid = [
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
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 1, 1, 0]
            ]
        self.t_game.current_block = LBlock()

        self.t_game.auto_tetris()
        result = [1, 2, 3, 3]

        for i in range(len(result)):
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].column, result[i])
        self.assertEqual(self.t_game.current_block.rotation_state, 0)

    def test_auto_tetris_not_empty_grid_1_rotate(self):
        self.t_game.grid.grid = [
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
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
            ]
        self.t_game.current_block = LBlock()

        self.t_game.auto_tetris()
        result = [1, 1, 1, 2]

        for i in range(len(result)):
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].column, result[i])
        self.assertEqual(self.t_game.current_block.rotation_state, 1)


    def test_auto_tetris_not_empty_grid_2_rotate(self):
        self.t_game.grid.grid = [
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
            [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 0, 0]
            ]
        self.t_game.current_block = LBlock()

        self.t_game.auto_tetris()
        result = [2, 2, 3, 4]

        for i in range(len(result)):
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].column, result[i])
        self.assertEqual(self.t_game.current_block.rotation_state, 2)

    def test_auto_tetris_not_empty_grid_3_rotate(self):
        self.t_game.grid.grid = [
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
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 0, 0, 0]
            ]
        self.t_game.current_block = LBlock()

        self.t_game.auto_tetris()
        result = [0, 1, 1, 1]

        for i in range(len(result)):
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].column, result[i])
        self.assertEqual(self.t_game.current_block.rotation_state, 3)


    def test_auto_tetris_empty_cells_under_block_3_rotation(self):
        self.t_game.grid.grid = [
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
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
            ]
        self.t_game.current_block = LBlock()

        self.t_game.auto_tetris()
        result = [8, 9, 9, 9]

        for i in range(len(result)):
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].column, result[i])
        self.assertEqual(self.t_game.current_block.rotation_state, 3)

    def test_auto_tetris_empty_cells_under_block_rotation(self):
        self.t_game.grid.grid = [
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
            [0, 0, 1, 0, 1, 0, 0, 1, 1, 0],
            [0, 0, 1, 0, 1, 1, 0, 1, 1, 0],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
            ]
        self.t_game.current_block = LBlock()

        self.t_game.auto_tetris()
        result = [0, 1, 1, 1]

        for i in range(len(result)):
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].column, result[i])
        self.assertEqual(self.t_game.current_block.rotation_state, 3)

        for i in range(len(result)):
            self.assertEqual(self.t_game.current_block.get_cell_positions()[i].column, result[i])
        self.assertEqual(self.t_game.current_block.rotation_state, 3)




class TestBlock(unittest.TestCase):
    def setUp(self):
        self.t_block = LBlock()

    def tearDown(self):
        del self.t_block

    def test_move(self):
        first_col_offset = self.t_block.column_offset 
        first_row_offset = self.t_block.row_offset 
        self.t_block.move(6, -3)
        self.assertEqual(self.t_block.column_offset, first_col_offset - 3)
        self.assertEqual(self.t_block.row_offset, first_row_offset + 6)

    def test_get_cell_positions(self):
        self.t_block.row_offset = 3
        self.t_block.column_offset = 3

        result = [Position(1, 0), Position(1, 1), Position(1, 2), Position(0, 2)]
        for i in range(4):
            self.assertEqual(self.t_block.get_cell_positions()[i].column, result[i].column + self.t_block.column_offset) 
            self.assertEqual(self.t_block.get_cell_positions()[i].row, result[i].row + self.t_block.row_offset)
    
    def test_rotate_1_rotate(self):
        first_rotation = self.t_block.rotation_state 
        self.t_block.rotate()
        self.assertEqual(self.t_block.rotation_state, first_rotation + 1)

    def test_rotate_4_rotates(self):
        first_rotation = self.t_block.rotation_state 
        for i in range((len(self.t_block.cells))):
            self.t_block.rotate()
        self.assertEqual(self.t_block.rotation_state, first_rotation)

    def test_undo_rotations_first_0_rotate(self):
        first_rotation = self.t_block.rotation_state 
        self.t_block.undo_rotation()
        self.assertEqual(self.t_block.rotation_state, 3)

    def test_undo_rotations_first_3_rotate(self):
        self.t_block.rotation_state = 3
        self.t_block.undo_rotation()
        self.assertEqual(self.t_block.rotation_state, 2)


if __name__ == '__main__':
    unittest.main()
