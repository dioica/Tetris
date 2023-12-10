import random
from grid import Grid
from position import Position
from blocks import *

class Game:
    def __init__(self):
        self.grid = Grid()
        #self.blocks = []
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        self.grid.clear_full_rows()
        if self.block_fits() == False:
            self.game_over = True

        self.auto_tetris()
            
        

    def auto_tetris(self):
        #self.current_block = self.next_block
        #self.next_block = self.get_random_block()

        # словарь с пустыми клетками, который надо перебрать
        dict_of_empty_cells = self.grid.search_empty_cells()
        for row in dict_of_empty_cells:
            for column in dict_of_empty_cells.get(row):
                print(row, " ", column)

                # для каждой клетки попробовать расположить блок 
                # перебрав все повороты блока
                for rotate in range(len(self.current_block.cells)):
                    if rotate != 0:
                        self.rotate()

                        # если не удается повернуть блок
                        # двигать, пока не получится повернуть
                        if self.current_block.rotation_state != rotate:
                            self.move_for_rotation(rotate)
                        
                # разместить блок над пустой клеткой
                
                # найти строку, где он остановится

                # подсчисать количество пустых клеток под блоком
                ## если 0, конец
                ## иначе сравнить и если это наилучщий вариант, то запомнить

        
    def search_fall_position(self):


        return 0
        
    def move_for_rotation(self, rotate):
        for i in range(4):
            self.move_left()
            self.rotate()
            if self.current_block.rotation_state == rotate:
                return 0

        for i in range(4):
            self.move_right()
            self.rotate()
            if self.current_block.rotation_state == rotate:
                return 0 

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True
    
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False:
            self.current_block.undo_rotation()

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)