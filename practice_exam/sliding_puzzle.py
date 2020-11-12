# Constants
DIM = 4 # dimension of the board DIMxDIM
EMPTYSLOT = 0
QUIT = 0

def initialize_board():
    ''' Creates the initial board according to the user input.
    The board is a list of lists.
    The list contains DIM elements (rows), each of which contains DIM elements (columns)'''
    numbers = input().split()
    numbers = [int(number) for number in numbers]
    puzzle_board = []
    index = 0
    for _ in range(DIM):
        row = numbers[index:index + DIM]
        index += DIM
        puzzle_board.append(row)

    return puzzle_board
    
def display(puzzle_board):
    ''' Display the board, printing it one row in each line '''
    print()
    for i in range(DIM):
        for j in range(DIM):
            if puzzle_board[i][j] == EMPTYSLOT:
                print("\t", end="")
            else:
                print(str(puzzle_board[i][j]) + "\t", end="")
        print()
    print()

def get_position(grid_object, number):
    for i in range(DIM):
        for j in range(DIM):
            if grid_object[i][j] == number:
                return (i, j)

def get_new_position(grid_object, tuple_object):
    i,j = tuple_object

    if j > 0 and grid_object[i][j - 1] == EMPTYSLOT:
        return (i, j - 1)
    elif j < DIM - 1 and grid_object[i][j + 1] == EMPTYSLOT:
        return (i, j + 1)
    elif i > 0 and grid_object[i - 1][j] == EMPTYSLOT:
        return (i - 1, j)
    elif i < DIM - 1 and grid_object[i + 1][j] == EMPTYSLOT:
        return (i + 1, j)

def movement_func(grid_object, int_object):
    current_pos = get_position(grid_object, int_object)
    new_position = get_new_position(grid_object, current_pos)

    if new_position != None:
        current_i_pos, current_j_pos = current_pos
        new_i_pos, new_j_pos = new_position
        grid_object[current_i_pos][current_j_pos] = EMPTYSLOT
        grid_object[new_i_pos][new_j_pos] = int_object

def main():
    puzzle_board = initialize_board()
    number_input = -1

    while number_input != QUIT:
        display(puzzle_board)
        number_input = int(input())
        movement_func(puzzle_board, number_input)

main()