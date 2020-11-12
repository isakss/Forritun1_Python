"""
This program allows the entry of four students and three grades belonging to each student into a dictionary.
The program then prints the students in alphabetical order and then prints out the highest grade average.
"""
STUDENT_NUMBER = 4
GRADE_NUMBER = 3

def get_highest_average(dictionary_object):
    max_average = 0.0
    highest_student = ""

    for key, value in dictionary_object.items():
        grade_average = sum(value)/len(value)
        
        if grade_average > max_average:
            max_average = grade_average
            highest_student = key
    
    print("Student with highest average grade:")
    print("{} has an average grade of {:.2f}".format(highest_student, max_average))

def convert_to_float(list_object):
    return [float(element) for element in list_object]

def print_student_list(dictionary_object):
    print("Student list:")

    for key, value in sorted(dictionary_object.items()):
        print("{}: {}".format(key, value))

def student_entry_loop():
    count = 0
    student_dictionary = {}

    while count < STUDENT_NUMBER:
        grade_list = []
        student_name = input("Student name: ")

        for i in range(1, GRADE_NUMBER + 1):
            student_grade = input("Input grade number {}: ".format(i))
            grade_list.append(student_grade)

        float_grade_list = convert_to_float(grade_list)    
        
        student_dictionary[student_name] = float_grade_list
        count += 1
    
    return student_dictionary

def main():
    student_dict = student_entry_loop()
    print_student_list(student_dict)
    get_highest_average(student_dict)

main()
