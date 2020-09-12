#This program prints out the odd numbers in the range of 15 down to 3

number_limit = 15

while number_limit >= 3:
    if number_limit % 2 != 0:
        print(number_limit)
    number_limit -= 1