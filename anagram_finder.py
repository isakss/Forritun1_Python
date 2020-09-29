"""
This program takes two words from user input and checks if they are anagrams of each other
"""

def main_func():
    words_list = input("Enter two words seperated with a space: ").split()

    word1 = words_list[0]
    word2 = words_list[1]

    word1_sorted = sort_string(word1)
    word2_sorted = sort_string(word2)

    anagram_check(word1_sorted,word2_sorted)


def sort_string(string_object):
    return sorted(string_object)

def anagram_check(string_1,string_2):
    if string_1 == string_2:
        print("The two words are anagrams.")
    else:
        print("The two words are not anagrams")

main_func()