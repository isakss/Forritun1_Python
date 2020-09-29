def get_numbers_list():
    numbers_list = input("Enter scores separated by space: ").split()
    return numbers_list

def cast_to_float(list_object):
    return [float(element) for element in list_object]

def remove_two_lowest(list_object):
    list_object.remove(min(list_object))
    list_object.remove(min(list_object))
    return list_object

def sum_list(list_object):
    return sum(list_object)

def main_func():
    numbers_list = get_numbers_list()
    if len(numbers_list) < 2:
        print("At least two scores needed!")
    else:
        float_list = cast_to_float(numbers_list)
        clean_numbers_list = remove_two_lowest(float_list)
        sum_from_list = sum_list(clean_numbers_list)
        print("Sum of scores (two lowest removed): {}".format(round(sum_from_list,1)))

main_func()