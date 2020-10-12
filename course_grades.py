"""
This program takes information about students and their coursework and calculates their final grades based on the weight of each course factor
"""

def read_file(string_object):
    """ Opens and reads through a file, returning none if it isnt found """
    try:
        return open(string_object,"r")
    except FileNotFoundError:
        return None

def populate_weight_list(file_object):
    """ Takes information from a file object containing course weights and puts it into a list """
    new_list = []

    for line in file_object:
        new_list.append(line.split())
    
    return new_list

def populate_grades_list(file_object):
    """ Takes information from a file containing student emails and grades and puts each in seperate lists """
    email_list = []
    grade_list = []

    for line in file_object:
        tmp_list = line.split()
        email_list.append(tmp_list[0])
        grade_list.append(tmp_list[1::])

    for value_list in grade_list:
        for i, value in enumerate(value_list):
            value_list[i] = float(value)

    return email_list, grade_list

def populate_weight_tuple_list(list_object):
    """ Takes elements from a list containing course part names and their weights and returns a list of tuples containing those elements """
    tuple_list = []

    for i in range(len(list_object[0])):
        weight_tuple = (list_object[0][i], float(list_object[1][i]))
        tuple_list.append(weight_tuple)
    
    return tuple_list

def populate_grades_tuple_list(list_object1, list_object2):
    """ Takes elements from a list containing student emails and a list containing grades and returns a list of corresponding emails and grades in tuples """
    tuple_list = []

    for i in range(len(list_object1)):
        grades_tuple = (list_object1[i], list_object2[i])
        tuple_list.append(grades_tuple)
    
    return tuple_list

def calculate_final_grade(list_object1, list_object2):
    """ Takes lists containing information about grades and course weights and calculates the final grade from the course """

    list_object1 = [list(element) for element in list_object1]              #Have to turn the tuples in the list to lists so that we can add the final grade to the list

    for i in range(len(list_object1)):
        final_grade = 0.0
        for j in range(len(list_object1[i][1])):
            final_grade += (list_object1[i][1][j] * list_object2[j][1])
        list_object1[i].append(final_grade)
    
    list_object1 = [tuple(element) for element in list_object1]             #Turn the lists in the list into tuples again

    return list_object1

def print_results(list_object1, list_object2):
    """ Takes lists containing information about course parts and student grades and prints them in a formatted menu """
    STUDENT_COLUMN = 16
    GENERAL_COLUMN = 14

    print()
    print("{:>{}}".format("Student ID",STUDENT_COLUMN),end="")

    for i in range(len(list_object1)):
        print("{:>{}}".format(list_object1[i][0],GENERAL_COLUMN),end="")
    
    print("{:>{}}".format("Course grade",GENERAL_COLUMN))

    for tuple_element in list_object2:

        print("{:>{}}".format(tuple_element[0],STUDENT_COLUMN),end="")

        for i, value in enumerate(tuple_element[1]):
            print("{:>{}}".format(value,GENERAL_COLUMN),end="")
        
        print("{:>{}}".format(round(tuple_element[-1],2),GENERAL_COLUMN))


def main_func():
    """ Main function """

    parts_file_name = input("Enter filename for parts: ")
    parts_file = read_file(parts_file_name)

    if parts_file == None:
        print("File {} not found".format(parts_file_name))
    else:
        parts_list = populate_weight_list(parts_file)
        weight_tuples_list = populate_weight_tuple_list(parts_list)
        print(weight_tuples_list)

        grades_file_name = input("Enter filename for grades: ")
        grade_file = read_file(grades_file_name)
        if grade_file == None:
            print("File {} not found".format(grades_file_name))
        else:
            email_list, grades_list = populate_grades_list(grade_file)
            grades_tuple_list = populate_grades_tuple_list(email_list, grades_list)
            print(grades_tuple_list)

            modified_grade_tuple_list = calculate_final_grade(grades_tuple_list, weight_tuples_list)
            print(modified_grade_tuple_list)

            print_results(weight_tuples_list,modified_grade_tuple_list)

main_func()     
