#This program takes two strings from user input and compares their length, the program only states something when the strings are of equal length

str_1 = input("Enter first string: ")
str_2 = input("Enter second string: ")

if len(str_1) == len(str_2):
    print("The strings are the same length")
else:
    print("The strings are of different lengths")

