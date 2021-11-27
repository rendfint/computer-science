#Write a program that repeatedly prompts a user for integer numbers until the 
#user enters 'done'. Once 'done' is entered, print out the largest and 
#smallest of the numbers. If the user enters anything other than a valid 
#number catch it with a try/except and put out an appropriate message and 
#ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

smallest_number = None
largest_number = None

while True :
    number = input("Enter a number: ")
    if number == "done" :
        break
    try :
        int_number = int(number)
    except :
        print("Invalid input")
        continue

    if smallest_number is None and largest_number is None :
        smallest_number = int_number
        largest_number = int_number
    if int_number > largest_number :
        largest_number = int_number
    if int_number < smallest_number :
        smallest_number = int_number


print("Maximum is", largest_number)
print("Minimum is", smallest_number)
