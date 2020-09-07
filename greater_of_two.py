#This program accepts two integers from user input and compares the to see which one is greater

int_1 = int(input("Enter the first number: "))
int_2 = int(input("Enter the second number: "))

if int_1 > int_2:
    print(int_1,"is greater than",int_2)
elif int_2 > int_1:
    print(int_2,"is greater than",int_1)
else:
    print("The numbers are equal")