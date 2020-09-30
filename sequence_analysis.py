"""
This program reads values from files, inserts them into a list and then prints that list unsorted, sorted, cumulative sum and median value from that particular list.
Wrong values are handled, as are invalid file reads.
"""
#File handling functions: The functions below are meant to take in strings that represent the names of the files being examined
#The function read_files does exactly as it states and handles cases where files do not exist. The second function takes the data from the file in question and puts it in a more workable form
def read_file(file_name):
    try:
        open_file = open(file_name, "r")
        return open_file
    except FileNotFoundError:
        return None

def get_file_data(file_object):
    str_list = []
    
    for line in file_object:
        str_list.append(line)
    return str_list

#The function populate_list uses the data from the files that have been read and converts numeric values from string types into float types, strings that are not numeric are ignored 
def populate_list(list_object):
    file_object = read_file(list_object)

    if file_object == None:
        return None
    else:
        str_list = get_file_data(file_object)

        num_list = []

        for line in str_list:
            try:
                num_list.append(float(line.strip()))   
            except ValueError:
                pass
        return num_list

#The three functions below perform the necessary analysis operations that the program is intended to perform
def sort_list(list_object):
    return sorted(list_object)

def get_cumulative_sum(list_object):
    tmp_sum = 0
    cumulative_sum_list = []

    for i in range(len(list_object)):
        tmp_sum += list_object[i]
        cumulative_sum_list.append(round(tmp_sum,1))
    return str(cumulative_sum_list)[1:-1]

def get_median(list_object):
    median = 0
    middle_index = 0

    if len(list_object) % 2 != 0:
        median += len(list_object) // 2
        return list_object[median]
    elif len(list_object) % 2 == 0:
        middle_index += len(list_object) // 2
        median = (list_object[middle_index-1] + list_object[middle_index]) / 2
        return round(median,2)

#The two functions below handle the printing of results depending on the contents of the files analyzed
def print_results(list_value,numeric_list,sorted_list):
    print("\nFile {}".format(list_value))
    print("\tSequence:")
    print("\t\t{} ".format(str(numeric_list)[1:-1]).replace(",",""))
    print("\tCumulative sum:")
    print("\t\t{} ".format(get_cumulative_sum(numeric_list).replace(",","")))
    print("\tSorted sequence:")
    print("\t\t{} ".format(str(sorted_list)[1:-1]).replace(",",""))
    print("\tMedian:")
    print("\t\t{}".format(get_median(sorted_list)))

def print_empty(list_value):
    print("\nFile {}".format(list_value))
    print("\tSequence:")
    print()
    print("\tCumulative sum:")
    print()
    print("\tSorted sequence:")
    print()
    print("\tMedian:")
    print()

#The function below handles the core work of the program and calls other necessary functions
def process_all_files(file_list_object):
    filename_list = file_list_object
    
    for i, value in enumerate(filename_list):

        num_list = populate_list(filename_list[i])
        if num_list == None:
            print("\nFile {} not found".format(value))
            break
        else:
            if num_list == []:
                print_empty(value)
            else:
                sorted_list = sort_list(num_list)

                print_results(value,num_list,sorted_list)

#This is the main function
def main_func():
    filename_list = input("Enter filenames: ").split()
    process_all_files(filename_list)

main_func()