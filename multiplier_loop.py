#This program takes in an integer from user input, loops through numbers 2 to 15 and multiplies them with the entered number

multiplier = int(input("Enter the multiplier: "))

for i in range(2,16):
    print(i * multiplier)