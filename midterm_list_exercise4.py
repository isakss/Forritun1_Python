"""
This program allows the user to input as many values into a list as the user dictates and then finds the highest element from that list.
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

def get_max_from_list(list_object):
    max_value = 0
    for element in list_object:
        if element > max_value:
            max_value = element
    return max_value

def main_func():
    size_num = int(input("Enter the size of the list: "))
    value_list = populate_list(size_num)
    max_list_value = get_max_from_list(value_list)

    print(value_list)
    print("The highest value from the list is {}".format(max_list_value))

main_func()