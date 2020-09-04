#Project 3: Fibo Abundant
#This prgram takes in a number from a users input and prints out the numbers in the fibonacci sequence
#between 0 and that number, and also prints out numbers that are abundant within that range depending on input from
#user when prompted.

fibo_abundant_str = input("Input f|a|b (fibonacci, abundant or both): ")

sequence_len = 0
max_number = 0

#Initialize the first two numbers in the fibonacci sequence as well as a tmp variable
#to store the original value of a in, that way it can be used in the calculations effectively

fibonacci_a = 0
fibonacci_b = 1
tmp = 0 

sum_of_divisors = 0

if fibo_abundant_str == "f":

    sequence_len = int(input("Input the length of the sequence: "))
    
    print("Fibonacci Sequence: ")
    print("-------------------")

    for i in range(0,sequence_len):
        print(fibonacci_a)
        tmp = fibonacci_a
        fibonacci_a = fibonacci_b
        fibonacci_b = tmp + fibonacci_b
elif fibo_abundant_str == "a":

    max_number = int(input("Input the max number to check: "))

    print("Abundant numbers:")
    print("-----------------")

    for i in range(1,max_number+1):
        for j in range(1,i):
            if i % j == 0:
                sum_of_divisors += j
        if sum_of_divisors > i:
            print(i)
        sum_of_divisors = 0
elif fibo_abundant_str == "b":

    sequence_len = int(input("Input the length of the sequence: "))
    
    print("Fibonacci Sequence: ")
    print("-------------------")

    for i in range(0,sequence_len):
        print(fibonacci_a)
        tmp = fibonacci_a
        fibonacci_a = fibonacci_b
        fibonacci_b = tmp + fibonacci_b
    
    max_number = int(input("Input the max number to check: "))

    print("Abundant numbers:")
    print("-----------------")

    for i in range(1,max_number+1):
        for j in range(1,i):
            if i % j == 0:
                sum_of_divisors += j
        if sum_of_divisors > i:
            print(i)
        sum_of_divisors = 0


        

    
