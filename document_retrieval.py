"""
This program reads documents from a file into a list, populates a dictionary with the words from the list of documents as the keys and the set
of document numbers as the value for each word. The program then enables the user to search for specific words and find out in which documents
they occur, as well as enabling the user to print out the contents of a document associated with a given number. 
"""

import string

def read_file(string_object):
    """Read through a given file"""
    try:
        return open(string_object,"r")
    except FileNotFoundError:
        return None

def get_documents(file_object):
    """Get documents from a given file stream, returns a list of document strings"""
    document_list = []
    document_string = ""

    for line in file_object:
        line = line.strip()
        if line == "<NEW DOCUMENT>":
            document_list.append(document_string)
            document_string = ""
        else:
            document_string += (line + " \n")
    
    document_list.append(document_string)

    return document_list

def populate_word_list(list_object):
    """Turns a list of sentances into a cleaned list of words"""
    word_list = []

    for element in list_object:
        sentance = "".join([char for char in element if char not in string.punctuation])   #Removes punctuation from a sentance in the list
        word_list.append(sentance.strip().lower().split())
           
    return word_list

def populate_word_dictionary(list_object):
    """Initializes a dictionary with the keys being words from a list of words, 
    and the values being the number of the documents in which that word occurs"""

    new_dictionary = {}

    for element in list_object:
        for word in element:
            if word not in new_dictionary:
                new_dictionary[word] = set()
            else:
                pass
    
    for word in new_dictionary:
        for i in range(0,len(list_object)):
            if word in list_object[i]:
                new_dictionary[word].add(i)

    return new_dictionary        

def get_search_results(list_object, dictionary_object):
    """Searches through a given word dictionary and returns a set which is the intersection of the sets of document numbers belonging to the words being
    searched for, returns an empty set if a word does not exist in the dictionary"""

    tmp_doc_list = []

    for element in list_object:
        try:
            tmp_doc_list.append(dictionary_object[element])
        except KeyError:
            tmp_doc_list.append(set())
    
    intersect_set = tmp_doc_list[0].intersection(*tmp_doc_list)

    return intersect_set

def print_menu():
    """Prints the operations menu."""

    print("What would you like to do?")
    print("1. Search Documents")
    print("2. Print Document")
    print("3. Quit Program")

def menu_loop(list_object, dictionary_object):
    """Performs the necessary functions of the program and calls other functions to do so.
    Goes on until the user enters a choice that exits the program"""

    print_menu()
    choice_input = input("> ")

    while choice_input == "1" or choice_input == "2":
        if choice_input == "1":
            word_input_list = input("Enter search words: ").lower().split()
            search_result = get_search_results(word_input_list, dictionary_object)

            if search_result == set():
                print("No match.\n")
            else:
                print("Documents that fit search:",*search_result,"\n")
        elif choice_input == "2":
            document_number_input = int(input("Enter document number: "))
            try:
                doc_result = list_object[document_number_input]
                print("Document #{}".format(document_number_input))
                print(doc_result)
            except IndexError:
                print("No match.\n")

        print_menu()
        choice_input = input("> ")
    else:
        print("Exiting program.")

def main_func():
    """Main function"""

    file_name = input("Document collection: ")
    open_file = read_file(file_name)

    if open_file == None:
        print("Documents not found.")
    else:
        print()
        document_list = get_documents(open_file)
        word_list = populate_word_list(document_list)
        word_dictionary = populate_word_dictionary(word_list)

        menu_loop(document_list, word_dictionary)
    
    open_file.close()
        
main_func()
