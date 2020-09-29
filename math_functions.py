#This program is comprised of a series of functions capable of performing various mathmatical calculations depending on user input.
#This program will enable the user to perform three different calculations based on input when prompted, one will print the sum of all numbers >= 2  up to a number inserted by the user
#Another will sum the first n numbers in the fibonacci sequence, n being a number from user input larger than 2.
#The third will approximate the eulers number by using the first n numbers in a specified formula, n being a number from user input
#The user can continue to perform calculations when prompted until an 'x' is entered, incorect inputs will be handled

import math

def menu_display():
    print("Please choose one of the options below:")
    print("a. Display the sum of the first N natural numbers. ")
    print("b. Display the sum of the first N Fibonacci numbers. ")
    print("c. Display the approximate value of e using N terms.")
    print("x. Exit from the program.")
    print()
    

def calculation_function():
    menu_display()

    options_str = input("Enter option: ")

    while options_str != "x":
        if options_str != "a" and options_str != "b" and options_str != "c":
            print("Unrecognized option {}".format(options_str))
            menu_display()
        elif options_str == "a":
            N_str = input("Enter N: ")
            N_nat_sum = sum_natural(N_str)

            if N_nat_sum == None:
                print("Error: {} was not a valid number.".format(N_str))
            else:    
                print("Natural number sum: {} ".format(N_nat_sum))
            print()
        elif options_str == "b":
            N_str = input("Enter N: ")
            N_fib_sum = sum_fibonacci(N_str)

            if N_fib_sum == None:
                print("Error: {} was not a valid number.".format(N_str))
            else:
                print("Fibonacci sum: {} ".format(N_fib_sum))
            print()
        elif options_str == "c":
            N_str = input("Enter N: ")
            N_euler_appr = euler_approximation(N_str)

            if N_euler_appr == None:
                print("Error: {} was not a valid number.".format(N_str))
            else:
                print("Euler approximation: {} ".format(N_euler_appr))
            print()
        
        options_str = input("Enter option: ")
        
        
def cast_to_int(string):
    is_numeric = check_if_numeric(string)

    if is_numeric:
        int_string = int(string)
        if int_string >= 2:
            return int_string
        else:
            return False
    else:
        return False


def sum_natural(n_str):
    n_int = cast_to_int(n_str)

    if n_int == False:
        return None
    else:
        sum_of_n = 0

        for i in range(1,n_int+1):
            sum_of_n += i
    
        return sum_of_n


def sum_fibonacci(n_str):
    n_int = cast_to_int(n_str)

    if n_int == False:
        return None
    else:

        fibo_1 = 0
        fibo_2 = 1
        tmp = 0

        fibo_sum = 0

        for i in range(1,n_int):
            tmp = fibo_1
            fibo_1 = fibo_2
            fibo_2 += tmp

            fibo_sum += fibo_1

        return fibo_sum


def euler_approximation(n_str):
    n_int = cast_to_int(n_str)

    if n_int == False:
        return None
    else:
        approx_sum = 1

        for i in range(1,n_int):
            approx_sum = approx_sum + (1/(math.factorial(i)))
    
        return round(approx_sum,5)


def check_if_numeric(n_str):
    if n_str.isdigit():
        return True
    else:
        return False


calculation_function()

    