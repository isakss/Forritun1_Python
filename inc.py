#This program has a defined increment function that takes a number and adds one to it

def inc(num):
    result = num + 1
    return result

number = int(input("Enter a number to increment: "))

number_incremented = inc(number)

print("Number after being incremented: {}".format(number_incremented))