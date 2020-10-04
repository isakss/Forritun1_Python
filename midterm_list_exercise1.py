"""This program allows the user to input an integer representing the size of a list, it then allows the user to insert that many elements into the list"""

def populate_list(int_object):
    new_list = []
    while len(new_list) != int_object:
        list_element = input("Enter an element to put into the list: ")
        new_list.append(list_element)
    return new_list

def main_func():
    size_num = int(input("Enter the size of the list: "))
    value_list = populate_list(size_num)

    print(value_list)

main_func()