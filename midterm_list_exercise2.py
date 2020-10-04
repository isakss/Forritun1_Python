"""
This program allows the user to input a number that represents the length of a list, input that many elements, and then enter one value to
determine if it exists within the list
"""

def populate_list(int_object):
    new_list = []
    while len(new_list) != int_object:
        list_element = input("Enter an element to put into the list: ")
        new_list.append(list_element)
    return new_list

def find_element_in_list(list_object, target_string):
    if target_string in list_object:
        return True
    else:
        return False

def main_func():
    size_num = int(input("Enter the size of the list: "))
    target_string = input("Enter target value to find: ")

    value_list = populate_list(size_num)
    is_in_list = find_element_in_list(value_list, target_string)

    print(value_list)

    if is_in_list:
        print("{} is in the list".format(target_string))
    else:
        print("{} is not in the list".format(target_string))

main_func()