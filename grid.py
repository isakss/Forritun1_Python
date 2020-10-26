"""
This program consists of a class that initializes a grid with the number of rows and columns determined by parameters passed by the user.
The class has functions that enable movement in the grid, as well as a function that reports the current position of the positional symbol within the grid.
"""
class Grid(object):
    def __init__(self, grid_rows = 1, grid_columns = 1):
        """ Initialize grid object variables """
        self.tile_symbol = "o"
        self.pos_symbol = "x"

        self.grid = []
        self.y_pos = 1                                     #Keep track of pos_symbol
        self.x_pos = 1
        self.grid_pos_y = 0                                #Keep track of index location within grid
        self.grid_pos_x = 0

        self.grid_row_len = grid_rows                      #Store length of rows and columns within variables that we can use
        self.grid_column_len = grid_columns

        for i in range(self.grid_row_len):                 #Initialize grid with tile symbols
            gridline = []
            for j in range(self.grid_column_len):
                gridline.append(self.tile_symbol)
            self.grid.append(gridline)
        
        self.grid[0][0] = self.pos_symbol                  #Initialize first value of grid as positional symbol
        
    def current_pos(self):
        """ Returns a tuple containing the current x and y position of the position symbol """
        return (self.y_pos, self.x_pos)

    def move_right(self):
        """ Moves the positional symbol within the grid to the right along the x axis, if edge of grid is encountered the positional symbol moves to the start of the current row """
        if self.grid_pos_x == self.grid_column_len - 1:
            self.grid_pos_x = 0
            self.x_pos = 1

            self.grid[self.grid_pos_y][-1] = self.tile_symbol
            self.grid[self.grid_pos_y][self.grid_pos_x] = self.pos_symbol
        else:
            self.grid[self.grid_pos_y][self.grid_pos_x] = self.tile_symbol
            self.grid[self.grid_pos_y][self.grid_pos_x + 1] = self.pos_symbol

            self.grid_pos_x += 1
            self.x_pos += 1
    
    def move_left(self):
        """ Moves the positional symbol within the grid to the left along the x axis, if edge of grid is encountered the positional symbol moves to the beginning of the current row """
        if self.grid_pos_x == 0:
            self.grid_pos_x = self.grid_column_len - 1
            self.x_pos = self.grid_column_len

            self.grid[self.grid_pos_y][0] = self.tile_symbol
            self.grid[self.grid_pos_y][self.grid_pos_x] = self.pos_symbol
        else:
            self.grid[self.grid_pos_y][self.grid_pos_x] = self.tile_symbol
            self.grid[self.grid_pos_y][self.grid_pos_x - 1] = self.pos_symbol

            self.grid_pos_x -= 1
            self.x_pos -= 1

    def move_up(self):
        """ Moves the positional symbol upwards along the y axis of the grid, if top of grid is encountered the positional symbol moves to the bottom of the grid """
        if self.grid_pos_y == 0:
            self.grid_pos_y = self.grid_row_len -1
            self.y_pos = self.grid_row_len

            self.grid[0][self.grid_pos_x] = self.tile_symbol
            self.grid[self.grid_pos_y][self.grid_pos_x] = self.pos_symbol
        else:
            self.grid[self.grid_pos_y][self.grid_pos_x] = self.tile_symbol
            self.grid[self.grid_pos_y - 1][self.grid_pos_x] = self.pos_symbol

            self.grid_pos_y -= 1
            self.y_pos -= 1
    
    def move_down(self):
        """ Moves the positional symbol downwards along the y axis of the grid, if bottom of grid is encountered the positional symbol moves to the top of the grid """

        if self.grid_pos_y == len(self.grid) - 1:
            self.grid_pos_y = 0
            self.y_pos = 1

            self.grid[-1][self.grid_pos_x] = self.tile_symbol
            self.grid[self.grid_pos_y][self.grid_pos_x] = self.pos_symbol
        else:
            self.grid[self.grid_pos_y][self.grid_pos_x] = self.tile_symbol
            self.grid[self.grid_pos_y + 1][self.grid_pos_x] = self.pos_symbol

            self.grid_pos_y += 1
            self.y_pos += 1

    def __str__(self):
        grid_str = ""

        for list_element in self.grid:
            for element in list_element:
                grid_str += element
            grid_str += "\n"
        
        return str(grid_str)

