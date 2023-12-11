import random
from grid import Grid
from position import Position
from blocks import *

class Game:
    def __init__(self):
        self.grid = Grid()
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

        if self.current_block.id == 1:
            # словарь с пустыми клетками, который надо перебрать
            dict_of_empty_cells = self.grid.search_empty_cells()

            min_empty_cells = 1000
            best_rotation = 0
            best_pos_column = 0

            for row in dict_of_empty_cells:
                for column in dict_of_empty_cells.get(row):
                    #print(row, " ", column)

                    # для каждой клетки попробовать расположить блок 
                    # перебрав все повороты блока
                    for rotate in range(len(self.current_block.cells)):
                        if rotate != 0 or (rotate == 0 and self.current_block.rotation_state != 0):
                            self.rotate()

                            # если не удается повернуть блок
                            # двигать, пока не получится повернуть
                            if self.current_block.rotation_state != rotate:
                                self.move_for_rotation(rotate)
                        
                        # разместить блок над пустой клеткой
                        if self.current_block.get_cell_positions()[self.current_block.X[self.current_block.rotation_state]].column > column:
                            for i in range(self.current_block.get_cell_positions()[self.current_block.X[self.current_block.rotation_state]].column - column):
                                self.move_left()
                        elif self.current_block.get_cell_positions()[self.current_block.X[self.current_block.rotation_state]].column < column:
                            for i in range(column - self.current_block.get_cell_positions()[self.current_block.X[self.current_block.rotation_state]].column):
                                self.move_right()

                        ppp = self.current_block.get_cell_positions()[self.current_block.X[self.current_block.rotation_state]].column
                        print(self.current_block.get_cell_positions()[self.current_block.X[self.current_block.rotation_state]].column)


                        # найти строку, где он остановится
                        fall_row = self.fall_position()
                        print("Пустая клетка", row, " ", column)
                        print("Поворот", self.current_block.rotation_state)
                        print("Позиция падения", fall_row)
                        

                        # подсчисать количество пустых клеток под блоком
                        count_of_empty_cells = self.count_of_empty_cells_under_block(fall_row)
                        print("количество пустых клеток", count_of_empty_cells)
                        print()

                        ## если 0, конец
                        if count_of_empty_cells == 0:
                            return 0
                        ## иначе сравнить и если это наилучщий вариант, то запомнить
                        elif count_of_empty_cells < min_empty_cells:
                            min_empty_cells = count_of_empty_cells
                            best_pos_column = self.current_block.get_cell_positions()[self.current_block.X[self.current_block.rotation_state]].column
                            best_rotation = self.current_block.rotation_state
        
            # все клетки перебраны      

            '''
            # нужный поворот блока
            if self.current_block.rotation_state != best_rotation:
                self.move_for_rotation(rotate)


            # смещение блока
            if self.current_block.get_cell_positions()[self.current_block.X[self.current_block.rotation_state]].column > column:
                for i in range(self.current_block.get_cell_positions()[self.current_block.X[self.current_block.rotation_state]].column - column):
                    self.move_left()
            elif self.current_block.get_cell_positions()[self.current_block.X[self.current_block.rotation_state]].column < column:
                for i in range(column - self.current_block.get_cell_positions()[self.current_block.X[self.current_block.rotation_state]].column):
                    self.move_right()

            print(min_empty_cells)
            return(0)
            '''

    def count_of_empty_cells_under_block(self, fall_row):
        count = 0
        for row in range (self.grid.num_rows - 1, fall_row, -1):
            for column in range(self.current_block.get_cell_positions()[0].column, self.current_block.get_cell_positions()[0].column + self.current_block.lenght[self.current_block.rotation_state]):
                if self.grid.is_empty(row, column) == True:
                    count += 1

        for i in range(len(self.current_block.irregularities[self.current_block.rotation_state])):
            if self.current_block.irregularities[self.current_block.rotation_state][i] != 0:
                qqq = fall_row
                qqqq = fall_row - self.current_block.irregularities[self.current_block.rotation_state][i]
                for row in range (fall_row, fall_row - self.current_block.irregularities[self.current_block.rotation_state][i], -1):
                    r = row
                    c = self.current_block.get_cell_positions()[0].column + i
                    if self.grid.is_empty(row, self.current_block.get_cell_positions()[0].column + i):
                        count += 1

        #q = self.current_block.irregularities[self.current_block.rotation_state]
        #for i in range(len(self.current_block.irregularities[self.current_block.rotation_state])):
            #if self.grid.is_empty(self.current_block.get_cell_positions()[i].column)
            #count += self.current_block.irregularities[self.current_block.rotation_state][i]

        return count
        
    def fall_position(self):
        r = self.current_block.rotation_state
        x = self.current_block.X[r]
        q1 = self.current_block.get_cell_positions()[x].row
        q2 = self.grid.num_rows

        c = self.current_block.cells[r]
        cl = len(self.current_block.cells[r])

        x0 = self.current_block.get_cell_positions()[0].row
        xx0 = self.current_block.get_cell_positions()[0].column

        for i in range(self.current_block.get_cell_positions()[self.current_block.X[r]].row, self.grid.num_rows - 1):
            #for cell in range(self.current_block.cells[r]):
            for j in range(len(self.current_block.cells[r])):
                r1 = self.current_block.get_cell_positions()[j].row + i
                c1 = self.current_block.get_cell_positions()[j].column 
                if self.current_block.get_cell_positions()[j].row + i > 19:
                    return (self.current_block.get_cell_positions()[self.current_block.X[r]].row + i - 1 )
                if self.grid.is_empty(self.current_block.get_cell_positions()[j].row + i, self.current_block.get_cell_positions()[j].column) == False:
                    return (self.current_block.get_cell_positions()[self.current_block.X[r]].row + i - 1 )
        return 19
        
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