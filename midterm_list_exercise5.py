"""
This program allows the user to input as many values into a list as the user dictates and then finds the lowest element from that list.
The program ignores values that are not of type int.
"""

def populate_list(int_object):
    new_list = []
    while len(new_list) != int_object:
        list_element = input("Enter an element to put into the list: ")
        try:
            new_list.append(int(list_element))
        except ValueError:
            pass     
    return new_list

def get_min_from_list(list_object):
    min_value = list_object[0]
    for element in list_object:
        if element < min_value:
            min_value = element
    return min_value

def main_func():
    size_num = int(input("Enter the size of the list: "))
    value_list = populate_list(size_num)
    min_list_value = get_min_from_list(value_list)

    print(value_list)
    print("The lowest value from the list is {}".format(min_list_value))

main_func()