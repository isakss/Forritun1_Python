import string
import operator

def read_file(string_object):
    try:
        return open(string_object,"r")
    except FileNotFoundError:
        return None

def get_word_list(file_object):
    clean_list = []
    
    for line in file_object:
        line = line.strip().split()
        for word in line:
            word = word.lower()
            clean_list.append(word.strip(string.punctuation))
    
    return clean_list

def find_bigrams(list_object):
    bigrams_list = [bigram for bigram in zip(list_object[:-1], list_object[1:])]
    return bigrams_list

def populate_bigram_dict(list_object):
    new_bigram_dictionary = {}

    for element in list_object:
        if element in new_bigram_dictionary:
            new_bigram_dictionary[element] += 1
        else:
            new_bigram_dictionary[element] = 1
    
    return new_bigram_dictionary

def convert_to_tuples_list(dictionary_object):
    tuples_list = [(key, value) for key, value in dictionary_object.items()]
    return sorted(tuples_list, key = operator.itemgetter(1), reverse = True)

def main_func():
    file_name = input("Enter name of file: ")
    open_file = read_file(file_name)
    
    if open_file == None:
        print("File {} not found.".format(file_name))
    else:
        word_list = get_word_list(open_file)
        bigrams_list = find_bigrams(word_list)
        bigram_dict = populate_bigram_dict(bigrams_list)
        sorted_bigram_list = convert_to_tuples_list(bigram_dict)

        print(sorted_bigram_list)

main_func()