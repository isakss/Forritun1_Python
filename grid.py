
class Grid(object):
    def __init__(self, grid_rows = 1, grid_columns = 1):
        self.grid = []
        self.x_pos = 1
        self.y_pos = 1
        self.grid_pos_x = 0
        self.grid_pos_y = 0

        self.grid_row_len = grid_rows
        self.grid_column_len = grid_columns

        for i in range(self.grid_row_len):
            gridline = []
            for j in range(self.grid_column_len):
                gridline.append("o")
            self.grid.append(gridline)
        
        self.grid[0][0] = "x"
        
    def current_pos(self):
        return (self.x_pos, self.y_pos)

    def move_right(self):
        
        if self.grid_pos_y == self.grid[self.grid_pos_x][-1]:
            self.grid_pos_y = 0
            self.y_pos = 1

            self.grid[self.grid_pos_x][-1] = "0"
            self.grid[self.grid_pos_x][self.grid_pos_y] = "x"
        else:
            self.grid[self.grid_pos_x][self.grid_pos_y] = "o"
            self.grid[self.grid_pos_x][self.grid_pos_y + 1] = "x"

            self.grid_pos_y += 1
            self.y_pos += 1
    
    def move_left(self):

        if self.grid_pos_y == self.grid[self.grid_pos_x][0]:
            self.grid_pos_y = -1
            self.y_pos = self.grid_column_len

            self.grid[self.grid_pos_x][0] = "o"
            self.grid[self.grid_pos_x][self.grid_pos_y] = "x"
        else:
            self.grid[self.grid_pos_x][self.grid_pos_y] = "o"
            self.grid[self.grid_pos_x][self.grid_pos_y - 1] = "x"

            self.grid_pos_y -= 1
            self.y_pos -= 1

    def move_up(self):

        if self.grid_pos_x == self.grid[0][self.grid_pos_y]:
            self.grid_pos_x = -1
            self.x_pos = self.grid_row_len

            self.grid[0][self.grid_pos_y] = "o"
            self.grid[self.grid_pos_x][self.grid_pos_y] = "x"
        else:
            self.grid[self.grid_pos_x][self.grid_pos_y] = "o"
            self.grid[self.grid_pos_x + 1][self.grid_pos_y] = "x"

            self.grid_pos_x += 1
            self.x_pos += 1
    
    def move_down(self):
        if self.grid_pos_x == self.grid[-1][self.grid_pos_y]:
            self.grid_pos_x = 0
            self.x_pos = 1

            self.grid[-1][self.grid_pos_y] = "o"
            self.grid[self.grid_pos_x][self.grid_pos_y] = "x"
        else:
            self.grid[self.grid_pos_x][self.grid_pos_y] = "o"
            self.grid[self.grid_pos_x - 1][self.grid_pos_y] = "x"

            self.grid_pos_x -= 1
            self.x_pos -= 1

    def __str__(self):
        grid_str = ""

        for list_element in self.grid:
            for element in list_element:
                grid_str += element
            grid_str += "\n"
        
        return str(grid_str)

a_grid = Grid(3,4)
print(a_grid) 
print(a_grid.current_pos())

a_grid.move_right()
print(a_grid)
print(a_grid.current_pos())

a_grid.move_left()
print(a_grid)
print(a_grid.current_pos())

a_grid.move_down()
print(a_grid)
print(a_grid.current_pos())

a_grid.move_down()
print(a_grid)
print(a_grid.current_pos())

a_grid.move_up()
print(a_grid)
