# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'
X_POS = 0
Y_POS = 0

def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')
    
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move

def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid

def get_position(move, x_pos, y_pos):
    if move == LEFT:
        if x_pos > 0:
            x_pos = x_pos - 1
        else:
            x_pos = DIM - 1
    elif move == RIGHT:
        if x_pos < DIM - 1:
            x_pos = x_pos + 1
        else:
            x_pos = 0
    elif move == UP:
        if y_pos > 0:
            y_pos = y_pos - 1
        else:
            y_pos = DIM - 1
    elif move == DOWN:
        if y_pos < DIM - 1:
            y_pos = y_pos + 1
        else:
            y_pos = 0 
    
    return y_pos, x_pos

def grid_movement_loop(grid_object):
    x_pos = X_POS
    y_pos = Y_POS

    movement = get_move()
    
    while movement != QUIT:

        grid_object[y_pos][x_pos] = EMPTY
        y_pos, x_pos = get_position(movement, x_pos, y_pos)
        grid_object[y_pos][x_pos] = POSITION
        
        print_grid(grid_object)
        movement = get_move()

def print_grid(grid_object):
    for list_element in grid_object:
        for element in list_element:
            print(element, end=" ")
        print()
    print()    

def main():
    grid = initialize_grid()
    print_grid(grid)
    grid_movement_loop(grid)

main()