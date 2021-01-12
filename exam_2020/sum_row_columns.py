def open_file(file_name):
    try:
        return open(file_name, "r")
    except FileNotFoundError:
        return None

def read_matrix(file_object):
    matrix = []

    for line in file_object:
        line = line.strip().split()
        matrix.append([int(element) for element in line])
    
    return matrix

def row_sum_same(matrix):
    established_sum = sum(matrix[0])
    total_row_sum = 0

    for element in matrix:
        if sum(element) != established_sum:
            total_row_sum = 0
            break
        else:
            total_row_sum = established_sum
    
    return total_row_sum
        
def col_sum_same(matrix):
    established_sum = 0
    total_col_sum = 0

    for i in range(0,len(matrix)):
        established_sum += matrix[0][i]
    
    for x in range(0, len(matrix)):
        tmp_sum = 0
        for j in range(0, len(matrix)):
            tmp_sum += matrix[j][x]
        if tmp_sum != established_sum:
            total_col_sum = 0
            break
        else:
            total_col_sum = established_sum
    
    return total_col_sum

def print_matrix(matrix):
    for list_element in matrix:
        for element in list_element:
            print("{}\t".format(element), end="")
        print()

def determine_if_same(row_sum, col_sum):
    if row_sum == col_sum:
        print("Same sums")
    else:
        print("Not same sums")

def main():
    filename = input("File name: ")
    read_file = open_file(filename)

    if read_file == None:
        print("File not found")
    else:
        int_matrix = read_matrix(read_file)

        row_sum = row_sum_same(int_matrix)
        col_sum = col_sum_same(int_matrix)

        print_matrix(int_matrix)
        determine_if_same(row_sum, col_sum)

main()