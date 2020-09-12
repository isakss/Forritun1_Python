#This program takes in an integer from user input, and states whether it is less than 10 or between 10 and 20
#If the number is lower than 0 the program prints "Too low" and "Too high" should it be greater than or equal to 20

number = int(input("Enter a number: "))

if number < 10 and number >= 0:
    print("Less than 10")
elif number >= 10 and number < 20:
    print("Between 10 and 20")
elif number < 0:
    print("The value is too low!")
else:
    print("The value is too high!")