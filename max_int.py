#This program takes in a series of positive integers from user input 
#until a negative integers is entered, at which point the program stops running and outputs the highest integer

#Input vatriables from the user

num_int = int(input("Input a number: "))
max_int = 0  #we want to create a variable that will store the maximum integer at each iteration

#We want some way to keep track of the integers being entered until the input is less than 0
#In other words we want the calculations to continue while the input from the user is a positive integer

while num_int >= 0:                                                      
    num_int = int(input("Input a number: "))

    for i in range(0,num_int):                #At each iteration we run through the series of numbers entered
        if num_int > max_int:                 #We want to compare the value entered with the current maximum from the entry
            max_int = num_int                 #If the current maximum is lower than the number entered we make that number the new maximum

print("The maximum is", max_int)              #Afterwards we display the maximum in any way we like 


    
