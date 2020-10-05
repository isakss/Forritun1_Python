"""
This program allows the user to create a list of designated size, input size many elements into the list, and then creates a new list without duplicate values.
All non numeric values are ignored.
"""

def populate_list(int_object):
    new_list = []
    while len(new_list) != int_object:
        try:
            list_element = int(input("Enter an element to put into the list: "))
            new_list.append(list_element)
        except ValueError:
            pass
    return new_list

def find_unique_elements(list_object):
    new_unique_list = []

    for element in list_object:
        if element not in new_unique_list:
            new_unique_list.append(element)
    return new_unique_list

def main_func():
    size_num = int(input("Enter the size of the list: "))
    value_list = populate_list(size_num)
    unique_list = find_unique_elements(value_list)

    print("The list: {}".format(value_list))
    print("The list without duplicates: {}".format(unique_list))

main_func()