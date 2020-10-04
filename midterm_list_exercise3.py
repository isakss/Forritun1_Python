def populate_list(int_object):
    new_list = []
    while len(new_list) != int_object:
        list_element = input("Enter an element to put into the list: ")
        new_list.append(list_element)
    return new_list

def count_target_element(list_object, target_value):
    element_count = 0

    for element in list_object:
        if element == target_value:
            element_count += 1
    return element_count

def main_func():
    size_num = int(input("Enter the size of the list: "))

    value_list = populate_list(size_num)

    print(value_list)

    target_value = input("Enter a target value: ")
    target_instances = count_target_element(value_list, target_value)
    
    print("{} instances of {} in the list".format(target_instances, target_value))

main_func()