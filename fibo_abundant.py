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

sum_of_divisors = 0            #We also want a variable that can keep the value for the sum of the divisors of a set number at each iteration

if fibo_abundant_str == "f":

    sequence_len = int(input("Input the length of the sequence: "))
    
    print("Fibonacci Sequence: ")
    print("-------------------")

    for i in range(0,sequence_len):
        print(fibonacci_a)
        tmp = fibonacci_a                                           #Keep the original value of a so it can be used in further calculation
        fibonacci_a = fibonacci_b                                   #Assign the value of the next number after a to a
        fibonacci_b = tmp + fibonacci_b                             #Assign the sum of the original value of a and b to get the next number in the sequence
elif fibo_abundant_str == "a":

    max_number = int(input("Input the max number to check: "))

    print("Abundant numbers:")
    print("-----------------")

    for i in range(1,max_number+1):
        for j in range(1,i):                            #In this iteration we run through range of 1 to the number being checked
            if i % j == 0:                              #at each iteration we run through the range of 1 to the current number being checked to see if it has any divisors
                sum_of_divisors += j                    #If some number in the current iterative range is a divisor we add it to the sum of divisors variable
        if sum_of_divisors > i:                         #If at some point the sum of divisors exceeds the current number in the iteration we print that sum
            print(i)
        sum_of_divisors = 0                             #At the end of the inner iteration we reset the sum variable for the next outer iteration
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


        

    
