def read_file(string_object):
    try:
        return open(string_object, "r")
    except FileNotFoundError:
        return None

def populate_flyers_dict(file_object):
    new_flyer_dict = {}

    for line in file_object:
        flyer, country = line.strip().split(" ")

        key_flyer = flyer
        value = (country,)
        
        if key_flyer in new_flyer_dict and country not in new_flyer_dict[key_flyer]:
            new_flyer_dict[key_flyer] += value
        else:
            new_flyer_dict[key_flyer] = value

    return new_flyer_dict

def print_flyers(dictionary_object):
    sorted_flyer_list = sorted(dictionary_object.items())

    for key, country_tuple in sorted_flyer_list:
        country_list = sorted(country_tuple)
        print("{}:".format(key))
        for element in country_list:
            print("\t{}".format(element))

    get_highest_visit_rate(sorted_flyer_list) 

def get_highest_visit_rate(list_object):
    max_len = 0
    person_str =""

    for key, country_tuple in list_object:
        if len(country_tuple) > max_len:
            max_len = len(country_tuple)
            person_str = key

    print("\n")        

    print("{} has traveled to {} countries.".format(person_str, max_len)) 

def main():
    file_name = input("Enter file name: ")
    open_file = read_file(file_name)

    if open_file == None:
        print("File {} not found!".format(file_name))
    else:
        flyer_dict = populate_flyers_dict(open_file)
        print_flyers(flyer_dict)

main()