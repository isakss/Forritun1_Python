#This program takes two integers a and b as input from the user, next the program takes in integers in the range of 1 to 3
#Where 1 will sum the two numbers together, 2 will subtract them and 3 will multiply them with each other
#Should any other number be entered it will result in an invalid input

int_a = int(input("Enter the value for a: "))
int_b = int(input("Enter the value for b: "))

choice = int(input("Enter the operation you would like to run (1 addition, 2 subtraction, 3 multiplication): "))

if choice == 1:
    print(int_a + int_b)
elif choice == 2:
    print(int_a - int_b)
elif choice == 3:
    print(int_a * int_b)
else:
    print("Invalid input.")