#This program takes three integers from user input and then states which of them is the largest

int_1 = int(input("Enter first number: "))
int_2 = int(input("Enter second number: "))
int_3 = int(input("Enter third number: "))

min_int = 0

if int_1 < int_2 and int_1 < int_3:
    min_int = int_1
elif int_2 < int_1 and int_2 < int_3:
    min_int = int_2
else:
    min_int = int_3

print(min_int,"is the lowest number of the three")