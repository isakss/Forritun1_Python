#This program takes in two numbers from user input and prints all integers between them

lower_int = int(input("Enter the lower number: "))
higher_int = int(input("Enter the higher number: "))

if lower_int >= higher_int:
    print("The lower number must be lower than the higher one!")
else:
    for i in range(lower_int,higher_int + 1):
        print(i)