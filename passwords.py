#This program allows users to create passwords until they enter the letter q, the program
#should only allow passwords of length 6 to 20 that contain at least one lowercase letter, one uppercase letter and one number
#the program counts the total amount of passwords created, how many of them were valid and how many were invalid

password_string = input("Enter a new password: ")

count_total = 0
count_valid = 0
count_invalid = 0

#We want to define three boolean constants that begin as false for use in our iterations and then change to true if the relevant conditions
#are met

#We also want to keep the minimum length of a string and the maximum length of a string as constants

str_len_min = 6
str_len_max = 20

while password_string != "q":

    has_upper_case = False
    has_lower_case = False
    has_number = False

    if len(password_string) < str_len_min or len(password_string) > str_len_max:
        print("Invalid length")

        count_invalid += 1
        count_total += 1

        password_string = input("Enter a new password: ")
    else:
        for char in password_string:
            if char.islower():
                has_lower_case = True                              #Here we iterate over each character within the entered password string
            
            if char.isupper():                                     #and change the status of the boolean variables if a lower case letter, upper case letter
                has_upper_case = True                              #or a numeric value is found so we can apply the appropriate error messages
            
            if char.isnumeric():
                has_number = True
        
        if has_lower_case == False:
            print("At least one lower case letter needed")
        
        if has_upper_case == False:
            print("At least one upper case letter needed")
        
        if has_number == False:
            print("At least one number needed")
        
        if has_lower_case == True and has_upper_case == True and has_number == True:
            print("Valid password of length",len(password_string))
            count_valid += 1
        else:
            count_invalid += 1
        
        count_total += 1

        password_string = input("Enter a new password: ")

print("You tried {} passwords, {} valid, {} invalid".format(count_total,count_valid,count_invalid))

            




                

            
        

    