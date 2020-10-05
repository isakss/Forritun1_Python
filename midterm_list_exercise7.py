"""
This program allows the user to create a list of designated size, input size many elements into the list, and then calculates the average from the list.
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

def get_average(list_object):
    sum_of_list = 0

    for element in list_object:
        sum_of_list += element

    average_of_list = sum_of_list / len(list_object)

    return round(average_of_list,2)

def main_func():
    size_num = int(input("Enter the size of the list: "))
    value_list = populate_list(size_num)
    average_of_list = get_average(value_list)

    print(value_list)
    print("The average of the list is {}".format(average_of_list))

main_func()