"""
This program allows the user to input as many values into a list as the user dictates and then finds the sum of all elements from that list.
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

def get_list_sum(list_object):
    sum_of_list = 0
    for element in list_object:
        sum_of_list += element
    return sum_of_list

def main_func():
    size_num = int(input("Enter the size of the list: "))
    value_list = populate_list(size_num)
    list_sum = get_list_sum(value_list)

    print(value_list)
    print("The sum of the list is {}".format(list_sum))

main_func()